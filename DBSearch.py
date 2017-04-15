import MySQLdb
from Tkinter import *

class App:

    def __init__(self, master):

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


root = Tk()
app = App(root)
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
