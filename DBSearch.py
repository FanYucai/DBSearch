import MySQLdb
from Tkinter import *

class App(object):
    def __init__(self, master):
        self.col1Content = ''
        self.col2Content = ''
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

        self.showSQL = 'qwq'
        self.searchButton = Button(master, text='search', borderwidth=2, command=self.searchDB)
        self.searchButton.grid(row=3, column=2)

        self.sqlLabel = Label(master, textvariable=self.showSQL, justify=CENTER)
        self.sqlLabel.grid(row=0, columnspan=3)

    def searchDB(self):
#        self.col1Content = self.col1Entry.get().strip()
#        self.col2Content = self.col2Entry.get().strip()
        self.showSQL = self.col1Content + ' ' + self.col2Content
        return

"""
        frame = Frame(master)
        frame.pack()

        self.inputSearch = Button(
            frame, text="QUIT", fg="red", command=frame.quit
            )
        self.inputSearch.pack(side=LEFT)

        self.hi_there = Button(frame, text="Hello", command=self.say_hi)
        self.hi_there.pack(side=LEFT)

    def say_hi(self):
        print "hi there, everyone!"
"""

root = Tk()
app = App(root)
#root.bind('<Return>', App.searchDB)
#entryCol1 = Entry(top)
#entryCol2 = Entry(top)


#entryCol1.pack()
#entryCol2.pack()

#### SQL part####

db = MySQLdb.connect("localhost","root","12345678","labdb")

cursor = db.cursor()

sql = """insert into testtable(testCol1, testCol2) values (666, 666)""";

try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()

db.close()

#### SQL part end ####

root.mainloop()
