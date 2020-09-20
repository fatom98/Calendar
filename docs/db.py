import json, pprint

tur = "https://us04web.zoom.us/j/8391860248?pwd=UFQ3bmtodVZmMm1NN2wxOFcreWpwZz09"
fen = "https://us04web.zoom.us/j/8391860248?pwd=UFQ3bmtodVZmMm1NN2wxOFcreWpwZz09"
mat = "https://us04web.zoom.us/j/8391860248?pwd=UFQ3bmtodVZmMm1NN2wxOFcreWpwZz09"
common = "https://us04web.zoom.us/j/8391860248?pwd=UFQ3bmtodVZmMm1NN2wxOFcreWpwZz09"
eng = "https://us04web.zoom.us/j/9018960986?pwd=Qzk1Sm9kMmxId0NyNnVlR0hSbnRJdz09"
pe = "https://us04web.zoom.us/j/3452723043?pwd=bE03cktJOHZ2Lzg2Tmt0amREVGpEdz09"
kuran = "https://us04web.zoom.us/j/3809392513?pwd=ODV0V2g1bTFhcmxBaU80dW90TnF4Zz09"
life ="https://us04web.zoom.us/j/8391860248?pwd=UFQ3bmtodVZmMm1NN2wxOFcreWpwZz09"
gor = "https://us04web.zoom.us/j/3314303377"
mus = "https://us04web.zoom.us/j/4975962849"
value = ""
robot = ""
skills = ""


lectures = {
    "Monday": {1: f"{eng}", 2: f"{life}", 3: f"{tur}", 4: f"{mus}", 5: f"{mat}", 6: f"{fen}", 7: f"{value}"},
    "Tuesday": {1: f"{tur}", 2: f"{tur}", 3: f"{eng}", 4: f"{pe}", 5: f"{mat}", 6: f"{eng}", 7: f"{fen}"},
    "Wednesday": {1: f"{tur}", 2: f"{kuran}", 3: f"{eng}", 4: f"{mat}", 5: f"{fen}", 6: f"{tur}", 7: f"{robot}"},
    "Thursday": {1: f"{eng}", 2: f"{tur}", 3: f"{life}", 4: f"{kuran}", 5: f"{mat}", 6: f"{gor}", 7: f"{tur}"},
    "Friday": {1: f"{eng}", 2: f"{mat}", 3: f"{tur}", 4: f"{skills}", 5: f"{life}", 6: f"{tur}", 7: f"{eng}"}
}

def dump():
    with open("calendar.json", "w") as file:

        json.dump(lectures, file, indent = 2)

def load():
    with open("calendar.json", "r") as file:

        dic = json.load(file)

    pprint.pprint(dic)

#dump()
#load()


