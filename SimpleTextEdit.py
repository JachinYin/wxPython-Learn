# -*- coding: utf-8 -*-
'''
简单文本编辑器
Author: Jachin
Data: 2017- 11- 25
'''
import os
import wx


class MainWindow(wx.Frame):
    def __init__(self, parent, title):
        self.dirname=''

        wx.Frame.__init__(self, parent, title=title, size=(600,400)
                          ,style = wx.DEFAULT_FRAME_STYLE,pos = (400,100))
        self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        self.CreateStatusBar() # A StatusBar in the bottom of the window

        #btn = wx.Button(self,pos = (200,300))
        # Setting up the menu.
        filemenu= wx.Menu()
        editMenu = wx.Menu()

        # wx.ID_ABOUT and wx.ID_EXIT are standard ids provided by wxWidgets.
        menuOpen = filemenu.Append(wx.ID_OPEN, "&打开","打开一个需要编辑的文件")
        menuAbout = filemenu.Append(wx.ID_ABOUT, "&关于","这是一个简单的文本编辑器")
        menuExit = filemenu.Append(wx.ID_EXIT,"&退出","退出程序")

        menuCopy = editMenu.Append(wx.ID_COPY,'复制','复制选中文本')
        menuPaste = editMenu.Append(wx.ID_PASTE,'粘贴','粘贴剪贴板的内容')

        # Creating the menubar.
        menuBar = wx.MenuBar()
        menuBar.Append(filemenu,"&文件") # Adding the "filemenu" to the MenuBar
        menuBar.Append(editMenu,"&编辑")
        self.SetMenuBar(menuBar)  # Adding the MenuBar to the Frame content.

        # Set events.
        self.Bind(wx.EVT_MENU, self.OnOpen, menuOpen)
        self.Bind(wx.EVT_MENU, self.OnAbout, menuAbout)
        self.Bind(wx.EVT_MENU, self.OnExit, menuExit)
        self.Bind(wx.EVT_MENU, self.OnCopy, menuCopy)
        self.Bind(wx.EVT_MENU, self.OnPaste, menuPaste)

        self.SetStatusText('状态栏')

        self.Show(True)

    def OnOpen(self,e):
        """ Open a file"""
        dlg = wx.FileDialog(self, "选择一个文件", self.dirname, "", "*.*", wx.FD_OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            self.filename = dlg.GetFilename()
            self.dirname = dlg.GetDirectory()
            f = open(os.path.join(self.dirname, self.filename), 'r')
            self.control.SetValue(f.read())
            f.close()
        dlg.Destroy()

    def OnAbout(self,e):
        # A message dialog box with an OK button. wx.OK is a standard ID in wxWidgets.
        dlg = wx.MessageDialog( self, "一个小型的文本编辑器\nAuthor:柒夕影", "关于简单编辑器", wx.OK)
        dlg.ShowModal() # Show it
        dlg.Destroy() # finally destroy it when finished.

    def OnExit(self,e):
        self.Close(True)  # Close the frame.

    def OnCopy(self,e):
        print e

    def OnPaste(self,e):
        pass


app = wx.App(False)
frame = MainWindow(None, "简单编辑器")
app.MainLoop()
