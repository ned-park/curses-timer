#!/usr/bin/env python3

import curses, getopt, sys, time

def printUsage(filename): 
    print('Usage:', filename, '-h <hours> -m <minutes> -s <seconds>')
    exit(1)

def main(filename, argv):
    inHr = 0
    inMin = 0  
    inSec = 0
    try:
        opts, args = getopt.getopt(argv, "s:m:h:",[])
        if len(opts) < 1:
            printUsage(filename)
    except getopt.GetoptError:
        printUsage(filename)
    for opt, arg in opts:
        if opt == '-h':
            inHr = int(arg)
        elif opt == '-m':
            min = int(arg)
            inMin = min % 60
            inHr += min // 60
        elif opt == '-s':
            sec = int(arg)
            inSec = sec % 60
            min = sec // 60
            if min > 60:
                hours = min // 60
                inHr += hours
                min = min // 60
                inMin += min
        else: 
            printUsage(filename)

    scr = curses.initscr()
    scr.nodelay(1)
    try:
        for hr in range(inHr, -1, -1):
            for min in range(inMin, -1, -1):
                for sec in range(inSec, -1, -1):
                    out = str(hr).rjust(2, '0') + ':' + str(min).rjust(2, '0') + ':' + str(sec).rjust(2, '0')
                    scr.addstr(0, 0, out)
                    c = scr.getch()
                    if c == 3 or c == 113 or c == 27: # Ctrl + c or 'q'
                        raise KeyboardInterrupt
                    elif c == 112 or c == 32: 
                        scr.nodelay(0)
                        scr.refresh()
                        out = str(hr).rjust(2, '0') + ':' + str(min).rjust(2, '0') + ':' + str(sec).rjust(2, '0')
                        scr.addstr(0, 0, out)
                        c = scr.getch()
                        scr.nodelay(1)
                    scr.refresh()
                    time.sleep(1)
                inSec = 59
            inMin = 59
    
    
    except KeyboardInterrupt:
        scr.addstr(3,0, "Program terminated")
        scr.refresh()
    
    finally: 
        scr.refresh()
    
    curses.endwin()
    exit(0)

if __name__ == "__main__":
    main(sys.argv[0], sys.argv[1:])
