from typing import (
    List
)

from pydantic import (
    BaseModel,
    Field
)

from blackjack.models.card import Card

class Player(BaseModel):
    player_id: int
    username: str
    current_game_id: int | None = Field(default=None)
    hand: List[Card] = Field(default=[])
    balance: float = Field(default=0)
    bet: float = Field(default=0)


