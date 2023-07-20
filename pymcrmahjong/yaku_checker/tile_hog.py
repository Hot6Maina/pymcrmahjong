from common import DivisionPartTypeEnum, YakuEnum
from agari_info import AgariInfo
from division import Division
from base_yaku import BaseYaku
from tile import Tiles


class Tile_hog(BaseYaku):
    def __init__(self):
        super().__init__(YakuEnum.TRIPLE_PUNG)

    def is_satisfied(self, division: Division, agari_info: AgariInfo):
        count = [0] * 10
        for part in division.parts:
            if part.counts.is_containing_only(Tiles.NUMBERS):
                if part.type == DivisionPartTypeEnum.QUAD:
                    continue
                for number in part.counts.get_tile_number:
                    count[number] += 1
        return count.count(4)
