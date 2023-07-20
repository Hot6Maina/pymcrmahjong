from common import YakuEnum, TileTypeEnum
from agari_info import AgariInfo
from division import Division
from base_yaku import BaseYaku


class OneVoidedSuit(BaseYaku):
    def __init__(self):
        super().__init__(YakuEnum.ONE_VOIDED_SUIT)

    def is_satisfied(self, division: Division, agari_info: AgariInfo):
        tile_type_set = set([part.tile_type for part in division.parts])
        count = 0
        for tile_type in tile_type_set:
            if tile_type in (TileTypeEnum.MAN, TileTypeEnum.SOU, TileTypeEnum.PIN):
                count += 1
        return int(count == 2)

