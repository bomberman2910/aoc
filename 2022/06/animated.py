import curses
from curses import wrapper
from collections import Counter

WINDOW_LENGTH = 14
BORDER = 15

def main(stdscr):
    if curses.has_colors():
        curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
        curses.init_pair(3, curses.COLOR_YELLOW, curses.COLOR_BLACK)

    stdscr.clear()

    message = content[0]

    for i in range(WINDOW_LENGTH, len(message) + 1):
        window_start = i - WINDOW_LENGTH
        window_end = i
        window_content = message[window_start : window_end]
        duplicate_chars_in_window = [character for character, count in Counter(window_content).items() if count > 1]
        display_window_start = window_start - BORDER
        display_window_end = window_end + BORDER
        
        stdscr.addstr(1, 0, f"Start of element: {i}")
        for x in range(display_window_end - display_window_start):
            current_x = x
            if(x == BORDER):
                if(curses.has_colors()):
                    stdscr.addstr(3, current_x, '[', curses.color_pair(3))
                else:
                    stdscr.addstr(3, current_x, '[')
            if(x >= BORDER):
                current_x += 1
            if(x == WINDOW_LENGTH + BORDER):
                if(curses.has_colors()):
                    stdscr.addstr(3, current_x, ']', curses.color_pair(3))
                else:
                    stdscr.addstr(3, current_x, ']')
            if(x >= WINDOW_LENGTH + BORDER):
                current_x += 1
            if(curses.has_colors() and x >= BORDER and x < WINDOW_LENGTH + BORDER):
                if(message[display_window_start + x] in duplicate_chars_in_window):
                    stdscr.addstr(3, current_x, message[display_window_start + x], curses.color_pair(2))
                else:
                    stdscr.addstr(3, current_x, message[display_window_start + x], curses.color_pair(1))
            else:
                if((display_window_start + x < 0 and current_x < BORDER) or (display_window_start + x >= len(message) and current_x > WINDOW_LENGTH + BORDER)):
                    stdscr.addstr(3, current_x, ' ')
                else:
                    stdscr.addstr(3, current_x, message[display_window_start + x])
        if(len(set(window_content)) == WINDOW_LENGTH):
            stdscr.addstr(5, 0, 'Success')
            stdscr.refresh()
            break
        stdscr.refresh()
        curses.napms(1000)
    stdscr.getkey()

file = open("test.txt", "r")
content = file.read().splitlines()

wrapper(main)