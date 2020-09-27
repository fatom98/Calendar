import json, pprint

tur = "https://us04web.zoom.us/j/8391860248?pwd=UFQ3bmtodVZmMm1NN2wxOFcreWpwZz09"
fen = "https://us04web.zoom.us/j/8391860248?pwd=UFQ3bmtodVZmMm1NN2wxOFcreWpwZz09"
mat = "https://us04web.zoom.us/j/8391860248?pwd=UFQ3bmtodVZmMm1NN2wxOFcreWpwZz09"
common = "https://us04web.zoom.us/j/8391860248?pwd=UFQ3bmtodVZmMm1NN2wxOFcreWpwZz09"
eng = "https://us04web.zoom.us/j/9018960986?pwd=Qzk1Sm9kMmxId0NyNnVlR0hSbnRJdz09"
pe = "https://us04web.zoom.us/j/3452723043?pwd=bE03cktJOHZ2Lzg2Tmt0amREVGpEdz09"
kuran = "https://us04web.zoom.us/j/3809392513?pwd=ODV0V2g1bTFhcmxBaU80dW90TnF4Zz09"
life ="https://us04web.zoom.us/j/8391860248?pwd=UFQ3bmtodVZmMm1NN2wxOFcreWpwZz09"
robot = "https://us04web.zoom.us/j/5609504756?pwd=MVMzTU8xaTlBV1U3Yjd1RzRVVHRPdz09"
skills = "https://us04web.zoom.us/j/7918989451?pwd=VUNEdkE0R0VxQisyVU9TZitQSU1QQT09"
gor = "https://us04web.zoom.us/j/3314303377"
mus = "https://us04web.zoom.us/j/4975962849"
value = "https://us04web.zoom.us/j/6868293773"


lectures = {
    "Monday": {1: f"{eng}", 2: f"{life}", 3: f"{tur}", 4: f"{mus}", 5: f"{mat}", 6: f"{fen}", 7: f"{value}"},
    "Tuesday": {1: f"{tur}", 2: f"{tur}", 3: f"{eng}", 4: f"{pe}", 5: f"{mat}", 6: f"{eng}", 7: f"{kuran}"},
    "Wednesday": {1: f"{tur}", 2: f"{eng}", 3: f"{robot}", 4: f"{tur}", 5: f"{mat}", 6: f"{mat}", 7: f"{fen}"},
    "Thursday": {1: f"{eng}", 2: f"{life}", 3: f"{kuran}", 4: f"{tur}", 5: f"{mat}", 6: f"{gor}", 7: f"{tur}"},
    "Friday": {1: f"{eng}", 2: f"{life}", 3: f"{fen}", 4: f"{skills}", 5: f"{tur}", 6: f"{tur}", 7: f"{eng}"}
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


