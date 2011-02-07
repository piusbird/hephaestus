## Module bitle.unix.util
## Matt Arnold <marnold@tuxfamily.org>
## Date: 2-4-11
## Purpose: Unix utility functions that aren't
## useful in the win32 port
## This file is part of bitlespeak

import os

def xsel_read():
    
    fp = os.popen('xsel')
    retval = fp.read()
    if retval == None:
        retval = "no text selected"
    return retval + '\n'
                                  