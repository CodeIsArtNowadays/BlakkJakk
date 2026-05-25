from pydantic import BaseModel


class Card:
	suit: str
	rank: str

class Hand:
	cards: list[Card]
	value: int


