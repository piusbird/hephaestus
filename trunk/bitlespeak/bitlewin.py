## File bitlespeak.py: BitleSpeak Main program 
## Matt Arnold <matt@thegnuguru.org> 6-30-10
##
## Copyright (c) 2010 Matt Arnold
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
 
import sys
import os.path
from bitle.util import *

try:  
    import pygtk  
    pygtk.require("2.0")  
except: 
    pass  
try:  
    import gtk  
except:  
    print("GTK Not Availible")
    sys.exit(1)

from bitle import loader
from bitle.config import *
from bitle.ui.gnome import BitleSpeak


def main(*argv):

    l_res = loader.app_init()
    print "app init done"
    if l_res:
        print "hit if"
        from bitle.win32.SAPISP import load_plugin
        spkr = load_plugin(l_res)
        app = BitleSpeak((spkr,l_res), xsel = False)
    else:
        print "Run this in debugger"
        exit(1)
if __name__ == '__main__':
    
    main(sys.argv)
    gtk.main()
