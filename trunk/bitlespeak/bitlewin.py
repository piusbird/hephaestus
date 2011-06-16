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
import pythoncom
import gobject
import gtk
from bitle.ui.widgets import app_error
# remove the Traditional pygtk require semantics doesn't work once compiled
# so we shall assume that people downloading source code have build deps installed

from bitle import loader
from bitle.config import *
from bitle.ui.gnome import BitleSpeak


def test(test_num):
    from bitle.win32.SAPI import SAPISupervisor
    spv = SAPISupervisor()
    if test_num == 1:
        dict = spv.get_voice_table()
        vlist = dict.items()
        for i in vlist:
            print(i)
    exit(3)
def main(argv):
    print argv
    if len(argv) > 1 and argv[1] == 'lsvoices':
        test(1)
    l_res = loader.app_init()
    if l_res:
        from bitle.win32.SAPISP import load_plugin
        spkr = load_plugin(l_res)
        app = BitleSpeak((spkr,l_res), xsel = False)
    else:
        app_error(E_FATAL, "Loader error, please see website\n http://code.mornold.info/btilespeak/docs", 0)
        exit(1)
if __name__ == '__main__':

    pythoncom.CoInitializeEx(pythoncom.COINIT_MULTITHREADED)    
    main(sys.argv)
    gobject.threads_init()
    gtk.main()
