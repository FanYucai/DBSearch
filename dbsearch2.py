#!/usr/bin/python
# -*- coding:utf-8 -*-
import MySQLdb
import wx
import wx.grid as gridlib
# colLabels = ["Sid", "Sname", "Sage", "Ssex", "Sclass", "Sdept", "Saddr"]
colLabels = ["Sid", "Sage", "Ssex", "Sdept", "Sname", "Saddr", "Sclass"]

class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, "My Frame", size=(670, 600))
        panel = wx.Panel(self, -1)

        ################################ gird ################################
        self.grid = gridlib.Grid(panel, -1, pos=(60, 200), size=(553, 300))
        self.grid.CreateGrid(0,7)
        for i in range(7):
            self.grid.SetColLabelValue(i, colLabels[i])
            self.grid.SetColSize(i, 79)
        self.grid.SetColSize(0, 89)
        self.grid.SetColSize(1, 56)
        self.grid.SetColSize(2, 56)
        self.grid.SetColSize(3, 56)
        self.grid.SetColSize(5, 140)
        self.grid.HideRowLabels()
        ################################ gird ################################

        wx.StaticText(panel, -1, u"学号", pos=(10, 10))
        wx.StaticText(panel, -1, u"姓名", pos=(10, 40))
        wx.StaticText(panel, -1, u"年龄自", pos=(10, 70))
        wx.StaticText(panel, -1, u"到", pos=(100, 70))
        wx.StaticText(panel, -1, u"性别", pos=(10, 100))
        wx.StaticText(panel, -1, u"班级", pos=(200, 10))
        wx.StaticText(panel, -1, u"学院", pos=(200, 40))
        wx.StaticText(panel, -1, u"地址", pos=(200, 70))

        self.Ssex = wx.ComboBox(panel, -1, "", pos=(60, 100), size=(104, 27), choices=[u"-", u"男", u"女"])
        self.Sid = wx.TextCtrl(panel, -1, "", pos=(60, 10))
        self.Sname = wx.TextCtrl(panel, -1, "", pos=(60, 40))
        self.Sage1 = wx.TextCtrl(panel, -1, "", pos=(60, 70), size=(36, 21))
        self.Sage2 = wx.TextCtrl(panel, -1, "", pos=(124, 70), size=(36, 21))
        self.Sclass = wx.TextCtrl(panel, -1, "", pos=(250, 10))
        self.Sdept = wx.TextCtrl(panel, -1, "", pos=(250, 40))
        self.Saddr = wx.TextCtrl(panel, -1, "", pos=(250, 70))
        # self.ResDisplay = wx.TextCtrl(panel, -1, "", pos=(60, 200), size=(550, 200), style=wx.TE_MULTILINE)
        self.sqlText = wx.TextCtrl(panel, -1, "", pos=(60, 140), size=(553, 50), style=wx.TE_READONLY)
        self.buttonSearch = wx.Button(panel, label=u"查询", pos=(250, 100), size=(100, 27))
        self.buttonSearch.Bind(wx.EVT_BUTTON, self.searchSql)

    def OnMove(self, event):
        pos = event.GetPosition()
        self.Sid.SetValue("%s, %s" % (pos.x, pos.y))

    def searchSql(self, event):
        # display sql text:
        sqlDisplay = "SELECT * FROM Student WHERE"

        self.ValSid = self.Sid.GetValue()
        self.ValSname = self.Sname.GetValue()
        self.ValSage1 = self.Sage1.GetValue()
        self.ValSage2 = self.Sage2.GetValue()
        self.ValSclass = self.Sclass.GetValue()
        self.ValSdept = self.Sdept.GetValue()
        self.ValSaddr = self.Saddr.GetValue()
        self.ValSsex = self.Ssex.GetValue()

        hasPreAnd = 0

        if len(self.ValSid) != 0:
            if '%' in self.ValSid:
                sqlDisplay += " Sid like " + "'" + self.ValSid + "'"
            else:
                sqlDisplay += " Sid=" + "'" + self.ValSid + "'"
            hasPreAnd = 1

        if len(self.ValSname) != 0:
            if hasPreAnd == 1:
                sqlDisplay += " AND"
            if '%' in self.ValSname:
                sqlDisplay += " Sname like " + "'" + self.ValSname + "'"
            else:
                sqlDisplay += " Sname=" + "'" + self.ValSname + "'"
            hasPreAnd = 1

        if len(self.ValSage1) != 0:
            if hasPreAnd == 1:
                sqlDisplay += " AND"
            sqlDisplay += " Sage>=" + self.ValSage1
            hasPreAnd = 1

        if len(self.ValSage2) != 0:
            if hasPreAnd == 1:
                sqlDisplay += " AND"
            sqlDisplay += " Sage<=" + self.ValSage2
            hasPreAnd = 1

        if len(self.ValSclass) != 0:
            if hasPreAnd == 1:
                sqlDisplay += " AND"
            if '%' in self.ValSclass:
                sqlDisplay += " Sclass like " + "'" + self.ValSclass + "'"            
            else:
                sqlDisplay += " Sclass=" + "'" + self.ValSclass + "'"
            hasPreAnd = 1

        if len(self.ValSdept) != 0:
            if hasPreAnd == 1:
                sqlDisplay += " AND"
            if '%' in self.ValSdept:
                sqlDisplay += " Sdept like " + "'" + self.ValSdept + "'"            
            else:
                sqlDisplay += " Sdept=" + "'" + self.ValSdept + "'"
            hasPreAnd = 1

        if len(self.ValSaddr) != 0:
            if hasPreAnd == 1:
                sqlDisplay += " AND"
            if '%' in self.ValSaddr:
                sqlDisplay += " Saddr like " + "'" + self.ValSaddr + "'"            
            else:
                sqlDisplay += " Saddr=" + "'" + self.ValSaddr + "'"
            hasPreAnd = 1

        if self.ValSsex != '-':
            if hasPreAnd == 1:
                sqlDisplay += " AND"
            if '%' in self.ValSsex:
                sqlDisplay += " Ssex like " + "'" + self.ValSsex + "'"            
            else:
                sqlDisplay += " Ssex=" + "'" + self.ValSsex + "'"
            hasPreAnd = 1

        if hasPreAnd == 0:
            sqlDisplay = u"请至少指定一个查询条件"
        else:
            sqlDisplay += ';'

        self.sqlText.SetValue(sqlDisplay)
        
        ################# search in MySQL ################
         
        db = MySQLdb.connect("localhost", "root", "12345678", "labdb", charset='utf8')
        cursor = db.cursor()
        sql = sqlDisplay
        # sql = "select * from student where Saddr like '吉林%';"
        # sql = sqlDisplay.encode('utf8')
        
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            # delete previous infomation
            for i in range(self.grid.GetNumberRows()):
                self.grid.DeleteRows(0)
            # append row for the grid to display result
            for resi in range(len(results)):
                self.grid.AppendRows()
                for resj in range(7):
                    self.grid.SetCellValue(resi, resj, unicode(results[resi][resj]))
            # set readonly attr for grid
            self.grid.EnableEditing(False)

        except:
            print "Error: unable to fecth data"

        db.close()

        ################# search in MySQL ################

if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame()
    frame.Show(True)
    app.MainLoop()
