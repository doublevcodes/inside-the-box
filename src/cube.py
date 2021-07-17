from blessed.formatters import FormattingString


class Cube(dict):
    """Class to store and manipulate the Rubik's Cube."""

    def __init__(self, colours: tuple[FormattingString, ...]) -> None:
        self.colours = colours
        super().__init__({face_name: [i for _ in range(9)]
                          for i, face_name in enumerate(("F", "B", "R", "L", "U", "D"))})

    def render(self, sq_height: int = 2) -> str:
        """Return a string representation of the cube."""
        output = ""
        sq_width = int(2.5 * sq_height)
        height_of_bottom_view = 3 * sq_height + 4
        total_width_of_whole = 4 + (sq_width + (height_of_bottom_view - 1) * 2) * 3

        # ------------------------------------------------------------
        # top view
        height_of_top_view = 3 * sq_height + 4
        # print(height_of_top_view)
        top_grid_check = int((height_of_top_view - 1) / 3)

        # calculation of vertical indexes
        v_indexes = []
        for i in range(height_of_top_view - 1, 0, -1):
            number_of_spaces_before = int(((total_width_of_whole - 4) - (sq_width + i * 2) * 3) / 2)
            if i % top_grid_check == 0:
                v_indexes.append(number_of_spaces_before)

        # print(v_indexes)

        for i in range(height_of_top_view - 1, 0, -1):
            # print(i)
            # calculation of previous spaces
            # total_width_of_whole = 120 if 4 height of single square
            # number of spaces, padding before the middle section
            number_of_spaces_before = int(((total_width_of_whole - 4) - (sq_width + i * 2) * 3) / 2)
            # print(number_of_spaces_before)
            # vertical grids in top left section
            if number_of_spaces_before != 0:
                output += '|'

            if i % top_grid_check != 0:
                if v_indexes[0] < number_of_spaces_before - 1 < v_indexes[1]:
                    output += self.colours[self['L'][0]](' ' * (number_of_spaces_before - 1))
                elif v_indexes[1] < number_of_spaces_before - 1 < v_indexes[2]:
                    # print(v_indexes[1], end="")
                    output += self.colours[self['L'][0]](' ' * (v_indexes[1] - 1))
                    output += '|'
                    output += self.colours[self['L'][1]](' ' * (number_of_spaces_before - v_indexes[1] - 1))
                else:
                    output += self.colours[self['L'][0]](' ' * (v_indexes[1] - 1))
                    output += '|'
                    output += self.colours[self['L'][1]](' ' * (v_indexes[1] - 1))
                    output += '|'
                    output += self.colours[self['L'][2]](' ' * (number_of_spaces_before - v_indexes[2] - 1))
            else:
                # print("-" * (number_of_spaces_before - 1), end="")
                if i % (sq_height + 1) == 0:
                    # print("-" * (number_of_spaces_before - 1), end="")
                    if i == (sq_height + 1):
                        output += self.colours[self['L'][0]](' ' * int((number_of_spaces_before - 1) / 2))
                        output += '|'
                        output += self.colours[self['L'][1]](' ' * int((number_of_spaces_before - 1) / 2))
                    elif i == (sq_height + 1) * 2:
                        output += self.colours[self['L'][0]](' ' * (number_of_spaces_before - 1))
                    else:
                        # should never reach this point but if it does
                        output += '-' * (number_of_spaces_before - 1)
                        # print(i,end="")

            # code for blank lines, will be inside the \||/ only
            if i % top_grid_check == 0:
                output += '\\'
                output += '-' * (sq_width + i * 2)
                output += '\\'
                output += '-' * (sq_width + i * 2)
                output += '/'
                output += '-' * (sq_width + i * 2)
                output += '/'
            else:
                # middle part of top view
                output += '\\'
                if i <= sq_height + 1:
                    output += self.colours[self['U'][6]](' ' * (sq_width + i * 2))
                elif i <= sq_height * 2 + 1:
                    output += self.colours[self['U'][3]](' ' * (sq_width + i * 2))
                else:
                    output += self.colours[self['U'][0]](' ' * (sq_width + i * 2))

                output += '\\'
                if i <= sq_height + 1:
                    output += self.colours[self['U'][7]](' ' * (sq_width + i * 2))
                elif i <= sq_height * 2 + 1:
                    output += self.colours[self['U'][4]](' ' * (sq_width + i * 2))
                else:
                    output += self.colours[self['U'][1]](' ' * (sq_width + i * 2))

                output += '/'
                if i <= sq_height + 1:
                    output += self.colours[self['U'][8]](' ' * (sq_width + i * 2))
                elif i <= sq_height * 2 + 1:
                    output += self.colours[self['U'][5]](' ' * (sq_width + i * 2))
                else:
                    output += self.colours[self['U'][2]](' ' * (sq_width + i * 2))

                output += '/'

            # number of spaces, padding after the middle section

            # vertical bars at the top right section
            # print("q" * (number_of_spaces_before - 1), end="")

            if i % top_grid_check != 0:
                if v_indexes[0] < number_of_spaces_before - 1 < v_indexes[1]:
                    output += self.colours[self['R'][2]](' ' * (number_of_spaces_before - 1))
                elif v_indexes[1] < number_of_spaces_before - 1 < v_indexes[2]:
                    # print(v_indexes[1], end="")
                    output += self.colours[self['R'][1]](' ' * (number_of_spaces_before - v_indexes[1] - 1))
                    output += '|'
                    output += self.colours[self['R'][2]](' ' * (v_indexes[1] - 1))
                else:
                    output += self.colours[self['R'][0]](' ' * (number_of_spaces_before - v_indexes[2] - 1))
                    output += '|'
                    output += self.colours[self['R'][1]](' ' * (v_indexes[1] - 1))
                    output += '|'
                    output += self.colours[self['R'][2]](' ' * (v_indexes[1] - 1))
            else:
                # print("6" * (number_of_spaces_before - 1), end="")
                if i % (sq_height + 1) == 0:
                    # print("-" * (number_of_spaces_before - 1), end="")
                    if i == (sq_height + 1):
                        output += self.colours[self['R'][1]](' ' * int((number_of_spaces_before - 1) / 2))
                        output += '|'
                        output += self.colours[self['R'][2]](' ' * int((number_of_spaces_before - 1) / 2))
                    elif i == (sq_height + 1) * 2:
                        output += self.colours[self['R'][2]](' ' * (number_of_spaces_before - 1))
                    else:
                        # should never reach this point but if it does
                        output += '-' * (number_of_spaces_before - 1)

            if number_of_spaces_before != 0:
                output += '|'
            output += '\n'

        # ------------------------------------------------------------
        # middle grid - front face - 3x3 box - 4 lines of same length
        height_of_middle_view = 3 * sq_height + 4
        number_of_spaces_before = int(((total_width_of_whole - 4) - sq_width * 3) / 2)
        diagonal_height = sq_height + 2
        diagonal_segment = int((number_of_spaces_before - 3) / diagonal_height)
        # print(height_of_middle_view)
        # print(diagonal_height)

        width_indexes = []
        # first diagonal indexes calculation
        for i in range(0, diagonal_height):
            inner_w_index = [i, i * diagonal_segment, i * diagonal_segment + (diagonal_segment - 1)]
            width_indexes.append(inner_w_index)

        # reversed values for lower diagonal
        lower_diagonal_indexes = width_indexes.copy()
        lower_diagonal_indexes.reverse()

        # lines with no diagonal indications
        for i in range(0, height_of_middle_view - diagonal_height * 2):
            inner_w_index = [i + diagonal_height, -1, -1]
            width_indexes.append(inner_w_index)

        # second diagonal indexes calculation
        for i in range(0, diagonal_height):
            inner_w_index = [i + height_of_middle_view - diagonal_height,
                             lower_diagonal_indexes[i][1],
                             lower_diagonal_indexes[i][2]]
            width_indexes.append(inner_w_index)

        # index calculations for after middle section
        (width_right_indexes) = width_indexes.copy()
        right_diagonal_indexes = []

        for i in range(0, diagonal_height):
            right_diagonal_indexes.append(width_indexes[i])

        right_diagonal_indexes.reverse()

        for i in range(0, diagonal_height):
            width_right_indexes[i] = right_diagonal_indexes[i]
            width_right_indexes[height_of_middle_view - i - 1] = right_diagonal_indexes[i]

        singe_face_vertical = int((number_of_spaces_before - 3) / 3)
        # print(width_indexes)
        for h in range(0, len(width_indexes)):
            for num in range(0, len(width_indexes[h])):
                if width_indexes[h][num] > singe_face_vertical * 2 + 1:
                    if num != 0:
                        width_indexes[h][num] += 2
                elif width_indexes[h][num] > singe_face_vertical:
                    if num != 0:
                        width_indexes[h][num] += 1

        # ACTUAL MIDDLE LOOP
        for i in range(0, height_of_middle_view):

            # space padding before middle
            number_of_spaces_before = int(((total_width_of_whole - 4) - sq_width * 3) / 2)
            # print(int((number_of_spaces_before - 3)), end="")
            output += '|'
            before_middle_begins = int((number_of_spaces_before - 3)) + 2
            singe_face_vertical = int((number_of_spaces_before - 3) / 3)
            # print(singe_face_vertical)
            for j in range(0, before_middle_begins):
                if j == singe_face_vertical or j == singe_face_vertical * 2 + 1:
                    output += '|'
                else:
                    if width_indexes[i][1] <= j <= width_indexes[i][2]:
                        if j == width_indexes[i][1] or j == width_indexes[i][2]:
                            if i > int(height_of_middle_view / 2):
                                output += '/'
                            else:
                                output += '\\'
                        elif j > width_indexes[i][1] or j < width_indexes[i][2]:
                            output += '-'
                    else:
                        if j > width_indexes[i][1]:
                            if width_indexes[i][1] == -1:
                                if j < singe_face_vertical:
                                    output += self.colours[self['L'][3]](' ')
                                elif j < singe_face_vertical * 2 + 1:
                                    output += self.colours[self['L'][4]](' ')
                                else:
                                    output += self.colours[self['L'][5]](' ')
                            else:
                                # NEED HEIGHT /2 logic and then if else logic
                                if i > int(height_of_middle_view / 2):
                                    if j < singe_face_vertical:
                                        output += self.colours[self['L'][6]](' ')
                                    elif j < singe_face_vertical * 2 + 1:
                                        output += self.colours[self['L'][7]](' ')
                                    else:
                                        output += self.colours[self['L'][8]](' ')
                                    # print("k",end="")
                                else:
                                    if j < singe_face_vertical:
                                        output += self.colours[self['L'][0]](' ')
                                    elif j < singe_face_vertical * 2 + 1:
                                        output += self.colours[self['L'][1]](' ')
                                    else:
                                        output += self.colours[self['L'][2]](' ')
                                    # print("o",end="")
                                # print("g", end="")
                        else:
                            if j < singe_face_vertical:
                                output += self.colours[self['L'][3]](' ')
                            elif j < singe_face_vertical * 2 + 1:
                                output += self.colours[self['L'][4]](' ')
                            else:
                                output += self.colours[self['L'][5]](' ')
                            # print("b", end="")

            # code for blank lines, will be inside the |||| only
            if i % top_grid_check == 0:
                output += '|'
                output += '-' * sq_width
                output += '|'
                output += '-' * sq_width
                output += '|'
                output += '-' * sq_width
                output += '|'
            else:
                # middle part of middle part
                output += '|'
                if i <= sq_height + 1:
                    output += self.colours[self['B'][0]](' ' * sq_width)
                elif i <= sq_height * 2 + 1:
                    output += self.colours[self['B'][3]](' ' * sq_width)
                else:
                    output += self.colours[self['B'][6]](' ' * sq_width)

                output += '|'
                if i <= sq_height + 1:
                    output += self.colours[self['B'][1]](' ' * sq_width)
                elif i <= sq_height * 2 + 1:
                    output += self.colours[self['B'][4]](' ' * sq_width)
                else:
                    output += self.colours[self['B'][7]](' ' * sq_width)

                output += '|'
                if i <= sq_height + 1:
                    output += self.colours[self['B'][2]](' ' * sq_width)
                elif i <= sq_height * 2 + 1:
                    output += self.colours[self['B'][5]](' ' * sq_width)
                else:
                    output += self.colours[self['B'][8]](' ' * sq_width)

                output += '|'

            before_middle_begins = int((number_of_spaces_before - 3)) + 2
            singe_face_vertical = int((number_of_spaces_before - 3) / 3)
            # print(singe_face_vertical)
            for j in range(0, before_middle_begins):
                if j == singe_face_vertical or j == singe_face_vertical * 2 + 1:
                    output += '|'
                else:
                    if width_right_indexes[i][1] <= j <= width_right_indexes[i][2]:
                        if j == width_right_indexes[i][1] or j == width_right_indexes[i][2]:
                            if i > int(height_of_middle_view / 2):
                                output += '\\'
                            else:
                                output += '/'
                        elif j > width_right_indexes[i][1] or j < width_right_indexes[i][2]:
                            output += '-'
                    else:
                        if j > width_right_indexes[i][1]:
                            if j < singe_face_vertical:
                                output += self.colours[self['R'][3]](' ')
                            elif j < singe_face_vertical * 2 + 1:
                                output += self.colours[self['R'][4]](' ')
                            else:
                                output += self.colours[self['R'][5]](' ')
                        else:
                            if i > int(height_of_middle_view / 2):
                                if j < singe_face_vertical:
                                    output += self.colours[self['R'][6]](' ')
                                elif j < singe_face_vertical * 2 + 1:
                                    output += self.colours[self['R'][7]](' ')
                                else:
                                    output += self.colours[self['R'][8]](' ')
                                # print("k",end="")
                            else:
                                if j < singe_face_vertical:
                                    output += self.colours[self['R'][0]](' ')
                                elif j < singe_face_vertical * 2 + 1:
                                    output += self.colours[self['R'][1]](' ')
                                else:
                                    output += self.colours[self['R'][2]](' ')

                                # print("y", end="")
            output += "|\n"
        # ------------------------------------------------------------
        # bottom view
        height_of_bottom_view = 3 * sq_height + 4
        # print(height_of_bottom_view)
        for i in range(1, height_of_bottom_view):

            # same padding we provided before top we need to keep before
            number_of_spaces_before = int(((total_width_of_whole - 4) - (sq_width + i * 2) * 3) / 2)

            # vertical bars at start of bottom left section
            if number_of_spaces_before != 0:
                output += '|'

            # print("z" * (number_of_spaces_before - 1), end="")
            if i % top_grid_check != 0:
                if v_indexes[0] < number_of_spaces_before - 1 < v_indexes[1]:
                    output += self.colours[self['L'][6]](' ' * (number_of_spaces_before - 1))
                elif v_indexes[1] < number_of_spaces_before - 1 < v_indexes[2]:
                    # print(v_indexes[1], end="")
                    output += self.colours[self['L'][6]](' ' * (v_indexes[1] - 1))
                    output += '|'
                    output += self.colours[self['L'][7]](' ' * (number_of_spaces_before - v_indexes[1] - 1))
                else:
                    output += self.colours[self['L'][6]](' ' * (v_indexes[1] - 1))
                    output += '|'
                    output += self.colours[self['L'][7]](' ' * (v_indexes[1] - 1))
                    output += '|'
                    output += self.colours[self['L'][8]](' ' * (number_of_spaces_before - v_indexes[2] - 1))
            else:
                # print("8" * (number_of_spaces_before - 1), end="")
                if i % (sq_height + 1) == 0:
                    # print("-" * (number_of_spaces_before - 1), end="")
                    if i == (sq_height + 1):
                        output += self.colours[self['L'][6]](' ' * int((number_of_spaces_before - 1) / 2))
                        output += '|'
                        output += self.colours[self['L'][7]](' ' * int((number_of_spaces_before - 1) / 2))
                    elif i == (sq_height + 1) * 2:
                        output += self.colours[self['L'][6]](' ' * (number_of_spaces_before - 1))
                    else:
                        # should never reach this point but if it does
                        output += '-' * (number_of_spaces_before - 1)

            # print(number_of_spaces_before)

            # code for blank lines, will be inside the |||| only
            if i % top_grid_check == 0:
                # middle part of bottom view
                output += '/'
                output += '-' * (sq_width + i * 2)
                output += '/'
                output += '-' * (sq_width + i * 2)
                output += '\\'
                output += '-' * (sq_width + i * 2)
                output += '\\'
            else:
                # middle part of bottom view
                output += '/'

                if i <= sq_height + 1:
                    output += self.colours[self['D'][0]](' ' * (sq_width + i * 2))
                elif i <= sq_height * 2 + 1:
                    output += self.colours[self['D'][3]](' ' * (sq_width + i * 2))
                else:
                    output += self.colours[self['D'][6]](' ' * (sq_width + i * 2))
                # print(' ' * (sq_width + i*2), end="")
                output += '/'
                if i <= sq_height + 1:
                    output += self.colours[self['D'][1]](' ' * (sq_width + i * 2))
                elif i <= sq_height * 2 + 1:
                    output += self.colours[self['D'][4]](' ' * (sq_width + i * 2))
                else:
                    output += self.colours[self['D'][7]](' ' * (sq_width + i * 2))
                output += '\\'
                if i <= sq_height + 1:
                    output += self.colours[self['D'][2]](' ' * (sq_width + i * 2))
                elif i <= sq_height * 2 + 1:
                    output += self.colours[self['D'][5]](' ' * (sq_width + i * 2))
                else:
                    output += self.colours[self['D'][8]](' ' * (sq_width + i * 2))
                output += '\\'

            # same padding we provided before top we need to keep after also
            # vertical bars at the top right section
            if i % top_grid_check != 0:
                if v_indexes[0] < number_of_spaces_before - 1 < v_indexes[1]:
                    output += self.colours[self['R'][8]](' ' * (number_of_spaces_before - 1))
                elif v_indexes[1] < number_of_spaces_before - 1 < v_indexes[2]:
                    # print(v_indexes[1], end="")
                    output += self.colours[self['R'][7]](' ' * (number_of_spaces_before - v_indexes[1] - 1))
                    output += '|'
                    output += self.colours[self['R'][8]](' ' * (v_indexes[1] - 1))
                else:
                    output += self.colours[self['R'][6]](' ' * (number_of_spaces_before - v_indexes[2] - 1))
                    output += '|'
                    output += self.colours[self['R'][7]](' ' * (v_indexes[1] - 1))
                    output += '|'
                    output += self.colours[self['R'][8]](' ' * (v_indexes[1] - 1))
            else:
                # print("-" * (number_of_spaces_before - 1), end="")
                if i % (sq_height + 1) == 0:
                    # print("-" * (number_of_spaces_before - 1), end="")
                    if i == (sq_height + 1):
                        output += self.colours[self['R'][7]](' ' * int((number_of_spaces_before - 1) / 2))
                        output += '|'
                        output += self.colours[self['R'][8]](' ' * int((number_of_spaces_before - 1) / 2))
                    elif i == (sq_height + 1) * 2:
                        output += self.colours[self['R'][8]](' ' * (number_of_spaces_before - 1))
                    else:
                        # should never reach this point but if it does
                        output += '-' * (number_of_spaces_before - 1)

            if number_of_spaces_before != 0:
                output += '|'
            output += '\n'

        return output
