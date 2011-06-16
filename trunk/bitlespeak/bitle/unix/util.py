## Module bitle.unix.util
## Matt Arnold <marnold@tuxfamily.org>
## Date: 2-4-11
## Purpose: Unix utility functions that aren't
## useful in the win32 port
## This file is part of bitlespeak

## Copyright (c) 2011 Matt Arnold
## BitleSpeak is free software: you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation, either version 3 of the License, or
## (at your option) any later version.
## BitleSpeak is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.
## You should have received a copy of the GNU General Public License
## along with BitleSpeak.  If not, see <http://www.gnu.org/licenses/>.

import os

def xsel_read():
    
    fp = os.popen('xsel')
    retval = fp.read()
    if retval == None:
        retval = "no text selected"
    return retval + '\n'
                                  
