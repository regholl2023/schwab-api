from typing import Literal

from schwab.models.utils import SchwabDataModel


class Screener(SchwabDataModel):
    change: float
    description: str
    direction: Literal["up", "down"]
    last: float
    symbol: str
    total_volume: int
