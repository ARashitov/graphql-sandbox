import typing
import strawberry

from src.strawberry_server import db
from src.strawberry_server import schemas


@strawberry.type(name="test")
class Query:
    bets: typing.List[schemas.Bet] = strawberry.field(resolver=db.get_bets)
    events: typing.List[schemas.Event] = strawberry.field(resolver=db.get_events)
    users: typing.List[schemas.User] = strawberry.field(resolver=db.get_users)
    transactions: typing.List[schemas.Transaction] = strawberry.field(resolver=db.get_transactions)


schema = strawberry.Schema(query=Query)
