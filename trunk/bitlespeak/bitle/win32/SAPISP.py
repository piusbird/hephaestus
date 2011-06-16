# Module: SAPISP
# Purpose: Implements: Speach_Plugin
#
# Author: Matt Arnold <marnold@tuxfamily.org>
# Start-Date: 2-4-11

## Copyright (c) 2010-2010 Matt Arnold 
## BitleSpeak is free software: you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation, either version 3 of the License, or
## (at your option) any later version.
## BitleSpeak is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.
## You should have received a copy of the GNU General Public License
## along with BitleSpeak.  If not, see <http://www.gnu.org/licenses/>
from bitle.config import *
from bitle.util import BitleError
from bitle.win32.SAPI import SAPISupervisor
import platform

if platform.system() != 'Windows':
    print "This build of bitlespeak requires MS Windows"
    exit(2)

_short_name = "SAPISP"

def load_plugin(cfg):

    l_rate = l_voice = l_vol = None # placeholders for parsed values from ini file    
      
    c_voice = cfg.get(_short_name, 'voice')
    if c_voice == 'default':
        l_voice = None
    else:
        l_voice = c_voice
    
    c_rate = cfg.get(_short_name, 'rate')
    if c_rate == 'default':
        l_rate = SP_DEF_SETTING
    else:
        l_rate = int(c_rate)

    c_vol = cfg.get(_short_name, 'volume')
    if c_vol == 'default':
        l_vol = SP_DEF_SETTING
    else:
        l_vol = int(c_vol)
    sp_com = SAPISupervisor(l_voice, l_rate, l_vol)
    spkr = SAPISP(sp_com)
    dbg = DEBUG
    spkr.set_parm("DEBUG", dbg)
    return spkr

class SAPISP(object):

    def __init__(self, spcom):
        self.spv = spcom
        self.drvparm = {'DEBUG': 0}
        return

    def speak(self, text):

        self.spv.speak(text)
        print "return from speak"
        return
    def stop(self):
        self.pause()
        self.spv.purge = True ## not a COM property so we can do direct xs
        return
    def pause(self):
        print "pause s2"
        self.spv.pause()
        return
    def resume(self):
        self.spv.resume()
        return
    
    def is_running(self):
    
        rs = self.spv.query_running_state()
        if rs < 2:
            return False
        else:
            return True
        return False # Never get here just here for syntax sale
    def set_parm(self, key, val):
        
        self.drvparm[key] = val
    
    def get_parm(self, key):
    
        if key == None:
            
            return self.drvparm
        
        return self.drvparm[key]

