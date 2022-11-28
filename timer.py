#!/usr/bin/python3

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
            inMin = int(arg)
        elif opt == '-s':
            inSec = int(arg)
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
                    if c == 3 or c == 113: # Ctrl + c or 'q'
                        raise KeyboardInterrupt
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
