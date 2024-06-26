from typing import Optional, Dict
from typing import List
import decimal
from pydantic import BaseModel, field_validator


class LoanStateBase(BaseModel):
    protocol_id: str
    block: int
    timestamp: int
    user: Optional[str]
    collateral: Optional[Dict]
    debt: Optional[Dict]
    deposit: Optional[Dict]

    class Config:
        orm_mode = True


class LoanStateResponse(LoanStateBase):
    pass


class OrderBookModel(BaseModel):
    """
    A data model class that validates data user entered
    """

    token_a: str
    token_b: str
    block: int
    timestamp: int
    dex: str
    asks: List[tuple[float, float]]
    bids: List[tuple[float, float]]

    @field_validator("asks", "bids")
    def convert_decimals_to_floats(
        cls, value: List[tuple[decimal.Decimal, decimal.Decimal]]
    ) -> List[tuple[float, float]]:
        """
        Convert decimal values to floats
        :param value: list of tuples of decimal values
        :return: list of tuples of float values
        """
        return [(float(a), float(b)) for a, b in value]
