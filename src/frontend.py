from typing import List

from blessed import Terminal

from cube.colour import Colour

term = Terminal()

SQ_HEIGHT = 2
SQ_WIDTH = SQ_HEIGHT * 2 + int(SQ_HEIGHT / 2)
TOTAL_HEIGHT = 3 * SQ_HEIGHT
TOTAL_WIDTH = 3 * SQ_WIDTH

#  middle top face - top middle frame
color_list = [Colour.WHITE, Colour.YELLOW, Colour.RED,
              Colour.INDIGO, Colour.WHITE, Colour.GREEN,
              Colour.BLUE, Colour.YELLOW, Colour.RED]

#  middle face
color_list2 = [Colour.WHITE, Colour.YELLOW, Colour.RED,
               Colour.INDIGO, Colour.WHITE, Colour.GREEN,
               Colour.BLUE, Colour.YELLOW, Colour.RED]

#  middle bot face
color_list3 = [Colour.WHITE, Colour.YELLOW, Colour.RED,
               Colour.INDIGO, Colour.WHITE, Colour.GREEN,
               Colour.BLUE, Colour.YELLOW, Colour.RED]

#  left face
color_list4 = [Colour.WHITE, Colour.YELLOW, Colour.RED,
               Colour.INDIGO, Colour.WHITE, Colour.GREEN,
               Colour.BLUE, Colour.YELLOW, Colour.RED]

#  right face
color_list5 = [Colour.WHITE, Colour.YELLOW, Colour.RED,
               Colour.INDIGO, Colour.WHITE, Colour.GREEN,
               Colour.BLUE, Colour.YELLOW, Colour.RED]


face_colors = []
face_colors.append(color_list)
face_colors.append(color_list2)
face_colors.append(color_list3)
face_colors.append(color_list4)
face_colors.append(color_list5)

print(face_colors[2][0])


