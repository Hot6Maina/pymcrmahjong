from common import YakuEnum
from agari_info import AgariInfo
from division import Division
from tile import Tiles
from base_yaku import BaseYaku


class NoHonors(BaseYaku):
    def __init__(self):
        super().__init__(YakuEnum.NO_HONORS)

    def is_satisfied(self, division: Division, agari_info: AgariInfo):
        return int(division.tile_count.is_containing_only(Tiles.NUMBERS))
