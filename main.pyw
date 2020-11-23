from tkinter import *
from tkinter.ttk import Treeview
from tkinter.messagebox import *
from datetime import datetime
from docs.db import common, eng, mus, pe, kuran, gor, life, value, robot, skills, programs
import webbrowser
import json


width = 850
height = 650
color = "#030519"


class GUI(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)
        with open("docs/calendar.json", "r") as file:
            self.calendar = json.load(file)
        self.initUI()

    def initUI(self):
        self.pack(expand=True, fill=BOTH)

        frame1 = Frame(self, bg=color)
        frame1.pack(fill=X, pady=10)

        frame2 = Frame(self, bg=color)
        frame2.pack(fill=X, pady=20)

        frame3 = Frame(self, bg=color)
        frame3.pack(fill=X, pady=30)

        Label(frame1, text="Ders Takvimi", font="ComicSans 25", bg=color, fg="white").pack(fill=X)

        tree = Treeview(frame2)
        tree['show'] = "headings"
        tree["columns"] = ("week", "one", "two", "three", "four", "five", "six", "seven")
        tree.pack()

        treeWidth = 106

        tree.column("week", width=treeWidth, anchor=W)
        tree.column("one", width=treeWidth, anchor=W)
        tree.column("two", width=treeWidth, anchor=W)
        tree.column("three", width=treeWidth, anchor=W)
        tree.column("four", width=treeWidth, anchor=W)
        tree.column("five", width=treeWidth, anchor=W)
        tree.column("six", width=treeWidth, anchor=W)
        tree.column("seven", width=treeWidth, anchor=W)

        tree.heading("week", text="")
        tree.heading("one", text="1.Ders")
        tree.heading("two", text="2.Ders")
        tree.heading("three", text="3.Ders")
        tree.heading("four", text="4.Ders")
        tree.heading("five", text="5.Ders")
        tree.heading("six", text="6.Ders")
        tree.heading("seven", text="7.Ders")

        tree.insert("", "end", text="", values=("Pazartesi", programs[0][0][1],  programs[0][1][1], programs[0][2][1], programs[0][3][1], programs[0][4][1], programs[0][5][1], programs[0][6][1]))
        tree.insert("", "end", text="", values=("Salı",  programs[1][0][1], programs[1][1][1], programs[1][2][1], programs[1][3][1], programs[1][4][1], programs[1][5][1], programs[1][6][1]))
        tree.insert("", "end", text="", values=("Çarşamba", programs[2][0][1], programs[2][1][1], programs[2][2][1], programs[2][3][1], programs[2][4][1], programs[2][5][1], programs[2][6][1]))
        tree.insert("", "end", text="", values=("Perşembe", programs[3][0][1], programs[3][1][1], programs[3][2][1], programs[3][3][1], programs[3][4][1], programs[3][5][1], programs[3][6][1]))
        tree.insert("", "end", text="", values=("Cuma", programs[4][0][1], programs[4][1][1], programs[4][2][1], programs[4][3][1], programs[4][4][1], programs[4][5][1], programs[4][6][1]))

        Label(frame3, text="\n\n\t09.30 - 10.05 -> 1.Ders\t\n\n"
                           "\t10.20 - 10.55 -> 2.Ders\t\n\n"
                           "\t11.05 - 11.40 -> 3.Ders\t\n\n"
                           "\t11.50 - 12.25 -> 4.Ders\t\n\n"
                           "\t12.35 - 13.10 -> 5.Ders\t\n\n"
                           "\t16.40 - 17.15 -> 6.Ders\t\n\n"
                           "\t17.25 - 18.00 -> 7.Ders\t\n\n",
                           borderwidth=3, relief="groove").grid(row=0, column=0)

        teachers = Button(frame3, text="Dersler", command=self.newWindow, height=3, width=15)
        teachers.grid(row=0, column=1)

        lecture = Button(frame3, text="Derse Gir", command=self.which, height=3, width=15)
        lecture.grid(row=0, column=2)

        Grid.columnconfigure(frame3, 0, weight=1)
        Grid.columnconfigure(frame3, 1, weight=1)
        Grid.columnconfigure(frame3, 2, weight=1)

    def which(self):
        try:
            self.nw.destroy()
        except AttributeError:
            pass

        day = datetime.now().strftime("%A")
        hour = datetime.now().strftime("%H")
        minute = datetime.now().strftime("%M")

        if day not in self.calendar:
            showerror("Hata", "Bugün ders yok")

        elif int(hour) < 9 or int(hour) > 17:
            showerror("Hata", "Ders saati değil")

        else:
            ders = self.number(int(hour), int(minute))

            if ders == -1:
                showerror("Hata", "Dersler bitti. Geçmiş olsun ")

            elif ders == 0:
                showinfo("Info", "Şimdi öğle tenefüsü vakti. Ders yok")
            else:
                url = self.calendar.get(day).get(str(ders))
                self.open(url)

    def number(self, hour: int, minute: int) -> int:

        if hour == 9:
            return 1

        elif hour == 10:
            if minute < 50:
                return 2
            else:
                return 3

        elif hour == 11:
            if minute < 35:
                return 3
            else:
                return 4

        elif hour == 12:
            if minute < 20:
                return 4

            else:
                return 5

        elif hour == 13 or hour == 14 or hour == 15:
            return 0

        elif hour == 16:
            if minute < 30:
                return 0

            else:
                return 6

        elif hour == 17:
            if minute < 10:
                return 6
            else:
                return 7

    def newWindow(self):
        self.nw = Toplevel()
        self.nw.title("Ders Takvimi")
        self.nwWidth = 304
        self.nwHeight = 460
        self.nw.config(bg="#015578")

        self.nw.geometry(f"{self.nwWidth}x{self.nwHeight}+{int(screenWidth / 2 - self.nwWidth / 2)}+{int(screenHeight / 2 - self.nwHeight / 2) - 30}")

        buttonWidth = 15
        buttonHeight = 3

        tur = Button(self.nw, text="Türkçe", width=buttonWidth, height=buttonHeight, command=lambda name="t": self.prof(name))
        tur.grid(row=0, column=0, pady=10)

        mat = Button(self.nw, text="Matematik", width=buttonWidth, height=buttonHeight, command=lambda name="m": self.prof(name))
        mat.grid(row=0, column=1, pady=10)

        fen = Button(self.nw, text="Fen ve Teknoloji", width=buttonWidth, height=buttonHeight, command=lambda name="f": self.prof(name))
        fen.grid(row=1, column=0, pady=10)

        ing = Button(self.nw, text="İngilizce", width=buttonWidth, height=buttonHeight, command=lambda name="i": self.prof(name))
        ing.grid(row=1, column=1, pady=10)

        muzik = Button(self.nw, text="Müzik", width=buttonWidth, height=buttonHeight, command=lambda name="mu": self.prof(name))
        muzik.grid(row=2, column=0, pady=10)

        beden = Button(self.nw, text="Beden Eğitimi", width=buttonWidth, height=buttonHeight, command=lambda name="b": self.prof(name))
        beden.grid(row=2, column=1, pady=10)

        kur = Button(self.nw, text="Kuran", width=buttonWidth, height=buttonHeight, command=lambda name="k": self.prof(name))
        kur.grid(row=3, column=0, pady=10)

        resim = Button(self.nw, text="Görsel Sanatlar", width=buttonWidth, height=buttonHeight, command=lambda name="g": self.prof(name))
        resim.grid(row=3, column=1, pady=10)

        hayat = Button(self.nw, text="Hayat Bilgisi", width=buttonWidth, height=buttonHeight, command=lambda name="h": self.prof(name))
        hayat.grid(row=4, column=0, pady=10)

        deger = Button(self.nw, text="Değerler Eğitimi", width=buttonWidth, height=buttonHeight, command=lambda name="d": self.prof(name))
        deger.grid(row=4, column=1, pady=10)

        rob = Button(self.nw, text="Robotik", width=buttonWidth, height=buttonHeight, command=lambda name="r": self.prof(name))
        rob.grid(row=5, column=0, pady=10)

        skl = Button(self.nw, text="Skills", width=buttonWidth, height=buttonHeight, command=lambda name="s": self.prof(name))
        skl.grid(row=5, column=1, pady=10)

        Grid.columnconfigure(self.nw, 0, weight=1)
        Grid.columnconfigure(self.nw, 1, weight=1)

    def prof(self, name):
        self.nw.destroy()

        if name == "t":
            link = common
        elif name == "m":
            link = common
        elif name == "f":
            link = common
        elif name == "i":
            link = eng
        elif name == "mu":
            link = mus
        elif name == "b":
            link = pe
        elif name == "k":
            link = kuran
        elif name == "g":
            link = gor
        elif name == "h":
            link = life
        elif name == "d":
            link = value
        elif name == "r":
            link = robot
        else:
            link = skills

        self.open(link[0])

    def open(self, url):
        webbrowser.register('chrome', None, webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
        print(url)
        webbrowser.get('chrome').open(url)


if __name__ == '__main__':
    root = Tk()
    app = GUI(root)
    root.title("Ders Takvimi")
    screenWidth = root.winfo_screenwidth()
    screenHeight = root.winfo_screenheight()
    root.geometry(f"{width}x{height}+{int(screenWidth / 2 - width / 2)}+{int(screenHeight / 2 - height / 2) - 30}")
    root.iconphoto(True, PhotoImage(file="images/icon.png"))
    app.config(bg=color)
    root.mainloop()
