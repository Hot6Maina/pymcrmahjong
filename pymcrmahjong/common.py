from enum import Enum, auto


class UpperStrEnum(str, Enum):
    def _generate_next_value_(name, start, count, last_values):
        return name.upper()


class TileTypeEnum(UpperStrEnum):
    MAN = auto()
    PIN = auto()
    SOU = auto()
    WIND = auto()
    DRAGON = auto()
    FLOWER = auto()
    ETC = auto()


class CallTypeEnum(UpperStrEnum):
    CHII = auto()
    PON = auto()
    CONCEALED_KAN = auto()
    BIG_MELDED_KAN = auto()
    SMALL_MELDED_KAN = auto()


class DivisionPartTypeEnum(UpperStrEnum):
    HEAD = auto()
    SEQUENCE = auto()
    TRIPLE = auto()
    QUAD = auto()
    KNITTED = auto()
    HONORS = auto()
    THIRTEEN_ORPHANS = auto()


class HandShapeEnum(UpperStrEnum):
    SEVEN_PAIRS = auto()
    THIRTEEN_ORPHANS = auto()
    HONORS_AND_KITTED_TILES = auto()
    BASE = auto()


class WaitEnum(UpperStrEnum):
    SINGLE_WAIT = auto()
    CLOSED_WAIT = auto()
    EDGE_WAIT = auto()
    ELSE_WAIT = auto()


class BodyFuReasonEnum(UpperStrEnum):
    OPENED_NORMAL_TRIPLE = auto()
    OPENED_OUTSIDE_TRIPLE = auto()
    CONCEALED_NORMAL_TRIPLE = auto()
    CONCEALED_OUTSIDE_TRIPLE = auto()

    OPENED_NORMAL_QUAD = auto()
    OPENED_OUTSIDE_QUAD = auto()
    CONCEALED_NORMAL_QUAD = auto()
    CONCEALED_OUTSIDE_QUAD = auto()


# FuReasonEnum = (
#     HandShapeFuReasonEnum
#     | WaitFuReasonEnum
#     | HeadFuReasonEnum
#     | AgariTypeFuReasonEnum
#     | BodyFuReasonEnum
# )


class YakuEnum(UpperStrEnum):
    # 88 points
    BIG_FOUR_WINDS = auto()
    BIG_THREE_DRAGONS = auto()
    ALL_GREEN = auto()
    NINE_GATES = auto()
    FOUR_KONGS = auto()
    SEVEN_SHIFTED_PAIRS = auto()
    THIRTEEN_ORPHANS = auto()

    # 64 points
    ALL_TERMINALS = auto()
    LITTLE_FOUR_WINDS = auto()
    LITTLE_THREE_DRAGONS = auto()
    ALL_HONORS = auto()
    FOUR_CONCEALED_PUNGS = auto()
    PURE_TERMINAL_CHOWS = auto()

    # 48 points
    QUADRUPLE_CHOW = auto()
    FOUR_PURE_SHIFTED_PUNGS = auto()

    # 32 points
    FOUR_PURE_SHIFTED_CHOWS = auto()
    THREE_KONGS = auto()
    ALL_TERMINALS_AND_HONORS = auto()

    # 24 points
    SEVEN_PAIRS = auto()
    GREATER_HONORS_AND_KNITTED_TILES = auto()
    ALL_EVEN_PUNGS = auto()
    FULL_FLUSH = auto()
    PURE_TRIPLE_CHOW = auto()
    PURE_SHIFTED_PUNGS = auto()
    UPPER_TILES = auto()
    MIDDLE_TILES = auto()
    LOWER_TILES = auto()

    # 16 points
    PURE_STRAIGHT = auto()
    THREE_SUITED_TERMINAL_CHOWS = auto()
    PURE_SHIFTED_CHOWS = auto()
    ALL_FIVES = auto()
    TRIPLE_PUNG = auto()
    THREE_CONCEALED_PUNGS = auto()

    # 12 points
    LESSER_HONORS_AND_KNITTED_TILES = auto()
    KNITTED_STRAIGHT = auto()
    UPPER_FOUR = auto()
    LOWER_FOUR = auto()
    BIG_THREE_WINDS = auto()

    # 8 points
    MIXED_STRAIGHT = auto()
    REVERSIBLE_TILES = auto()
    MIXED_TRIPLE_CHOW = auto()
    CHICKEN_HAND = auto()
    LAST_TILE_DRAW = auto()
    LAST_TILE_CLAIM = auto()
    OUT_WITH_REPLACEMENT_TILE = auto()
    ROBBING_THE_KONG = auto()
    TWO_CONCEALED_KONGS = auto()

    # 6 points
    ALL_PUNGS = auto()
    HALF_FLUSH = auto()
    MIXED_SHIFTED_CHOWS = auto()
    ALL_TYPES = auto()
    MELDED_HAND = auto()
    TWO_DRAGONS_PUNGS = auto()

    # 4 points
    OUTSIDE_HAND = auto()
    FULLY_CONCEALED_HAND = auto()
    TWO_MELDED_KONGS = auto()
    LAST_TILE = auto()

    # 2 points
    DRAGON_PUNG = auto()
    PREVALENT_WIND = auto()
    SEAT_WIND = auto()
    CONCEALED_HAND = auto()
    ALL_CHOWS = auto()
    TILE_HOG = auto()
    DOUBLE_PUNG = auto()
    TWO_CONCEALED_PUNGS = auto()
    CONCEALED_KONG = auto()
    ALL_SIMPLES = auto()

    # 1 point
    PURE_DOUBLE_CHOW = auto()
    MIXED_DOUBLE_CHOW = auto()
    SHORT_STRAIGHT = auto()
    TWO_TERMINAL_CHOWS = auto()
    PUNG_OF_TERMINALS_OR_HONORS = auto()
    MELDED_KONG = auto()
    ONE_VOIDED_SUIT = auto()
    NO_HONORS = auto()
    EDGE_WAIT = auto()
    CLOSED_WAIT = auto()
    SINGLE_WAIT = auto()
    SELF_DRAWN = auto()
    FLOWER = auto()