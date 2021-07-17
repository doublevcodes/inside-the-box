import os
from collections import namedtuple
from configparser import ConfigParser
from enum import Enum, auto
from pathlib import Path
from typing import Optional

from blessed import Terminal, keyboard

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
            "top": control(Actions.ROTATE, "top"),
            "bottom": control(Actions.ROTATE, "bottom"),
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
            for key in config_controls[k].split('¦'):
                self.keymap[key] = v

        # initialise cube from config here i.e. self.cube = Cube.from_config(...) or similar

        # set up terminal, clear screen and set colours to specified values in config
        self.term = Terminal()
        print(self.term.home)
        if (rgb_colour := self.hex_to_rgb(self.config["colours"]["foreground"])) is not None:
            print(self.term.color_rgb(*rgb_colour))
        if (rgb_colour := self.hex_to_rgb(self.config["colours"]["background"])) is not None:
            print(self.term.on_color_rgb(*rgb_colour))
        print(self.term.clear)

        self.commands = []

    @staticmethod
    def hex_to_rgb(colour_string: str) -> Optional[tuple]:
        """Return a tuple of rgb values, or None if the hex string is invalid."""
        colour_string.lstrip('#')
        try:
            rgb = tuple(int(colour_string[i:i+2], 16) for i in (0, 2, 4))
            return rgb
        except ValueError:
            return None

    def on_exit(self) -> None:
        """Shut down gracefully and save the config."""
        print(self.term.normal)
        # update cube in config here i.e. call function on cube to get it in this format, and set config key
        with open(self.config_path, "w") as f:
            self.config.write(f)

    def update_screen(self) -> None:
        """Update the screen with the new data."""
        # draw cube here
        # draw current commands here
        pass

    def try_execute(self, *, force: bool = False) -> None:
        """Try to execute the current commands."""
        # parse the commands
        parsed = []
        command = namedtuple("Command", "face modifier")
        modifiers = ("anti_clockwise", "one_eighty")
        for i, action in enumerate(self.commands):
            if action in modifiers:
                # modifiers are caught by the previous action, so skip them
                # this does, however, mean multiple modifiers in a row are ignored
                continue
            elif i == len(self.commands) - 1:
                # only process an ambiguous last command if force is true
                if force:
                    parsed.append(command(action, None))
            elif self.commands[i + 1] not in modifiers:
                parsed.append(command(action, None))
            else:
                # if there's a modifier after it, add it with the modifier as well
                parsed.append(command(action, self.commands[i + 1]))

        # remove executed commands
        if force or self.commands[-1] in modifiers:
            self.commands = []
        else:
            self.commands = [self.commands[-1]]

        for command in parsed:
            pass  # call cube's rotate/twist function here with modifier or resolve the modifier if necessary

    def run(self) -> None:
        """Run the main loop, handling key presses and rendering the scene."""
        with self.term.fullscreen(), self.term.cbreak():
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
                            self.commands.append(action.param)
                            if self.config["controls"]["input_type"] == "auto":  # see config for input type details
                                force = self.config["controls"].getboolean("do_instant")
                                self.try_execute(force=force)
                    elif val.is_sequence and val.code == 343:
                        self.try_execute(force=True)

                    self.update_screen()
                    val = self.term.inkey()
            except KeyboardInterrupt:
                pass
            self.on_exit()


if __name__ == "__main__":
    Application().run()
