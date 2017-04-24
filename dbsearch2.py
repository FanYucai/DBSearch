#!/usr/bin/python  
# -*- coding:utf-8 -*- 
import MySQLdb
import wx
class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, "My Frame", size = (400, 400))
        panel = wx.Panel(self, -1)
        # panel.Bind(wx.EVT_MOTION, self.OnMove)
        wx.StaticText(panel, -1, "Sid", pos = (10, 10))
        wx.StaticText(panel, -1, "Sname", pos = (10, 40))
        wx.StaticText(panel, -1, "Sage", pos = (10, 70))
        wx.StaticText(panel, -1, "Sex", pos = (10, 100))
        
        wx.StaticText(panel, -1, "Sclass", pos = (200, 10))
        wx.StaticText(panel, -1, "Sdept", pos = (200, 40))
        wx.StaticText(panel, -1, u"地址", pos = (200, 70))
        
        # wx.StaticText(panelSname, -1, "Sname", pos = (13, 12))
        # wx.StaticText(panelSage, -1, "Sage", pos = (15, 12))
        self.Ssex = wx.ComboBox(panel, -1, "", pos = (60, 100), size=(102,27), choices = [u"男", u"女", 'male']) 
        # self.rbox = wx.RadioBox(panel, label = u"性别", pos = (60,100), choices = [u"男", u"女"] , majorDimension = 1, style = wx.RA_SPECIFY_ROWS)
        self.Sid = wx.TextCtrl(panel, -1, "", pos = (60, 10))
        self.Sname = wx.TextCtrl(panel, -1, "", pos = (60, 40))
        self.Sage = wx.TextCtrl(panel, -1, "", pos = (60, 70))
        self.Sclass = wx.TextCtrl(panel, -1, "", pos = (250, 10))
        self.Sdept = wx.TextCtrl(panel, -1, "", pos = (250, 40))
        self.Saddr = wx.TextCtrl(panel, -1, "", pos = (250, 70))

        self.sqlText = wx.TextCtrl(panel, -1, "", pos = (60, 140), size=(300, 50))

        self.buttonSearch = wx.Button(panel, label="Search", pos=(270, 100))
        self.buttonSearch.Bind(wx.EVT_BUTTON, self.searchSql)

    def OnMove(self, event):
        pos = event.GetPosition()
        self.Sid.SetValue("%s, %s" %(pos.x, pos.y))

    def searchSql(self, event):
        #display:
        sqlDisplay = "SELECT * FROM Student WHERE"

        self.ValSid     = self.Sid.GetValue() 
        self.ValSname   = self.Sname.GetValue() 
        self.ValSage    = self.Sage.GetValue()
        self.ValSclass  = self.Sclass.GetValue() 
        self.ValSdept   = self.Sdept.GetValue() 
        self.ValSaddr   = self.Saddr.GetValue()
        self.ValSsex    = self.Ssex.GetValue()
        print self.ValSsex
        
        hasPreAnd = 0
        if len(self.ValSid) != 0 :
            sqlDisplay += " Sid="       + self.ValSid
            hasPreAnd = 1
        if len(self.ValSname) != 0:
            if hasPreAnd == 1:
                sqlDisplay += " AND"
            sqlDisplay += " Sname="     + self.ValSname
            hasPreAnd = 1
        if len(self.ValSage) != 0 :            
            if hasPreAnd == 1:
                sqlDisplay += " AND"
            sqlDisplay += " Sage="      + self.ValSage
            hasPreAnd = 1
        if len(self.ValSclass) != 0 :
            if hasPreAnd == 1:
                sqlDisplay += " AND"
            sqlDisplay += " Sclass="    + self.ValSclass
            hasPreAnd = 1
        if len(self.ValSdept) != 0 :
            if hasPreAnd == 1:
                sqlDisplay += " AND"
            sqlDisplay += " Sdept="     + self.ValSdept
            hasPreAnd = 1
        if len(self.ValSaddr) != 0 :
            if hasPreAnd == 1:
                sqlDisplay += " AND"            
            sqlDisplay += " Saddr="     + self.ValSaddr
            hasPreAnd = 1
        if len(self.ValSsex) != 0 : 
            if hasPreAnd == 1:
                sqlDisplay += " AND"           
            sqlDisplay += " Ssex="  + self.ValSsex

        self.sqlText.SetValue(sqlDisplay)
        #search in MySQL:
       
        db = MySQLdb.connect("localhost", "root", "12345678", "labdb")
        cursor = db.cursor()
        sql = sqlDisplay
        # sql = "select * from student"
        # sql = "SELECT * FROM TESTTABLE WHERE testCol1=%d AND testCol2=%d" % (col1, col2)
        try:
            cursor.execute(sql)
            # db.commit()
            results = cursor.fetchall()
            print ("共%d条查询结果\n") % len(results)
            # for row in results:
            #     resCol1 = row[0]
            #     resCol2 = row[1]
            #     print "row[1] = %d, row[2] = %d\n" % (resCol1, resCol2)    
        except:
            print "Error: unable to fecth data"

        db.close()

if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = MyFrame()
    frame.Show(True)
    app.MainLoop()