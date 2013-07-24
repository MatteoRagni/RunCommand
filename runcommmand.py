#!/usr/bin/env python

#### SIMPLE COMMAND RUN ####
# MatteoRagni 2013

# SysWait :: read -p "Press any key to continue... " -n1 -s
# insert in a script called "syswait" somewhere in PATH

import pygtk
pygtk.require('2.0')
import gtk
import os

# This global variable is needed to make the widget disappear
# from the screen
global Command

class RunBox:

    # this method is called on textbox modify
    # will be used in future for completion features
    def modify_callback(self, widget, input):
        input_text = input.get_text()
        return

    # This method is called on keypressed event = Enter
    def activate_callback(self, widget, input, mainwin):
        global Command
        Command = input.get_text()
        mainwin.hide()
        gtk.main_quit()
        return

    # This method is called when  pressed Ctrl+Enter to run program in console
    def activate_callback_term(self, widget, keyval, input, window):
        global Command
        combination = gtk.accelerator_get_label(keyval.keyval,keyval.state)
        if combination == "Ctrl+Mod2+Return" or combination == "Ctrl+Return":
            Command = 'x-terminal-emulator -T "Run" -e bash -c "' + input.get_text() + ' && syswait "'
            window.hide()
            gtk.main_quit()
        return

    # Exit on esc
    def exit_on_esc(self, widget, keyval):
        code = gtk.accelerator_get_label(keyval.keyval,keyval.state)
        if code == "Mod2+Escape" or code == "Escape":
            gtk.main_quit()
        return


    # Draw Gui
    def __init__(self):

        ##### CONFIGURATIONS ######
        # Edit here for dimensions
        H = 350             # window height
        W = 45              # window width
        Borders = 10        # window border
        MaxText = 1000      # max text length
        InputW = 40         # input box width
        # Do not edit below #######

        # MAINWINDOW
        # create a new window
        mainwin = gtk.Window(gtk.WINDOW_TOPLEVEL)
        
        # Settings mainwin
        mainwin.set_size_request(H, W)
        mainwin.set_border_width(Borders)
        mainwin.set_title('Run Command')
        
        # Release resources on delete events
        mainwin.connect('delete_event', lambda w,e: gtk.main_quit())

        # INPUTBOX
        # Generate text entry box
        inputbox = gtk.Entry()
        mainwin.add(inputbox)
        # dimensioni della textbox
        inputbox.set_max_length(MaxText)
        inputbox.set_width_chars(InputW)
        
        # Eventi di inputbox
        #inputbox.add_events(gtk.gdk.KEY_PRESS_MASK)
        mainwin.connect('key-press-event',self.exit_on_esc)
        inputbox.connect('changed', self.modify_callback, inputbox)
        inputbox.connect('activate', self.activate_callback, inputbox, mainwin)
        inputbox.connect('key-press-event', self.activate_callback_term, inputbox, mainwin)
        
        # Inserisce il testo iniziale e lo seleziona
        inputbox.set_text('Insert command here...')
        inputbox.select_region(0, len(inputbox.get_text()))
        
        # showall
        inputbox.show()
        mainwin.show()

        return

def main():
    global Command
    gtk.main()
    os.system(Command)
    return 0

if __name__ == "__main__":
    RunBox()
    main()
