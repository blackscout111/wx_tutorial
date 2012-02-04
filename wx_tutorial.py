#!/usr/bin/python

import os
import wx # The GUI API
from bcWxWidgets import Ctrl


###############################################################################
class MainWindow(wx.Frame):
    """ A simple text editor

        This is a program that was made by following the wxPython tutorial on
        line.
    """
#______________________________________________________________________________
    def __init__(self, parent, title):

        # Initialize the parent frame
        # *** A -1 specifies defautl parameter
        wx.Frame.__init__(self, parent, title=title, size = (500, 800))
        self.SetIcon(wx.Icon('icon.png', wx.BITMAP_TYPE_PNG))

        # The text box.  TE_MULTILINE give it multiple line edits
        self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)

        # A status bar in the bottom of the window
        self.CreateStatusBar()

        # Make menus for the menubar
        filemenu = wx.Menu()
        helpmenu = wx.Menu()

        # Make the menu items
        menuAbout = helpmenu.Append(wx.ID_ABOUT, "&About",
                                   " Information about this program")
        filemenu.AppendSeparator()
        menuOpen = filemenu.Append(wx.ID_OPEN, "&Open",
                                   "Open a file for editing")
        menuSave = filemenu.Append(wx.ID_SAVE, "&Save", "Save the file")
        filemenu.AppendSeparator()
        menuExit = filemenu.Append(wx.ID_EXIT, "E&xit",
                                   "Terminate the program")

        # Create the menubar
        menuBar = wx.MenuBar()
        menuBar.Append(filemenu, "&File")
        menuBar.Append(helpmenu, "&Help")
        self.SetMenuBar(menuBar)

        # Set menubar events
        self.Bind(wx.EVT_MENU, self.OnAbout, menuAbout)
        self.Bind(wx.EVT_MENU, self.OnExit, menuExit)
        self.Bind(wx.EVT_MENU, self.OnOpen, menuOpen)
        self.Bind(wx.EVT_MENU, self.OnSave, menuSave)

        # Make the parameter panel
        ppanel = wx.Panel(self, -1, style=wx.SUNKEN_BORDER)
        psizer = wx.BoxSizer(wx.VERTICAL)

        # Make the controls
        self.ctrls = []
        for i in range(2,6):
            tmp = Ctrl.PanelCtrl(ppanel, "Ground Control", 0, 10, 0.3, i)
            self.ctrls.append(tmp)
            psizer.Add(tmp.sizer, 1, wx.ALIGN_CENTER | wx.EXPAND)

        # Make the apply button
        apply_button = wx.Button(ppanel,
                                 id=wx.ID_APPLY,
                                 label="&Apply Changes")
        self.Bind(wx.EVT_BUTTON, self.OnApply, apply_button)
        apply_sizer = wx.BoxSizer(wx.HORIZONTAL)
        apply_sizer.Add(apply_button, 0, wx.ALIGN_CENTER)

        psizer.Add(apply_sizer, 1, wx.ALIGN_CENTER)
        ppanel.SetSizer(psizer)
        ppanel.SetAutoLayout(True)

        # Add the parameter panel, and apply button
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.control, 2, wx.EXPAND)
        self.sizer.Add(ppanel, 1, wx.EXPAND)

        # Layout sizers
        self.SetSizer(self.sizer)
        self.SetAutoLayout(True)

        # Make the frame visible
        self.Show(True)
    
    def OnAbout(self, event):
        """ A message dialog box with an OK button.

            wx.OK is a standard ID in wxWidgets
        """
        msg = "A small text editor"
        title = "About sample editor"
        dlgID = wx.OK
        dlg = wx.MessageDialog(self, msg, title, dlgID)
        dlg.ShowModal() # Show it
        dlg.Destroy() # finally destroy it when finished

    def OnExit(self, event):
        self.Close(True)
    
    def OnOpen(self, event):
        """ Open a file """
        self.dirname = ''
        dlg = wx.FileDialog(self, "Choose a file",
                            self.dirname, "", "*.*", wx.OPEN)

        if  dlg.ShowModal() == wx.ID_OK:
            self.filename = dlg.GetFilename()
            self.dirname = dlg.GetDirectory()
            f = open(self.dirname + '/' + self.filename, 'r')
            self.control.SetValue(f.read())
            f.close()
            newTitle = "Small Editor - " + self.dirname
            self.SetTitle(newTitle)

            dlg.Destroy()

    def OnSave(self, event):
        """ Save a file """
        self.dirname = ''
        dlg = wx.FileDialog(self, "Save file",
                            self.dirname, "file Name", "*.*", wx.SAVE)
        if  dlg.ShowModal() == wx.ID_OK:
            self.filename = dlg.GetFilename()
            self.dirname = dlg.GetDirectory()
            f = open(self.dirname + '/' + self.filename, 'w')
            print self.dirname
            print self.filename
            print self.dirname + self.filename
            f.write(self.control.GetValue())
            f.close()
            newTitle = "Small Editor - " + self.dirname
            self.SetTitle(newTitle)

            dlg.Destroy()

    def OnApply(self, event):
        """ Opens up a message box. """
        ctrls = self.ctrls
        msg = [ctrls[i].GetValue() for i in range(0,len(ctrls))]
        msg = str(msg)
        title = "Slave response"
        dlgID = wx.OK
        dlg = wx.MessageDialog(self, msg, title, dlgID)
        dlg.ShowModal() # Show it
        dlg.Destroy() # finally destroy it when finished



###############################################################################
# Create an instance of the application without redirecting output to a window
app = wx.App(False)

# Create the main window
frame = MainWindow(None, 'Small editor')
frame.Center()

# Start the application loop
app.MainLoop()


