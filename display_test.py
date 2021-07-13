from math import ceil, floor
scale_unit = 1
unit_width = scale_unit * 5
unit_height = scale_unit * 2

display_height = unit_height * 9 + 10
display_width = unit_width * 9 + 10


def print_display(display):
    [print(display_line) for display_line in display]


def replace_character(string, position, character):
    string = [character if i == position else string[i] for i in range(len(string))]
    return ''.join(string)


def add_line(display, start_x, start_y, end_x, end_y, character, horizontal=True):
    if end_x == start_x:
        x = end_x
        for i in range(start_y, end_y + 1):
            display[i] = replace_character(display[i], x, character)
    elif end_y == start_y:
        y = end_y
        for i in range(start_x, end_x + 1):
            display[y] = replace_character(display[y], i, character)
    elif horizontal:
        for i in range(start_y, end_y + 1):
            x_best = start_x + int((end_x - start_x)/(end_y - start_y) * (i - start_y))
            display[i] = replace_character(display[i], x_best, character)
    else:
        for i in range(start_x, end_x + 1):
            y_best = start_y + int((end_y - start_y)/(end_x - start_x) * (i - start_x))
            display[y_best] = replace_character(display[y_best], i, character)


def add_block(display, top_left_x, top_left_y, top_right_x, top_right_y,
              bottom_left_x, bottom_left_y, bottom_right_x, bottom_right_y, character, horizontal=True):
    if horizontal:
        # Determine affected rows
        ymin = min(top_left_y, top_right_y)
        ymax = max(bottom_left_y, bottom_right_y)
        for i in range(ymin, ymax + 1):
            # need to accommodate where the bounding edges are not the left or right edges - FIX
            first_x_affected = top_left_x + \
                ceil((bottom_left_x - top_left_x)/(bottom_left_y - top_left_y) * (i - top_left_y))
            last_x_affected = top_right_x + \
                floor((bottom_right_x - top_right_x)/(bottom_right_y - top_right_y) * (i - top_right_y))
            for j in range(first_x_affected, last_x_affected + 1):
                display[i] = replace_character(display[i], j, character)
    else:
        xmin = min(top_left_x, bottom_left_x)
        xmax = max(top_right_x, bottom_right_x)
        for i in range(xmin, xmax + 1):
            # need to accommodate where the bounding edges are not the left or right edges - FIX
            first_y_affected = top_left_y + \
                ceil((top_right_y - top_left_y)/(top_right_x - top_left_x) * (i - top_left_x))
            last_y_affected = bottom_left_y + \
                floor((bottom_right_y - bottom_left_y)/(bottom_right_x - bottom_left_x) * (i - bottom_left_x))
            for j in range(first_y_affected, last_y_affected + 1):
                display[j] = replace_character(display[j], i, character)


display = ['.' * display_width] * display_height
add_block(display, 0, 0, unit_width * 3 + 3, 0, unit_width * 1 + 1,
          unit_height * 1 + 1, int((unit_width * 10 + 10)/3), unit_height * 1 + 1, 'O')
add_block(display, 0, 0, unit_width * 1 + 1, unit_height * 1 + 1, 0,
          unit_height * 3 + 3, unit_width * 1 + 1, int((unit_height * 10 + 10)/3), 'U', horizontal=False)
add_line(display, 0, 0, unit_width * 3 + 3, unit_height * 3 + 3, '\\')
add_line(display, unit_width * 3 + 3, 0, unit_width * 4 + 4, unit_height * 3 + 3, '\\')
add_line(display, 0, unit_height * 3 + 3, unit_width * 3 + 3, unit_height * 4 + 4, '\\', horizontal=False)
add_line(display, unit_width * 6 + 6, 0, unit_width * 5 + 5, unit_height * 3 + 3, '/')
add_line(display, unit_width * 9 + 9, 0, unit_width * 6 + 6, unit_height * 3 + 3, '/')
add_line(display, 0, 0, 0, unit_height * 9 + 9, '|')
add_line(display, unit_width * 1 + 1, unit_height * 1 + 1, unit_width * 1 + 1, unit_height * 8 + 8, '|')
add_line(display, 0, 0, unit_width * 9 + 9, 0, '-')
add_line(display, unit_width * 1 + 1, unit_height * 1 + 1, unit_width * 8 + 8, unit_height * 1 + 1, '-')
print_display(display)
