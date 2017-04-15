#! usr/bin/python #coding=utf-8
import MySQLdb
import string
from Tkinter import *

class App(object):
    def __init__(self, master):
        self.col1Content = StringVar('')
        self.col2Content = StringVar('')
        self.sqlContent = StringVar('')
        # self.col1Content.set('')
        # self.col2Content.set('')

        self.master = master
        self.col1 = Label(master, text="col1", borderwidth=2)
        self.col1.grid(row=1, sticky=W)

        self.col2 = Label(master, text="col2", borderwidth=2)
        self.col2.grid(row=2, sticky=W)

        self.col1Entry = Entry(master, textvariable=self.col1Content)
        self.col1Entry.grid(row=1, column=1, columnspan=2)
        self.col1Entry.focus_set()

        self.col2Entry = Entry(master, textvariable=self.col2Content)
        self.col2Entry.grid(row=2, column=1, columnspan=2)

        self.sqlEntry = Entry(master, textvariable=self.sqlContent)
        self.sqlEntry.grid(row=1, column=1, columnspan=2)

        self.searchButton = Button(master, text='search', borderwidth=2, command=self.searchDB)
        self.searchButton.grid(row=3, column=2)


    def searchDB(self, *args):
        db = MySQLdb.connect("localhost","root","12345678","labdb")
        cursor = db.cursor()
        col1, col2 = int(self.col1Content.get()), int(self.col2Content.get())
        sql = "select * from testtable where testCol1=%d and testCol2=%d" % (col1, col2);
        print sql
        
        try:
            cursor.execute(sql)
            # db.commit()
            results = cursor.fetchall()
            print ("共%d条查询结果\n") % len(results)
            for row in results:
                resCol1 = row[0]
                resCol2 = row[1]
                print "row[1] = %d, row[2] = %d\n" % (resCol1, resCol2)
                # print self.col1Content.get(), self.col2Content.get(), "hahaha"
        except:
            print "Error: unable to fecth data"

        db.close()
        return results

    # def insertDB(self):

    # def deleteDB(self):

    # def updateDB(self):


root = Tk()
app = App(root)
root.bind('<Return>', app.searchDB)
root.mainloop()