def horizontal_grid_lines(face_colors: List) -> None:
    """Takes List of list of colors as parameter

    List of colors should contain faces in order
    middle top face
    middle face
    middle bot face
    left face
    right face
    """
    height_of_bottom_view = 3 * SQ_HEIGHT + 4
    total_width_of_whole = 4 + (SQ_WIDTH + (height_of_bottom_view-1)*2)*3

    # ------------------------------------------------------------
    # top view
    height_of_top_view = 3 * SQ_HEIGHT + 4
    # print(height_of_top_view)
    top_grid_check = int((height_of_top_view-1)/3)

    # calculation of vertical indexes
    v_indexes = []
    for i in range(height_of_top_view-1, 0, -1):
        number_of_spaces_before = int(((total_width_of_whole-4) - (SQ_WIDTH + i*2)*3)/2)
        if (i % top_grid_check == 0):
            v_indexes.append(number_of_spaces_before)

    # print(v_indexes)

    for i in range(height_of_top_view-1, 0, -1):
        # print(i)
        # calculation of previous spaces
        # total_width_of_whole = 120 if 4 height of single square
        # number of spaces, padding before the middle section
        number_of_spaces_before = int(((total_width_of_whole-4) - (SQ_WIDTH + i*2)*3)/2)
        # print(number_of_spaces_before)
        # vertical grids in top left section
        if (number_of_spaces_before != 0):
            print("|", end="")

        if (i % top_grid_check != 0):
            if (number_of_spaces_before - 1 > v_indexes[0] and number_of_spaces_before - 1 < v_indexes[1]):
                print(face_colors[3][0].value("w" * (number_of_spaces_before - 1)), end="")
            elif (number_of_spaces_before - 1 > v_indexes[1] and number_of_spaces_before - 1 < v_indexes[2]):
                # print(v_indexes[1], end="")
                print(face_colors[3][0].value("a" * (v_indexes[1]-1)), end="")
                print("|", end="")
                print(face_colors[3][1].value("s" * (number_of_spaces_before - v_indexes[1] - 1)), end="")
            else:
                print(face_colors[3][0].value("d" * (v_indexes[1]-1)), end="")
                print("|", end="")
                print(face_colors[3][1].value("e" * (v_indexes[1]-1)), end="")
                print("|", end="")
                print(face_colors[3][2].value("f" * (number_of_spaces_before - v_indexes[2] - 1)), end="")
        else:
            print("-" * (number_of_spaces_before - 1), end="")

        # code for blank lines, will be inside the \||/ only
        if (i % top_grid_check == 0):
            print("\\", end="")
            print("-" * (SQ_WIDTH + i*2), end="")
            print("\\", end="")
            print("-" * (SQ_WIDTH + i*2), end="")
            print("/", end="")
            print("-" * (SQ_WIDTH + i*2), end="")
            print("/", end="")
        else:
            # middle part of top view
            print("\\", end="")
            if i <= SQ_HEIGHT + 1:
                print(face_colors[0][6].value(" " * (SQ_WIDTH + i*2)), end="")
            elif i <= SQ_HEIGHT*2 + 1:
                print(face_colors[0][3].value(" " * (SQ_WIDTH + i*2)), end="")
            else:
                print(face_colors[0][0].value(" " * (SQ_WIDTH + i*2)), end="")

            print("\\", end="")
            if i <= SQ_HEIGHT + 1:
                print(face_colors[0][7].value(" " * (SQ_WIDTH + i*2)), end="")
            elif i <= SQ_HEIGHT*2 + 1:
                print(face_colors[0][4].value(" " * (SQ_WIDTH + i*2)), end="")
            else:
                print(face_colors[0][1].value(" " * (SQ_WIDTH + i*2)), end="")

            print("/", end="")
            if i <= SQ_HEIGHT + 1:
                print(face_colors[0][8].value(" " * (SQ_WIDTH + i*2)), end="")
            elif i <= SQ_HEIGHT*2 + 1:
                print(face_colors[0][5].value(" " * (SQ_WIDTH + i*2)), end="")
            else:
                print(face_colors[0][2].value(" " * (SQ_WIDTH + i*2)), end="")

            print("/", end="")

        # number of spaces, padding after the middle section

        # vertical bars at the top right section
        # print("q" * (number_of_spaces_before - 1), end="")

        if (i % top_grid_check != 0):
            if (number_of_spaces_before - 1 > v_indexes[0] and number_of_spaces_before - 1 < v_indexes[1]):
                print("w" * (number_of_spaces_before - 1), end="")
            elif (number_of_spaces_before - 1 > v_indexes[1] and number_of_spaces_before - 1 < v_indexes[2]):
                # print(v_indexes[1], end="")
                print("a" * (number_of_spaces_before - v_indexes[1] - 1), end="")
                print("|", end="")
                print("s" * (v_indexes[1]-1), end="")
            else:
                print("d" * (number_of_spaces_before - v_indexes[2] - 1), end="")
                print("|", end="")
                print("e" * (v_indexes[1]-1), end="")
                print("|", end="")
                print("f" * (v_indexes[1]-1), end="")
        else:
            print("-" * (number_of_spaces_before - 1), end="")

        if (number_of_spaces_before != 0):
            print("|", end="")
        print()

    # ------------------------------------------------------------
    # middle grid - frontface - 3x3 box - 4 lines of same length
    height_of_middle_view = 3 * SQ_HEIGHT + 4
    number_of_spaces_before = int(((total_width_of_whole - 4) - (SQ_WIDTH)*3)/2)
    diagonal_height = SQ_HEIGHT + 2
    diagonal_segment = int((number_of_spaces_before - 3) / diagonal_height)
    # print(height_of_middle_view)
    # print(diagonal_height)

    width_indexes = []
    # first diagonal indexes calculation
    for i in range(0, diagonal_height):
        inner_w_index = []
        inner_w_index.append(i)
        inner_w_index.append(i*diagonal_segment)
        inner_w_index.append(i*diagonal_segment + (diagonal_segment-1))
        width_indexes.append(inner_w_index)

    # reversed values for lower diagonal
    lower_diagonal_indexes = width_indexes.copy()
    lower_diagonal_indexes.reverse()

    # lines with no diagonal indications
    for i in range(0, height_of_middle_view - diagonal_height*2):
        inner_w_index = []
        inner_w_index.append(i + diagonal_height)
        inner_w_index.append(-1)
        inner_w_index.append(-1)
        width_indexes.append(inner_w_index)

    # second diagonal indexes calculation
    for i in range(0, diagonal_height):
        inner_w_index = []
        inner_w_index.append(i + height_of_middle_view - diagonal_height)
        inner_w_index.append(lower_diagonal_indexes[i][1])
        inner_w_index.append(lower_diagonal_indexes[i][2])
        width_indexes.append(inner_w_index)

    # indexcalculations for after middle section
    (width_right_indexes) = width_indexes.copy()
    right_diagonal_indexes = []

    for i in range(0, diagonal_height):
        right_diagonal_indexes.append(width_indexes[i])

    right_diagonal_indexes.reverse()

    for i in range(0, diagonal_height):

        width_right_indexes[i] = right_diagonal_indexes[i]
        width_right_indexes[height_of_middle_view-i-1] = right_diagonal_indexes[i]

    singe_face_vertical = int((number_of_spaces_before - 3) / 3)
    # print(width_indexes)
    for h in range(0, len(width_indexes)):
        for num in range(0, len(width_indexes[h])):
            if width_indexes[h][num] > singe_face_vertical * 2 + 1:
                if (num != 0):
                    width_indexes[h][num] += 2
            elif width_indexes[h][num] > singe_face_vertical:
                if (num != 0):
                    width_indexes[h][num] += 1

    '''print("MAJOR VARIABLES")
    print("number_of_spaces_before" + str(number_of_spaces_before))
    print("diagonal_height" + str(diagonal_height))
    print("diagonal_segment" + str(diagonal_segment))
    print("total_width_of_whole" + str(total_width_of_whole))
    print("singe_face_vertical" + str(singe_face_vertical))
    '''
    # ACTUAL MIDDLE LOOP
    for i in range(0, height_of_middle_view):

        # space padding before middle
        number_of_spaces_before = int(((total_width_of_whole-4) - (SQ_WIDTH)*3)/2)
        # print(int((number_of_spaces_before -3)), end="")

        print("|", end="")
        before_middle_begins = int((number_of_spaces_before - 3)) + 2
        singe_face_vertical = int((number_of_spaces_before - 3) / 3)
        # print(singe_face_vertical)
        for j in range(0, before_middle_begins):
            if (j == singe_face_vertical or j == singe_face_vertical*2 + 1):
                print("|", end="")
            else:
                if (j >= width_indexes[i][1] and j <= width_indexes[i][2]):
                    if j == width_indexes[i][1] or j == width_indexes[i][2]:
                        if i > int(height_of_middle_view/2):
                            print("/", end="")
                        else:
                            print("\\", end="")
                    elif j > width_indexes[i][1] or j < width_indexes[i][2]:
                        print("-", end="")
                else:
                    if (j > width_indexes[i][1]):
                        print("a", end="")
                    else:
                        print("b", end="")

        '''# vertical bars middle section before face
        print("|", end="")
        print("a" * int((number_of_spaces_before -3)/3), end="")
        print("|", end="")
        print("a" * int((number_of_spaces_before -3)/3), end="")
        print("|", end="")
        print("a" * int((number_of_spaces_before -3)/3), end="")'''

        # code for blank lines, will be inside the |||| only
        if (i % top_grid_check == 0):
            print("|", end="")
            print("-" * (SQ_WIDTH), end="")
            print("|", end="")
            print("-" * (SQ_WIDTH), end="")
            print("|", end="")
            print("-" * (SQ_WIDTH), end="")
            print("|", end="")
        else:
            # middle part of middle part
            print("|", end="")
            if i <= SQ_HEIGHT + 1:
                print(face_colors[1][0].value(" " * (SQ_WIDTH)), end="")
            elif i <= SQ_HEIGHT*2 + 1:
                print(face_colors[1][3].value(" " * (SQ_WIDTH)), end="")
            else:
                print(face_colors[1][6].value(" " * (SQ_WIDTH)), end="")

            print("|", end="")
            if i <= SQ_HEIGHT + 1:
                print(face_colors[1][1].value(" " * (SQ_WIDTH)), end="")
            elif i <= SQ_HEIGHT*2 + 1:
                print(face_colors[1][4].value(" " * (SQ_WIDTH)), end="")
            else:
                print(face_colors[1][7].value(" " * (SQ_WIDTH)), end="")

            print("|", end="")
            if i <= SQ_HEIGHT + 1:
                print(face_colors[1][2].value(" " * (SQ_WIDTH)), end="")
            elif i <= SQ_HEIGHT*2 + 1:
                print(face_colors[1][5].value(" " * (SQ_WIDTH)), end="")
            else:
                print(face_colors[1][8].value(" " * (SQ_WIDTH)), end="")

            print("|", end="")

        before_middle_begins = int((number_of_spaces_before - 3)) + 2
        singe_face_vertical = int((number_of_spaces_before - 3) / 3)
        # print(singe_face_vertical)
        for j in range(0, before_middle_begins):
            if (j == singe_face_vertical or j == singe_face_vertical*2 + 1):
                print("|", end="")
            else:
                if (j >= width_right_indexes[i][1] and j <= width_right_indexes[i][2]):
                    if j == width_right_indexes[i][1] or j == width_right_indexes[i][2]:
                        if i > int(height_of_middle_view/2):
                            print("\\", end="")
                        else:
                            print("/", end="")
                    elif j > width_right_indexes[i][1] or j < width_right_indexes[i][2]:
                        print("-", end="")
                else:
                    if (j > width_right_indexes[i][1]):
                        print("a", end="")
                    else:
                        print("b", end="")

        '''
        # space padding after middle
        print("a" * int((number_of_spaces_before -3)/3), end="")
        print("|", end="")
        print("a" * int((number_of_spaces_before -3)/3), end="")
        print("|", end="")
        print("a" * int((number_of_spaces_before -3)/3), end="")
        print("|", end="")
        print()
        '''
        print("|", end="")
        print()
    # ------------------------------------------------------------
    # bottom view
    height_of_bottom_view = 3 * SQ_HEIGHT + 4
    # print(height_of_bottom_view)
    for i in range(1, height_of_bottom_view):

        # same padding we provided before top we need to keep before
        number_of_spaces_before = int(((total_width_of_whole-4) - (SQ_WIDTH + i*2)*3)/2)

        # vertical bars at start of bottom left section
        if (number_of_spaces_before != 0):
            print("|", end="")

        # print("z" * (number_of_spaces_before - 1), end="")
        if (i % top_grid_check != 0):
            if (number_of_spaces_before - 1 > v_indexes[0] and number_of_spaces_before - 1 < v_indexes[1]):
                print("w" * (number_of_spaces_before - 1), end="")
            elif (number_of_spaces_before - 1 > v_indexes[1] and number_of_spaces_before - 1 < v_indexes[2]):
                # print(v_indexes[1], end="")
                print("a" * (v_indexes[1]-1), end="")
                print("|", end="")
                print("s" * (number_of_spaces_before - v_indexes[1] - 1), end="")
            else:
                print("d" * (v_indexes[1]-1), end="")
                print("|", end="")
                print("e" * (v_indexes[1]-1), end="")
                print("|", end="")
                print("f" * (number_of_spaces_before - v_indexes[2] - 1), end="")
        else:
            print("-" * (number_of_spaces_before - 1), end="")

        # print(number_of_spaces_before)

        # code for blank lines, will be inside the |||| only
        if (i % top_grid_check == 0):
            # middle part of bottom view
            print("/", end="")
            print("-" * (SQ_WIDTH + i*2), end="")
            print("/", end="")
            print("-" * (SQ_WIDTH + i*2), end="")
            print("\\", end="")
            print("-" * (SQ_WIDTH + i*2), end="")
            print("\\", end="")
        else:
            # middle part of bottom view
            print("/", end="")

            if i <= SQ_HEIGHT + 1:
                print(face_colors[2][0].value(" " * (SQ_WIDTH + i*2)), end="")
            elif i <= SQ_HEIGHT*2 + 1:
                print(face_colors[2][3].value(" " * (SQ_WIDTH + i*2)), end="")
            else:
                print(face_colors[2][6].value(" " * (SQ_WIDTH + i*2)), end="")
            # print(" " * (SQ_WIDTH + i*2), end="")
            print("/", end="")
            if i <= SQ_HEIGHT + 1:
                print(face_colors[2][1].value(" " * (SQ_WIDTH + i*2)), end="")
            elif i <= SQ_HEIGHT*2 + 1:
                print(face_colors[2][4].value(" " * (SQ_WIDTH + i*2)), end="")
            else:
                print(face_colors[2][7].value(" " * (SQ_WIDTH + i*2)), end="")
            print("\\", end="")
            if i <= SQ_HEIGHT + 1:
                print(face_colors[2][2].value(" " * (SQ_WIDTH + i*2)), end="")
            elif i <= SQ_HEIGHT*2 + 1:
                print(face_colors[2][5].value(" " * (SQ_WIDTH + i*2)), end="")
            else:
                print(face_colors[2][8].value(" " * (SQ_WIDTH + i*2)), end="")
            print("\\", end="")

        # same padding we provided before top we need to keep after also
        # vertical bars at the top right section
        if (i % top_grid_check != 0):
            if (number_of_spaces_before - 1 > v_indexes[0] and number_of_spaces_before - 1 < v_indexes[1]):
                print("w" * (number_of_spaces_before - 1), end="")
            elif (number_of_spaces_before - 1 > v_indexes[1] and number_of_spaces_before - 1 < v_indexes[2]):
                # print(v_indexes[1], end="")
                print("a" * (number_of_spaces_before - v_indexes[1] - 1), end="")
                print("|", end="")
                print("s" * (v_indexes[1]-1), end="")
            else:
                print("d" * (number_of_spaces_before - v_indexes[2] - 1), end="")
                print("|", end="")
                print("e" * (v_indexes[1]-1), end="")
                print("|", end="")
                print("f" * (v_indexes[1]-1), end="")
        else:
            print("-" * (number_of_spaces_before - 1), end="")

        if (number_of_spaces_before != 0):
            print("|", end="")
        print()


horizontal_grid_lines(face_colors)
