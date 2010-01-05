# -*- coding: utf-8 -*-
### BEGIN LICENSE
# This file is in the public domain
### END LICENSE

import sys
import os
import gtk

from p2pvpnmgr.p2pvpnmgrconfig import getdatapath

class AboutP2pvpnmgrDialog(gtk.AboutDialog):
    __gtype_name__ = "AboutP2pvpnmgrDialog"

    def __init__(self):
        """__init__ - This function is typically not called directly.
        Creation of a AboutP2pvpnmgrDialog requires redeading the associated ui
        file and parsing the ui definition extrenally, 
        and then calling AboutP2pvpnmgrDialog.finish_initializing().
    
        Use the convenience function NewAboutP2pvpnmgrDialog to create 
        NewAboutP2pvpnmgrDialog objects.
    
        """
        pass

    def finish_initializing(self, builder):
        """finish_initalizing should be called after parsing the ui definition
        and creating a AboutP2pvpnmgrDialog object with it in order to finish
        initializing the start of the new AboutP2pvpnmgrDialog instance.
    
        """
        #get a reference to the builder and set up the signals
        self.builder = builder
        self.builder.connect_signals(self)

        #code for other initialization actions should be added here

def NewAboutP2pvpnmgrDialog():
    """NewAboutP2pvpnmgrDialog - returns a fully instantiated
    AboutP2pvpnmgrDialog object. Use this function rather than
    creating a AboutP2pvpnmgrDialog instance directly.
    
    """

    #look for the ui file that describes the ui
    ui_filename = os.path.join(getdatapath(), 'ui', 'AboutP2pvpnmgrDialog.ui')
    if not os.path.exists(ui_filename):
        ui_filename = None

    builder = gtk.Builder()
    builder.add_from_file(ui_filename)    
    dialog = builder.get_object("about_p2pvpnmgr_dialog")
    dialog.finish_initializing(builder)
    return dialog

if __name__ == "__main__":
    dialog = NewAboutP2pvpnmgrDialog()
    dialog.show()
    gtk.main()

