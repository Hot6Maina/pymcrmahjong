from common import YakuEnum
from agari_info import AgariInfo
from division import Division
from tile import Tiles
from base_yaku import BaseYaku


class HalfOutsideHand(BaseYaku):
    def __init__(self):
        super().__init__(YakuEnum.HALF_OUTSIDE_HAND)

    def is_satisfied(self, division: Division, agari_info: AgariInfo):
        return all(
            not part.counts.is_containing_only(Tiles.SIMPLES) for part in division.parts
        )
