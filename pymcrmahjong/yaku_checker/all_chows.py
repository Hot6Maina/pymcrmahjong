from common import YakuEnum, DivisionPartTypeEnum, TileTypeEnum
from agari_info import AgariInfo
from division import Division
from base_yaku import BaseYaku


class AllChows(BaseYaku):
    def __init__(self):
        super().__init__(YakuEnum.ALL_CHOWS)

    def is_satisfied(self, division: Division, agari_info: AgariInfo):
        good_flag = True
        for part in division.parts:
            if part.type == DivisionPartTypeEnum.HEAD:
                if part.tile_type not in (TileTypeEnum.MAN, TileTypeEnum.PIN, TileTypeEnum.SOU):
                    good_flag = False
                    break
            elif part.type not in (DivisionPartTypeEnum.SEQUENCE, DivisionPartTypeEnum.KNITTED):
                good_flag = False
                break
        return int(good_flag)
