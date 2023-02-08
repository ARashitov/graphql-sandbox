import typing

import strawberry
from strawberry.fastapi import GraphQLRouter
from fastapi import FastAPI

from src.strawberry_server import db
from src.strawberry_server import schemas


@strawberry.type(name="query")
class Query:
    bets: typing.List[schemas.Bet] = strawberry.field(resolver=db.get_bets)
    events: typing.List[schemas.Event] = strawberry.field(resolver=db.get_events)
    users: typing.List[schemas.User] = strawberry.field(resolver=db.get_users)
    transactions: typing.List[schemas.Transaction] = strawberry.field(resolver=db.get_transactions)


@strawberry.type(name="mutation")
class Mutation:

    @strawberry.field
    def add_user(
            self,
            first_name: str,
            last_name: str) -> schemas.User:
        user = schemas.User(
            first_name=first_name,
            last_name=last_name,
        )
        # Some IO operation
        return user


schema = strawberry.Schema(query=Query, mutation=Mutation)
graphql_app = GraphQLRouter(schema)


app = FastAPI()
app.include_router(graphql_app, prefix="/graphql")
