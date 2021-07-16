from enum import Enum, auto
from typing import Any

from blessed import Terminal

term = Terminal()


class ColourMeta(Enum):
    """
    Enumeration from which Colour derives in order to provide custom auto() function.

    This enum defines a custom auto() function through the _generate_next_value_() function, which enum.Enum
    uses internally. It makes the auto() function return the enum value's name but in all lowercase
    """

    def _generate_next_value_(name: str, start: int, count: int, last_values: list[Any]) -> Any:
        return name.lower()


class Colour(ColourMeta):
    """
    An enumeration holding all possible values for the colours present on a cube.

    This enum derives from ColourMeta so that all enumeration values are their name, but in lower
    case. Therefore:

        >>> print(repr(Colour.WHITE))
        <Colour.WHITE: 'white'>

    This decision was merely arbitrary but follows a more meaningful convention than assigning each enum
    value a number in increasing order.
    """

    UNDEFINED = auto()
    WHITE = term.on_white
    YELLOW = term.on_yellow
    RED = term.on_red
    INDIGO = term.on_indigo
    BLUE = term.on_blue
    GREEN = term.on_green
