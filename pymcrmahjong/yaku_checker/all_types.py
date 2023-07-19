from common import YakuEnum, TileTypeEnum
from agari_info import AgariInfo
from division import Division
from base_yaku import BaseYaku


class AllTypes(BaseYaku):
    def __init__(self):
        super().__init__(YakuEnum.ALL_TYPES)

    def is_satisfied(self, division: Division, agari_info: AgariInfo):
        return int(set([part.tile_type for part in division.parts])
                   == {TileTypeEnum.MAN, TileTypeEnum.SOU, TileTypeEnum.PIN, TileTypeEnum.WIND, TileTypeEnum.DRAGON})

