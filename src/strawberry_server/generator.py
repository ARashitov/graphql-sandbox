import datetime
import typing as tp

from faker import Faker
import numpy as np

from src.strawberry_server import schemas


class BetGenerator:

    def __init__(self):
        self.faker = Faker()

    def generate_credit_card(self) -> dict[str, tp.Union[str, int, float]]:
        return schemas.CreditCard(**{
            "expire_date": self.faker.credit_card_expire(),
            "number": self.faker.credit_card_number(),
            "provider": self.faker.credit_card_provider(),
            "security_code": self.faker.credit_card_security_code(),
        })

    def generate_money_details(self) -> dict[str, tp.Union[str, int, float]]:
        money_amt = self.faker.random.normalvariate(mu=100, sigma=40)
        money_amt = round(np.clip(money_amt, a_min=1, a_max=money_amt), 4)
        currency = self.faker.currency()
        return schemas.Money(**{
            "currency_code": currency[0],
            "currency_name": currency[1],
            "amount": money_amt,
        })

    def generate_user(self) -> dict[str, tp.Union[str, int, float]]:
        return schemas.User(**{
            "first_name": self.faker.first_name_male(),
            "last_name": self.faker.last_name_male(),
        })

    def generate_device_details(self):
        if self.faker.boolean(60):
            platform_token = self.faker.android_platform_token
        else:
            platform_token = self.faker.ios_platform_token
        return schemas.Device(
            device=platform_token(),
            application_version=self.faker.random.choice(["v2", "v3", "v4"]),
        )

    def generate_event_timestamp(self) -> str:
        return str(datetime.datetime.now())

    def generate_event(self):
        return schemas.Event(**{
            "id": self.faker.uuid4(),
            "timestamp": self.generate_event_timestamp(),
        })

    def generate(self) -> dict:
        return schemas.Bet(**{
            "transaction": schemas.Transaction(**{
                "money": self.generate_money_details(),
                "credit_card": self.generate_credit_card(),
            }),
            "user": self.generate_user(),
            "device": self.generate_device_details(),
            "event": self.generate_event(),
        })
