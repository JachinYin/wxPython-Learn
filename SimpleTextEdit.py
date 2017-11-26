# -*- coding: utf-8 -*-
'''
简单文本编辑器
Author: Jachin
Data: 2017- 11- 25
'''
import os
import wx
import time
import re

class MainWindow(wx.Frame):
    def __init__(self, parent, title):
        self.dirname=''

        wx.Frame.__init__(self, parent, title=title, size=(600,400)
                          ,style = wx.DEFAULT_FRAME_STYLE,pos = (400,100))
        self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE|wx.TE_RICH)
        self.CreateStatusBar() # A StatusBar in the bottom of the window

        #btn = wx.Button(self,pos = (200,300))
        # Setting up the menu.
        filemenu= wx.Menu()
        editMenu = wx.Menu()
        formatMenu = wx.Menu()
        viewMenu = wx.Menu()
        helpMenu = wx.Menu()

        # wx.ID_ABOUT and wx.ID_EXIT are standard ids provided by wxWidgets.
        menuOpen = filemenu.Append(wx.ID_OPEN, "&打开","打开一个需要编辑的文件")
        menuSave = filemenu.Append(wx.ID_SAVE, "&保存","保存一个已经编辑好的文件")
        filemenu.AppendSeparator()
        menuExit = filemenu.Append(wx.ID_EXIT,"&退出","退出程序")

        menuUndo = editMenu.Append(wx.ID_UNDO,'撤销','返回上一步的操作')
        editMenu.AppendSeparator()#添加分隔线
        menuCut = editMenu.Append(wx.ID_CUT,'剪切','剪切选中文本')
        menuCopy = editMenu.Append(wx.ID_COPY,'复制','复制选中文本')
        menuPaste = editMenu.Append(wx.ID_PASTE,'粘贴','粘贴剪贴板的内容')
        menuDelete = editMenu.Append(wx.ID_DELETE,'删除','删除选中的内容')
        editMenu.AppendSeparator()
        menuSearch = editMenu.Append(wx.ID_HELP_SEARCH,'查找','查找内容')
        editMenu.AppendSeparator()
        menuChoseAll = editMenu.Append(wx.ID_SELECTALL,'全选','全选文本框的内容')
        menuDate = editMenu.Append(wx.ID_ANY,'时间/日期','插入时间/日期')

        menuFont = formatMenu.Append(wx.ID_SELECT_FONT,'字体','选择字体')

        self.shst = menuStatus = viewMenu.Append(wx.ID_STATIC,'状态栏','隐藏状态栏',wx.ITEM_CHECK)

        menuAbout = helpMenu.Append(wx.ID_ABOUT, "关于","这是一个简单的文本编辑器")

        # Creating the menubar.
        menuBar = wx.MenuBar()
        menuBar.Append(filemenu,"文件(&F)") # Adding the "filemenu" to the MenuBar
        menuBar.Append(editMenu,"编辑(&E)")
        menuBar.Append(formatMenu,"格式(&O)")
        menuBar.Append(viewMenu,"查看(&V)")
        menuBar.Append(helpMenu,"帮助(&H)")
        self.SetMenuBar(menuBar)  # Adding the MenuBar to the Frame content.

        # Set events.
        self.Bind(wx.EVT_MENU, self.OnOpen, menuOpen)
        self.Bind(wx.EVT_MENU, self.OnSave, menuSave)
        self.Bind(wx.EVT_MENU, self.OnExit, menuExit)

        self.Bind(wx.EVT_MENU, self.OnUndo, menuUndo)
        self.Bind(wx.EVT_MENU, self.OnCut, menuCut)
        self.Bind(wx.EVT_MENU, self.OnCopy, menuCopy)
        self.Bind(wx.EVT_MENU, self.OnPaste, menuPaste)
        self.Bind(wx.EVT_MENU, self.OnDelete, menuDelete)
        self.Bind(wx.EVT_MENU, self.OnSearch, menuSearch)
        self.Bind(wx.EVT_MENU, self.OnChoseAll, menuChoseAll)
        self.Bind(wx.EVT_MENU,self.OnDate,menuDate)

        self.Bind(wx.EVT_MENU,self.OnStatus,menuStatus)

        self.Bind(wx.EVT_MENU, self.OnAbout, menuAbout)

        self.Bind(wx.EVT_MENU,self.OnFont,menuFont)

        self.SetStatusText('状态栏')

        self.Show(True)

    def OnOpen(self,e):
        """ Open a file"""
        slg = wx.FileDialog(self, "选择一个文件", self.dirname, "", "*.txt", wx.FD_OPEN)
        if slg.ShowModal() == wx.ID_OK:
            self.filename = slg.GetFilename()
            self.dirname = slg.GetDirectory()
            f = open(os.path.join(self.dirname, self.filename), 'r')
            self.control.SetValue(f.read())
            f.close()
        slg.Destroy()

    def OnSave(self,e):
        """ Save a file"""
        dlg = wx.FileDialog(self, "保存", self.dirname, "", "*.txt", wx.FD_SAVE)
        if dlg.ShowModal() == wx.ID_OK:
            self.filename = dlg.GetPath()
            self.control.SaveFile(self.filename)
        dlg.Destroy()


    def OnExit(self,e):
        self.Close(True)  # Close the frame.


    def OnUndo(self,e):
        self.control.Undo()

    def OnCut(self,e):
        self.control.Cut()

    def OnCopy(self,e):
        self.control.Copy()

    def OnPaste(self,e):
        self.control.Paste()

    def OnDelete(self,e):
        '''删除选中的文本'''
        i,j = self.control.GetSelection()
        #self.control.Replace(i,j,'')
        self.control.Remove(i,j)

    def OnChoseAll(self,e):
        self.control.SelectAll()

    def OnDate(self,e):
        date = time.strftime("%H:%M:%S %Y/%m/%d", time.localtime())
        self.control.WriteText(date)

    def OnFont(self,e):
        '''字体设置'''
        flg = wx.FontDialog(self,wx.FontData())

        if flg.ShowModal() == wx.ID_OK:
            data = flg.GetFontData()
            font = data.GetChosenFont()
            self.control.SetFont(font)
        flg.Destroy()

    def OnStatus(self,e):
        if self.shst.IsChecked():
            self.StatusBar.Show()
        else:
            self.StatusBar.Hide()

    def OnAbout(self,e):
        # A message dialog box with an OK button. wx.OK is a standard ID in wxWidgets.
        #dlg = wx.MessageBox("一个小型的文本编辑器\nBy:柒夕影", "关于简单编辑器", wx.OK)
        dlg = wx.MessageDialog(self, "一个小型的文本编辑器\n最后更新:2017-11-25\n\nBy:柒夕影", "关于 简单编辑器", wx.OK)
        dlg.ShowModal() # Show it
        dlg.Destroy() # finally destroy it when finished.


    def OnSearch(self,e):
        self.search = wx.Frame(self,title = '查找', size=(400,200)
                          ,style = wx.DEFAULT_FRAME_STYLE,pos = (480,180))
        self.search.SetBackgroundColour('white')
        self.find = wx.TextCtrl(self.search,style=wx.TE_LEFT,size = (250,25),pos = (40,40))

        btn_search = wx.Button(self.search,wx.ID_ANY,'查找',size = (35,25),pos = (300,40))
        btn_search.Bind(wx.EVT_BUTTON,self.Search)
        self.search.Show()

    def Search(self,e):
        keyw = self.find.GetValue().encode('utf-8')
        text = self.control.GetValue().encode('utf-8')
        reg = r".*?(%s){1,}.*?"%keyw
        results = re.findall(reg,text)
        for item in results:
            i,j = self.control.GetSelection()
            print i,j
            self.control.SetSelection(i,j)
            print item


app = wx.App(False)
frame = MainWindow(None, "简单编辑器")
app.MainLoop()
