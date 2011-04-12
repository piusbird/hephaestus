# Module: bitle.ui.widgets
# Purpose encapsulate some dialog boxen in
# handy functions
# Author Matt Arnold <marnold@tuxfamily.org>
# Date 4-11-11

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

import gtk # we assume pygtk is already init by this point
import platform

NATIVE_WSET = platform.system() # will eventually be more then this
# so its here rather then bitle.config

def g_txt_fload(parent=None):
    dialog = gtk.FileChooserDialog("Open..",
                               parent,
                               gtk.FILE_CHOOSER_ACTION_OPEN,
                               (gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL,
                                gtk.STOCK_OPEN, gtk.RESPONSE_OK))

    dialog.set_default_response(gtk.RESPONSE_OK)
    filter = gtk.FileFilter()
    filter.set_name("Text Files")
    filter.add_pattern("*.txt")
    dialog.add_filter(filter)

    response = dialog.run()
    
    if response == gtk.RESPONSE_OK:
        fname = dialog.get_filename()
        dialog.destroy()
        return fname
    dialog.destroy()    
    return None


def g_txt_fsave(parent=None):
    dialog = gtk.FileChooserDialog("Save...",
                               parent,
                               gtk.FILE_CHOOSER_ACTION_SAVE,
                               (gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL,
                                gtk.STOCK_SAVE, gtk.RESPONSE_OK))

    dialog.set_default_response(gtk.RESPONSE_OK)
    filter = gtk.FileFilter()
    filter.set_name("Text Files")
    filter.add_pattern("*.txt")
    dialog.add_filter(filter)

    response = dialog.run()
    
    if response == gtk.RESPONSE_OK:
        fname = dialog.get_filename()
        dialog.destroy()
        return fname
        
    dialog.destroy()
    return None
