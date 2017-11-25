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
        menuSave = filemenu.Append(wx.ID_OPEN, "&保存","保存一个已经编辑好的文件")
        menuAbout = filemenu.Append(wx.ID_ABOUT, "&关于","这是一个简单的文本编辑器")
        menuExit = filemenu.Append(wx.ID_EXIT,"&退出","退出程序")

        menuClear = editMenu.Append(wx.ID_CLEAR,'清除','清除文本框的全部内容')
        menuCut = editMenu.Append(wx.ID_CUT,'剪切','剪切选中文本')
        menuCopy = editMenu.Append(wx.ID_COPY,'复制','复制选中文本')
        menuPaste = editMenu.Append(wx.ID_PASTE,'粘贴','粘贴剪贴板的内容')
        menuDelete = editMenu.Append(wx.ID_DELETE,'删除','删除选中的内容')
        menuChoseAll = editMenu.Append(wx.ID_SELECTALL,'全选','全选文本框的内容')

        # Creating the menubar.
        menuBar = wx.MenuBar()
        menuBar.Append(filemenu,"&文件") # Adding the "filemenu" to the MenuBar
        menuBar.Append(editMenu,"&编辑")
        self.SetMenuBar(menuBar)  # Adding the MenuBar to the Frame content.

        # Set events.
        self.Bind(wx.EVT_MENU, self.OnOpen, menuOpen)
        self.Bind(wx.EVT_MENU, self.OnSave, menuSave)
        self.Bind(wx.EVT_MENU, self.OnAbout, menuAbout)
        self.Bind(wx.EVT_MENU, self.OnExit, menuExit)

        self.Bind(wx.EVT_MENU, self.OnClear, menuClear)
        self.Bind(wx.EVT_MENU, self.OnCut, menuCut)
        self.Bind(wx.EVT_MENU, self.OnCopy, menuCopy)
        self.Bind(wx.EVT_MENU, self.OnPaste, menuPaste)
        self.Bind(wx.EVT_MENU, self.OnDelete, menuDelete)
        self.Bind(wx.EVT_MENU, self.OnChoseAll, menuChoseAll)

        self.SetStatusText('状态栏')

        self.Show(True)

    def OnOpen(self,e):
        """ Open a file"""
        dlg = wx.FileDialog(self, "选择一个文件", self.dirname, "", "*.txt", wx.FD_OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            self.filename = dlg.GetFilename()
            self.dirname = dlg.GetDirectory()
            f = open(os.path.join(self.dirname, self.filename), 'r')
            self.control.SetValue(f.read())
            f.close()
        dlg.Destroy()

    def OnSave(self,e):
        """ Save a file"""
        dlg = wx.FileDialog(self, "保存", self.dirname, "", "*.txt", wx.FD_SAVE)
        if dlg.ShowModal() == wx.ID_OK:
            self.filename = dlg.GetPath()
            self.control.SaveFile(self.filename)
        dlg.Destroy()

    def OnAbout(self,e):
        # A message dialog box with an OK button. wx.OK is a standard ID in wxWidgets.
        #dlg = wx.MessageBox("一个小型的文本编辑器\nBy:柒夕影", "关于简单编辑器", wx.OK)
        dlg = wx.MessageDialog(self, "一个小型的文本编辑器\n最后更新:2017-11-25\n\nBy:柒夕影", "关于 简单编辑器", wx.OK)
        dlg.ShowModal() # Show it
        dlg.Destroy() # finally destroy it when finished.

    def OnExit(self,e):
        self.Close(True)  # Close the frame.


    def OnClear(self,e):
        self.control.Clear()

    def OnCut(self,e):
        self.control.Cut()

    def OnCopy(self,e):
        self.control.Copy()

    def OnPaste(self,e):
        self.control.Paste()

    def OnDelete(self,e):
        '''删除选中的文本'''
        i,j = self.control.GetSelection()
        self.control.Replace(i,j,'')

    def OnChoseAll(self,e):
        self.control.SelectAll()

app = wx.App(False)
frame = MainWindow(None, "简单编辑器")
app.MainLoop()
