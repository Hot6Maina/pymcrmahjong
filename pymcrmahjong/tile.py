from __future__ import annotations

from common import TileTypeEnum


class Tile(int):
    def __new__(cls, value, *args, **kwargs):
        if value not in range(35):
            raise ValueError("Tile should be in 0~34")
        return super(cls, cls).__new__(cls, value)

    @property
    def type(self) -> TileTypeEnum:
        if 0 <= self < 9:
            return TileTypeEnum.MAN
        elif 9 <= self < 18:
            return TileTypeEnum.PIN
        elif 18 <= self < 27:
            return TileTypeEnum.SOU
        elif 27 <= self < 31:
            return TileTypeEnum.WIND
        elif 31 <= self < 34:
            return TileTypeEnum.DRAGON
        else:
            return TileTypeEnum.FLOWER

    @property
    def number(self) -> int:
        return self - 30 if self > 30 else self % 9 + 1


class Tiles:
    MANS = [Tile(value) for value in range(9)]
    PINS = [Tile(value) for value in range(9, 18)]
    SOUS = [Tile(value) for value in range(18, 27)]
    WINDS = [Tile(value) for value in range(27, 31)]
    DRAGONS = [Tile(value) for value in range(31, 34)]
    FLOWER = [Tile(value) for value in range(34, 35)]

    NUMBERS = MANS + PINS + SOUS
    HONORS = WINDS + DRAGONS
    DEFAULTS = NUMBERS + HONORS + FLOWER

    EVENS = [MANS[i] for i in range(1, 9, 2)] + [PINS[i] for i in range(1, 9, 2)] + [SOUS[i] for i in range(1, 9, 2)]
    FIVES = [MANS[4] + PINS[4] + SOUS[4]]
    NUMBER_COUNT = [0 for i in range(10)]
    LOWER_FOURS = MANS[:4] + PINS[:4] + SOUS[:4]
    UPPER_FOURS = MANS[5:] + PINS[5:] + SOUS[5:]
    LOWERS = MANS[:3] + PINS[:3] + SOUS[:3]
    MIDDLES = MANS[3:6] + PINS[3:6] + SOUS[3:6]
    UPPERS = MANS[6:] + PINS[6:] + SOUS[6:]

    TERMINALS = [MANS[0], MANS[8], PINS[0], PINS[8], SOUS[0], SOUS[8]]
    TERMINALS_AND_HONORS = TERMINALS + HONORS

    STRAIGHT_STARTS = MANS[0:7] + PINS[0:7] + SOUS[0:7]
    PARTIAL_STRAIGHT_STARTS = MANS[0:8] + PINS[0:8] + SOUS[0:8]

    SIMPLES = MANS[1:8] + PINS[1:8] + SOUS[1:8]
    GREENS = [SOUS[1], SOUS[2], SOUS[3], SOUS[5], SOUS[7], DRAGONS[1]]
    REVERSEABLE = [PINS[0], PINS[1], PINS[2], PINS[3], PINS[4], PINS[7], PINS[8],
                   SOUS[1], SOUS[3], SOUS[4], SOUS[5], SOUS[7], SOUS[8], DRAGONS[0]]
