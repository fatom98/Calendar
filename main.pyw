from tkinter import *
from tkinter.ttk import Treeview
from tkinter.messagebox import *
from datetime import datetime
import webbrowser, json

width = 804
height = 600
color = "#630611"


class GUI(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.initUI()


    def initUI(self):
        self.pack(expand = True, fill = BOTH)

        frame1 = Frame(self)
        frame1.pack(fill = X)

        frame2 = Frame(self, bg = color)
        frame2.pack(fill = X, pady = 20)

        frame3 = Frame(self, bg = color)
        frame3.pack(fill = X, pady = 30)

        Label(frame1, text = "Ders Takvimi", font = "ComicSans 16", bg = "#015578", fg = "white").pack(fill = X)

        tree = Treeview(frame2)
        tree['show'] = "headings"
        tree["columns"] = ("week", "one" , "two", "three", "four", "five")
        tree.pack()

        treeWidth = 134

        tree.column("week", width = treeWidth, anchor = W)
        tree.column("one", width = treeWidth, anchor = W)
        tree.column("two", width = treeWidth, anchor = W)
        tree.column("three", width = treeWidth, anchor = W)
        tree.column("four", width = treeWidth, anchor = W)
        tree.column("five", width = treeWidth, anchor = W)

        tree.heading("week", text = "")
        tree.heading("one", text = "1.Ders")
        tree.heading("two", text = "2.Ders")
        tree.heading("three", text = "3.Ders")
        tree.heading("four", text = "4.Ders")
        tree.heading("five", text = "5.Ders")

        tree.insert("", "end", text = "", values = ("Pazartesi", "İngilizce", "Görsel Sanatlar", "Türkçe", "Hayat Bilgisi", "Matematik"))
        tree.insert("", "end", text = "", values = ("Salı", "İngilizce", "Kuran", "Türkçe", "Matematik", "Türkçe"))
        tree.insert("", "end", text = "", values = ("Çarşamba", "Beden Eğitimi", "İngilizce", "Hayat Bilgisi", "Fen ve Teknoloji", "Matematik"))
        tree.insert("", "end", text = "", values = ("Perşembe", "Matematik", "Türkçe", "Müzik", "İngilizce", "İngilizce"))
        tree.insert("", "end", text = "", values = ("Cuma", "Kuran", "Matematik", "Fen", "Türkçe", "İngilizce"))

        Label(frame3, text = "\n\n\t14.00 - 14.30 -> 1.Ders\t\n\n"
                             "\t14.40 - 15.10 -> 2.Ders\t\n\n"
                             "\t15.20 - 15.50 -> 3.Ders\t\n\n"
                             "\t16.00 - 16.30 -> 4.Ders\t\n\n"
                             "\t16.40 - 17.10 -> 5.Ders\t\n\n", borderwidth = 3, relief = "groove").grid(row = 0, column = 0)

        lecture = Button(frame3, text = "Derse Gir", command = self.which, height = 3, width = 15)
        lecture.grid(row = 0, column = 1)

        Grid.columnconfigure(frame3, 0, weight = 1)
        Grid.columnconfigure(frame3, 1, weight = 1)

    def which(self):
        day = datetime.now().strftime("%A")
        hour = datetime.now().strftime("%H")
        minute = datetime.now().strftime("%M")

        with open("docs/calendar.json", "r") as file:
            calendar = json.load(file)

        if day not in calendar:
            showerror("Hata","Bugün ders yok")

        elif int(hour) < 13 or int(hour) > 17:
            showerror("Hata", "Ders saati değil")

        else:
            ders = self.number(int(hour), int(minute))

            if ders is -1:
                showerror("Hata", "Ders saati değil")

            else:
                url = calendar.get(day).get(str(ders))
                webbrowser.register('chrome', None, webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
                webbrowser.get('chrome').open(url)

    def number(self, hour: int, minute: int) -> int:

        if hour is 13:
            return 1

        elif hour is 14:
            if 0 <= minute < 30:
                return 1

            elif minute >= 30:
                return 2


        elif hour is 15:

            if 0 <= minute < 10:
                return 2

            elif 10 <= minute < 50:
                return 3

            else:
                return 4

        elif hour is 16:

            if 0 <= minute < 30:
                return 4

            elif 30 <= minute:
                return 5


        else:
            if 0 <= minute < 10:
                return 5

            else:
                return -1


if __name__ == '__main__':
    root = Tk()
    app = GUI(root)
    root.title("Ders Takvimi")
    screenWidth = root.winfo_screenwidth()
    screenHeight = root.winfo_screenheight()
    root.geometry(f"{width}x{height}+{ int(screenWidth/2 - width/2) }+{ int(screenHeight/2 - height/2) - 30 }")
    root.iconphoto(True, PhotoImage(file = "images/icon.png"))
    app.config(bg = color)
    root.mainloop()