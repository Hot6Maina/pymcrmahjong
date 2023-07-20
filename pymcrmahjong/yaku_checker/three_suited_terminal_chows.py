from common import DivisionPartTypeEnum, YakuEnum
from agari_info import AgariInfo
from division import Division
from base_yaku import BaseYaku
from tile import Tiles


class ThreeSuitedTerminalChows(BaseYaku):
    def __init__(self):
        super().__init__(YakuEnum.THREE_SUITED_TERMINAL_CHOWS)

    def is_satisfied(self, division: Division, agari_info: AgariInfo):
        if not (division.tile_count.is_containing_only(Tiles.NUMBERS)):
            return int(False)
        first_number_list = []
        head_tile_type = -1
        for part in division.parts:
            if part.type == DivisionPartTypeEnum.HEAD:
                if part.counts.get_tile_number[0] != 5:
                    return int(False)
            head_tile_type = part.tile_type
        if head_tile_type == -1:
            return int(False)

        first_number_dict = {
            Tiles.SOUS: [],
            Tiles.PINS: [],
            Tiles.MANS: []
        }
        for part in division.parts:
            if part.type == DivisionPartTypeEnum.HEAD:
                continue
            elif part.type == DivisionPartTypeEnum.SEQUENCE:
                if part.tile_type == head_tile_type:
                    return int(False)
                first_number_dict[part.tile_type].append(part.counts.get_tile_number[0])
            else:
                return int(False)
        for tile_type, start_number_list in first_number_dict:
            if tile_type == head_tile_type:
                continue
            if len(start_number_list) != 2 or start_number_list[0] != 1 or start_number_list[1] != 7:
                return int(False)
        return int(True)
