# Module: bitle.win32.SAPI
# Purpose:
# Minimal MS-SAPI bindings for the SPVoice and related
# COM objects see MSDN for more information
# Wow marnold referenced MSDN are pigs flying yet :)
#
# Implements: Speach_Plugin see docs/speach_plugin.txt
#
# Author: Matt Arnold <marnold@tuxfamily.org>
# Start-Date: 2-4-11

## Copyright (c) 2010-1010 Matt Arnold 
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
import win32com.client
import pythoncom
from win32com.client import * # redundent in the strict sense but this is win32
# so we will ignore lint on this
import gtk
import gobject
from bitle.config import *
from bitle.util import BitleError
from bitle.util import dbgprint
from threading import Thread



class SAPISupervisor(object):
    """
    Access SPVoice object Calling conventions
    and method names have been altered to python guidelines
    and key data structures have been re implemented in
    to optimize performence. I'll try to document as I go
    but its best to RTFS

    Warning: This module only provides access to text-to-speech functions
    not the voice recognition introduced in longhorn

    Warning This object is not complete, hence the Minimal in the header above    
    
    """

    def __init__(self, voice=None , rate=SP_DEF_SETTING, vol=SP_DEF_SETTING):
        """
        Constructor for SPVoice
        @param voice: The voice description of the starting voice
        or None for the default voice
        @parm rate the reading speed an int
        pass SP_DEF_SETTING for the system default
        @param vol reading volume a non-negitve int
        ditto for the default
        """
        pythoncom.CoInitializeEx(pythoncom.COINIT_MULTITHREADED)
        self.sp_voice = win32com.client.Dispatch('Sapi.SpVoice')

        # Build the voice_table now or we'll keep rebuilding it
        # every time we set the voice. We take a slight hit on
        # startup. However the overall performence gain is
        # more than worth the extra 1.2s of startup time 
        self.voice_table = {}
        voice_licom = self.sp_voice.GetVoices()
        for i in range(voice_licom.Count):
            vt = voice_licom.Item(i)
            self.voice_table[vt.GetDescription()] = vt

        if rate != SP_DEF_SETTING:
            self.sp_voice.Rate = rate
        if voice is not None:
            self.sp_voice.Voice = self.voice_table[voice]
            # This will not catch an exception for an invalid voice
            # yet. TODO after beta
        if vol != SP_DEF_SETTING:
            self.sp_voice.Volume = vol
		## comply with my interface
		self.purge = False


    def get_voice_table(self):
        """
        Return a pydict with voice descriptions(str) as key
        and pointers to ISpeechObjectTokens as values
        but please don't use said pointers unless you've read the
        MS docs fully
        """
        return self.voice_table


    def query_running_state(self):
        """
        Returms ethier MS_RSR_DONE or MS_RSR_SPEAKING
        as per Microsoft's RunningState enum
        """
        return self.sp_voice.Status.RunningState

    # note that these next methods violate python conventions,
    # but we need them to debug stuff,
    # and for a planned feature so we'll ignore good style oncev again
    def _get_voice_t(self):
        """
        Returns a pointer ISpeechObjectToken
        READ MS DOCS BEFORE playing with it
        """
        return self.sp_voice.Voice

    def _set_voice_t(self, vt):
        """
        EEK allows the loading of unlisted voices
        by setting it by pointer
        will crash the application if not careful
        """
        self.sp_voice.Voice = vt

    def get_voice(self):
        """
        Gets the name of the current voice
        """
        return self.sp_voice.GetDescription()

    def set_voice(self, voice_desc):
        """
        set voice by using the table
        """
        if voice_desc in self.voice_table:
            self.sp_voice.Voice = self.voice_table[voice_desc]
        else:
            raise BittleError("Invalid Voice")

    ## I'm lazy
    def get_sp_voice(self):
        return self.sp_voice
    def speak(self, text):

        if (self.query_running_state() == 1 and self.purge): ## enum RunningState            
           self.sp_voice.Speak(text, SVSFlagsAsync, SVSFPurgeBeforeSpeak)
		   self.purge = False
		elif self.query_running_state() == 1:
			self.sp_voice.Speak(text, SVSFlagsAsync)
		
			
        return
            
            
    def pause(self):
        """
        Pause the reading
        """
        dbgprint("pause s3")
        x = self.sp_voice.Pause()
        dbgprint("pause " + str(x))
        return

    def resume(self):
        """
        Resume the reading
        """
        self.sp_voice.Resume()
        return
    # stub for future fast-forward/rewind support
    def skip(self, type, num):
        pass
 



    

