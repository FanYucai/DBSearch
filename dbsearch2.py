#!/usr/bin/python  
# -*- coding:utf-8 -*- 

import wx
class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, "My Frame", size = (400, 400))
        panel = wx.Panel(self, -1)
        panel.Bind(wx.EVT_MOTION, self.OnMove)
        wx.StaticText(panel, -1, "ID", pos = (10, 10))
        wx.StaticText(panel, -1, "Name", pos = (10, 40))
        wx.StaticText(panel, -1, "Age", pos = (10, 70))
        
        # wx.StaticText(panelName, -1, "Name", pos = (13, 12))
        # wx.StaticText(panelAge, -1, "Age", pos = (15, 12))
        
        self.id = wx.TextCtrl(panel, -1, "", pos = (60, 10))
        self.name = wx.TextCtrl(panel, -1, "", pos = (60, 40))
        self.age = wx.TextCtrl(panel, -1, "", pos = (60, 70))
        self.sqlText = wx.TextCtrl(panel, -1, "", pos = (60, 130), size=(300, 50))

        self.buttonSearch = wx.Button(panel, label="Search", pos=(270, 90))
        buttonSearch.Bind(wx.EVT_BUTTON, self.searchSql)

    def OnMove(self, event):
        pos = event.GetPosition()
        self.id.SetValue("%s, %s" %(pos.x, pos.y))

    def searchSql(self, event):
        #display:
        sqlDisplay = "" 
        self.sqlText.SetValue("SELECT * FROM Student WHERE 123")
        #search in MySQL:

if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = MyFrame()
    frame.Show(True)
    app.MainLoop()