from common import YakuEnum, DivisionPartTypeEnum, TileTypeEnum
from agari_info import AgariInfo
from division import Division
from tile import Tiles
from base_yaku import BaseYaku


class AllEvenPungs(BaseYaku):
    def __init__(self):
        super().__init__(YakuEnum.ALL_EVEN_PUNGS)

    def is_satisfied(self, division: Division, agari_info: AgariInfo):
        good_flag = True
        for part in division.parts:
            if not part.counts.is_containing_only(Tiles.EVENS):
                good_flag = False
                break
        num_triplets = sum(
            1
            for part in division.parts
            if part.type is DivisionPartTypeEnum.TRIPLE
            or part.type is DivisionPartTypeEnum.QUAD
        )
        return int(num_triplets == 4 and good_flag)
