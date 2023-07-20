from common import DivisionPartTypeEnum, YakuEnum
from agari_info import AgariInfo
from division import Division
from base_yaku import BaseYaku
from tile import Tiles


class PureTerminalChows(BaseYaku):
    def __init__(self):
        super().__init__(YakuEnum.PURE_TERMINAL_CHOWS)

    def is_satisfied(self, division: Division, agari_info: AgariInfo):
        if not (division.tile_count.is_containing_only(Tiles.MANS)
                or division.tile_count.is_containing_only(Tiles.PINS)
                or division.tile_count.is_containing_only(Tiles.SOUS)
        ):
            return int(False)
        first_number_list = []
        for part in division.parts:
            if part.type == DivisionPartTypeEnum.HEAD:
                if part.counts.get_tile_number[0] != 5:
                    return int(False)
            elif part.type == DivisionPartTypeEnum.SEQUENCE:
                first_number_list.append(part.counts.get_tile_number[0])
            else:
                return int(False)
        first_number_list.sort()
        if len(first_number_list) != 4:
            return int(False)
        return int(first_number_list[0] == first_number_list[1] == 1 and
                   first_number_list[2] == first_number_list[3] == 7)
