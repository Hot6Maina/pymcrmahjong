from common import DivisionPartTypeEnum, YakuEnum
from agari_info import AgariInfo
from division import Division
from tile import Tiles
from base_yaku import BaseYaku


class DragonPung(BaseYaku):
    def __init__(self):
        super().__init__(YakuEnum.DRAGON_PUNG)

    def is_satisfied(self, division: Division, agari_info: AgariInfo):
        return sum(
            1
            for part in division.parts
            if
            (
                part.type is DivisionPartTypeEnum.TRIPLE
                or part.type is DivisionPartTypeEnum.QUAD
            )
            and part.counts.is_containing_only(Tiles.DRAGONS)

        )
