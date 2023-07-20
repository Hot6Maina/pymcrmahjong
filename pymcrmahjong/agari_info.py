from pydantic import BaseModel

from tile import Tile, Tiles
from common import WaitEnum


class AgariInfo(BaseModel):
    is_tsumo_agari: bool = False
    is_concealed_hand: bool = False
    round_wind: Tile = Tiles.WINDS[0]
    player_wind: Tile = Tiles.WINDS[0]
    is_last_tile: bool = False
    is_last_draw: bool = False
    is_last_discard: bool = False
    is_replacement_tile: bool = False
    is_robbing_the_kong: bool = False
    wait_type: WaitEnum = WaitEnum.ELSE_WAIT
