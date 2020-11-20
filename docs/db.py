import json
import pprint


tur = ("https://us04web.zoom.us/j/8391860248?pwd=UFQ3bmtodVZmMm1NN2wxOFcreWpwZz09", "Türkçe")
fen = ("https://us04web.zoom.us/j/8391860248?pwd=UFQ3bmtodVZmMm1NN2wxOFcreWpwZz09", "Fen ve Teknoloji")
mat = ("https://us04web.zoom.us/j/8391860248?pwd=UFQ3bmtodVZmMm1NN2wxOFcreWpwZz09", "Matematik")
common = ("https://us04web.zoom.us/j/8391860248?pwd=UFQ3bmtodVZmMm1NN2wxOFcreWpwZz09", "")
eng = ("https://us04web.zoom.us/j/9018960986?pwd=Qzk1Sm9kMmxId0NyNnVlR0hSbnRJdz09", "İngilizce")
pe = ("https://us04web.zoom.us/j/3452723043?pwd=bE03cktJOHZ2Lzg2Tmt0amREVGpEdz09", "Beden Eğitimi")
kuran = ("https://us04web.zoom.us/j/3809392513?pwd=ODV0V2g1bTFhcmxBaU80dW90TnF4Zz09", "Kuran")
life = ("https://us04web.zoom.us/j/8391860248?pwd=UFQ3bmtodVZmMm1NN2wxOFcreWpwZz09", "Hayat Bilgisi")
robot = ("https://us04web.zoom.us/j/5609504756?pwd=MVMzTU8xaTlBV1U3Yjd1RzRVVHRPdz09", "Robotik Kodlama")
skills = ("https://us04web.zoom.us/j/7918989451?pwd=VUNEdkE0R0VxQisyVU9TZitQSU1QQT09", "Skills")
gor = ("https://us04web.zoom.us/j/3314303377", "Görsel Sanatlar")
mus = ("https://us04web.zoom.us/j/4975962849", "Müzik")
value = ("https://us04web.zoom.us/j/6868293773", "Değerler Eğitimi")

programs = [
    [mat, fen, pe, eng, tur, kuran, tur],
    [tur, eng, mat, skills, life, tur, kuran],
    [mat, fen, life, mus, eng, tur, eng],
    [tur, robot, tur, eng, value, gor, mat],
    [fen, mat, tur, life, tur, eng, eng]
]


lectures = {
    "Monday": {1: programs[0][0][0], 2: programs[0][1][0], 3: programs[0][2][0], 4: programs[0][3][0], 5: programs[0][4][0], 6: programs[0][5][0], 7: programs[0][6][0]},
    "Tuesday": {1: programs[1][0][0], 2: programs[1][1][0], 3: programs[1][2][0], 4: programs[1][3][0], 5: programs[1][4][0], 6: programs[1][5][0], 7: programs[1][6][0]},
    "Wednesday": {1: programs[2][0][0], 2: programs[2][1][0], 3: programs[2][2][0], 4: programs[2][3][0], 5: programs[2][4][0], 6: programs[2][5][0], 7: programs[2][6][0]},
    "Thursday": {1: programs[3][0][0], 2: programs[3][1][0], 3: programs[3][2][0], 4: programs[3][3][0], 5: programs[3][4][0], 6: programs[3][5][0], 7: programs[3][6][0]},
    "Friday": {1: programs[4][0][0], 2: programs[4][1][0], 3: programs[4][2][0], 4: programs[4][3][0], 5: programs[4][4][0], 6: programs[4][5][0], 7: programs[4][6][0]}
}


def dump():

    with open("docs/calendar.json", "w") as file:

        json.dump(lectures, file, indent=2)


def load():

    with open("docs/calendar.json", "r") as file:

        dic = json.load(file)

    pprint.pprint(dic)


# dump()
# load()
