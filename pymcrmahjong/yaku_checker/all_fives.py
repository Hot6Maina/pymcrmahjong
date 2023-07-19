from common import YakuEnum
from tile import Tiles
from agari_info import AgariInfo
from division import Division
from base_yaku import BaseYaku


class AllFives(BaseYaku):
    def __init__(self):
        super().__init__(YakuEnum.ALL_FIVES)

    def is_satisfied(self, division: Division, agari_info: AgariInfo):
        return int(all(part.counts.count_tile(Tiles.FIVES) for part in division.parts))

