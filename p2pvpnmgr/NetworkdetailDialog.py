# -*- coding: utf-8 -*-
### BEGIN LICENSE
# This file is in the public domain
### END LICENSE

import sys
import os
import gtk

from desktopcouch.records.record import Record

from p2pvpnmgr.p2pvpnmgrconfig import getdatapath

record_type = "http://unum.whitlark.org/todo/p2pvpnDoc"

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


    def load_from_couch(self, _id):

        target = self.database.get_record(_id)

        if target:
            self.builder.get_object("net_name").set_text(target["net_name"])
            self.builder.get_object("ifc_name").set_text(target["ifc_name"])
            self.builder.get_object("supernode_address").set_text(target["supernode_address"])
            self.builder.get_object("log_location").set_text(target["log_location"])
            self.builder.get_object("autostart").set_active(target["autostart"])
            self.builder.get_object("allow_broadcast").set_active(target["allow_broadcast"])
            self.builder.get_object("db_replicate").set_text(target["db_replicate"])

    def ok(self, widget, data=None):
        """ok - The user has elected to save the changes.
        Called before the dialog returns gtk.RESONSE_OK from run().

        """
        net_name = self.builder.get_object("net_name").get_text()  #or set_text


        ifc_name = self.builder.get_object("ifc_name").get_text()
        supernode_address = self.builder.get_object("supernode_address").get_text()
        log_location = self.builder.get_object("log_location").get_text()
        autostart = self.builder.get_object("autostart").get_active()
        allow_broadcast = self.builder.get_object("allow_broadcast").get_active()
        db_replicate = self.builder.get_object("db_replicate").get_text()

        print "Save called: %s, %s, %s, %s, %s" % (net_name, ifc_name, supernode_address, log_location, allow_broadcast)

        results = self.database.get_records(record_type = record_type,
                                            create_view = True)

        #update a record that has the same title
        for result in results:
            document = result.value
            if document["net_name"] == net_name:
                self.database.update_fields(result.id, {"ifc_name": ifc_name,
                                                  "supernode_address": supernode_address,
                                                  "log_location": log_location,
                                                  "db_replicate": db_replicate,
                                                  "autostart": autostart,
                                                  "allow_broadcast": allow_broadcast,})
                return

        new_rec = Record({"record_type": record_type,
                          "net_name": net_name,
                          "ifc_name": ifc_name,
                          "supernode_address": supernode_address,
                          "log_location": log_location,
                          "db_replicate": db_replicate,
                          "autostart": autostart,
                          "allow_broadcast": allow_broadcast,})
        self.database.put_record(new_rec)


    def cancel(self, widget, data=None):
        """cancel - The user has elected cancel changes.
        Called before the dialog returns gtk.RESPONSE_CANCEL for run()

        """
        pass

def NewNetworkdetailDialog(database, _id=None):
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
    if _id is not None:
        dialog.load_from_couch(_id)
    return dialog

if __name__ == "__main__":
    dialog = NewNetworkdetailDialog()
    dialog.show()
    gtk.main()

