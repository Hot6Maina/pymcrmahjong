from common import YakuEnum
from agari_info import AgariInfo
from division import Division
from tile import Tiles
from base_yaku import BaseYaku


class HalfFlush(BaseYaku):
    def __init__(self):
        super().__init__(YakuEnum.HALF_FLUSH)

    def is_satisfied(self, division: Division, agari_info: AgariInfo):
        tile_count = division.tile_count
        return (
            tile_count.is_containing_only(Tiles.MANS + Tiles.HONORS)
            or tile_count.is_containing_only(Tiles.PINS + Tiles.HONORS)
            or tile_count.is_containing_only(Tiles.SOUS + Tiles.HONORS)
        ) and not tile_count.is_containing_only(Tiles.NUMBERS)
