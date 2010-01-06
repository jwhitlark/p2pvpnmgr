# -*- coding: utf-8 -*-
### BEGIN LICENSE
# This file is in the public domain
### END LICENSE

import sys
import os
import gtk

from desktopcouch.records.record import Record

from p2pvpnmgr.p2pvpnmgrconfig import getdatapath

class NetworkdetailDialog(gtk.Dialog):
    __gtype_name__ = "NetworkdetailDialog"

    def __init__(self):
        """__init__ - This function is typically not called directly.
        Creation of a NetworkdetailDialog requires redeading the associated ui
        file and parsing the ui definition extrenally,
        and then calling NetworkdetailDialog.finish_initializing().

        Use the convenience function NewNetworkdetailDialog to create
        a NetworkdetailDialog object.

        """
        pass

    def finish_initializing(self, builder):
        """finish_initalizing should be called after parsing the ui definition
        and creating a NetworkdetailDialog object with it in order to finish
        initializing the start of the new NetworkdetailDialog instance.

        """
        #get a reference to the builder and set up the signals
        self.builder = builder
        self.builder.connect_signals(self)


    def ok(self, widget, data=None):
        """ok - The user has elected to save the changes.
        Called before the dialog returns gtk.RESONSE_OK from run().

        """
        record_type = "http://unum.whitlark.org/todo/p2pvpnDoc"
        net_name = self.builder.get_object("net_name").get_text()  #or set_text
        ifc_name = self.builder.get_object("ifc_name").get_text()
        supernode_address = self.builder.get_object("supernode_address").get_text()
        log_location = self.builder.get_object("log_location").get_text()
        autostart = self.builder.get_object("autostart").get_active()
        allow_broadcast = self.builder.get_object("allow_broadcast").get_active()
        db_replicate = self.builder.get_object("db_replicate").get_text()

        print "Save called: %s, %s, %s, %s" % (net_name, ifc_name, supernode_address, log_location)

        results = self.database.get_records(record_type = record_type,
                                            create_view = True)

        new_rec = Record({"record_type": record_type,
                          "net_name": net_name,
                          "ifc_name": ifc_name,
                          "supernode_address": supernode_address,
                          "log_location": log_location,
                          "db_replicate": db_replicate,
                          "autostart": autostart,
                          "allows_broadcast": allow_broadcast,})
        self.database.put_record(new_rec)
        self.destroy()


    def cancel(self, widget, data=None):
        """cancel - The user has elected cancel changes.
        Called before the dialog returns gtk.RESPONSE_CANCEL for run()

        """
        self.destroy()

def NewNetworkdetailDialog(database):
    """NewNetworkdetailDialog - returns a fully instantiated
    dialog-camel_case_nameDialog object. Use this function rather than
    creating NetworkdetailDialog instance directly.

    """

    #look for the ui file that describes the ui
    ui_filename = os.path.join(getdatapath(), 'ui', 'NetworkdetailDialog.ui')
    if not os.path.exists(ui_filename):
        ui_filename = None

    builder = gtk.Builder()
    builder.add_from_file(ui_filename)
    dialog = builder.get_object("networkdetail_dialog")
    dialog.finish_initializing(builder)
    dialog.database = database
    return dialog

if __name__ == "__main__":
    dialog = NewNetworkdetailDialog()
    dialog.show()
    gtk.main()

