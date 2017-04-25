#!/usr/bin/python  
# -*- coding:utf-8 -*- 
import MySQLdb
import wx
class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, "My Frame", size = (400, 400))
        panel = wx.Panel(self, -1)
        # panel.Bind(wx.EVT_MOTION, self.OnMove)
        wx.StaticText(panel, -1, u"学号", pos = (10, 10))
        wx.StaticText(panel, -1, u"姓名", pos = (10, 40))
        wx.StaticText(panel, -1, u"年龄", pos = (10, 70))
        wx.StaticText(panel, -1, u"性别", pos = (10, 100))
        
        wx.StaticText(panel, -1, u"班级", pos = (200, 10))
        wx.StaticText(panel, -1, u"学院", pos = (200, 40))
        wx.StaticText(panel, -1, u"地址", pos = (200, 70))
        
        # wx.StaticText(panelSname, -1, "Sname", pos = (13, 12))
        # wx.StaticText(panelSage, -1, "Sage", pos = (15, 12))
        self.Ssex = wx.ComboBox(panel, -1, "", pos = (60, 100), size=(102,27), choices = [u"男", u"女"]) 
        # self.rbox = wx.RadioBox(panel, label = u"性别", pos = (60,100), choices = [u"男", u"女"] , majorDimension = 1, style = wx.RA_SPECIFY_ROWS)
        self.Sid = wx.TextCtrl(panel, -1, "", pos = (60, 10))
        self.Sname = wx.TextCtrl(panel, -1, "", pos = (60, 40))
        self.Sage = wx.TextCtrl(panel, -1, "", pos = (60, 70))
        self.Sclass = wx.TextCtrl(panel, -1, "", pos = (250, 10))
        self.Sdept = wx.TextCtrl(panel, -1, "", pos = (250, 40))
        self.Saddr = wx.TextCtrl(panel, -1, "", pos = (250, 70))
        self.ResDisplay = wx.TextCtrl(panel, -1, "", pos = (60, 200), size=(300, 50))

        self.sqlText = wx.TextCtrl(panel, -1, "", pos = (60, 140), size=(300, 50))

        self.buttonSearch = wx.Button(panel, label="Search", pos=(270, 100))
        self.buttonSearch.Bind(wx.EVT_BUTTON, self.searchSql)
        
        # sizer = wx.BoxSizer(wx.VERTICAL)
        # sizer.Add(self.Sid,flag=wx.EXPAND)
        # sizer.Add(self.Sname,flag=wx.EXPAND)
        # sizer.Add(self.Sage,flag=wx.EXPAND)
        # sizer.Add(self.Sclass,flag=wx.EXPAND)
        # sizer.Add(self.Sdept,flag=wx.EXPAND)
        # sizer.Add(self.Saddr,flag=wx.EXPAND)
        # sizer.Add(self.sqlText,flag=wx.EXPAND)
        # sizer.Add(self.ResDisplay,flag=wx.EXPAND)
        # sizer.Add(self.buttonSearch,flag=wx.EXPAND)
        # sizer.Add(self.Sname,flag=wx.EXPAND)

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
        
        hasPreAnd = 0
        if len(self.ValSid) != 0 :
            sqlDisplay += " Sid=" + "'" + self.ValSid + "'"
            hasPreAnd = 1
        if len(self.ValSname) != 0:
            if hasPreAnd == 1:
                sqlDisplay += " AND"
            sqlDisplay += " Sname=" + "'" + self.ValSname + "'"
            hasPreAnd = 1
        if len(self.ValSage) != 0 :            
            if hasPreAnd == 1:
                sqlDisplay += " AND"
            sqlDisplay += " Sage=" + "'" + self.ValSage + "'"
            hasPreAnd = 1
        if len(self.ValSclass) != 0 :
            if hasPreAnd == 1:
                sqlDisplay += " AND"
            sqlDisplay += " Sclass=" + "'" + self.ValSclass + "'"
            hasPreAnd = 1
        if len(self.ValSdept) != 0 :
            if hasPreAnd == 1:
                sqlDisplay += " AND"
            sqlDisplay += " Sdept=" + "'" + self.ValSdept + "'"
            hasPreAnd = 1
        if len(self.ValSaddr) != 0 :
            if hasPreAnd == 1:
                sqlDisplay += " AND"            
            sqlDisplay += " Saddr=" + "'" + self.ValSaddr + "'"
            hasPreAnd = 1
        if len(self.ValSsex) != 0 : 
            if hasPreAnd == 1:
                sqlDisplay += " AND"           
            sqlDisplay += " Ssex=" + "'" + self.ValSsex + "'"

        sqlDisplay += ';'

        self.sqlText.SetValue(sqlDisplay)
        #search in MySQL:
       
        db = MySQLdb.connect("localhost", "root", "12345678", "labdb", charset = 'utf8')
        cursor = db.cursor()
        sql = sqlDisplay
        # sql = sqlDisplay.encode('utf8')
        print sql
        try:
            cursor.execute(sql)
            # db.commit()
            results = cursor.fetchall()
            resDisplayValue = ""
            print ("共%d条查询结果\n") % len(results)
            for row in results:
                resSid    = row[0]          + "\t"
                resSage   = unicode(row[1]) + "\t"
                resSsex   = row[2]          + "\t"
                resSdept  = row[3]          + "\t"
                resSname  = row[4]          + "\t"
                resSaddr  = row[5]          + "\t"
                resSclass = row[6]          + "\n"
                resDisplayValue += resSid+resSage+resSsex+resSdept+resSname+resSaddr+resSclass
                # print resDisplayValue
            self.ResDisplay.SetValue(resDisplayValue)
        except:
            print "Error: unable to fecth data"

        db.close()

if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = MyFrame()
    frame.Show(True)
    app.MainLoop()