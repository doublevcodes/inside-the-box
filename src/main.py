import os
from collections import namedtuple
from configparser import ConfigParser
from enum import Enum, auto
from pathlib import Path
from typing import Optional

from blessed import Terminal, keyboard

from cube import Cube

SOFTWARE_NAME = "Terminal Rubik's Cube"


class Actions(Enum):
    """Enum to store control actions."""

    ORBIT = auto()
    ROTATE = auto()


class Application:
    """Application class to handle the program whilst running."""

    def __init__(self) -> None:
        """Initialise variables such as the terminal and load configuration data."""
        # get config path and make it if it doesn't exist
        self.config = ConfigParser()
        self.config_path = Path(
            os.environ.get("APPDATA")
            or os.environ.get("XDG_CONFIG_HOME")
            or (Path(os.environ.get("HOME")) / ".config")
        ) / SOFTWARE_NAME
        self.config_path.mkdir(parents=True, exist_ok=True)
        self.config_path /= "config.ini"

        # load default config then override with user config (if defined)
        # invalid values entered in the config will be ignored
        self.config.read("default_config.ini")
        if self.config_path.exists():
            self.config.read(self.config_path)

        control = namedtuple("Control", "action param")
        key_groups = {
            "orbit_left": control(Actions.ORBIT, "left"),
            "orbit_right": control(Actions.ORBIT, "right"),
            "orbit_up": control(Actions.ORBIT, "up"),
            "orbit_down": control(Actions.ORBIT, "down"),
            "front": control(Actions.ROTATE, "front"),
            "back": control(Actions.ROTATE, "back"),
            "top": control(Actions.ROTATE, "up"),
            "bottom": control(Actions.ROTATE, "down"),
            "left": control(Actions.ROTATE, "left"),
            "right": control(Actions.ROTATE, "right"),
            "anti_clockwise": control(Actions.ROTATE, "anti_clockwise"),
            "one_eighty": control(Actions.ROTATE, "one_eighty")
        }

        # re-map commands from control=key to {key: control} for every defined control
        # control is composed of an action and a parameter, and each action is managed by a separate function
        self.keymap = {}
        config_controls = self.config["controls"]
        for k, v in key_groups.items():
            for key in config_controls[k].split('|'):
                self.keymap[key] = v

        # set up terminal, clear screen and set colours to specified values in config
        self.term = Terminal()
        print(self.term.home)
        if (rgb_colour := self.hex_to_rgb(self.config["colours"]["foreground"])) is not None:
            print(self.term.color_rgb(*rgb_colour))
        if (rgb_colour := self.hex_to_rgb(self.config["colours"]["background"])) is not None:
            print(self.term.on_color_rgb(*rgb_colour))
        print(self.term.clear)

        # initialise cube from config, defaulting to black if a colour is invalid
        self.cube = Cube(tuple(self.term.on_color_rgb(*(self.hex_to_rgb(self.config["colours"][str(i)]) or (0, 0, 0)))
                               for i in range(6)))  # todo load from config (status)

        self.last_command = ''
        self.parsed = []
        self.command_string_lookup = {"front": 'F', "back": 'B', "left": 'L', "right": 'R', "up": 'U', "down": 'D',
                                      "one_eighty": '2', 'anti_clockwise': "'", '': ''}
        self.modifiers = ("anti_clockwise", "one_eighty", '')  # the empty strings are for the initial value

    @staticmethod
    def hex_to_rgb(colour_string: str) -> Optional[tuple]:
        """Return a tuple of rgb values, or None if the hex string is invalid."""
        colour_string = colour_string.lstrip('#')
        try:
            rgb = tuple(int(colour_string[i:i+2], 16) for i in (0, 2, 4))
            return rgb
        except ValueError:
            return None

    def commands_as_string(self) -> str:
        """Return a string representation of the current list of commands."""
        # a better way to do this (and controls in general) would be to use enums for actions and parameters, however
        # due to time constraints, I am going to leave it at this rather than refactoring now
        output = ""
        for command in self.parsed:
            output += self.command_string_lookup[command.face]
            if command.modifier:
                output += self.command_string_lookup[command.modifier]
        output += f"({self.command_string_lookup['' if self.last_command in self.modifiers else self.last_command]})"
        return output

    def on_exit(self) -> None:
        """Shut down gracefully and save the config."""
        print(self.term.normal)
        # todo update cube in config here i.e. call function on cube to get it in this format, and set config key
        with open(self.config_path, "w") as f:
            self.config.write(f)

    def draw(self, string: str, x: int, y: int) -> None:
        """Draw a multiline string @ (x, y) on the screen without disrupting other parts of the screen."""
        for row, line in enumerate(string.split('\n')):
            print(f"{self.term.move_xy(x, y + row)}{line}")

    def update_screen(self) -> None:
        """Update the screen with the new data."""
        print(self.term.clear)
        # draw cube todo use config height or get terminal height
        self.draw(self.cube.render(2), 2, 2)
        # clear line then draw current commands
        print(f"{self.term.home}{self.term.clear_eol}{self.term.home}{self.commands_as_string()}")

    def try_parse(self, action: str, *, force: bool = False) -> None:
        """Try to parse the current commands."""
        # parsing could be improved by using enums and making 'command' static if we have time
        command = namedtuple("Command", "face modifier")

        # parse the commands
        if force:
            # if we are forcing it, we don't care what the last action is, and modifiers don't matter
            if action not in self.modifiers:
                self.parsed.append(command(action, None))
        elif self.last_command not in self.modifiers:
            # if the last action is a face (and force is false), we are either adding a face or a modified face
            if action in self.modifiers:
                self.parsed.append(command(self.last_command, action))
            else:
                self.parsed.append(command(self.last_command, None))

        self.last_command = action

    def execute_commands(self) -> None:
        """Execute the current commands."""
        for command in self.parsed:
            pass  # call cube's rotate/twist function here with modifier or resolve the modifier if necessary

        # remove executed commands
        self.parsed = []

    def run(self) -> None:
        """Run the main loop, handling key presses and rendering the scene."""
        with self.term.fullscreen(), self.term.cbreak(), self.term.hidden_cursor():
            val = keyboard.Keystroke()
            # keep running until q or esc is pressed, or a keyboard interrupt is received
            try:
                while val.lower() != 'q' and val.code != 361:
                    # if the key is contained within the key map, fetch the associated action and execute it
                    if (key := str(val.code or val)) in self.keymap.keys():
                        action = self.keymap[key]
                        if action.action == Actions.ORBIT:
                            pass  # change view angle here
                        elif action.action == Actions.ROTATE:
                            # if there is time, refactoring the control scheme to accept combos for modifiers would be
                            # good, e.g. SHIFT + FACE = ANTI CLOCKWISE etc.
                            if self.config["controls"]["input_type"] == "auto":  # see config for input type details
                                force = self.config["controls"].getboolean("do_instant")
                                self.try_parse(action.param, force=force)
                                self.execute_commands()
                            else:
                                self.try_parse(action.param)
                    elif val.is_sequence and val.code == 343:
                        self.execute_commands()
                    # if we have time, adding backspace to remove a command or undo would be useful

                    self.update_screen()
                    val = self.term.inkey()
            except KeyboardInterrupt:
                pass
            self.on_exit()


if __name__ == "__main__":
    Application().run()  # todo use arg parse to provide help, plus add option to clear config
