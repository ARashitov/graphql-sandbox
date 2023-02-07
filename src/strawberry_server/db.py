from src.strawberry_server.generator import BetGenerator

N_BETS = 20
generator = BetGenerator()


BETS = [
    generator.generate() for i in range(N_BETS)
]


def get_bets():
    return BETS


def get_users():
    return [
        bet.user for bet in BETS
    ]


def get_events():
    return [
        bet.event for bet in BETS
    ]


def get_transactions():
    return [
        bet.transaction for bet in BETS
    ]
