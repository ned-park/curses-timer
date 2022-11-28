# curses-timer
A simple curses based timer that shows time remaining and allows commandline chaining.  It should work fine on GNU/Linux and probably
the BSD's.  It may work on windows too, but that's entirely untested so it may not.

The sleep command is a wonderful thing.  There are times though, when it's nice to know how much time remains.  timer.py
provides a simple curses based timer that shows how much time is remaining.  As is typical of shell commands it can be 
chained to other commands using || and && to alert the user that the timer has finished.  

# Requirements
python3, curses

# Installation
timer.py to somewhere in your path and invoke it from a terminal.  Edit the #! line if your path to python differs, 
you can find that out with the `which python3` command.  

# Usage
Run timer.py with no arguments to get usage help, unspecified arguments default to 0, but at least one of 
-s, -m, or -h must be non-zero for the command to successfully run.  

# Examples
To set a 3 hour, 2 minute and 1 second timer
    timer.py -h 3 -m 2 -s 1 

To set a 30 minute timer and begin playing your current mpd playlist when it finishes (requires mpd and mpc to be installed and configured to work)
    timer.py -m 30 && mpc play
    
# Stopping a running timer
Ctrl+c and q will both exit the program when it's running.  

# Planned improvements
Pause feature to suspend and resume an existing timer
