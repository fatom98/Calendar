import json, pprint

tur = "https://us04web.zoom.us/j/8391860248?pwd=UFQ3bmtodVZmMm1NN2wxOFcreWpwZz09"
fen = "https://us04web.zoom.us/j/8391860248?pwd=UFQ3bmtodVZmMm1NN2wxOFcreWpwZz09"
mat = "https://us04web.zoom.us/j/8391860248?pwd=UFQ3bmtodVZmMm1NN2wxOFcreWpwZz09"
common = "https://us04web.zoom.us/j/8391860248?pwd=UFQ3bmtodVZmMm1NN2wxOFcreWpwZz09"
eng = "https://us04web.zoom.us/j/9018960986?pwd=Qzk1Sm9kMmxId0NyNnVlR0hSbnRJdz09"
mus = "https://us04web.zoom.us/j/4975962849"
pe = "https://us04web.zoom.us/j/3452723043"
kuran = "https://us04web.zoom.us/j/4103999829"
gor = "https://us04web.zoom.us/j/3314303377"
life ="https://us04web.zoom.us/j/8391860248?pwd=UFQ3bmtodVZmMm1NN2wxOFcreWpwZz09"


lectures = {
    "Monday": {1: f"{eng}", 2: f"{gor}", 3: f"{tur}", 4: f"{life}", 5: f"{mat}"},
    "Tuesday": {1: f"{eng}", 2: f"{kuran}", 3: f"{tur}", 4: f"{mat}", 5: f"{tur}"},
    "Wednesday": {1: f"{pe}", 2: f"{eng}", 3: f"{life}", 4: f"{fen}", 5: f"{mat}"},
    "Thursday": {1: f"{mat}", 2: f"{tur}", 3: f"{mus}", 4: f"{eng}", 5: f"{eng}"},
    "Friday": {1: f"{kuran}", 2: f"{mat}", 3: f"{fen}", 4: f"{tur}", 5: f"{eng}"}
}

def dump():
    with open("docs/calendar.json", "w") as file:

        json.dump(lectures, file, indent = 2)

def load():
    with open("docs/calendar.json", "r") as file:

        dic = json.load(file)

    pprint.pprint(dic)

#dump()
#load()


