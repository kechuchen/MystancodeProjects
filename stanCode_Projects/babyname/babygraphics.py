"""
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.

YOUR DESCRIPTION HERE
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index of the current year in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                              with the specified year.
    """

    space = (width - GRAPH_MARGIN_SIZE * 2) / len(YEARS)
    x = GRAPH_MARGIN_SIZE + int(year_index) * space
    return x


def draw_fixed_lines(canvas):
    """
    Erases all existing information on the given canvas and then
    draws the fixed background lines on it.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.

    Returns:
        This function does not return any value.
    """
    canvas.delete('all')  # delete all existing lines from the canvas

    # Write your code below this line
    #################################
    canvas.create_line(GRAPH_MARGIN_SIZE, 0, GRAPH_MARGIN_SIZE, CANVAS_HEIGHT, width=LINE_WIDTH)
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH - GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE,
                       width=LINE_WIDTH)
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, CANVAS_WIDTH - GRAPH_MARGIN_SIZE,
                       CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, width=LINE_WIDTH)

    for year_index in range(len(YEARS)):
        space = get_x_coordinate(CANVAS_WIDTH, year_index)
        canvas.create_line(space, 0, space, CANVAS_HEIGHT, width=LINE_WIDTH)
        canvas.create_text(space + TEXT_DX, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, text=YEARS[year_index], anchor=tkinter.NW)


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)  # draw the fixed background grid

    # Write your code below this line
    #################################

    rank_space = (CANVAS_HEIGHT-2*GRAPH_MARGIN_SIZE)/MAX_RANK
    color_count = -1            # count the number for color use
    for name in lookup_names:
        rank = []               # rank number
        spacex = []             # each x's coordinate
        color_count += 1        # count the number of color
        color_index = color_count % len(COLORS)         # text color's index
        for year_index in range(len(YEARS)):
            space = get_x_coordinate(CANVAS_WIDTH, year_index)
            spacex.append(space)
            y = str(YEARS[year_index])
            if y in name_data[name]:
                rank.append(name_data[name][y])
            else:
                rank.append(MAX_RANK)

        for j in range(len(YEARS)-1):
            canvas.create_line(spacex[j], GRAPH_MARGIN_SIZE+rank_space*int(rank[j]),
                               spacex[j+1], GRAPH_MARGIN_SIZE+rank_space*int(rank[j+1]),
                               width=LINE_WIDTH, fill=COLORS[color_index]
                               )
        for k in range(len(YEARS)):
            if int(rank[k]) == MAX_RANK:
                canvas.create_text(spacex[k]+TEXT_DX, GRAPH_MARGIN_SIZE + rank_space * int(rank[k]),
                                   text=(name, "*"), anchor=tkinter.SW, fill=COLORS[color_index]
                               )
            else:
                canvas.create_text(spacex[k] + TEXT_DX, GRAPH_MARGIN_SIZE + rank_space * int(rank[k]),
                                   text=(name, rank[k]), anchor=tkinter.SW, fill=COLORS[color_index])





# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
