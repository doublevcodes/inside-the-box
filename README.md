# Python Discord Code Jam 8 (Summer 2021) - Virtuous Vultures

Theme: Think Inside the Box

## Project Details

We are "inside" the box, a Rubik's cube to be exact.

## What does the project currently do?

- When you run the program, you can see the inside of a Rubik's cube inside the terminal.
- You can enter in instructions (default u, i, o, j, k, l, m, ', 2) which will show up at the top (unless auto and do-instant are set in the config), and you can execute them, although this does nothing.
- You can change colours, buttons and input methods in a config file

The theme was inside the box, so we literally (figuratively) placed you inside the box. Our box being a Rubik's cube. If you were inside an actual cube you would be able to see 5 sides of the cube with one face not visible as humans don't have eyes on the back of their head.

## Installation

For running the program blessed library along with standard python is enough. You can install blessed by simply running `pip install blessed`

If using pipenv, you can also run `pipenv install` or if you are just using pip you can also run `pip install -r requirements.txt`.

Python 3.9 has been used for this program, and so is recommended, however it may still run on other versions of Python.

## What could've been?

If we were vigilant enough we would've made the program so that User when pressed different keys would actually able to manipulate the cube.

The cube would rotate faces, change colours, and we would give Users an option to scramble the cube, and they would then solve it. Alas, it wasn't finished in time.

## What would've been on the todo list:

* The loading and saving of the cube from config
* Rotate the cube in the view
* The ability to actually rotate sides of the cube
* Few (many) code improvements
* Fix *lots* of bugs
