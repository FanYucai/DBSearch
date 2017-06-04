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

        self.Ssex = wx.ComboBox(panel, -1, "", pos=(60, 100), choices=[u"-", u"男", u"女"], size=(36,21))
        self.SsexP = wx.ComboBox(panel, -1, "", pos=(124, 100), choices=[u"-", u"男", u"女"], size=(36,21))
        
        self.Sid = wx.TextCtrl(panel, -1, "", pos=(60, 10), size=(36,21))
        self.SidP = wx.TextCtrl(panel, -1, "", pos=(124, 10), size=(36,21))

        self.Sname = wx.TextCtrl(panel, -1, "", pos=(60, 40), size=(36,21))
        self.SnameP = wx.TextCtrl(panel, -1, "", pos=(124, 40), size=(36,21))

        self.Sage1 = wx.TextCtrl(panel, -1, "", pos=(60, 70), size=(36, 21))
        self.Sage2 = wx.TextCtrl(panel, -1, "", pos=(124, 70), size=(36, 21))

        self.Sclass = wx.TextCtrl(panel, -1, "", pos=(250, 10), size=(36,21))
        self.SclassP = wx.TextCtrl(panel, -1, "", pos=(314, 10), size=(36,21))

        self.Sdept = wx.TextCtrl(panel, -1, "", pos=(250, 40), size=(36,21))
        self.SdeptP = wx.TextCtrl(panel, -1, "", pos=(314, 40), size=(36,21))

        self.Saddr = wx.TextCtrl(panel, -1, "", pos=(250, 70), size=(36,21))
        self.SaddrP = wx.TextCtrl(panel, -1, "", pos=(314, 70), size=(36,21))

        # self.ResDisplay = wx.TextCtrl(panel, -1, "", pos=(60, 200), size=(550, 200), style=wx.TE_MULTILINE)
        self.sqlText = wx.TextCtrl(panel, -1, "", pos=(60, 140), size=(553, 50), style=wx.TE_READONLY)
        
        self.buttonSearch = wx.Button(panel, label=u"查询", pos=(450, 10), size=(100, 27))
        self.buttonSearch.Bind(wx.EVT_BUTTON, self.searchSql)

        self.buttonSearch = wx.Button(panel, label=u"插入", pos=(450, 40), size=(100, 27))
        self.buttonSearch.Bind(wx.EVT_BUTTON, self.insertSql)

        self.buttonSearch = wx.Button(panel, label=u"更新", pos=(450, 70), size=(100, 27))
        self.buttonSearch.Bind(wx.EVT_BUTTON, self.updateSql)

        self.buttonSearch = wx.Button(panel, label=u"删除", pos=(450, 100), size=(100, 27))
        self.buttonSearch.Bind(wx.EVT_BUTTON, self.deleteSql)

    def deleteSql(self, event):
        # display sql text:
        sqlDisplay = "delete FROM Student WHERE"

        self.ValSid = self.Sid.GetValue()
        self.ValSname = self.Sname.GetValue()
        self.ValSage1 = self.Sage1.GetValue()
        self.ValSclass = self.Sclass.GetValue()
        self.ValSdept = self.Sdept.GetValue()
        self.ValSaddr = self.Saddr.GetValue()
        self.ValSsex = self.Ssex.GetValue()

        hasPreAnd = 0

        if len(self.ValSid) != 0:
            sqlDisplay += " Sid=" + "'" + self.ValSid + "'"
            hasPreAnd = 1

        if len(self.ValSname) != 0:
            if hasPreAnd == 1:
                sqlDisplay += " AND"
            sqlDisplay += " Sname=" + "'" + self.ValSname + "'"
            hasPreAnd = 1

        if len(self.ValSage1) != 0:
            if hasPreAnd == 1:
                sqlDisplay += " AND"
            sqlDisplay += " Sage=" + self.ValSage1
            hasPreAnd = 1

        if len(self.ValSclass) != 0:
            if hasPreAnd == 1:
                sqlDisplay += " AND"
            sqlDisplay += " Sclass=" + "'" + self.ValSclass + "'"
            hasPreAnd = 1

        if len(self.ValSdept) != 0:
            if hasPreAnd == 1:
                sqlDisplay += " AND"
            sqlDisplay += " Sdept=" + "'" + self.ValSdept + "'"
            hasPreAnd = 1

        if len(self.ValSaddr) != 0:
            if hasPreAnd == 1:
                sqlDisplay += " AND"
            sqlDisplay += " Saddr=" + "'" + self.ValSaddr + "'"
            hasPreAnd = 1

        if self.ValSsex == u'男' or self.ValSsex == u'女':
            if hasPreAnd == 1:
                sqlDisplay += " AND"
            sqlDisplay += " Ssex=" + "'" + self.ValSsex + "'"
            hasPreAnd = 1

        if hasPreAnd == 0:
            sqlDisplay = u"请至少指定一个删除条件"
        else:
            sqlDisplay += ';'

        self.sqlText.SetValue(sqlDisplay)

        # SQL 插入语句
        db = MySQLdb.connect("localhost", "root", "12345678", "dblab", charset='utf8')
        cursor = db.cursor()
        try:
            sql = sqlDisplay
            # 执行sql语句
            cursor.execute(sql)
            # 提交到数据库执行
            db.commit()
            dlg = wx.MessageDialog(None, u"删除数据成功", u"标题信息", wx.YES_DEFAULT | wx.ICON_QUESTION)
            if dlg.ShowModal() == wx.ID_YES:
                self.Close(True)
            dlg.Destroy()
        except:
            dlg = wx.MessageDialog(None, u"删除出错，请检查数据", u"标题信息", wx.ICON_ERROR | wx.ICON_QUESTION)
            if dlg.ShowModal() == wx.ID_YES:
                self.Close(True)
            dlg.Destroy()
            db.rollback()

    def insertSql(self, event):
        self.ValSid = self.SidP.GetValue()
        self.ValSname = self.SnameP.GetValue()
        self.ValSage1 = self.Sage2.GetValue()
        # self.ValSage = self.Sage.GetValue()
        self.ValSclass = self.SclassP.GetValue()
        self.ValSdept = self.SdeptP.GetValue()
        self.ValSaddr = self.SaddrP.GetValue()
        self.ValSsex = self.SsexP.GetValue()

        # SQL 插入语句
        db = MySQLdb.connect("localhost", "root", "12345678", "dblab", charset='utf8')
        cursor = db.cursor()
        try:
            sql = "INSERT INTO Student(Sid, Sage, Ssex, Sdept, Sname, Saddr, Sclass) VALUES ('%s', %s, '%s', '%s', '%s', '%s', '%s')" % (self.ValSid, self.ValSage1, self.ValSsex, self.ValSdept, self.ValSname, self.ValSaddr, self.ValSclass)
            # 执行sql语句
            cursor.execute(sql)
            # 提交到数据库执行
            db.commit()
            dlg = wx.MessageDialog(None, u"插入数据成功", u"标题信息", wx.YES_DEFAULT | wx.ICON_QUESTION)
            if dlg.ShowModal() == wx.ID_YES:
                self.Close(True)
            dlg.Destroy()
        except:
            dlg = wx.MessageDialog(None, u"插入出错，请检查数据", u"标题信息", wx.ICON_ERROR | wx.ICON_QUESTION)
            if dlg.ShowModal() == wx.ID_YES:
                self.Close(True)
            dlg.Destroy()
            db.rollback()


    def updateSql(self, event):
        self.ValSid = self.Sid.GetValue()
        self.ValSname = self.Sname.GetValue()
        self.ValSage1 = self.Sage1.GetValue()
        # self.ValSage = self.Sage.GetValue()
        self.ValSclass = self.Sclass.GetValue()
        self.ValSdept = self.Sdept.GetValue()
        self.ValSaddr = self.Saddr.GetValue()
        self.ValSsex = self.Ssex.GetValue()

        self.ValSidP = self.SidP.GetValue()
        self.ValSnameP = self.SnameP.GetValue()
        self.ValSage2 = self.Sage2.GetValue()
        # self.ValSage = self.Sage.GetValue()
        self.ValSclassP = self.SclassP.GetValue()
        self.ValSdeptP = self.SdeptP.GetValue()
        self.ValSaddrP = self.SaddrP.GetValue()
        self.ValSsexP = self.SsexP.GetValue()

        # SQL 更新语句
        db = MySQLdb.connect("localhost", "root", "12345678", "dblab", charset='utf8')
        cursor = db.cursor()
        # try:
        sqlDisplay = "update Student set"

        if len(self.ValSidP) != 0:
            sqlDisplay += " Sid=" + "'" + self.ValSidP + "'"
            hasPreAnd = 1

        if len(self.ValSnameP) != 0:
            if hasPreAnd == 1:
                sqlDisplay += " ,"
            sqlDisplay += " Sname=" + "'" + self.ValSnameP + "'"
            hasPreAnd = 1

        if len(self.ValSage1) != 0:
            if hasPreAnd == 1:
                sqlDisplay += " ,"
            sqlDisplay += " Sage=" + self.ValSage2
            hasPreAnd = 1

        if len(self.ValSclassP) != 0:
            if hasPreAnd == 1:
                sqlDisplay += " ,"
            sqlDisplay += " Sclass=" + "'" + self.ValSclassP + "'"
            hasPreAnd = 1

        if len(self.ValSdeptP) != 0:
            if hasPreAnd == 1:
                sqlDisplay += " ,"
            sqlDisplay += " Sdept=" + "'" + self.ValSdeptP + "'"
            hasPreAnd = 1

        if len(self.ValSaddrP) != 0:
            if hasPreAnd == 1:
                sqlDisplay += " ,"
            sqlDisplay += " Saddr=" + "'" + self.ValSaddrP + "'"
            hasPreAnd = 1

        if self.ValSsexP == u'男' or self.ValSsexP == u'女':
            if hasPreAnd == 1:
                sqlDisplay += " ,"
            sqlDisplay += " Ssex=" + "'" + self.ValSsexP + "'"
            hasPreAnd = 1

        if hasPreAnd == 0:
            sqlDisplay = u"请至少指定一个更新项"
        else:
            sqlDisplay += " WHERE"
            hasPreAnd = 0
            if len(self.ValSid) != 0:
                sqlDisplay += " Sid=" + "'" + self.ValSid + "'"
                hasPreAnd = 1

            if len(self.ValSname) != 0:
                if hasPreAnd == 1:
                    sqlDisplay += " AND"
                sqlDisplay += " Sname=" + "'" + self.ValSname + "'"
                hasPreAnd = 1

            if len(self.ValSage2) != 0:
                if hasPreAnd == 1:
                    sqlDisplay += " AND"
                sqlDisplay += " Sage=" + self.ValSage1
                hasPreAnd = 1

            if len(self.ValSclass) != 0:
                if hasPreAnd == 1:
                    sqlDisplay += " AND"
                sqlDisplay += " Sclass=" + "'" + self.ValSclass + "'"
                hasPreAnd = 1

            if len(self.ValSdept) != 0:
                if hasPreAnd == 1:
                    sqlDisplay += " AND"
                sqlDisplay += " Sdept=" + "'" + self.ValSdept + "'"
                hasPreAnd = 1

            if len(self.ValSaddr) != 0:
                if hasPreAnd == 1:
                    sqlDisplay += " AND"
                sqlDisplay += " Saddr=" + "'" + self.ValSaddr + "'"
                hasPreAnd = 1

            if self.ValSsex == u'男' or self.ValSsex == u'女':
                if hasPreAnd == 1:
                    sqlDisplay += " AND"
                sqlDisplay += " Ssex=" + "'" + self.ValSsex + "'"
                hasPreAnd = 1

            if hasPreAnd == 0:
                sqlDisplay = u"请至少指定一个条件"
            else:
                sqlDisplay += ';' 
        self.sqlText.SetValue(sqlDisplay)

        # 执行sql语句
        try: 
            cursor.execute(sqlDisplay)
            # 提交到数据库执行
            db.commit()
            dlg = wx.MessageDialog(None, u"更新数据成功", u"标题信息", wx.YES_DEFAULT | wx.ICON_QUESTION)
            if dlg.ShowModal() == wx.ID_YES:
                self.Close(True)
            dlg.Destroy()
        except:
            dlg = wx.MessageDialog(None, u"更新出错，请检查数据", u"标题信息", wx.ICON_ERROR | wx.ICON_QUESTION)
            if dlg.ShowModal() == wx.ID_YES:
                self.Close(True)
            dlg.Destroy()
            # Rollback in case there is any error
            db.rollback()

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
            sqlDisplay += " Sage=" + self.ValSage1
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

        if self.ValSsex == u'男' or self.ValSsex == u'女':
            if hasPreAnd == 1:
                sqlDisplay += " AND"
            sqlDisplay += " Ssex=" + "'" + self.ValSsex + "'"
            hasPreAnd = 1

        if hasPreAnd == 0:
            sqlDisplay = u"SELECT * FROM Student;"
        else:
            sqlDisplay += ';'

        self.sqlText.SetValue(sqlDisplay)
        
        ################# search in MySQL ################
         
        db = MySQLdb.connect("localhost", "root", "12345678", "dblab", charset='utf8')
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
