import strawberry


@strawberry.type
class Device:
    device: str
    application_version: str


@strawberry.type
class CreditCard:
    expire_date: str
    number: str
    provider: str
    security_code: str


@strawberry.type
class Money:
    currency_code: str
    currency_name: str
    amount: float


@strawberry.type
class User:
    first_name: str
    last_name: str


@strawberry.type
class Event:
    id: str
    timestamp: str


@strawberry.type
class Transaction:
    money: Money
    credit_card: CreditCard


@strawberry.type
class Bet:
    transaction: Transaction
    user: User
    device: Device
    event: Event
