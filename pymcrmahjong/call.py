from pydantic import BaseModel

from common import CallTypeEnum
from tile import Tile


class Call(BaseModel):
    type: CallTypeEnum
    tiles: list[Tile]
    call_idx: int
