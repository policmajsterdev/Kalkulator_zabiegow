from tkinter import *
from tkinter import ttk
import pandas as pd



def sprawdz_ceny():
    if cena_01.get().count(",") or cena_02.get().count(",") or cena_03.get().count(",") or cena_04.get().count(
            ",") or cena_05.get().count(",") or cena_06.get().count(",") or cena_07.get().count(
        ",") or cena_08.get().count(",") or cena_09.get().count(",") or cena_10.get().count(",") or cena_11.get().count(
        ",") or cena_12.get().count(",") or cena_13.get().count(",") or cena_14.get().count(",") or cena_15.get().count(
        ",") or cena_16.get().count(",") or cena_17.get().count(",") or cena_18.get().count(",") or cena_19.get().count(
        ",") or cena_20.get().count(",") or cena_21.get().count(",") or cena_22.get().count(",") or cena_23.get().count(
        ",") or cena_24.get().count(",") or cena_25.get().count(",") or cena_26.get().count(",") or cena_27.get().count(
        ",") or cena_28.get().count(",") or cena_29.get().count(",") or cena_30.get().count(",") or cena_31.get().count(
        ",") or cena_32.get().count(",") or cena_33.get().count(",") or cena_34.get().count(",") or cena_35.get().count(
        ",") or cena_36.get().count(",") or cena_37.get().count(",") or cena_38.get().count(",") or cena_39.get().count(
        ",") or cena_40.get().count(","):
        alarm_przec = Label(root, image=img_info1, borderwidth=0, highlightthickness=0)
        alarm_przec.place(relx=0.45, rely=0.08)
        alarm_przec = Label(root, image=img_info2, borderwidth=0, highlightthickness=0)
        alarm_przec.place(relx=0.45, rely=0.11)
    else:
        alarm_przec = Label(root, image=img_info3, borderwidth=0, highlightthickness=0)
        alarm_przec.place(relx=0.45, rely=0.08)
        alarm_przec = Label(root, image=img_info4, borderwidth=0, highlightthickness=0)
        alarm_przec.place(relx=0.45, rely=0.11)

        # Przelicznik uruchamia się po zakończeniu
        buttonik = Button(root, image=img_zliczanie, command=przelicz, borderwidth=0, highlightthickness=0)
        buttonik.place(relx=0.6, rely=0.085)
    return

def dopisz():
    if nazwa_01.get() == "--puste--":
        entry_cena_01 = Entry(root, textvariable=cena_01, justify=CENTER, width=14)
        entry_cena_01.insert(0, "0")
        entry_cena_01.grid(row=11, column=2)
    elif nazwa_01.get() == "Ablator":
        entry_cena_01 = Entry(root, textvariable=cena_01, justify=CENTER, width=14)
        entry_cena_01.insert(0, "572")
        entry_cena_01.grid(row=11, column=2)
    elif nazwa_01.get() == "Anestezjolog":
        entry_cena_01 = Entry(root, textvariable=cena_01, justify=CENTER, width=14, bg="#ffff00")
        entry_cena_01.insert(0, "350")
        entry_cena_01.grid(row=11, column=2)
    elif nazwa_01.get() == "Butelka 400ml do długotrwałego odsysania ran j.u. sterylna":
        entry_cena_01 = Entry(root, textvariable=cena_01, justify=CENTER, width=14)
        entry_cena_01.insert(0, "4")
        entry_cena_01.grid(row=11, column=2)
    elif nazwa_01.get() == "Doba":
        entry_cena_01 = Entry(root, textvariable=cena_01, justify=CENTER, width=14)
        entry_cena_01.insert(0, "700")
        entry_cena_01.grid(row=11, column=2)
    elif nazwa_01.get() == "Dren łączący do ssaka Grena":
        entry_cena_01 = Entry(root, textvariable=cena_01, justify=CENTER, width=14)
        entry_cena_01.insert(0, "5")
        entry_cena_01.grid(row=11, column=2)
    elif nazwa_01.get() == "Dren Redona Ch 16 dł. 800mm z trokarem":
        entry_cena_01 = Entry(root, textvariable=cena_01, justify=CENTER, width=14)
        entry_cena_01.insert(0, "29.74")
        entry_cena_01.grid(row=11, column=2)
    elif nazwa_01.get() == "Dren do pompy Artrex":
        entry_cena_01 = Entry(root, textvariable=cena_01, justify=CENTER, width=14)
        entry_cena_01.insert(0, "108")
        entry_cena_01.grid(row=11, column=2)
    elif nazwa_01.get() == "Drut wiercący 2,4 x 311":
        entry_cena_01 = Entry(root, textvariable=cena_01, justify=CENTER, width=14)
        entry_cena_01.insert(0, "139.60")
        entry_cena_01.grid(row=11, column=2)
    elif nazwa_01.get() == "Fartuch jałowy L":
        entry_cena_01 = Entry(root, textvariable=cena_01, justify=CENTER, width=14)
        entry_cena_01.insert(0, "17")
        entry_cena_01.grid(row=11, column=2)
    elif nazwa_01.get() == "Fartuch jałowy M":
        entry_cena_01 = Entry(root, textvariable=cena_01, justify=CENTER, width=14)
        entry_cena_01.insert(0, "15.28")
        entry_cena_01.grid(row=11, column=2)
    elif nazwa_01.get() == "Fartuch jałowy XL":
        entry_cena_01 = Entry(root, textvariable=cena_01, justify=CENTER, width=14)
        entry_cena_01.insert(0, "20.84")
        entry_cena_01.grid(row=11, column=2)
    elif nazwa_01.get() == "FasatThread BioComposite Interference Screw 8x30":
        entry_cena_01 = Entry(root, textvariable=cena_01, justify=CENTER, width=14)
        entry_cena_01.insert(0, "594")
        entry_cena_01.grid(row=11, column=2)
    elif nazwa_01.get() == "Folia operacyjna, jałowa 45cm x 55cm":
        entry_cena_01 = Entry(root, textvariable=cena_01, justify=CENTER, width=14)
        entry_cena_01.insert(0, "9.99")
        entry_cena_01.grid(row=11, column=2)
    elif nazwa_01.get() == "Gaziki 10 x 10cm":
        entry_cena_01 = Entry(root, textvariable=cena_01, justify=CENTER, width=14)
        entry_cena_01.insert(0, "0.10")
        entry_cena_01.grid(row=11, column=2)
    elif nazwa_01.get() == "Igła 0,6 x 60":
        entry_cena_01 = Entry(root, textvariable=cena_01, justify=CENTER, width=14)
        entry_cena_01.insert(0, "0.09")
        entry_cena_01.grid(row=11, column=2)
    elif nazwa_01.get() == "Igła 0,7 x 40":
        entry_cena_01 = Entry(root, textvariable=cena_01, justify=CENTER, width=14)
        entry_cena_01.insert(0, "0.05")
        entry_cena_01.grid(row=11, column=2)
    elif nazwa_01.get() == "Igła 0,8 x 40":
        entry_cena_01 = Entry(root, textvariable=cena_01, justify=CENTER, width=14)
        entry_cena_01.insert(0, "0.05")
        entry_cena_01.grid(row=11, column=2)
    elif nazwa_01.get() == "Igła 1,1 x 70":
        entry_cena_01 = Entry(root, textvariable=cena_01, justify=CENTER, width=14)
        entry_cena_01.insert(0, "0.16")
        entry_cena_01.grid(row=11, column=2)
    elif nazwa_01.get() == "Kaniulowana śruba int. biokompozytowa z osłonką jednoraz.":
        entry_cena_01 = Entry(root, textvariable=cena_01, justify=CENTER, width=14)
        entry_cena_01.insert(0, "594")
        entry_cena_01.grid(row=11, column=2)
    elif nazwa_01.get() == "Kaniulowana śruba int. biokompozytowa z pełnym gwintem":
        entry_cena_01 = Entry(root, textvariable=cena_01, justify=CENTER, width=14)
        entry_cena_01.insert(0, "594")
        entry_cena_01.grid(row=11, column=2)
    elif nazwa_01.get() == "Końcówka do Shavera":
        entry_cena_01 = Entry(root, textvariable=cena_01, justify=CENTER, width=14)
        entry_cena_01.insert(0, "270")
        entry_cena_01.grid(row=11, column=2)
    elif nazwa_01.get() == "Kotwica biokompozytowa SwiveLock":
        entry_cena_01 = Entry(root, textvariable=cena_01, justify=CENTER, width=14)
        entry_cena_01.insert(0, "918")
        entry_cena_01.grid(row=11, column=2)
    elif nazwa_01.get() == "Kotwica Corkscrew":
        entry_cena_01 = Entry(root, textvariable=cena_01, justify=CENTER, width=14)
        entry_cena_01.insert(0, "604")
        entry_cena_01.grid(row=11, column=2)
    elif nazwa_01.get() == "Kotwica FASTak":
        entry_cena_01 = Entry(root, textvariable=cena_01, justify=CENTER, width=14)
        entry_cena_01.insert(0, "432")
        entry_cena_01.grid(row=11, column=2)
    elif nazwa_01.get() == "Kotwica PEEK SwiveLock":
        entry_cena_01 = Entry(root, textvariable=cena_01, justify=CENTER, width=14)
        entry_cena_01.insert(0, "885.60")
        entry_cena_01.grid(row=11, column=2)
    elif nazwa_01.get() == "NaCl 3000ml":
        entry_cena_01 = Entry(root, textvariable=cena_01, justify=CENTER, width=14)
        entry_cena_01.insert(0, "29.72")
        entry_cena_01.grid(row=11, column=2)
    elif nazwa_01.get() == "NaCl 5000ml":
        entry_cena_01 = Entry(root, textvariable=cena_01, justify=CENTER, width=14)
        entry_cena_01.insert(0, "58.33")
        entry_cena_01.grid(row=11, column=2)
    elif nazwa_01.get() == "Nici Dafilon 2-0":
        entry_cena_01 = Entry(root, textvariable=cena_01, justify=CENTER, width=14)
        entry_cena_01.insert(0, "6.60")
        entry_cena_01.grid(row=11, column=2)
    elif nazwa_01.get() == "Nici Novosyn 2":
        entry_cena_01 = Entry(root, textvariable=cena_01, justify=CENTER, width=14)
        entry_cena_01.insert(0, "13")
        entry_cena_01.grid(row=11, column=2)
    elif nazwa_01.get() == "Nici Novosyn 2-0":
        entry_cena_01 = Entry(root, textvariable=cena_01, justify=CENTER, width=14)
        entry_cena_01.insert(0, "7.70")
        entry_cena_01.grid(row=11, column=2)
    elif nazwa_01.get() == "Nici Novosyn 3-0":
        entry_cena_01 = Entry(root, textvariable=cena_01, justify=CENTER, width=14)
        entry_cena_01.insert(0, "7.70")
        entry_cena_01.grid(row=11, column=2)
    elif nazwa_01.get() == "Nici Nylon 2-0":
        entry_cena_01 = Entry(root, textvariable=cena_01, justify=CENTER, width=14)
        entry_cena_01.insert(0, "2.50")
        entry_cena_01.grid(row=11, column=2)
    elif nazwa_01.get() == "Nici Nylon 3-0":
        entry_cena_01 = Entry(root, textvariable=cena_01, justify=CENTER, width=14)
        entry_cena_01.insert(0, "2")
        entry_cena_01.grid(row=11, column=2)
    elif nazwa_01.get() == "Nici PGLA":
        entry_cena_01 = Entry(root, textvariable=cena_01, justify=CENTER, width=14)
        entry_cena_01.insert(0, "11.60")
        entry_cena_01.grid(row=11, column=2)
    elif nazwa_01.get() == "Nici PremiCron 3":
        entry_cena_01 = Entry(root, textvariable=cena_01, justify=CENTER, width=14)
        entry_cena_01.insert(0, "6.50")
        entry_cena_01.grid(row=11, column=2)
    elif nazwa_01.get() == "Nici Vicryl 4-0":
        entry_cena_01 = Entry(root, textvariable=cena_01, justify=CENTER, width=14)
        entry_cena_01.insert(0, "7.50")
        entry_cena_01.grid(row=11, column=2)
    elif nazwa_01.get() == "Nitinol Guide Pin 1.1":
        entry_cena_01 = Entry(root, textvariable=cena_01, justify=CENTER, width=14)
        entry_cena_01.insert(0, "145.80")
        entry_cena_01.grid(row=11, column=2)
    elif nazwa_01.get() == "Osłona na przewody":
        entry_cena_01 = Entry(root, textvariable=cena_01, justify=CENTER, width=14)
        entry_cena_01.insert(0, "2.50")
        entry_cena_01.grid(row=11, column=2)
    elif nazwa_01.get() == "Ostrze Arthrex 90(86)x19x1,27":
        entry_cena_01 = Entry(root, textvariable=cena_01, justify=CENTER, width=14)
        entry_cena_01.insert(0, "216")
        entry_cena_01.grid(row=11, column=2)
    elif nazwa_01.get() == "Ostrze piły":
        entry_cena_01 = Entry(root, textvariable=cena_01, justify=CENTER, width=14)
        entry_cena_01.insert(0, "108")
        entry_cena_01.grid(row=11, column=2)
    elif nazwa_01.get() == "Pielęgniarka anest.":
        entry_cena_01 = Entry(root, textvariable=cena_01, justify=CENTER, width=14)
        entry_cena_01.insert(0, "50")
        entry_cena_01.grid(row=11, column=2)
    elif nazwa_01.get() == "Pielęgniarka instr.":
        entry_cena_01 = Entry(root, textvariable=cena_01, justify=CENTER, width=14)
        entry_cena_01.insert(0, "50")
        entry_cena_01.grid(row=11, column=2)
    elif nazwa_01.get() == "Pielęgniarka 'Noviline'":
        entry_cena_01 = Entry(root, textvariable=cena_01, justify=CENTER, width=14)
        entry_cena_01.insert(0, "30")
        entry_cena_01.grid(row=11, column=2)
    elif nazwa_01.get() == "Płytka PeekPower do osteotomii klinowej":
        entry_cena_01 = Entry(root, textvariable=cena_01, justify=CENTER, width=14)
        entry_cena_01.insert(0, "2160")
        entry_cena_01.grid(row=11, column=2)
    elif nazwa_01.get() == "Rękawice jałowe 6,5":
        entry_cena_01 = Entry(root, textvariable=cena_01, justify=CENTER, width=14)
        entry_cena_01.insert(0, "1.20")
        entry_cena_01.grid(row=11, column=2)
    elif nazwa_01.get() == "Rękawice jałowe 7,0":
        entry_cena_01 = Entry(root, textvariable=cena_01, justify=CENTER, width=14)
        entry_cena_01.insert(0, "1.20")
        entry_cena_01.grid(row=11, column=2)
    elif nazwa_01.get() == "Rękawice jałowe 7,5":
        entry_cena_01 = Entry(root, textvariable=cena_01, justify=CENTER, width=14)
        entry_cena_01.insert(0, "1.20")
        entry_cena_01.grid(row=11, column=2)
    elif nazwa_01.get() == "Rękawice jałowe 8,00":
        entry_cena_01 = Entry(root, textvariable=cena_01, justify=CENTER, width=14)
        entry_cena_01.insert(0, "1.20")
        entry_cena_01.grid(row=11, column=2)
    elif nazwa_01.get() == "Rękojeść Interpulse wysokoprzepływowa":
        entry_cena_01 = Entry(root, textvariable=cena_01, justify=CENTER, width=14)
        entry_cena_01.insert(0, "216")
        entry_cena_01.grid(row=11, column=2)
    elif nazwa_01.get() == "Serweta":
        entry_cena_01 = Entry(root, textvariable=cena_01, justify=CENTER, width=14)
        entry_cena_01.insert(0, "6")
        entry_cena_01.grid(row=11, column=2)
    elif nazwa_01.get() == "Simplex Hv z Gentamycyna 10x40g":
        entry_cena_01 = Entry(root, textvariable=cena_01, justify=CENTER, width=14)
        entry_cena_01.insert(0, "162")
        entry_cena_01.grid(row=11, column=2)
    elif nazwa_01.get() == "Skalpel 11":
        entry_cena_01 = Entry(root, textvariable=cena_01, justify=CENTER, width=14)
        entry_cena_01.insert(0, "0.38")
        entry_cena_01.grid(row=11, column=2)
    elif nazwa_01.get() == "Skalpel 13":
        entry_cena_01 = Entry(root, textvariable=cena_01, justify=CENTER, width=14)
        entry_cena_01.insert(0, "1")
        entry_cena_01.grid(row=11, column=2)
    elif nazwa_01.get() == "Skalpel 22":
        entry_cena_01 = Entry(root, textvariable=cena_01, justify=CENTER, width=14)
        entry_cena_01.insert(0, "00000")
        entry_cena_01.grid(row=11, column=2)
    elif nazwa_01.get() == "Śruba blokująca PeekPower do osteotomii":
        entry_cena_01 = Entry(root, textvariable=cena_01, justify=CENTER, width=14)
        entry_cena_01.insert(0, "194")
        entry_cena_01.grid(row=11, column=2)
    elif nazwa_01.get() == "System do mieszania próżniowego":
        entry_cena_01 = Entry(root, textvariable=cena_01, justify=CENTER, width=14)
        entry_cena_01.insert(0, "216")
        entry_cena_01.grid(row=11, column=2)
    elif nazwa_01.get() == "System wprowadzania implantów ACL TightRope":
        entry_cena_01 = Entry(root, textvariable=cena_01, justify=CENTER, width=14)
        entry_cena_01.insert(0, "702")
        entry_cena_01.grid(row=11, column=2)
    elif nazwa_01.get() == "Szew FiberWire 2":
        entry_cena_01 = Entry(root, textvariable=cena_01, justify=CENTER, width=14)
        entry_cena_01.insert(0, "86.40")
        entry_cena_01.grid(row=11, column=2)
    elif nazwa_01.get() == "Taśma przylepna 10x50":
        entry_cena_01 = Entry(root, textvariable=cena_01, justify=CENTER, width=14)
        entry_cena_01.insert(0, "1.04")
        entry_cena_01.grid(row=11, column=2)
    elif nazwa_01.get() == "Triathlon elem. udowy lewy":
        entry_cena_01 = Entry(root, textvariable=cena_01, justify=CENTER, width=14)
        entry_cena_01.insert(0, "3132")
        entry_cena_01.grid(row=11, column=2)
    elif nazwa_01.get() == "Triathlon PS wkładka x3-9mm #4":
        entry_cena_01 = Entry(root, textvariable=cena_01, justify=CENTER, width=14)
        entry_cena_01.insert(0, "756")
        entry_cena_01.grid(row=11, column=2)
    elif nazwa_01.get() == "Triathlon taca piszczelowa":
        entry_cena_01 = Entry(root, textvariable=cena_01, justify=CENTER, width=14)
        entry_cena_01.insert(0, "1296")
        entry_cena_01.grid(row=11, column=2)
    elif nazwa_01.get() == "Wkłady 3L z żelem":
        entry_cena_01 = Entry(root, textvariable=cena_01, justify=CENTER, width=14)
        entry_cena_01.insert(0, "10.26")
        entry_cena_01.grid(row=11, column=2)
    elif nazwa_01.get() == "Zestaw do artroskopii":
        entry_cena_01 = Entry(root, textvariable=cena_01, justify=CENTER, width=14)
        entry_cena_01.insert(0, "67")
        entry_cena_01.grid(row=11, column=2)
    elif nazwa_01.get() == "Zestaw do artroskopii barku":
        entry_cena_01 = Entry(root, textvariable=cena_01, justify=CENTER, width=14)
        entry_cena_01.insert(0, "108")
        entry_cena_01.grid(row=11, column=2)
    elif nazwa_01.get() == "Zestaw do drenażu":
        entry_cena_01 = Entry(root, textvariable=cena_01, justify=CENTER, width=14)
        entry_cena_01.insert(0, "14.23")
        entry_cena_01.grid(row=11, column=2)
    elif nazwa_01.get() == "Zestaw ortopedyczny":
        entry_cena_01 = Entry(root, textvariable=cena_01, justify=CENTER, width=14)
        entry_cena_01.insert(0, "28.08")
        entry_cena_01.grid(row=11, column=2)
    elif nazwa_01.get() == "Gaziki 20 x 10cm":
        entry_cena_01 = Entry(root, textvariable=cena_01, justify=CENTER, width=14)
        entry_cena_01.insert(0, "0.46")
        entry_cena_01.grid(row=11, column=2)
    else:
        entry_cena_01 = Entry(root, textvariable=cena_01, justify=CENTER, width=14, bg="#ffff00")
        entry_cena_01.insert(0, "0")
        entry_cena_01.grid(row=11, column=2)

    if nazwa_02.get() == "--puste--":
        entry_cena_02 = Entry(root, textvariable=cena_02, justify=CENTER, width=14)
        entry_cena_02.insert(0, "0")
        entry_cena_02.grid(row=12, column=2)
    elif nazwa_02.get() == "Ablator":
        entry_cena_02 = Entry(root, textvariable=cena_02, justify=CENTER, width=14)
        entry_cena_02.insert(0, "572")
        entry_cena_02.grid(row=12, column=2)
    elif nazwa_02.get() == "Anestezjolog":
        entry_cena_02 = Entry(root, textvariable=cena_02, justify=CENTER, width=14, bg="#ffff00")
        entry_cena_02.insert(0, "350")
        entry_cena_02.grid(row=12, column=2)
    elif nazwa_02.get() == "Butelka 400ml do długotrwałego odsysania ran j.u. sterylna":
        entry_cena_02 = Entry(root, textvariable=cena_02, justify=CENTER, width=14)
        entry_cena_02.insert(0, "4")
        entry_cena_02.grid(row=12, column=2)
    elif nazwa_02.get() == "Doba":
        entry_cena_02 = Entry(root, textvariable=cena_02, justify=CENTER, width=14)
        entry_cena_02.insert(0, "700")
        entry_cena_02.grid(row=12, column=2)
    elif nazwa_02.get() == "Dren łączący do ssaka Grena":
        entry_cena_02 = Entry(root, textvariable=cena_02, justify=CENTER, width=14)
        entry_cena_02.insert(0, "5")
        entry_cena_02.grid(row=12, column=2)
    elif nazwa_02.get() == "Dren Redona Ch 16 dł. 800mm z trokarem":
        entry_cena_02 = Entry(root, textvariable=cena_02, justify=CENTER, width=14)
        entry_cena_02.insert(0, "29.74")
        entry_cena_02.grid(row=12, column=2)
    elif nazwa_02.get() == "Dren do pompy Artrex":
        entry_cena_02 = Entry(root, textvariable=cena_02, justify=CENTER, width=14)
        entry_cena_02.insert(0, "108")
        entry_cena_02.grid(row=12, column=2)
    elif nazwa_02.get() == "Drut wiercący 2,4 x 311":
        entry_cena_02 = Entry(root, textvariable=cena_02, justify=CENTER, width=14)
        entry_cena_02.insert(0, "139.60")
        entry_cena_02.grid(row=12, column=2)
    elif nazwa_02.get() == "Fartuch jałowy L":
        entry_cena_02 = Entry(root, textvariable=cena_02, justify=CENTER, width=14)
        entry_cena_02.insert(0, "17")
        entry_cena_02.grid(row=12, column=2)
    elif nazwa_02.get() == "Fartuch jałowy M":
        entry_cena_02 = Entry(root, textvariable=cena_02, justify=CENTER, width=14)
        entry_cena_02.insert(0, "15.28")
        entry_cena_02.grid(row=12, column=2)
    elif nazwa_02.get() == "Fartuch jałowy XL":
        entry_cena_02 = Entry(root, textvariable=cena_02, justify=CENTER, width=14)
        entry_cena_02.insert(0, "20.84")
        entry_cena_02.grid(row=12, column=2)
    elif nazwa_02.get() == "FasatThread BioComposite Interference Screw 8x30":
        entry_cena_02 = Entry(root, textvariable=cena_02, justify=CENTER, width=14)
        entry_cena_02.insert(0, "594")
        entry_cena_02.grid(row=12, column=2)
    elif nazwa_02.get() == "Folia operacyjna, jałowa 45cm x 55cm":
        entry_cena_02 = Entry(root, textvariable=cena_02, justify=CENTER, width=14)
        entry_cena_02.insert(0, "9.99")
        entry_cena_02.grid(row=12, column=2)
    elif nazwa_02.get() == "Gaziki 10 x 10cm":
        entry_cena_02 = Entry(root, textvariable=cena_02, justify=CENTER, width=14)
        entry_cena_02.insert(0, "0.10")
        entry_cena_02.grid(row=12, column=2)
    elif nazwa_02.get() == "Igła 0,6 x 60":
        entry_cena_02 = Entry(root, textvariable=cena_02, justify=CENTER, width=14)
        entry_cena_02.insert(0, "0.09")
        entry_cena_02.grid(row=12, column=2)
    elif nazwa_02.get() == "Igła 0,7 x 40":
        entry_cena_02 = Entry(root, textvariable=cena_02, justify=CENTER, width=14)
        entry_cena_02.insert(0, "0.05")
        entry_cena_02.grid(row=12, column=2)
    elif nazwa_02.get() == "Igła 0,8 x 40":
        entry_cena_02 = Entry(root, textvariable=cena_02, justify=CENTER, width=14)
        entry_cena_02.insert(0, "0.05")
        entry_cena_02.grid(row=12, column=2)
    elif nazwa_02.get() == "Igła 1,1 x 70":
        entry_cena_02 = Entry(root, textvariable=cena_02, justify=CENTER, width=14)
        entry_cena_02.insert(0, "0.16")
        entry_cena_02.grid(row=12, column=2)
    elif nazwa_02.get() == "Kaniulowana śruba int. biokompozytowa z osłonką jednoraz.":
        entry_cena_02 = Entry(root, textvariable=cena_02, justify=CENTER, width=14)
        entry_cena_02.insert(0, "594")
        entry_cena_02.grid(row=12, column=2)
    elif nazwa_02.get() == "Kaniulowana śruba int. biokompozytowa z pełnym gwintem":
        entry_cena_02 = Entry(root, textvariable=cena_02, justify=CENTER, width=14)
        entry_cena_02.insert(0, "594")
        entry_cena_02.grid(row=12, column=2)
    elif nazwa_02.get() == "Końcówka do Shavera":
        entry_cena_02 = Entry(root, textvariable=cena_02, justify=CENTER, width=14)
        entry_cena_02.insert(0, "270")
        entry_cena_02.grid(row=12, column=2)
    elif nazwa_02.get() == "Kotwica biokompozytowa SwiveLock":
        entry_cena_02 = Entry(root, textvariable=cena_02, justify=CENTER, width=14)
        entry_cena_02.insert(0, "918")
        entry_cena_02.grid(row=12, column=2)
    elif nazwa_02.get() == "Kotwica Corkscrew":
        entry_cena_02 = Entry(root, textvariable=cena_02, justify=CENTER, width=14)
        entry_cena_02.insert(0, "604")
        entry_cena_02.grid(row=12, column=2)
    elif nazwa_02.get() == "Kotwica FASTak":
        entry_cena_02 = Entry(root, textvariable=cena_02, justify=CENTER, width=14)
        entry_cena_02.insert(0, "432")
        entry_cena_02.grid(row=12, column=2)
    elif nazwa_02.get() == "Kotwica PEEK SwiveLock":
        entry_cena_02 = Entry(root, textvariable=cena_02, justify=CENTER, width=14)
        entry_cena_02.insert(0, "885.60")
        entry_cena_02.grid(row=12, column=2)
    elif nazwa_02.get() == "NaCl 3000ml":
        entry_cena_02 = Entry(root, textvariable=cena_02, justify=CENTER, width=14)
        entry_cena_02.insert(0, "29.72")
        entry_cena_02.grid(row=12, column=2)
    elif nazwa_02.get() == "NaCl 5000ml":
        entry_cena_02 = Entry(root, textvariable=cena_02, justify=CENTER, width=14)
        entry_cena_02.insert(0, "58.33")
        entry_cena_02.grid(row=12, column=2)
    elif nazwa_02.get() == "Nici Dafilon 2-0":
        entry_cena_02 = Entry(root, textvariable=cena_02, justify=CENTER, width=14)
        entry_cena_02.insert(0, "6.60")
        entry_cena_02.grid(row=12, column=2)
    elif nazwa_02.get() == "Nici Novosyn 2":
        entry_cena_02 = Entry(root, textvariable=cena_02, justify=CENTER, width=14)
        entry_cena_02.insert(0, "13")
        entry_cena_02.grid(row=12, column=2)
    elif nazwa_02.get() == "Nici Novosyn 2-0":
        entry_cena_02 = Entry(root, textvariable=cena_02, justify=CENTER, width=14)
        entry_cena_02.insert(0, "7.70")
        entry_cena_02.grid(row=12, column=2)
    elif nazwa_02.get() == "Nici Novosyn 3-0":
        entry_cena_02 = Entry(root, textvariable=cena_02, justify=CENTER, width=14)
        entry_cena_02.insert(0, "7.70")
        entry_cena_02.grid(row=12, column=2)
    elif nazwa_02.get() == "Nici Nylon 2-0":
        entry_cena_02 = Entry(root, textvariable=cena_02, justify=CENTER, width=14)
        entry_cena_02.insert(0, "2.50")
        entry_cena_02.grid(row=12, column=2)
    elif nazwa_02.get() == "Nici Nylon 3-0":
        entry_cena_02 = Entry(root, textvariable=cena_02, justify=CENTER, width=14)
        entry_cena_02.insert(0, "2")
        entry_cena_02.grid(row=12, column=2)
    elif nazwa_02.get() == "Nici PGLA":
        entry_cena_02 = Entry(root, textvariable=cena_02, justify=CENTER, width=14)
        entry_cena_02.insert(0, "11.60")
        entry_cena_02.grid(row=12, column=2)
    elif nazwa_02.get() == "Nici PremiCron 3":
        entry_cena_02 = Entry(root, textvariable=cena_02, justify=CENTER, width=14)
        entry_cena_02.insert(0, "6.50")
        entry_cena_02.grid(row=12, column=2)
    elif nazwa_02.get() == "Nici Vicryl 4-0":
        entry_cena_02 = Entry(root, textvariable=cena_02, justify=CENTER, width=14)
        entry_cena_02.insert(0, "7.50")
        entry_cena_02.grid(row=12, column=2)
    elif nazwa_02.get() == "Nitinol Guide Pin 1.1":
        entry_cena_02 = Entry(root, textvariable=cena_02, justify=CENTER, width=14)
        entry_cena_02.insert(0, "145.80")
        entry_cena_02.grid(row=12, column=2)
    elif nazwa_02.get() == "Osłona na przewody":
        entry_cena_02 = Entry(root, textvariable=cena_02, justify=CENTER, width=14)
        entry_cena_02.insert(0, "2.50")
        entry_cena_02.grid(row=12, column=2)
    elif nazwa_02.get() == "Ostrze Arthrex 90(86)x19x1,27":
        entry_cena_02 = Entry(root, textvariable=cena_02, justify=CENTER, width=14)
        entry_cena_02.insert(0, "216")
        entry_cena_02.grid(row=12, column=2)
    elif nazwa_02.get() == "Ostrze piły":
        entry_cena_02 = Entry(root, textvariable=cena_02, justify=CENTER, width=14)
        entry_cena_02.insert(0, "108")
        entry_cena_02.grid(row=12, column=2)
    elif nazwa_02.get() == "Pielęgniarka anest.":
        entry_cena_02 = Entry(root, textvariable=cena_02, justify=CENTER, width=14)
        entry_cena_02.insert(0, "50")
        entry_cena_02.grid(row=12, column=2)
    elif nazwa_02.get() == "Pielęgniarka instr.":
        entry_cena_02 = Entry(root, textvariable=cena_02, justify=CENTER, width=14)
        entry_cena_02.insert(0, "50")
        entry_cena_02.grid(row=12, column=2)
    elif nazwa_02.get() == "Pielęgniarka 'Noviline'":
        entry_cena_02 = Entry(root, textvariable=cena_02, justify=CENTER, width=14)
        entry_cena_02.insert(0, "30")
        entry_cena_02.grid(row=12, column=2)
    elif nazwa_02.get() == "Płytka PeekPower do osteotomii klinowej":
        entry_cena_02 = Entry(root, textvariable=cena_02, justify=CENTER, width=14)
        entry_cena_02.insert(0, "2160")
        entry_cena_02.grid(row=12, column=2)
    elif nazwa_02.get() == "Rękawice jałowe 6,5":
        entry_cena_02 = Entry(root, textvariable=cena_02, justify=CENTER, width=14)
        entry_cena_02.insert(0, "1.20")
        entry_cena_02.grid(row=12, column=2)
    elif nazwa_02.get() == "Rękawice jałowe 7,0":
        entry_cena_02 = Entry(root, textvariable=cena_02, justify=CENTER, width=14)
        entry_cena_02.insert(0, "1.20")
        entry_cena_02.grid(row=12, column=2)
    elif nazwa_02.get() == "Rękawice jałowe 7,5":
        entry_cena_02 = Entry(root, textvariable=cena_02, justify=CENTER, width=14)
        entry_cena_02.insert(0, "1.20")
        entry_cena_02.grid(row=12, column=2)
    elif nazwa_02.get() == "Rękawice jałowe 8,00":
        entry_cena_02 = Entry(root, textvariable=cena_02, justify=CENTER, width=14)
        entry_cena_02.insert(0, "1.20")
        entry_cena_02.grid(row=12, column=2)
    elif nazwa_02.get() == "Rękojeść Interpulse wysokoprzepływowa":
        entry_cena_02 = Entry(root, textvariable=cena_02, justify=CENTER, width=14)
        entry_cena_02.insert(0, "216")
        entry_cena_02.grid(row=12, column=2)
    elif nazwa_02.get() == "Serweta":
        entry_cena_02 = Entry(root, textvariable=cena_02, justify=CENTER, width=14)
        entry_cena_02.insert(0, "6")
        entry_cena_02.grid(row=12, column=2)
    elif nazwa_02.get() == "Simplex Hv z Gentamycyna 10x40g":
        entry_cena_02 = Entry(root, textvariable=cena_02, justify=CENTER, width=14)
        entry_cena_02.insert(0, "162")
        entry_cena_02.grid(row=12, column=2)
    elif nazwa_02.get() == "Skalpel 11":
        entry_cena_02 = Entry(root, textvariable=cena_02, justify=CENTER, width=14)
        entry_cena_02.insert(0, "0.38")
        entry_cena_02.grid(row=12, column=2)
    elif nazwa_02.get() == "Skalpel 13":
        entry_cena_02 = Entry(root, textvariable=cena_02, justify=CENTER, width=14)
        entry_cena_02.insert(0, "1")
        entry_cena_02.grid(row=12, column=2)
    elif nazwa_02.get() == "Skalpel 22":
        entry_cena_02 = Entry(root, textvariable=cena_02, justify=CENTER, width=14)
        entry_cena_02.insert(0, "00000")
        entry_cena_02.grid(row=12, column=2)
    elif nazwa_02.get() == "Śruba blokująca PeekPower do osteotomii":
        entry_cena_02 = Entry(root, textvariable=cena_02, justify=CENTER, width=14)
        entry_cena_02.insert(0, "194")
        entry_cena_02.grid(row=12, column=2)
    elif nazwa_02.get() == "System do mieszania próżniowego":
        entry_cena_02 = Entry(root, textvariable=cena_02, justify=CENTER, width=14)
        entry_cena_02.insert(0, "216")
        entry_cena_02.grid(row=12, column=2)
    elif nazwa_02.get() == "System wprowadzania implantów ACL TightRope":
        entry_cena_02 = Entry(root, textvariable=cena_02, justify=CENTER, width=14)
        entry_cena_02.insert(0, "702")
        entry_cena_02.grid(row=12, column=2)
    elif nazwa_02.get() == "Szew FiberWire 2":
        entry_cena_02 = Entry(root, textvariable=cena_02, justify=CENTER, width=14)
        entry_cena_02.insert(0, "86.40")
        entry_cena_02.grid(row=12, column=2)
    elif nazwa_02.get() == "Taśma przylepna 10x50":
        entry_cena_02 = Entry(root, textvariable=cena_02, justify=CENTER, width=14)
        entry_cena_02.insert(0, "1.04")
        entry_cena_02.grid(row=12, column=2)
    elif nazwa_02.get() == "Triathlon elem. udowy lewy":
        entry_cena_02 = Entry(root, textvariable=cena_02, justify=CENTER, width=14)
        entry_cena_02.insert(0, "3132")
        entry_cena_02.grid(row=12, column=2)
    elif nazwa_02.get() == "Triathlon PS wkładka x3-9mm #4":
        entry_cena_02 = Entry(root, textvariable=cena_02, justify=CENTER, width=14)
        entry_cena_02.insert(0, "756")
        entry_cena_02.grid(row=12, column=2)
    elif nazwa_02.get() == "Triathlon taca piszczelowa":
        entry_cena_02 = Entry(root, textvariable=cena_02, justify=CENTER, width=14)
        entry_cena_02.insert(0, "1296")
        entry_cena_02.grid(row=12, column=2)
    elif nazwa_02.get() == "Wkłady 3L z żelem":
        entry_cena_02 = Entry(root, textvariable=cena_02, justify=CENTER, width=14)
        entry_cena_02.insert(0, "10.26")
        entry_cena_02.grid(row=12, column=2)
    elif nazwa_02.get() == "Zestaw do artroskopii":
        entry_cena_02 = Entry(root, textvariable=cena_02, justify=CENTER, width=14)
        entry_cena_02.insert(0, "67")
        entry_cena_02.grid(row=12, column=2)
    elif nazwa_02.get() == "Zestaw do artroskopii barku":
        entry_cena_02 = Entry(root, textvariable=cena_02, justify=CENTER, width=14)
        entry_cena_02.insert(0, "108")
        entry_cena_02.grid(row=12, column=2)
    elif nazwa_02.get() == "Zestaw do drenażu":
        entry_cena_02 = Entry(root, textvariable=cena_02, justify=CENTER, width=14)
        entry_cena_02.insert(0, "14.23")
        entry_cena_02.grid(row=12, column=2)
    elif nazwa_02.get() == "Zestaw ortopedyczny":
        entry_cena_02 = Entry(root, textvariable=cena_02, justify=CENTER, width=14)
        entry_cena_02.insert(0, "28.08")
        entry_cena_02.grid(row=12, column=2)
    elif nazwa_02.get() == "Gaziki 20 x 10cm":
        entry_cena_02 = Entry(root, textvariable=cena_02, justify=CENTER, width=14)
        entry_cena_02.insert(0, "0.46")
        entry_cena_02.grid(row=12, column=2)
    else:
        entry_cena_02 = Entry(root, textvariable=cena_02, justify=CENTER, width=14, bg="#ffff00")
        entry_cena_02.insert(0, "0")
        entry_cena_02.grid(row=12, column=2)

    if nazwa_03.get() == "--puste--":
        entry_cena_03 = Entry(root, textvariable=cena_03, justify=CENTER, width=14)
        entry_cena_03.insert(0, "0")
        entry_cena_03.grid(row=13, column=2)
    elif nazwa_03.get() == "Ablator":
        entry_cena_03 = Entry(root, textvariable=cena_03, justify=CENTER, width=14)
        entry_cena_03.insert(0, "572")
        entry_cena_03.grid(row=13, column=2)
    elif nazwa_03.get() == "Anestezjolog":
        entry_cena_03 = Entry(root, textvariable=cena_03, justify=CENTER, width=14, bg="#ffff00")
        entry_cena_03.insert(0, "350")
        entry_cena_03.grid(row=13, column=2)
    elif nazwa_03.get() == "Butelka 400ml do długotrwałego odsysania ran j.u. sterylna":
        entry_cena_03 = Entry(root, textvariable=cena_03, justify=CENTER, width=14)
        entry_cena_03.insert(0, "4")
        entry_cena_03.grid(row=13, column=2)
    elif nazwa_03.get() == "Doba":
        entry_cena_03 = Entry(root, textvariable=cena_03, justify=CENTER, width=14)
        entry_cena_03.insert(0, "700")
        entry_cena_03.grid(row=13, column=2)
    elif nazwa_03.get() == "Dren łączący do ssaka Grena":
        entry_cena_03 = Entry(root, textvariable=cena_03, justify=CENTER, width=14)
        entry_cena_03.insert(0, "5")
        entry_cena_03.grid(row=13, column=2)
    elif nazwa_03.get() == "Dren Redona Ch 16 dł. 800mm z trokarem":
        entry_cena_03 = Entry(root, textvariable=cena_03, justify=CENTER, width=14)
        entry_cena_03.insert(0, "29.74")
        entry_cena_03.grid(row=13, column=2)
    elif nazwa_03.get() == "Dren do pompy Artrex":
        entry_cena_03 = Entry(root, textvariable=cena_03, justify=CENTER, width=14)
        entry_cena_03.insert(0, "108")
        entry_cena_03.grid(row=13, column=2)
    elif nazwa_03.get() == "Drut wiercący 2,4 x 311":
        entry_cena_03 = Entry(root, textvariable=cena_03, justify=CENTER, width=14)
        entry_cena_03.insert(0, "139.60")
        entry_cena_03.grid(row=13, column=2)
    elif nazwa_03.get() == "Fartuch jałowy L":
        entry_cena_03 = Entry(root, textvariable=cena_03, justify=CENTER, width=14)
        entry_cena_03.insert(0, "17")
        entry_cena_03.grid(row=13, column=2)
    elif nazwa_03.get() == "Fartuch jałowy M":
        entry_cena_03 = Entry(root, textvariable=cena_03, justify=CENTER, width=14)
        entry_cena_03.insert(0, "15.28")
        entry_cena_03.grid(row=13, column=2)
    elif nazwa_03.get() == "Fartuch jałowy XL":
        entry_cena_03 = Entry(root, textvariable=cena_03, justify=CENTER, width=14)
        entry_cena_03.insert(0, "20.84")
        entry_cena_03.grid(row=13, column=2)
    elif nazwa_03.get() == "FasatThread BioComposite Interference Screw 8x30":
        entry_cena_03 = Entry(root, textvariable=cena_03, justify=CENTER, width=14)
        entry_cena_03.insert(0, "594")
        entry_cena_03.grid(row=13, column=2)
    elif nazwa_03.get() == "Folia operacyjna, jałowa 45cm x 55cm":
        entry_cena_03 = Entry(root, textvariable=cena_03, justify=CENTER, width=14)
        entry_cena_03.insert(0, "9.99")
        entry_cena_03.grid(row=13, column=2)
    elif nazwa_03.get() == "Gaziki 10 x 10cm":
        entry_cena_03 = Entry(root, textvariable=cena_03, justify=CENTER, width=14)
        entry_cena_03.insert(0, "0.10")
        entry_cena_03.grid(row=13, column=2)
    elif nazwa_03.get() == "Igła 0,6 x 60":
        entry_cena_03 = Entry(root, textvariable=cena_03, justify=CENTER, width=14)
        entry_cena_03.insert(0, "0.09")
        entry_cena_03.grid(row=13, column=2)
    elif nazwa_03.get() == "Igła 0,7 x 40":
        entry_cena_03 = Entry(root, textvariable=cena_03, justify=CENTER, width=14)
        entry_cena_03.insert(0, "0.05")
        entry_cena_03.grid(row=13, column=2)
    elif nazwa_03.get() == "Igła 0,8 x 40":
        entry_cena_03 = Entry(root, textvariable=cena_03, justify=CENTER, width=14)
        entry_cena_03.insert(0, "0.05")
        entry_cena_03.grid(row=13, column=2)
    elif nazwa_03.get() == "Igła 1,1 x 70":
        entry_cena_03 = Entry(root, textvariable=cena_03, justify=CENTER, width=14)
        entry_cena_03.insert(0, "0.16")
        entry_cena_03.grid(row=13, column=2)
    elif nazwa_03.get() == "Kaniulowana śruba int. biokompozytowa z osłonką jednoraz.":
        entry_cena_03 = Entry(root, textvariable=cena_03, justify=CENTER, width=14)
        entry_cena_03.insert(0, "594")
        entry_cena_03.grid(row=13, column=2)
    elif nazwa_03.get() == "Kaniulowana śruba int. biokompozytowa z pełnym gwintem":
        entry_cena_03 = Entry(root, textvariable=cena_03, justify=CENTER, width=14)
        entry_cena_03.insert(0, "594")
        entry_cena_03.grid(row=13, column=2)
    elif nazwa_03.get() == "Końcówka do Shavera":
        entry_cena_03 = Entry(root, textvariable=cena_03, justify=CENTER, width=14)
        entry_cena_03.insert(0, "270")
        entry_cena_03.grid(row=13, column=2)
    elif nazwa_03.get() == "Kotwica biokompozytowa SwiveLock":
        entry_cena_03 = Entry(root, textvariable=cena_03, justify=CENTER, width=14)
        entry_cena_03.insert(0, "918")
        entry_cena_03.grid(row=13, column=2)
    elif nazwa_03.get() == "Kotwica Corkscrew":
        entry_cena_03 = Entry(root, textvariable=cena_03, justify=CENTER, width=14)
        entry_cena_03.insert(0, "604")
        entry_cena_03.grid(row=13, column=2)
    elif nazwa_03.get() == "Kotwica FASTak":
        entry_cena_03 = Entry(root, textvariable=cena_03, justify=CENTER, width=14)
        entry_cena_03.insert(0, "432")
        entry_cena_03.grid(row=13, column=2)
    elif nazwa_03.get() == "Kotwica PEEK SwiveLock":
        entry_cena_03 = Entry(root, textvariable=cena_03, justify=CENTER, width=14)
        entry_cena_03.insert(0, "885.60")
        entry_cena_03.grid(row=13, column=2)
    elif nazwa_03.get() == "NaCl 3000ml":
        entry_cena_03 = Entry(root, textvariable=cena_03, justify=CENTER, width=14)
        entry_cena_03.insert(0, "29.72")
        entry_cena_03.grid(row=13, column=2)
    elif nazwa_03.get() == "NaCl 5000ml":
        entry_cena_03 = Entry(root, textvariable=cena_03, justify=CENTER, width=14)
        entry_cena_03.insert(0, "58.33")
        entry_cena_03.grid(row=13, column=2)
    elif nazwa_03.get() == "Nici Dafilon 2-0":
        entry_cena_03 = Entry(root, textvariable=cena_03, justify=CENTER, width=14)
        entry_cena_03.insert(0, "6.60")
        entry_cena_03.grid(row=13, column=2)
    elif nazwa_03.get() == "Nici Novosyn 2":
        entry_cena_03 = Entry(root, textvariable=cena_03, justify=CENTER, width=14)
        entry_cena_03.insert(0, "13")
        entry_cena_03.grid(row=13, column=2)
    elif nazwa_03.get() == "Nici Novosyn 2-0":
        entry_cena_03 = Entry(root, textvariable=cena_03, justify=CENTER, width=14)
        entry_cena_03.insert(0, "7.70")
        entry_cena_03.grid(row=13, column=2)
    elif nazwa_03.get() == "Nici Novosyn 3-0":
        entry_cena_03 = Entry(root, textvariable=cena_03, justify=CENTER, width=14)
        entry_cena_03.insert(0, "7.70")
        entry_cena_03.grid(row=13, column=2)
    elif nazwa_03.get() == "Nici Nylon 2-0":
        entry_cena_03 = Entry(root, textvariable=cena_03, justify=CENTER, width=14)
        entry_cena_03.insert(0, "2.50")
        entry_cena_03.grid(row=13, column=2)
    elif nazwa_03.get() == "Nici Nylon 3-0":
        entry_cena_03 = Entry(root, textvariable=cena_03, justify=CENTER, width=14)
        entry_cena_03.insert(0, "2")
        entry_cena_03.grid(row=13, column=2)
    elif nazwa_03.get() == "Nici PGLA":
        entry_cena_03 = Entry(root, textvariable=cena_03, justify=CENTER, width=14)
        entry_cena_03.insert(0, "11.60")
        entry_cena_03.grid(row=13, column=2)
    elif nazwa_03.get() == "Nici PremiCron 3":
        entry_cena_03 = Entry(root, textvariable=cena_03, justify=CENTER, width=14)
        entry_cena_03.insert(0, "6.50")
        entry_cena_03.grid(row=13, column=2)
    elif nazwa_03.get() == "Nici Vicryl 4-0":
        entry_cena_03 = Entry(root, textvariable=cena_03, justify=CENTER, width=14)
        entry_cena_03.insert(0, "7.50")
        entry_cena_03.grid(row=13, column=2)
    elif nazwa_03.get() == "Nitinol Guide Pin 1.1":
        entry_cena_03 = Entry(root, textvariable=cena_03, justify=CENTER, width=14)
        entry_cena_03.insert(0, "145.80")
        entry_cena_03.grid(row=13, column=2)
    elif nazwa_03.get() == "Osłona na przewody":
        entry_cena_03 = Entry(root, textvariable=cena_03, justify=CENTER, width=14)
        entry_cena_03.insert(0, "2.50")
        entry_cena_03.grid(row=13, column=2)
    elif nazwa_03.get() == "Ostrze Arthrex 90(86)x19x1,27":
        entry_cena_03 = Entry(root, textvariable=cena_03, justify=CENTER, width=14)
        entry_cena_03.insert(0, "216")
        entry_cena_03.grid(row=13, column=2)
    elif nazwa_03.get() == "Ostrze piły":
        entry_cena_03 = Entry(root, textvariable=cena_03, justify=CENTER, width=14)
        entry_cena_03.insert(0, "108")
        entry_cena_03.grid(row=13, column=2)
    elif nazwa_03.get() == "Pielęgniarka anest.":
        entry_cena_03 = Entry(root, textvariable=cena_03, justify=CENTER, width=14)
        entry_cena_03.insert(0, "50")
        entry_cena_03.grid(row=13, column=2)
    elif nazwa_03.get() == "Pielęgniarka instr.":
        entry_cena_03 = Entry(root, textvariable=cena_03, justify=CENTER, width=14)
        entry_cena_03.insert(0, "50")
        entry_cena_03.grid(row=13, column=2)
    elif nazwa_03.get() == "Pielęgniarka 'Noviline'":
        entry_cena_03 = Entry(root, textvariable=cena_03, justify=CENTER, width=14)
        entry_cena_03.insert(0, "30")
        entry_cena_03.grid(row=13, column=2)
    elif nazwa_03.get() == "Płytka PeekPower do osteotomii klinowej":
        entry_cena_03 = Entry(root, textvariable=cena_03, justify=CENTER, width=14)
        entry_cena_03.insert(0, "2160")
        entry_cena_03.grid(row=13, column=2)
    elif nazwa_03.get() == "Rękawice jałowe 6,5":
        entry_cena_03 = Entry(root, textvariable=cena_03, justify=CENTER, width=14)
        entry_cena_03.insert(0, "1.20")
        entry_cena_03.grid(row=13, column=2)
    elif nazwa_03.get() == "Rękawice jałowe 7,0":
        entry_cena_03 = Entry(root, textvariable=cena_03, justify=CENTER, width=14)
        entry_cena_03.insert(0, "1.20")
        entry_cena_03.grid(row=13, column=2)
    elif nazwa_03.get() == "Rękawice jałowe 7,5":
        entry_cena_03 = Entry(root, textvariable=cena_03, justify=CENTER, width=14)
        entry_cena_03.insert(0, "1.20")
        entry_cena_03.grid(row=13, column=2)
    elif nazwa_03.get() == "Rękawice jałowe 8,00":
        entry_cena_03 = Entry(root, textvariable=cena_03, justify=CENTER, width=14)
        entry_cena_03.insert(0, "1.20")
        entry_cena_03.grid(row=13, column=2)
    elif nazwa_03.get() == "Rękojeść Interpulse wysokoprzepływowa":
        entry_cena_03 = Entry(root, textvariable=cena_03, justify=CENTER, width=14)
        entry_cena_03.insert(0, "216")
        entry_cena_03.grid(row=13, column=2)
    elif nazwa_03.get() == "Serweta":
        entry_cena_03 = Entry(root, textvariable=cena_03, justify=CENTER, width=14)
        entry_cena_03.insert(0, "6")
        entry_cena_03.grid(row=13, column=2)
    elif nazwa_03.get() == "Simplex Hv z Gentamycyna 10x40g":
        entry_cena_03 = Entry(root, textvariable=cena_03, justify=CENTER, width=14)
        entry_cena_03.insert(0, "162")
        entry_cena_03.grid(row=13, column=2)
    elif nazwa_03.get() == "Skalpel 11":
        entry_cena_03 = Entry(root, textvariable=cena_03, justify=CENTER, width=14)
        entry_cena_03.insert(0, "0.38")
        entry_cena_03.grid(row=13, column=2)
    elif nazwa_03.get() == "Skalpel 13":
        entry_cena_03 = Entry(root, textvariable=cena_03, justify=CENTER, width=14)
        entry_cena_03.insert(0, "1")
        entry_cena_03.grid(row=13, column=2)
    elif nazwa_03.get() == "Skalpel 22":
        entry_cena_03 = Entry(root, textvariable=cena_03, justify=CENTER, width=14)
        entry_cena_03.insert(0, "00000")
        entry_cena_03.grid(row=13, column=2)
    elif nazwa_03.get() == "Śruba blokująca PeekPower do osteotomii":
        entry_cena_03 = Entry(root, textvariable=cena_03, justify=CENTER, width=14)
        entry_cena_03.insert(0, "194")
        entry_cena_03.grid(row=13, column=2)
    elif nazwa_03.get() == "System do mieszania próżniowego":
        entry_cena_03 = Entry(root, textvariable=cena_03, justify=CENTER, width=14)
        entry_cena_03.insert(0, "216")
        entry_cena_03.grid(row=13, column=2)
    elif nazwa_03.get() == "System wprowadzania implantów ACL TightRope":
        entry_cena_03 = Entry(root, textvariable=cena_03, justify=CENTER, width=14)
        entry_cena_03.insert(0, "702")
        entry_cena_03.grid(row=13, column=2)
    elif nazwa_03.get() == "Szew FiberWire 2":
        entry_cena_03 = Entry(root, textvariable=cena_03, justify=CENTER, width=14)
        entry_cena_03.insert(0, "86.40")
        entry_cena_03.grid(row=13, column=2)
    elif nazwa_03.get() == "Taśma przylepna 10x50":
        entry_cena_03 = Entry(root, textvariable=cena_03, justify=CENTER, width=14)
        entry_cena_03.insert(0, "1.04")
        entry_cena_03.grid(row=13, column=2)
    elif nazwa_03.get() == "Triathlon elem. udowy lewy":
        entry_cena_03 = Entry(root, textvariable=cena_03, justify=CENTER, width=14)
        entry_cena_03.insert(0, "3132")
        entry_cena_03.grid(row=13, column=2)
    elif nazwa_03.get() == "Triathlon PS wkładka x3-9mm #4":
        entry_cena_03 = Entry(root, textvariable=cena_03, justify=CENTER, width=14)
        entry_cena_03.insert(0, "756")
        entry_cena_03.grid(row=13, column=2)
    elif nazwa_03.get() == "Triathlon taca piszczelowa":
        entry_cena_03 = Entry(root, textvariable=cena_03, justify=CENTER, width=14)
        entry_cena_03.insert(0, "1296")
        entry_cena_03.grid(row=13, column=2)
    elif nazwa_03.get() == "Wkłady 3L z żelem":
        entry_cena_03 = Entry(root, textvariable=cena_03, justify=CENTER, width=14)
        entry_cena_03.insert(0, "10.26")
        entry_cena_03.grid(row=13, column=2)
    elif nazwa_03.get() == "Zestaw do artroskopii":
        entry_cena_03 = Entry(root, textvariable=cena_03, justify=CENTER, width=14)
        entry_cena_03.insert(0, "67")
        entry_cena_03.grid(row=13, column=2)
    elif nazwa_03.get() == "Zestaw do artroskopii barku":
        entry_cena_03 = Entry(root, textvariable=cena_03, justify=CENTER, width=14)
        entry_cena_03.insert(0, "108")
        entry_cena_03.grid(row=13, column=2)
    elif nazwa_03.get() == "Zestaw do drenażu":
        entry_cena_03 = Entry(root, textvariable=cena_03, justify=CENTER, width=14)
        entry_cena_03.insert(0, "14.23")
        entry_cena_03.grid(row=13, column=2)
    elif nazwa_03.get() == "Zestaw ortopedyczny":
        entry_cena_03 = Entry(root, textvariable=cena_03, justify=CENTER, width=14)
        entry_cena_03.insert(0, "28.08")
        entry_cena_03.grid(row=13, column=2)
    elif nazwa_03.get() == "Gaziki 20 x 10cm":
        entry_cena_03 = Entry(root, textvariable=cena_03, justify=CENTER, width=14)
        entry_cena_03.insert(0, "0.46")
        entry_cena_03.grid(row=13, column=2)
    else:
        entry_cena_03 = Entry(root, textvariable=cena_03, justify=CENTER, width=14, bg="#ffff00")
        entry_cena_03.insert(0, "0")
        entry_cena_03.grid(row=13, column=2)

    if nazwa_04.get() == "--puste--":
        entry_cena_04 = Entry(root, textvariable=cena_04, justify=CENTER, width=14)
        entry_cena_04.insert(0, "0")
        entry_cena_04.grid(row=14, column=2)
    elif nazwa_04.get() == "Ablator":
        entry_cena_04 = Entry(root, textvariable=cena_04, justify=CENTER, width=14)
        entry_cena_04.insert(0, "572")
        entry_cena_04.grid(row=14, column=2)
    elif nazwa_04.get() == "Anestezjolog":
        entry_cena_04 = Entry(root, textvariable=cena_04, justify=CENTER, width=14, bg="#ffff00")
        entry_cena_04.insert(0, "350")
        entry_cena_04.grid(row=14, column=2)
    elif nazwa_04.get() == "Butelka 400ml do długotrwałego odsysania ran j.u. sterylna":
        entry_cena_04 = Entry(root, textvariable=cena_04, justify=CENTER, width=14)
        entry_cena_04.insert(0, "4")
        entry_cena_04.grid(row=14, column=2)
    elif nazwa_04.get() == "Doba":
        entry_cena_04 = Entry(root, textvariable=cena_04, justify=CENTER, width=14)
        entry_cena_04.insert(0, "700")
        entry_cena_04.grid(row=14, column=2)
    elif nazwa_04.get() == "Dren łączący do ssaka Grena":
        entry_cena_04 = Entry(root, textvariable=cena_04, justify=CENTER, width=14)
        entry_cena_04.insert(0, "5")
        entry_cena_04.grid(row=14, column=2)
    elif nazwa_04.get() == "Dren Redona Ch 16 dł. 800mm z trokarem":
        entry_cena_04 = Entry(root, textvariable=cena_04, justify=CENTER, width=14)
        entry_cena_04.insert(0, "29.74")
        entry_cena_04.grid(row=14, column=2)
    elif nazwa_04.get() == "Dren do pompy Artrex":
        entry_cena_04 = Entry(root, textvariable=cena_04, justify=CENTER, width=14)
        entry_cena_04.insert(0, "108")
        entry_cena_04.grid(row=14, column=2)
    elif nazwa_04.get() == "Drut wiercący 2,4 x 311":
        entry_cena_04 = Entry(root, textvariable=cena_04, justify=CENTER, width=14)
        entry_cena_04.insert(0, "139.60")
        entry_cena_04.grid(row=14, column=2)
    elif nazwa_04.get() == "Fartuch jałowy L":
        entry_cena_04 = Entry(root, textvariable=cena_04, justify=CENTER, width=14)
        entry_cena_04.insert(0, "17")
        entry_cena_04.grid(row=14, column=2)
    elif nazwa_04.get() == "Fartuch jałowy M":
        entry_cena_04 = Entry(root, textvariable=cena_04, justify=CENTER, width=14)
        entry_cena_04.insert(0, "15.28")
        entry_cena_04.grid(row=14, column=2)
    elif nazwa_04.get() == "Fartuch jałowy XL":
        entry_cena_04 = Entry(root, textvariable=cena_04, justify=CENTER, width=14)
        entry_cena_04.insert(0, "20.84")
        entry_cena_04.grid(row=14, column=2)
    elif nazwa_04.get() == "FasatThread BioComposite Interference Screw 8x30":
        entry_cena_04 = Entry(root, textvariable=cena_04, justify=CENTER, width=14)
        entry_cena_04.insert(0, "594")
        entry_cena_04.grid(row=14, column=2)
    elif nazwa_04.get() == "Folia operacyjna, jałowa 45cm x 55cm":
        entry_cena_04 = Entry(root, textvariable=cena_04, justify=CENTER, width=14)
        entry_cena_04.insert(0, "9.99")
        entry_cena_04.grid(row=14, column=2)
    elif nazwa_04.get() == "Gaziki 10 x 10cm":
        entry_cena_04 = Entry(root, textvariable=cena_04, justify=CENTER, width=14)
        entry_cena_04.insert(0, "0.10")
        entry_cena_04.grid(row=14, column=2)
    elif nazwa_04.get() == "Igła 0,6 x 60":
        entry_cena_04 = Entry(root, textvariable=cena_04, justify=CENTER, width=14)
        entry_cena_04.insert(0, "0.09")
        entry_cena_04.grid(row=14, column=2)
    elif nazwa_04.get() == "Igła 0,7 x 40":
        entry_cena_04 = Entry(root, textvariable=cena_04, justify=CENTER, width=14)
        entry_cena_04.insert(0, "0.05")
        entry_cena_04.grid(row=14, column=2)
    elif nazwa_04.get() == "Igła 0,8 x 40":
        entry_cena_04 = Entry(root, textvariable=cena_04, justify=CENTER, width=14)
        entry_cena_04.insert(0, "0.05")
        entry_cena_04.grid(row=14, column=2)
    elif nazwa_04.get() == "Igła 1,1 x 70":
        entry_cena_04 = Entry(root, textvariable=cena_04, justify=CENTER, width=14)
        entry_cena_04.insert(0, "0.16")
        entry_cena_04.grid(row=14, column=2)
    elif nazwa_04.get() == "Kaniulowana śruba int. biokompozytowa z osłonką jednoraz.":
        entry_cena_04 = Entry(root, textvariable=cena_04, justify=CENTER, width=14)
        entry_cena_04.insert(0, "594")
        entry_cena_04.grid(row=14, column=2)
    elif nazwa_04.get() == "Kaniulowana śruba int. biokompozytowa z pełnym gwintem":
        entry_cena_04 = Entry(root, textvariable=cena_04, justify=CENTER, width=14)
        entry_cena_04.insert(0, "594")
        entry_cena_04.grid(row=14, column=2)
    elif nazwa_04.get() == "Końcówka do Shavera":
        entry_cena_04 = Entry(root, textvariable=cena_04, justify=CENTER, width=14)
        entry_cena_04.insert(0, "270")
        entry_cena_04.grid(row=14, column=2)
    elif nazwa_04.get() == "Kotwica biokompozytowa SwiveLock":
        entry_cena_04 = Entry(root, textvariable=cena_04, justify=CENTER, width=14)
        entry_cena_04.insert(0, "918")
        entry_cena_04.grid(row=14, column=2)
    elif nazwa_04.get() == "Kotwica Corkscrew":
        entry_cena_04 = Entry(root, textvariable=cena_04, justify=CENTER, width=14)
        entry_cena_04.insert(0, "604")
        entry_cena_04.grid(row=14, column=2)
    elif nazwa_04.get() == "Kotwica FASTak":
        entry_cena_04 = Entry(root, textvariable=cena_04, justify=CENTER, width=14)
        entry_cena_04.insert(0, "432")
        entry_cena_04.grid(row=14, column=2)
    elif nazwa_04.get() == "Kotwica PEEK SwiveLock":
        entry_cena_04 = Entry(root, textvariable=cena_04, justify=CENTER, width=14)
        entry_cena_04.insert(0, "885.60")
        entry_cena_04.grid(row=14, column=2)
    elif nazwa_04.get() == "NaCl 3000ml":
        entry_cena_04 = Entry(root, textvariable=cena_04, justify=CENTER, width=14)
        entry_cena_04.insert(0, "29.72")
        entry_cena_04.grid(row=14, column=2)
    elif nazwa_04.get() == "NaCl 5000ml":
        entry_cena_04 = Entry(root, textvariable=cena_04, justify=CENTER, width=14)
        entry_cena_04.insert(0, "58.33")
        entry_cena_04.grid(row=14, column=2)
    elif nazwa_04.get() == "Nici Dafilon 2-0":
        entry_cena_04 = Entry(root, textvariable=cena_04, justify=CENTER, width=14)
        entry_cena_04.insert(0, "6.60")
        entry_cena_04.grid(row=14, column=2)
    elif nazwa_04.get() == "Nici Novosyn 2":
        entry_cena_04 = Entry(root, textvariable=cena_04, justify=CENTER, width=14)
        entry_cena_04.insert(0, "13")
        entry_cena_04.grid(row=14, column=2)
    elif nazwa_04.get() == "Nici Novosyn 2-0":
        entry_cena_04 = Entry(root, textvariable=cena_04, justify=CENTER, width=14)
        entry_cena_04.insert(0, "7.70")
        entry_cena_04.grid(row=14, column=2)
    elif nazwa_04.get() == "Nici Novosyn 3-0":
        entry_cena_04 = Entry(root, textvariable=cena_04, justify=CENTER, width=14)
        entry_cena_04.insert(0, "7.70")
        entry_cena_04.grid(row=14, column=2)
    elif nazwa_04.get() == "Nici Nylon 2-0":
        entry_cena_04 = Entry(root, textvariable=cena_04, justify=CENTER, width=14)
        entry_cena_04.insert(0, "2.50")
        entry_cena_04.grid(row=14, column=2)
    elif nazwa_04.get() == "Nici Nylon 3-0":
        entry_cena_04 = Entry(root, textvariable=cena_04, justify=CENTER, width=14)
        entry_cena_04.insert(0, "2")
        entry_cena_04.grid(row=14, column=2)
    elif nazwa_04.get() == "Nici PGLA":
        entry_cena_04 = Entry(root, textvariable=cena_04, justify=CENTER, width=14)
        entry_cena_04.insert(0, "11.60")
        entry_cena_04.grid(row=14, column=2)
    elif nazwa_04.get() == "Nici PremiCron 3":
        entry_cena_04 = Entry(root, textvariable=cena_04, justify=CENTER, width=14)
        entry_cena_04.insert(0, "6.50")
        entry_cena_04.grid(row=14, column=2)
    elif nazwa_04.get() == "Nici Vicryl 4-0":
        entry_cena_04 = Entry(root, textvariable=cena_04, justify=CENTER, width=14)
        entry_cena_04.insert(0, "7.50")
        entry_cena_04.grid(row=14, column=2)
    elif nazwa_04.get() == "Nitinol Guide Pin 1.1":
        entry_cena_04 = Entry(root, textvariable=cena_04, justify=CENTER, width=14)
        entry_cena_04.insert(0, "145.80")
        entry_cena_04.grid(row=14, column=2)
    elif nazwa_04.get() == "Osłona na przewody":
        entry_cena_04 = Entry(root, textvariable=cena_04, justify=CENTER, width=14)
        entry_cena_04.insert(0, "2.50")
        entry_cena_04.grid(row=14, column=2)
    elif nazwa_04.get() == "Ostrze Arthrex 90(86)x19x1,27":
        entry_cena_04 = Entry(root, textvariable=cena_04, justify=CENTER, width=14)
        entry_cena_04.insert(0, "216")
        entry_cena_04.grid(row=14, column=2)
    elif nazwa_04.get() == "Ostrze piły":
        entry_cena_04 = Entry(root, textvariable=cena_04, justify=CENTER, width=14)
        entry_cena_04.insert(0, "108")
        entry_cena_04.grid(row=14, column=2)
    elif nazwa_04.get() == "Pielęgniarka anest.":
        entry_cena_04 = Entry(root, textvariable=cena_04, justify=CENTER, width=14)
        entry_cena_04.insert(0, "50")
        entry_cena_04.grid(row=14, column=2)
    elif nazwa_04.get() == "Pielęgniarka instr.":
        entry_cena_04 = Entry(root, textvariable=cena_04, justify=CENTER, width=14)
        entry_cena_04.insert(0, "50")
        entry_cena_04.grid(row=14, column=2)
    elif nazwa_04.get() == "Pielęgniarka 'Noviline'":
        entry_cena_04 = Entry(root, textvariable=cena_04, justify=CENTER, width=14)
        entry_cena_04.insert(0, "30")
        entry_cena_04.grid(row=14, column=2)
    elif nazwa_04.get() == "Płytka PeekPower do osteotomii klinowej":
        entry_cena_04 = Entry(root, textvariable=cena_04, justify=CENTER, width=14)
        entry_cena_04.insert(0, "2160")
        entry_cena_04.grid(row=14, column=2)
    elif nazwa_04.get() == "Rękawice jałowe 6,5":
        entry_cena_04 = Entry(root, textvariable=cena_04, justify=CENTER, width=14)
        entry_cena_04.insert(0, "1.20")
        entry_cena_04.grid(row=14, column=2)
    elif nazwa_04.get() == "Rękawice jałowe 7,0":
        entry_cena_04 = Entry(root, textvariable=cena_04, justify=CENTER, width=14)
        entry_cena_04.insert(0, "1.20")
        entry_cena_04.grid(row=14, column=2)
    elif nazwa_04.get() == "Rękawice jałowe 7,5":
        entry_cena_04 = Entry(root, textvariable=cena_04, justify=CENTER, width=14)
        entry_cena_04.insert(0, "1.20")
        entry_cena_04.grid(row=14, column=2)
    elif nazwa_04.get() == "Rękawice jałowe 8,00":
        entry_cena_04 = Entry(root, textvariable=cena_04, justify=CENTER, width=14)
        entry_cena_04.insert(0, "1.20")
        entry_cena_04.grid(row=14, column=2)
    elif nazwa_04.get() == "Rękojeść Interpulse wysokoprzepływowa":
        entry_cena_04 = Entry(root, textvariable=cena_04, justify=CENTER, width=14)
        entry_cena_04.insert(0, "216")
        entry_cena_04.grid(row=14, column=2)
    elif nazwa_04.get() == "Serweta":
        entry_cena_04 = Entry(root, textvariable=cena_04, justify=CENTER, width=14)
        entry_cena_04.insert(0, "6")
        entry_cena_04.grid(row=14, column=2)
    elif nazwa_04.get() == "Simplex Hv z Gentamycyna 10x40g":
        entry_cena_04 = Entry(root, textvariable=cena_04, justify=CENTER, width=14)
        entry_cena_04.insert(0, "162")
        entry_cena_04.grid(row=14, column=2)
    elif nazwa_04.get() == "Skalpel 11":
        entry_cena_04 = Entry(root, textvariable=cena_04, justify=CENTER, width=14)
        entry_cena_04.insert(0, "0.38")
        entry_cena_04.grid(row=14, column=2)
    elif nazwa_04.get() == "Skalpel 13":
        entry_cena_04 = Entry(root, textvariable=cena_04, justify=CENTER, width=14)
        entry_cena_04.insert(0, "1")
        entry_cena_04.grid(row=14, column=2)
    elif nazwa_04.get() == "Skalpel 22":
        entry_cena_04 = Entry(root, textvariable=cena_04, justify=CENTER, width=14)
        entry_cena_04.insert(0, "00000")
        entry_cena_04.grid(row=14, column=2)
    elif nazwa_04.get() == "Śruba blokująca PeekPower do osteotomii":
        entry_cena_04 = Entry(root, textvariable=cena_04, justify=CENTER, width=14)
        entry_cena_04.insert(0, "194")
        entry_cena_04.grid(row=14, column=2)
    elif nazwa_04.get() == "System do mieszania próżniowego":
        entry_cena_04 = Entry(root, textvariable=cena_04, justify=CENTER, width=14)
        entry_cena_04.insert(0, "216")
        entry_cena_04.grid(row=14, column=2)
    elif nazwa_04.get() == "System wprowadzania implantów ACL TightRope":
        entry_cena_04 = Entry(root, textvariable=cena_04, justify=CENTER, width=14)
        entry_cena_04.insert(0, "702")
        entry_cena_04.grid(row=14, column=2)
    elif nazwa_04.get() == "Szew FiberWire 2":
        entry_cena_04 = Entry(root, textvariable=cena_04, justify=CENTER, width=14)
        entry_cena_04.insert(0, "86.40")
        entry_cena_04.grid(row=14, column=2)
    elif nazwa_04.get() == "Taśma przylepna 10x50":
        entry_cena_04 = Entry(root, textvariable=cena_04, justify=CENTER, width=14)
        entry_cena_04.insert(0, "1.04")
        entry_cena_04.grid(row=14, column=2)
    elif nazwa_04.get() == "Triathlon elem. udowy lewy":
        entry_cena_04 = Entry(root, textvariable=cena_04, justify=CENTER, width=14)
        entry_cena_04.insert(0, "3132")
        entry_cena_04.grid(row=14, column=2)
    elif nazwa_04.get() == "Triathlon PS wkładka x3-9mm #4":
        entry_cena_04 = Entry(root, textvariable=cena_04, justify=CENTER, width=14)
        entry_cena_04.insert(0, "756")
        entry_cena_04.grid(row=14, column=2)
    elif nazwa_04.get() == "Triathlon taca piszczelowa":
        entry_cena_04 = Entry(root, textvariable=cena_04, justify=CENTER, width=14)
        entry_cena_04.insert(0, "1296")
        entry_cena_04.grid(row=14, column=2)
    elif nazwa_04.get() == "Wkłady 3L z żelem":
        entry_cena_04 = Entry(root, textvariable=cena_04, justify=CENTER, width=14)
        entry_cena_04.insert(0, "10.26")
        entry_cena_04.grid(row=14, column=2)
    elif nazwa_04.get() == "Zestaw do artroskopii":
        entry_cena_04 = Entry(root, textvariable=cena_04, justify=CENTER, width=14)
        entry_cena_04.insert(0, "67")
        entry_cena_04.grid(row=14, column=2)
    elif nazwa_04.get() == "Zestaw do artroskopii barku":
        entry_cena_04 = Entry(root, textvariable=cena_04, justify=CENTER, width=14)
        entry_cena_04.insert(0, "108")
        entry_cena_04.grid(row=14, column=2)
    elif nazwa_04.get() == "Zestaw do drenażu":
        entry_cena_04 = Entry(root, textvariable=cena_04, justify=CENTER, width=14)
        entry_cena_04.insert(0, "14.23")
        entry_cena_04.grid(row=14, column=2)
    elif nazwa_04.get() == "Zestaw ortopedyczny":
        entry_cena_04 = Entry(root, textvariable=cena_04, justify=CENTER, width=14)
        entry_cena_04.insert(0, "28.08")
        entry_cena_04.grid(row=14, column=2)
    elif nazwa_04.get() == "Gaziki 20 x 10cm":
        entry_cena_04 = Entry(root, textvariable=cena_04, justify=CENTER, width=14)
        entry_cena_04.insert(0, "0.46")
        entry_cena_04.grid(row=14, column=2)
    else:
        entry_cena_04 = Entry(root, textvariable=cena_04, justify=CENTER, width=14, bg="#ffff00")
        entry_cena_04.insert(0, "0")
        entry_cena_04.grid(row=14, column=2)

    if nazwa_05.get() == "--puste--":
        entry_cena_05 = Entry(root, textvariable=cena_05, justify=CENTER, width=14)
        entry_cena_05.insert(0, "0")
        entry_cena_05.grid(row=15, column=2)
    elif nazwa_05.get() == "Ablator":
        entry_cena_05 = Entry(root, textvariable=cena_05, justify=CENTER, width=14)
        entry_cena_05.insert(0, "572")
        entry_cena_05.grid(row=15, column=2)
    elif nazwa_05.get() == "Anestezjolog":
        entry_cena_05 = Entry(root, textvariable=cena_05, justify=CENTER, width=14, bg="#ffff00")
        entry_cena_05.insert(0, "350")
        entry_cena_05.grid(row=15, column=2)
    elif nazwa_05.get() == "Butelka 400ml do długotrwałego odsysania ran j.u. sterylna":
        entry_cena_05 = Entry(root, textvariable=cena_05, justify=CENTER, width=14)
        entry_cena_05.insert(0, "4")
        entry_cena_05.grid(row=15, column=2)
    elif nazwa_05.get() == "Doba":
        entry_cena_05 = Entry(root, textvariable=cena_05, justify=CENTER, width=14)
        entry_cena_05.insert(0, "700")
        entry_cena_05.grid(row=15, column=2)
    elif nazwa_05.get() == "Dren łączący do ssaka Grena":
        entry_cena_05 = Entry(root, textvariable=cena_05, justify=CENTER, width=14)
        entry_cena_05.insert(0, "5")
        entry_cena_05.grid(row=15, column=2)
    elif nazwa_05.get() == "Dren Redona Ch 16 dł. 800mm z trokarem":
        entry_cena_05 = Entry(root, textvariable=cena_05, justify=CENTER, width=14)
        entry_cena_05.insert(0, "29.74")
        entry_cena_05.grid(row=15, column=2)
    elif nazwa_05.get() == "Dren do pompy Artrex":
        entry_cena_05 = Entry(root, textvariable=cena_05, justify=CENTER, width=14)
        entry_cena_05.insert(0, "108")
        entry_cena_05.grid(row=15, column=2)
    elif nazwa_05.get() == "Drut wiercący 2,4 x 311":
        entry_cena_05 = Entry(root, textvariable=cena_05, justify=CENTER, width=14)
        entry_cena_05.insert(0, "139.60")
        entry_cena_05.grid(row=15, column=2)
    elif nazwa_05.get() == "Fartuch jałowy L":
        entry_cena_05 = Entry(root, textvariable=cena_05, justify=CENTER, width=14)
        entry_cena_05.insert(0, "17")
        entry_cena_05.grid(row=15, column=2)
    elif nazwa_05.get() == "Fartuch jałowy M":
        entry_cena_05 = Entry(root, textvariable=cena_05, justify=CENTER, width=14)
        entry_cena_05.insert(0, "15.28")
        entry_cena_05.grid(row=15, column=2)
    elif nazwa_05.get() == "Fartuch jałowy XL":
        entry_cena_05 = Entry(root, textvariable=cena_05, justify=CENTER, width=14)
        entry_cena_05.insert(0, "20.84")
        entry_cena_05.grid(row=15, column=2)
    elif nazwa_05.get() == "FasatThread BioComposite Interference Screw 8x30":
        entry_cena_05 = Entry(root, textvariable=cena_05, justify=CENTER, width=14)
        entry_cena_05.insert(0, "594")
        entry_cena_05.grid(row=15, column=2)
    elif nazwa_05.get() == "Folia operacyjna, jałowa 45cm x 55cm":
        entry_cena_05 = Entry(root, textvariable=cena_05, justify=CENTER, width=14)
        entry_cena_05.insert(0, "9.99")
        entry_cena_05.grid(row=15, column=2)
    elif nazwa_05.get() == "Gaziki 10 x 10cm":
        entry_cena_05 = Entry(root, textvariable=cena_05, justify=CENTER, width=14)
        entry_cena_05.insert(0, "0.10")
        entry_cena_05.grid(row=15, column=2)
    elif nazwa_05.get() == "Igła 0,6 x 60":
        entry_cena_05 = Entry(root, textvariable=cena_05, justify=CENTER, width=14)
        entry_cena_05.insert(0, "0.09")
        entry_cena_05.grid(row=15, column=2)
    elif nazwa_05.get() == "Igła 0,7 x 40":
        entry_cena_05 = Entry(root, textvariable=cena_05, justify=CENTER, width=14)
        entry_cena_05.insert(0, "0.05")
        entry_cena_05.grid(row=15, column=2)
    elif nazwa_05.get() == "Igła 0,8 x 40":
        entry_cena_05 = Entry(root, textvariable=cena_05, justify=CENTER, width=14)
        entry_cena_05.insert(0, "0.05")
        entry_cena_05.grid(row=15, column=2)
    elif nazwa_05.get() == "Igła 1,1 x 70":
        entry_cena_05 = Entry(root, textvariable=cena_05, justify=CENTER, width=14)
        entry_cena_05.insert(0, "0.16")
        entry_cena_05.grid(row=15, column=2)
    elif nazwa_05.get() == "Kaniulowana śruba int. biokompozytowa z osłonką jednoraz.":
        entry_cena_05 = Entry(root, textvariable=cena_05, justify=CENTER, width=14)
        entry_cena_05.insert(0, "594")
        entry_cena_05.grid(row=15, column=2)
    elif nazwa_05.get() == "Kaniulowana śruba int. biokompozytowa z pełnym gwintem":
        entry_cena_05 = Entry(root, textvariable=cena_05, justify=CENTER, width=14)
        entry_cena_05.insert(0, "594")
        entry_cena_05.grid(row=15, column=2)
    elif nazwa_05.get() == "Końcówka do Shavera":
        entry_cena_05 = Entry(root, textvariable=cena_05, justify=CENTER, width=14)
        entry_cena_05.insert(0, "270")
        entry_cena_05.grid(row=15, column=2)
    elif nazwa_05.get() == "Kotwica biokompozytowa SwiveLock":
        entry_cena_05 = Entry(root, textvariable=cena_05, justify=CENTER, width=14)
        entry_cena_05.insert(0, "918")
        entry_cena_05.grid(row=15, column=2)
    elif nazwa_05.get() == "Kotwica Corkscrew":
        entry_cena_05 = Entry(root, textvariable=cena_05, justify=CENTER, width=14)
        entry_cena_05.insert(0, "604")
        entry_cena_05.grid(row=15, column=2)
    elif nazwa_05.get() == "Kotwica FASTak":
        entry_cena_05 = Entry(root, textvariable=cena_05, justify=CENTER, width=14)
        entry_cena_05.insert(0, "432")
        entry_cena_05.grid(row=15, column=2)
    elif nazwa_05.get() == "Kotwica PEEK SwiveLock":
        entry_cena_05 = Entry(root, textvariable=cena_05, justify=CENTER, width=14)
        entry_cena_05.insert(0, "885.60")
        entry_cena_05.grid(row=15, column=2)
    elif nazwa_05.get() == "NaCl 3000ml":
        entry_cena_05 = Entry(root, textvariable=cena_05, justify=CENTER, width=14)
        entry_cena_05.insert(0, "29.72")
        entry_cena_05.grid(row=15, column=2)
    elif nazwa_05.get() == "NaCl 5000ml":
        entry_cena_05 = Entry(root, textvariable=cena_05, justify=CENTER, width=14)
        entry_cena_05.insert(0, "58.33")
        entry_cena_05.grid(row=15, column=2)
    elif nazwa_05.get() == "Nici Dafilon 2-0":
        entry_cena_05 = Entry(root, textvariable=cena_05, justify=CENTER, width=14)
        entry_cena_05.insert(0, "6.60")
        entry_cena_05.grid(row=15, column=2)
    elif nazwa_05.get() == "Nici Novosyn 2":
        entry_cena_05 = Entry(root, textvariable=cena_05, justify=CENTER, width=14)
        entry_cena_05.insert(0, "13")
        entry_cena_05.grid(row=15, column=2)
    elif nazwa_05.get() == "Nici Novosyn 2-0":
        entry_cena_05 = Entry(root, textvariable=cena_05, justify=CENTER, width=14)
        entry_cena_05.insert(0, "7.70")
        entry_cena_05.grid(row=15, column=2)
    elif nazwa_05.get() == "Nici Novosyn 3-0":
        entry_cena_05 = Entry(root, textvariable=cena_05, justify=CENTER, width=14)
        entry_cena_05.insert(0, "7.70")
        entry_cena_05.grid(row=15, column=2)
    elif nazwa_05.get() == "Nici Nylon 2-0":
        entry_cena_05 = Entry(root, textvariable=cena_05, justify=CENTER, width=14)
        entry_cena_05.insert(0, "2.50")
        entry_cena_05.grid(row=15, column=2)
    elif nazwa_05.get() == "Nici Nylon 3-0":
        entry_cena_05 = Entry(root, textvariable=cena_05, justify=CENTER, width=14)
        entry_cena_05.insert(0, "2")
        entry_cena_05.grid(row=15, column=2)
    elif nazwa_05.get() == "Nici PGLA":
        entry_cena_05 = Entry(root, textvariable=cena_05, justify=CENTER, width=14)
        entry_cena_05.insert(0, "11.60")
        entry_cena_05.grid(row=15, column=2)
    elif nazwa_05.get() == "Nici PremiCron 3":
        entry_cena_05 = Entry(root, textvariable=cena_05, justify=CENTER, width=14)
        entry_cena_05.insert(0, "6.50")
        entry_cena_05.grid(row=15, column=2)
    elif nazwa_05.get() == "Nici Vicryl 4-0":
        entry_cena_05 = Entry(root, textvariable=cena_05, justify=CENTER, width=14)
        entry_cena_05.insert(0, "7.50")
        entry_cena_05.grid(row=15, column=2)
    elif nazwa_05.get() == "Nitinol Guide Pin 1.1":
        entry_cena_05 = Entry(root, textvariable=cena_05, justify=CENTER, width=14)
        entry_cena_05.insert(0, "145.80")
        entry_cena_05.grid(row=15, column=2)
    elif nazwa_05.get() == "Osłona na przewody":
        entry_cena_05 = Entry(root, textvariable=cena_05, justify=CENTER, width=14)
        entry_cena_05.insert(0, "2.50")
        entry_cena_05.grid(row=15, column=2)
    elif nazwa_05.get() == "Ostrze Arthrex 90(86)x19x1,27":
        entry_cena_05 = Entry(root, textvariable=cena_05, justify=CENTER, width=14)
        entry_cena_05.insert(0, "216")
        entry_cena_05.grid(row=15, column=2)
    elif nazwa_05.get() == "Ostrze piły":
        entry_cena_05 = Entry(root, textvariable=cena_05, justify=CENTER, width=14)
        entry_cena_05.insert(0, "108")
        entry_cena_05.grid(row=15, column=2)
    elif nazwa_05.get() == "Pielęgniarka anest.":
        entry_cena_05 = Entry(root, textvariable=cena_05, justify=CENTER, width=14)
        entry_cena_05.insert(0, "50")
        entry_cena_05.grid(row=15, column=2)
    elif nazwa_05.get() == "Pielęgniarka instr.":
        entry_cena_05 = Entry(root, textvariable=cena_05, justify=CENTER, width=14)
        entry_cena_05.insert(0, "50")
        entry_cena_05.grid(row=15, column=2)
    elif nazwa_05.get() == "Pielęgniarka 'Noviline'":
        entry_cena_05 = Entry(root, textvariable=cena_05, justify=CENTER, width=14)
        entry_cena_05.insert(0, "30")
        entry_cena_05.grid(row=15, column=2)
    elif nazwa_05.get() == "Płytka PeekPower do osteotomii klinowej":
        entry_cena_05 = Entry(root, textvariable=cena_05, justify=CENTER, width=14)
        entry_cena_05.insert(0, "2160")
        entry_cena_05.grid(row=15, column=2)
    elif nazwa_05.get() == "Rękawice jałowe 6,5":
        entry_cena_05 = Entry(root, textvariable=cena_05, justify=CENTER, width=14)
        entry_cena_05.insert(0, "1.20")
        entry_cena_05.grid(row=15, column=2)
    elif nazwa_05.get() == "Rękawice jałowe 7,0":
        entry_cena_05 = Entry(root, textvariable=cena_05, justify=CENTER, width=14)
        entry_cena_05.insert(0, "1.20")
        entry_cena_05.grid(row=15, column=2)
    elif nazwa_05.get() == "Rękawice jałowe 7,5":
        entry_cena_05 = Entry(root, textvariable=cena_05, justify=CENTER, width=14)
        entry_cena_05.insert(0, "1.20")
        entry_cena_05.grid(row=15, column=2)
    elif nazwa_05.get() == "Rękawice jałowe 8,00":
        entry_cena_05 = Entry(root, textvariable=cena_05, justify=CENTER, width=14)
        entry_cena_05.insert(0, "1.20")
        entry_cena_05.grid(row=15, column=2)
    elif nazwa_05.get() == "Rękojeść Interpulse wysokoprzepływowa":
        entry_cena_05 = Entry(root, textvariable=cena_05, justify=CENTER, width=14)
        entry_cena_05.insert(0, "216")
        entry_cena_05.grid(row=15, column=2)
    elif nazwa_05.get() == "Serweta":
        entry_cena_05 = Entry(root, textvariable=cena_05, justify=CENTER, width=14)
        entry_cena_05.insert(0, "6")
        entry_cena_05.grid(row=15, column=2)
    elif nazwa_05.get() == "Simplex Hv z Gentamycyna 10x40g":
        entry_cena_05 = Entry(root, textvariable=cena_05, justify=CENTER, width=14)
        entry_cena_05.insert(0, "162")
        entry_cena_05.grid(row=15, column=2)
    elif nazwa_05.get() == "Skalpel 11":
        entry_cena_05 = Entry(root, textvariable=cena_05, justify=CENTER, width=14)
        entry_cena_05.insert(0, "0.38")
        entry_cena_05.grid(row=15, column=2)
    elif nazwa_05.get() == "Skalpel 13":
        entry_cena_05 = Entry(root, textvariable=cena_05, justify=CENTER, width=14)
        entry_cena_05.insert(0, "1")
        entry_cena_05.grid(row=15, column=2)
    elif nazwa_05.get() == "Skalpel 22":
        entry_cena_05 = Entry(root, textvariable=cena_05, justify=CENTER, width=14)
        entry_cena_05.insert(0, "00000")
        entry_cena_05.grid(row=15, column=2)
    elif nazwa_05.get() == "Śruba blokująca PeekPower do osteotomii":
        entry_cena_05 = Entry(root, textvariable=cena_05, justify=CENTER, width=14)
        entry_cena_05.insert(0, "194")
        entry_cena_05.grid(row=15, column=2)
    elif nazwa_05.get() == "System do mieszania próżniowego":
        entry_cena_05 = Entry(root, textvariable=cena_05, justify=CENTER, width=14)
        entry_cena_05.insert(0, "216")
        entry_cena_05.grid(row=15, column=2)
    elif nazwa_05.get() == "System wprowadzania implantów ACL TightRope":
        entry_cena_05 = Entry(root, textvariable=cena_05, justify=CENTER, width=14)
        entry_cena_05.insert(0, "702")
        entry_cena_05.grid(row=15, column=2)
    elif nazwa_05.get() == "Szew FiberWire 2":
        entry_cena_05 = Entry(root, textvariable=cena_05, justify=CENTER, width=14)
        entry_cena_05.insert(0, "86.40")
        entry_cena_05.grid(row=15, column=2)
    elif nazwa_05.get() == "Taśma przylepna 10x50":
        entry_cena_05 = Entry(root, textvariable=cena_05, justify=CENTER, width=14)
        entry_cena_05.insert(0, "1.04")
        entry_cena_05.grid(row=15, column=2)
    elif nazwa_05.get() == "Triathlon elem. udowy lewy":
        entry_cena_05 = Entry(root, textvariable=cena_05, justify=CENTER, width=14)
        entry_cena_05.insert(0, "3132")
        entry_cena_05.grid(row=15, column=2)
    elif nazwa_05.get() == "Triathlon PS wkładka x3-9mm #4":
        entry_cena_05 = Entry(root, textvariable=cena_05, justify=CENTER, width=14)
        entry_cena_05.insert(0, "756")
        entry_cena_05.grid(row=15, column=2)
    elif nazwa_05.get() == "Triathlon taca piszczelowa":
        entry_cena_05 = Entry(root, textvariable=cena_05, justify=CENTER, width=14)
        entry_cena_05.insert(0, "1296")
        entry_cena_05.grid(row=15, column=2)
    elif nazwa_05.get() == "Wkłady 3L z żelem":
        entry_cena_05 = Entry(root, textvariable=cena_05, justify=CENTER, width=14)
        entry_cena_05.insert(0, "10.26")
        entry_cena_05.grid(row=15, column=2)
    elif nazwa_05.get() == "Zestaw do artroskopii":
        entry_cena_05 = Entry(root, textvariable=cena_05, justify=CENTER, width=14)
        entry_cena_05.insert(0, "67")
        entry_cena_05.grid(row=15, column=2)
    elif nazwa_05.get() == "Zestaw do artroskopii barku":
        entry_cena_05 = Entry(root, textvariable=cena_05, justify=CENTER, width=14)
        entry_cena_05.insert(0, "108")
        entry_cena_05.grid(row=15, column=2)
    elif nazwa_05.get() == "Zestaw do drenażu":
        entry_cena_05 = Entry(root, textvariable=cena_05, justify=CENTER, width=14)
        entry_cena_05.insert(0, "14.23")
        entry_cena_05.grid(row=15, column=2)
    elif nazwa_05.get() == "Zestaw ortopedyczny":
        entry_cena_05 = Entry(root, textvariable=cena_05, justify=CENTER, width=14)
        entry_cena_05.insert(0, "28.08")
        entry_cena_05.grid(row=15, column=2)
    elif nazwa_05.get() == "Gaziki 20 x 10cm":
        entry_cena_05 = Entry(root, textvariable=cena_05, justify=CENTER, width=14)
        entry_cena_05.insert(0, "0.46")
        entry_cena_05.grid(row=15, column=2)
    else:
        entry_cena_05 = Entry(root, textvariable=cena_05, justify=CENTER, width=14, bg="#ffff00")
        entry_cena_05.insert(0, "0")
        entry_cena_05.grid(row=15, column=2)

    if nazwa_06.get() == "--puste--":
        entry_cena_06 = Entry(root, textvariable=cena_06, justify=CENTER, width=14)
        entry_cena_06.insert(0, "0")
        entry_cena_06.grid(row=16, column=2)
    elif nazwa_06.get() == "Ablator":
        entry_cena_06 = Entry(root, textvariable=cena_06, justify=CENTER, width=14)
        entry_cena_06.insert(0, "572")
        entry_cena_06.grid(row=16, column=2)
    elif nazwa_06.get() == "Anestezjolog":
        entry_cena_06 = Entry(root, textvariable=cena_06, justify=CENTER, width=14, bg="#ffff00")
        entry_cena_06.insert(0, "350")
        entry_cena_06.grid(row=16, column=2)
    elif nazwa_06.get() == "Butelka 400ml do długotrwałego odsysania ran j.u. sterylna":
        entry_cena_06 = Entry(root, textvariable=cena_06, justify=CENTER, width=14)
        entry_cena_06.insert(0, "4")
        entry_cena_06.grid(row=16, column=2)
    elif nazwa_06.get() == "Doba":
        entry_cena_06 = Entry(root, textvariable=cena_06, justify=CENTER, width=14)
        entry_cena_06.insert(0, "700")
        entry_cena_06.grid(row=16, column=2)
    elif nazwa_06.get() == "Dren łączący do ssaka Grena":
        entry_cena_06 = Entry(root, textvariable=cena_06, justify=CENTER, width=14)
        entry_cena_06.insert(0, "5")
        entry_cena_06.grid(row=16, column=2)
    elif nazwa_06.get() == "Dren Redona Ch 16 dł. 800mm z trokarem":
        entry_cena_06 = Entry(root, textvariable=cena_06, justify=CENTER, width=14)
        entry_cena_06.insert(0, "29.74")
        entry_cena_06.grid(row=16, column=2)
    elif nazwa_06.get() == "Dren do pompy Artrex":
        entry_cena_06 = Entry(root, textvariable=cena_06, justify=CENTER, width=14)
        entry_cena_06.insert(0, "108")
        entry_cena_06.grid(row=16, column=2)
    elif nazwa_06.get() == "Drut wiercący 2,4 x 311":
        entry_cena_06 = Entry(root, textvariable=cena_06, justify=CENTER, width=14)
        entry_cena_06.insert(0, "139.60")
        entry_cena_06.grid(row=16, column=2)
    elif nazwa_06.get() == "Fartuch jałowy L":
        entry_cena_06 = Entry(root, textvariable=cena_06, justify=CENTER, width=14)
        entry_cena_06.insert(0, "17")
        entry_cena_06.grid(row=16, column=2)
    elif nazwa_06.get() == "Fartuch jałowy M":
        entry_cena_06 = Entry(root, textvariable=cena_06, justify=CENTER, width=14)
        entry_cena_06.insert(0, "15.28")
        entry_cena_06.grid(row=16, column=2)
    elif nazwa_06.get() == "Fartuch jałowy XL":
        entry_cena_06 = Entry(root, textvariable=cena_06, justify=CENTER, width=14)
        entry_cena_06.insert(0, "20.84")
        entry_cena_06.grid(row=16, column=2)
    elif nazwa_06.get() == "FasatThread BioComposite Interference Screw 8x30":
        entry_cena_06 = Entry(root, textvariable=cena_06, justify=CENTER, width=14)
        entry_cena_06.insert(0, "594")
        entry_cena_06.grid(row=16, column=2)
    elif nazwa_06.get() == "Folia operacyjna, jałowa 45cm x 55cm":
        entry_cena_06 = Entry(root, textvariable=cena_06, justify=CENTER, width=14)
        entry_cena_06.insert(0, "9.99")
        entry_cena_06.grid(row=16, column=2)
    elif nazwa_06.get() == "Gaziki 10 x 10cm":
        entry_cena_06 = Entry(root, textvariable=cena_06, justify=CENTER, width=14)
        entry_cena_06.insert(0, "0.10")
        entry_cena_06.grid(row=16, column=2)
    elif nazwa_06.get() == "Igła 0,6 x 60":
        entry_cena_06 = Entry(root, textvariable=cena_06, justify=CENTER, width=14)
        entry_cena_06.insert(0, "0.09")
        entry_cena_06.grid(row=16, column=2)
    elif nazwa_06.get() == "Igła 0,7 x 40":
        entry_cena_06 = Entry(root, textvariable=cena_06, justify=CENTER, width=14)
        entry_cena_06.insert(0, "0.05")
        entry_cena_06.grid(row=16, column=2)
    elif nazwa_06.get() == "Igła 0,8 x 40":
        entry_cena_06 = Entry(root, textvariable=cena_06, justify=CENTER, width=14)
        entry_cena_06.insert(0, "0.05")
        entry_cena_06.grid(row=16, column=2)
    elif nazwa_06.get() == "Igła 1,1 x 70":
        entry_cena_06 = Entry(root, textvariable=cena_06, justify=CENTER, width=14)
        entry_cena_06.insert(0, "0.16")
        entry_cena_06.grid(row=16, column=2)
    elif nazwa_06.get() == "Kaniulowana śruba int. biokompozytowa z osłonką jednoraz.":
        entry_cena_06 = Entry(root, textvariable=cena_06, justify=CENTER, width=14)
        entry_cena_06.insert(0, "594")
        entry_cena_06.grid(row=16, column=2)
    elif nazwa_06.get() == "Kaniulowana śruba int. biokompozytowa z pełnym gwintem":
        entry_cena_06 = Entry(root, textvariable=cena_06, justify=CENTER, width=14)
        entry_cena_06.insert(0, "594")
        entry_cena_06.grid(row=16, column=2)
    elif nazwa_06.get() == "Końcówka do Shavera":
        entry_cena_06 = Entry(root, textvariable=cena_06, justify=CENTER, width=14)
        entry_cena_06.insert(0, "270")
        entry_cena_06.grid(row=16, column=2)
    elif nazwa_06.get() == "Kotwica biokompozytowa SwiveLock":
        entry_cena_06 = Entry(root, textvariable=cena_06, justify=CENTER, width=14)
        entry_cena_06.insert(0, "918")
        entry_cena_06.grid(row=16, column=2)
    elif nazwa_06.get() == "Kotwica Corkscrew":
        entry_cena_06 = Entry(root, textvariable=cena_06, justify=CENTER, width=14)
        entry_cena_06.insert(0, "604")
        entry_cena_06.grid(row=16, column=2)
    elif nazwa_06.get() == "Kotwica FASTak":
        entry_cena_06 = Entry(root, textvariable=cena_06, justify=CENTER, width=14)
        entry_cena_06.insert(0, "432")
        entry_cena_06.grid(row=16, column=2)
    elif nazwa_06.get() == "Kotwica PEEK SwiveLock":
        entry_cena_06 = Entry(root, textvariable=cena_06, justify=CENTER, width=14)
        entry_cena_06.insert(0, "885.60")
        entry_cena_06.grid(row=16, column=2)
    elif nazwa_06.get() == "NaCl 3000ml":
        entry_cena_06 = Entry(root, textvariable=cena_06, justify=CENTER, width=14)
        entry_cena_06.insert(0, "29.72")
        entry_cena_06.grid(row=16, column=2)
    elif nazwa_06.get() == "NaCl 5000ml":
        entry_cena_06 = Entry(root, textvariable=cena_06, justify=CENTER, width=14)
        entry_cena_06.insert(0, "58.33")
        entry_cena_06.grid(row=16, column=2)
    elif nazwa_06.get() == "Nici Dafilon 2-0":
        entry_cena_06 = Entry(root, textvariable=cena_06, justify=CENTER, width=14)
        entry_cena_06.insert(0, "6.60")
        entry_cena_06.grid(row=16, column=2)
    elif nazwa_06.get() == "Nici Novosyn 2":
        entry_cena_06 = Entry(root, textvariable=cena_06, justify=CENTER, width=14)
        entry_cena_06.insert(0, "13")
        entry_cena_06.grid(row=16, column=2)
    elif nazwa_06.get() == "Nici Novosyn 2-0":
        entry_cena_06 = Entry(root, textvariable=cena_06, justify=CENTER, width=14)
        entry_cena_06.insert(0, "7.70")
        entry_cena_06.grid(row=16, column=2)
    elif nazwa_06.get() == "Nici Novosyn 3-0":
        entry_cena_06 = Entry(root, textvariable=cena_06, justify=CENTER, width=14)
        entry_cena_06.insert(0, "7.70")
        entry_cena_06.grid(row=16, column=2)
    elif nazwa_06.get() == "Nici Nylon 2-0":
        entry_cena_06 = Entry(root, textvariable=cena_06, justify=CENTER, width=14)
        entry_cena_06.insert(0, "2.50")
        entry_cena_06.grid(row=16, column=2)
    elif nazwa_06.get() == "Nici Nylon 3-0":
        entry_cena_06 = Entry(root, textvariable=cena_06, justify=CENTER, width=14)
        entry_cena_06.insert(0, "2")
        entry_cena_06.grid(row=16, column=2)
    elif nazwa_06.get() == "Nici PGLA":
        entry_cena_06 = Entry(root, textvariable=cena_06, justify=CENTER, width=14)
        entry_cena_06.insert(0, "11.60")
        entry_cena_06.grid(row=16, column=2)
    elif nazwa_06.get() == "Nici PremiCron 3":
        entry_cena_06 = Entry(root, textvariable=cena_06, justify=CENTER, width=14)
        entry_cena_06.insert(0, "6.50")
        entry_cena_06.grid(row=16, column=2)
    elif nazwa_06.get() == "Nici Vicryl 4-0":
        entry_cena_06 = Entry(root, textvariable=cena_06, justify=CENTER, width=14)
        entry_cena_06.insert(0, "7.50")
        entry_cena_06.grid(row=16, column=2)
    elif nazwa_06.get() == "Nitinol Guide Pin 1.1":
        entry_cena_06 = Entry(root, textvariable=cena_06, justify=CENTER, width=14)
        entry_cena_06.insert(0, "145.80")
        entry_cena_06.grid(row=16, column=2)
    elif nazwa_06.get() == "Osłona na przewody":
        entry_cena_06 = Entry(root, textvariable=cena_06, justify=CENTER, width=14)
        entry_cena_06.insert(0, "2.50")
        entry_cena_06.grid(row=16, column=2)
    elif nazwa_06.get() == "Ostrze Arthrex 90(86)x19x1,27":
        entry_cena_06 = Entry(root, textvariable=cena_06, justify=CENTER, width=14)
        entry_cena_06.insert(0, "216")
        entry_cena_06.grid(row=16, column=2)
    elif nazwa_06.get() == "Ostrze piły":
        entry_cena_06 = Entry(root, textvariable=cena_06, justify=CENTER, width=14)
        entry_cena_06.insert(0, "108")
        entry_cena_06.grid(row=16, column=2)
    elif nazwa_06.get() == "Pielęgniarka anest.":
        entry_cena_06 = Entry(root, textvariable=cena_06, justify=CENTER, width=14)
        entry_cena_06.insert(0, "50")
        entry_cena_06.grid(row=16, column=2)
    elif nazwa_06.get() == "Pielęgniarka instr.":
        entry_cena_06 = Entry(root, textvariable=cena_06, justify=CENTER, width=14)
        entry_cena_06.insert(0, "50")
        entry_cena_06.grid(row=16, column=2)
    elif nazwa_06.get() == "Pielęgniarka 'Noviline'":
        entry_cena_06 = Entry(root, textvariable=cena_06, justify=CENTER, width=14)
        entry_cena_06.insert(0, "30")
        entry_cena_06.grid(row=16, column=2)
    elif nazwa_06.get() == "Płytka PeekPower do osteotomii klinowej":
        entry_cena_06 = Entry(root, textvariable=cena_06, justify=CENTER, width=14)
        entry_cena_06.insert(0, "2160")
        entry_cena_06.grid(row=16, column=2)
    elif nazwa_06.get() == "Rękawice jałowe 6,5":
        entry_cena_06 = Entry(root, textvariable=cena_06, justify=CENTER, width=14)
        entry_cena_06.insert(0, "1.20")
        entry_cena_06.grid(row=16, column=2)
    elif nazwa_06.get() == "Rękawice jałowe 7,0":
        entry_cena_06 = Entry(root, textvariable=cena_06, justify=CENTER, width=14)
        entry_cena_06.insert(0, "1.20")
        entry_cena_06.grid(row=16, column=2)
    elif nazwa_06.get() == "Rękawice jałowe 7,5":
        entry_cena_06 = Entry(root, textvariable=cena_06, justify=CENTER, width=14)
        entry_cena_06.insert(0, "1.20")
        entry_cena_06.grid(row=16, column=2)
    elif nazwa_06.get() == "Rękawice jałowe 8,00":
        entry_cena_06 = Entry(root, textvariable=cena_06, justify=CENTER, width=14)
        entry_cena_06.insert(0, "1.20")
        entry_cena_06.grid(row=16, column=2)
    elif nazwa_06.get() == "Rękojeść Interpulse wysokoprzepływowa":
        entry_cena_06 = Entry(root, textvariable=cena_06, justify=CENTER, width=14)
        entry_cena_06.insert(0, "216")
        entry_cena_06.grid(row=16, column=2)
    elif nazwa_06.get() == "Serweta":
        entry_cena_06 = Entry(root, textvariable=cena_06, justify=CENTER, width=14)
        entry_cena_06.insert(0, "6")
        entry_cena_06.grid(row=16, column=2)
    elif nazwa_06.get() == "Simplex Hv z Gentamycyna 10x40g":
        entry_cena_06 = Entry(root, textvariable=cena_06, justify=CENTER, width=14)
        entry_cena_06.insert(0, "162")
        entry_cena_06.grid(row=16, column=2)
    elif nazwa_06.get() == "Skalpel 11":
        entry_cena_06 = Entry(root, textvariable=cena_06, justify=CENTER, width=14)
        entry_cena_06.insert(0, "0.38")
        entry_cena_06.grid(row=16, column=2)
    elif nazwa_06.get() == "Skalpel 13":
        entry_cena_06 = Entry(root, textvariable=cena_06, justify=CENTER, width=14)
        entry_cena_06.insert(0, "1")
        entry_cena_06.grid(row=16, column=2)
    elif nazwa_06.get() == "Skalpel 22":
        entry_cena_06 = Entry(root, textvariable=cena_06, justify=CENTER, width=14)
        entry_cena_06.insert(0, "00000")
        entry_cena_06.grid(row=16, column=2)
    elif nazwa_06.get() == "Śruba blokująca PeekPower do osteotomii":
        entry_cena_06 = Entry(root, textvariable=cena_06, justify=CENTER, width=14)
        entry_cena_06.insert(0, "194")
        entry_cena_06.grid(row=16, column=2)
    elif nazwa_06.get() == "System do mieszania próżniowego":
        entry_cena_06 = Entry(root, textvariable=cena_06, justify=CENTER, width=14)
        entry_cena_06.insert(0, "216")
        entry_cena_06.grid(row=16, column=2)
    elif nazwa_06.get() == "System wprowadzania implantów ACL TightRope":
        entry_cena_06 = Entry(root, textvariable=cena_06, justify=CENTER, width=14)
        entry_cena_06.insert(0, "702")
        entry_cena_06.grid(row=16, column=2)
    elif nazwa_06.get() == "Szew FiberWire 2":
        entry_cena_06 = Entry(root, textvariable=cena_06, justify=CENTER, width=14)
        entry_cena_06.insert(0, "86.40")
        entry_cena_06.grid(row=16, column=2)
    elif nazwa_06.get() == "Taśma przylepna 10x50":
        entry_cena_06 = Entry(root, textvariable=cena_06, justify=CENTER, width=14)
        entry_cena_06.insert(0, "1.04")
        entry_cena_06.grid(row=16, column=2)
    elif nazwa_06.get() == "Triathlon elem. udowy lewy":
        entry_cena_06 = Entry(root, textvariable=cena_06, justify=CENTER, width=14)
        entry_cena_06.insert(0, "3132")
        entry_cena_06.grid(row=16, column=2)
    elif nazwa_06.get() == "Triathlon PS wkładka x3-9mm #4":
        entry_cena_06 = Entry(root, textvariable=cena_06, justify=CENTER, width=14)
        entry_cena_06.insert(0, "756")
        entry_cena_06.grid(row=16, column=2)
    elif nazwa_06.get() == "Triathlon taca piszczelowa":
        entry_cena_06 = Entry(root, textvariable=cena_06, justify=CENTER, width=14)
        entry_cena_06.insert(0, "1296")
        entry_cena_06.grid(row=16, column=2)
    elif nazwa_06.get() == "Wkłady 3L z żelem":
        entry_cena_06 = Entry(root, textvariable=cena_06, justify=CENTER, width=14)
        entry_cena_06.insert(0, "10.26")
        entry_cena_06.grid(row=16, column=2)
    elif nazwa_06.get() == "Zestaw do artroskopii":
        entry_cena_06 = Entry(root, textvariable=cena_06, justify=CENTER, width=14)
        entry_cena_06.insert(0, "67")
        entry_cena_06.grid(row=16, column=2)
    elif nazwa_06.get() == "Zestaw do artroskopii barku":
        entry_cena_06 = Entry(root, textvariable=cena_06, justify=CENTER, width=14)
        entry_cena_06.insert(0, "108")
        entry_cena_06.grid(row=16, column=2)
    elif nazwa_06.get() == "Zestaw do drenażu":
        entry_cena_06 = Entry(root, textvariable=cena_06, justify=CENTER, width=14)
        entry_cena_06.insert(0, "14.23")
        entry_cena_06.grid(row=16, column=2)
    elif nazwa_06.get() == "Zestaw ortopedyczny":
        entry_cena_06 = Entry(root, textvariable=cena_06, justify=CENTER, width=14)
        entry_cena_06.insert(0, "28.08")
        entry_cena_06.grid(row=16, column=2)
    elif nazwa_06.get() == "Gaziki 20 x 10cm":
        entry_cena_06 = Entry(root, textvariable=cena_06, justify=CENTER, width=14)
        entry_cena_06.insert(0, "0.46")
        entry_cena_06.grid(row=16, column=2)
    else:
        entry_cena_06 = Entry(root, textvariable=cena_06, justify=CENTER, width=14, bg="#ffff00")
        entry_cena_06.insert(0, "0")
        entry_cena_06.grid(row=16, column=2)

    if nazwa_07.get() == "--puste--":
        entry_cena_07 = Entry(root, textvariable=cena_07, justify=CENTER, width=14)
        entry_cena_07.insert(0, "0")
        entry_cena_07.grid(row=17, column=2)
    elif nazwa_07.get() == "Ablator":
        entry_cena_07 = Entry(root, textvariable=cena_07, justify=CENTER, width=14)
        entry_cena_07.insert(0, "572")
        entry_cena_07.grid(row=17, column=2)
    elif nazwa_07.get() == "Anestezjolog":
        entry_cena_07 = Entry(root, textvariable=cena_07, justify=CENTER, width=14, bg="#ffff00")
        entry_cena_07.insert(0, "350")
        entry_cena_07.grid(row=17, column=2)
    elif nazwa_07.get() == "Butelka 400ml do długotrwałego odsysania ran j.u. sterylna":
        entry_cena_07 = Entry(root, textvariable=cena_07, justify=CENTER, width=14)
        entry_cena_07.insert(0, "4")
        entry_cena_07.grid(row=17, column=2)
    elif nazwa_07.get() == "Doba":
        entry_cena_07 = Entry(root, textvariable=cena_07, justify=CENTER, width=14)
        entry_cena_07.insert(0, "700")
        entry_cena_07.grid(row=17, column=2)
    elif nazwa_07.get() == "Dren łączący do ssaka Grena":
        entry_cena_07 = Entry(root, textvariable=cena_07, justify=CENTER, width=14)
        entry_cena_07.insert(0, "5")
        entry_cena_07.grid(row=17, column=2)
    elif nazwa_07.get() == "Dren Redona Ch 16 dł. 800mm z trokarem":
        entry_cena_07 = Entry(root, textvariable=cena_07, justify=CENTER, width=14)
        entry_cena_07.insert(0, "29.74")
        entry_cena_07.grid(row=17, column=2)
    elif nazwa_07.get() == "Dren do pompy Artrex":
        entry_cena_07 = Entry(root, textvariable=cena_07, justify=CENTER, width=14)
        entry_cena_07.insert(0, "108")
        entry_cena_07.grid(row=17, column=2)
    elif nazwa_07.get() == "Drut wiercący 2,4 x 311":
        entry_cena_07 = Entry(root, textvariable=cena_07, justify=CENTER, width=14)
        entry_cena_07.insert(0, "139.60")
        entry_cena_07.grid(row=17, column=2)
    elif nazwa_07.get() == "Fartuch jałowy L":
        entry_cena_07 = Entry(root, textvariable=cena_07, justify=CENTER, width=14)
        entry_cena_07.insert(0, "17")
        entry_cena_07.grid(row=17, column=2)
    elif nazwa_07.get() == "Fartuch jałowy M":
        entry_cena_07 = Entry(root, textvariable=cena_07, justify=CENTER, width=14)
        entry_cena_07.insert(0, "15.28")
        entry_cena_07.grid(row=17, column=2)
    elif nazwa_07.get() == "Fartuch jałowy XL":
        entry_cena_07 = Entry(root, textvariable=cena_07, justify=CENTER, width=14)
        entry_cena_07.insert(0, "20.84")
        entry_cena_07.grid(row=17, column=2)
    elif nazwa_07.get() == "FasatThread BioComposite Interference Screw 8x30":
        entry_cena_07 = Entry(root, textvariable=cena_07, justify=CENTER, width=14)
        entry_cena_07.insert(0, "594")
        entry_cena_07.grid(row=17, column=2)
    elif nazwa_07.get() == "Folia operacyjna, jałowa 45cm x 55cm":
        entry_cena_07 = Entry(root, textvariable=cena_07, justify=CENTER, width=14)
        entry_cena_07.insert(0, "9.99")
        entry_cena_07.grid(row=17, column=2)
    elif nazwa_07.get() == "Gaziki 10 x 10cm":
        entry_cena_07 = Entry(root, textvariable=cena_07, justify=CENTER, width=14)
        entry_cena_07.insert(0, "0.10")
        entry_cena_07.grid(row=17, column=2)
    elif nazwa_07.get() == "Igła 0,6 x 60":
        entry_cena_07 = Entry(root, textvariable=cena_07, justify=CENTER, width=14)
        entry_cena_07.insert(0, "0.09")
        entry_cena_07.grid(row=17, column=2)
    elif nazwa_07.get() == "Igła 0,7 x 40":
        entry_cena_07 = Entry(root, textvariable=cena_07, justify=CENTER, width=14)
        entry_cena_07.insert(0, "0.05")
        entry_cena_07.grid(row=17, column=2)
    elif nazwa_07.get() == "Igła 0,8 x 40":
        entry_cena_07 = Entry(root, textvariable=cena_07, justify=CENTER, width=14)
        entry_cena_07.insert(0, "0.05")
        entry_cena_07.grid(row=17, column=2)
    elif nazwa_07.get() == "Igła 1,1 x 70":
        entry_cena_07 = Entry(root, textvariable=cena_07, justify=CENTER, width=14)
        entry_cena_07.insert(0, "0.16")
        entry_cena_07.grid(row=17, column=2)
    elif nazwa_07.get() == "Kaniulowana śruba int. biokompozytowa z osłonką jednoraz.":
        entry_cena_07 = Entry(root, textvariable=cena_07, justify=CENTER, width=14)
        entry_cena_07.insert(0, "594")
        entry_cena_07.grid(row=17, column=2)
    elif nazwa_07.get() == "Kaniulowana śruba int. biokompozytowa z pełnym gwintem":
        entry_cena_07 = Entry(root, textvariable=cena_07, justify=CENTER, width=14)
        entry_cena_07.insert(0, "594")
        entry_cena_07.grid(row=17, column=2)
    elif nazwa_07.get() == "Końcówka do Shavera":
        entry_cena_07 = Entry(root, textvariable=cena_07, justify=CENTER, width=14)
        entry_cena_07.insert(0, "270")
        entry_cena_07.grid(row=17, column=2)
    elif nazwa_07.get() == "Kotwica biokompozytowa SwiveLock":
        entry_cena_07 = Entry(root, textvariable=cena_07, justify=CENTER, width=14)
        entry_cena_07.insert(0, "918")
        entry_cena_07.grid(row=17, column=2)
    elif nazwa_07.get() == "Kotwica Corkscrew":
        entry_cena_07 = Entry(root, textvariable=cena_07, justify=CENTER, width=14)
        entry_cena_07.insert(0, "604")
        entry_cena_07.grid(row=17, column=2)
    elif nazwa_07.get() == "Kotwica FASTak":
        entry_cena_07 = Entry(root, textvariable=cena_07, justify=CENTER, width=14)
        entry_cena_07.insert(0, "432")
        entry_cena_07.grid(row=17, column=2)
    elif nazwa_07.get() == "Kotwica PEEK SwiveLock":
        entry_cena_07 = Entry(root, textvariable=cena_07, justify=CENTER, width=14)
        entry_cena_07.insert(0, "885.60")
        entry_cena_07.grid(row=17, column=2)
    elif nazwa_07.get() == "NaCl 3000ml":
        entry_cena_07 = Entry(root, textvariable=cena_07, justify=CENTER, width=14)
        entry_cena_07.insert(0, "29.72")
        entry_cena_07.grid(row=17, column=2)
    elif nazwa_07.get() == "NaCl 5000ml":
        entry_cena_07 = Entry(root, textvariable=cena_07, justify=CENTER, width=14)
        entry_cena_07.insert(0, "58.33")
        entry_cena_07.grid(row=17, column=2)
    elif nazwa_07.get() == "Nici Dafilon 2-0":
        entry_cena_07 = Entry(root, textvariable=cena_07, justify=CENTER, width=14)
        entry_cena_07.insert(0, "6.60")
        entry_cena_07.grid(row=17, column=2)
    elif nazwa_07.get() == "Nici Novosyn 2":
        entry_cena_07 = Entry(root, textvariable=cena_07, justify=CENTER, width=14)
        entry_cena_07.insert(0, "13")
        entry_cena_07.grid(row=17, column=2)
    elif nazwa_07.get() == "Nici Novosyn 2-0":
        entry_cena_07 = Entry(root, textvariable=cena_07, justify=CENTER, width=14)
        entry_cena_07.insert(0, "7.70")
        entry_cena_07.grid(row=17, column=2)
    elif nazwa_07.get() == "Nici Novosyn 3-0":
        entry_cena_07 = Entry(root, textvariable=cena_07, justify=CENTER, width=14)
        entry_cena_07.insert(0, "7.70")
        entry_cena_07.grid(row=17, column=2)
    elif nazwa_07.get() == "Nici Nylon 2-0":
        entry_cena_07 = Entry(root, textvariable=cena_07, justify=CENTER, width=14)
        entry_cena_07.insert(0, "2.50")
        entry_cena_07.grid(row=17, column=2)
    elif nazwa_07.get() == "Nici Nylon 3-0":
        entry_cena_07 = Entry(root, textvariable=cena_07, justify=CENTER, width=14)
        entry_cena_07.insert(0, "2")
        entry_cena_07.grid(row=17, column=2)
    elif nazwa_07.get() == "Nici PGLA":
        entry_cena_07 = Entry(root, textvariable=cena_07, justify=CENTER, width=14)
        entry_cena_07.insert(0, "11.60")
        entry_cena_07.grid(row=17, column=2)
    elif nazwa_07.get() == "Nici PremiCron 3":
        entry_cena_07 = Entry(root, textvariable=cena_07, justify=CENTER, width=14)
        entry_cena_07.insert(0, "6.50")
        entry_cena_07.grid(row=17, column=2)
    elif nazwa_07.get() == "Nici Vicryl 4-0":
        entry_cena_07 = Entry(root, textvariable=cena_07, justify=CENTER, width=14)
        entry_cena_07.insert(0, "7.50")
        entry_cena_07.grid(row=17, column=2)
    elif nazwa_07.get() == "Nitinol Guide Pin 1.1":
        entry_cena_07 = Entry(root, textvariable=cena_07, justify=CENTER, width=14)
        entry_cena_07.insert(0, "145.80")
        entry_cena_07.grid(row=17, column=2)
    elif nazwa_07.get() == "Osłona na przewody":
        entry_cena_07 = Entry(root, textvariable=cena_07, justify=CENTER, width=14)
        entry_cena_07.insert(0, "2.50")
        entry_cena_07.grid(row=17, column=2)
    elif nazwa_07.get() == "Ostrze Arthrex 90(86)x19x1,27":
        entry_cena_07 = Entry(root, textvariable=cena_07, justify=CENTER, width=14)
        entry_cena_07.insert(0, "216")
        entry_cena_07.grid(row=17, column=2)
    elif nazwa_07.get() == "Ostrze piły":
        entry_cena_07 = Entry(root, textvariable=cena_07, justify=CENTER, width=14)
        entry_cena_07.insert(0, "108")
        entry_cena_07.grid(row=17, column=2)
    elif nazwa_07.get() == "Pielęgniarka anest.":
        entry_cena_07 = Entry(root, textvariable=cena_07, justify=CENTER, width=14)
        entry_cena_07.insert(0, "50")
        entry_cena_07.grid(row=17, column=2)
    elif nazwa_07.get() == "Pielęgniarka instr.":
        entry_cena_07 = Entry(root, textvariable=cena_07, justify=CENTER, width=14)
        entry_cena_07.insert(0, "50")
        entry_cena_07.grid(row=17, column=2)
    elif nazwa_07.get() == "Pielęgniarka 'Noviline'":
        entry_cena_07 = Entry(root, textvariable=cena_07, justify=CENTER, width=14)
        entry_cena_07.insert(0, "30")
        entry_cena_07.grid(row=17, column=2)
    elif nazwa_07.get() == "Płytka PeekPower do osteotomii klinowej":
        entry_cena_07 = Entry(root, textvariable=cena_07, justify=CENTER, width=14)
        entry_cena_07.insert(0, "2160")
        entry_cena_07.grid(row=17, column=2)
    elif nazwa_07.get() == "Rękawice jałowe 6,5":
        entry_cena_07 = Entry(root, textvariable=cena_07, justify=CENTER, width=14)
        entry_cena_07.insert(0, "1.20")
        entry_cena_07.grid(row=17, column=2)
    elif nazwa_07.get() == "Rękawice jałowe 7,0":
        entry_cena_07 = Entry(root, textvariable=cena_07, justify=CENTER, width=14)
        entry_cena_07.insert(0, "1.20")
        entry_cena_07.grid(row=17, column=2)
    elif nazwa_07.get() == "Rękawice jałowe 7,5":
        entry_cena_07 = Entry(root, textvariable=cena_07, justify=CENTER, width=14)
        entry_cena_07.insert(0, "1.20")
        entry_cena_07.grid(row=17, column=2)
    elif nazwa_07.get() == "Rękawice jałowe 8,00":
        entry_cena_07 = Entry(root, textvariable=cena_07, justify=CENTER, width=14)
        entry_cena_07.insert(0, "1.20")
        entry_cena_07.grid(row=17, column=2)
    elif nazwa_07.get() == "Rękojeść Interpulse wysokoprzepływowa":
        entry_cena_07 = Entry(root, textvariable=cena_07, justify=CENTER, width=14)
        entry_cena_07.insert(0, "216")
        entry_cena_07.grid(row=17, column=2)
    elif nazwa_07.get() == "Serweta":
        entry_cena_07 = Entry(root, textvariable=cena_07, justify=CENTER, width=14)
        entry_cena_07.insert(0, "6")
        entry_cena_07.grid(row=17, column=2)
    elif nazwa_07.get() == "Simplex Hv z Gentamycyna 10x40g":
        entry_cena_07 = Entry(root, textvariable=cena_07, justify=CENTER, width=14)
        entry_cena_07.insert(0, "162")
        entry_cena_07.grid(row=17, column=2)
    elif nazwa_07.get() == "Skalpel 11":
        entry_cena_07 = Entry(root, textvariable=cena_07, justify=CENTER, width=14)
        entry_cena_07.insert(0, "0.38")
        entry_cena_07.grid(row=17, column=2)
    elif nazwa_07.get() == "Skalpel 13":
        entry_cena_07 = Entry(root, textvariable=cena_07, justify=CENTER, width=14)
        entry_cena_07.insert(0, "1")
        entry_cena_07.grid(row=17, column=2)
    elif nazwa_07.get() == "Skalpel 22":
        entry_cena_07 = Entry(root, textvariable=cena_07, justify=CENTER, width=14)
        entry_cena_07.insert(0, "00000")
        entry_cena_07.grid(row=17, column=2)
    elif nazwa_07.get() == "Śruba blokująca PeekPower do osteotomii":
        entry_cena_07 = Entry(root, textvariable=cena_07, justify=CENTER, width=14)
        entry_cena_07.insert(0, "194")
        entry_cena_07.grid(row=17, column=2)
    elif nazwa_07.get() == "System do mieszania próżniowego":
        entry_cena_07 = Entry(root, textvariable=cena_07, justify=CENTER, width=14)
        entry_cena_07.insert(0, "216")
        entry_cena_07.grid(row=17, column=2)
    elif nazwa_07.get() == "System wprowadzania implantów ACL TightRope":
        entry_cena_07 = Entry(root, textvariable=cena_07, justify=CENTER, width=14)
        entry_cena_07.insert(0, "702")
        entry_cena_07.grid(row=17, column=2)
    elif nazwa_07.get() == "Szew FiberWire 2":
        entry_cena_07 = Entry(root, textvariable=cena_07, justify=CENTER, width=14)
        entry_cena_07.insert(0, "86.40")
        entry_cena_07.grid(row=17, column=2)
    elif nazwa_07.get() == "Taśma przylepna 10x50":
        entry_cena_07 = Entry(root, textvariable=cena_07, justify=CENTER, width=14)
        entry_cena_07.insert(0, "1.04")
        entry_cena_07.grid(row=17, column=2)
    elif nazwa_07.get() == "Triathlon elem. udowy lewy":
        entry_cena_07 = Entry(root, textvariable=cena_07, justify=CENTER, width=14)
        entry_cena_07.insert(0, "3132")
        entry_cena_07.grid(row=17, column=2)
    elif nazwa_07.get() == "Triathlon PS wkładka x3-9mm #4":
        entry_cena_07 = Entry(root, textvariable=cena_07, justify=CENTER, width=14)
        entry_cena_07.insert(0, "756")
        entry_cena_07.grid(row=17, column=2)
    elif nazwa_07.get() == "Triathlon taca piszczelowa":
        entry_cena_07 = Entry(root, textvariable=cena_07, justify=CENTER, width=14)
        entry_cena_07.insert(0, "1296")
        entry_cena_07.grid(row=17, column=2)
    elif nazwa_07.get() == "Wkłady 3L z żelem":
        entry_cena_07 = Entry(root, textvariable=cena_07, justify=CENTER, width=14)
        entry_cena_07.insert(0, "10.26")
        entry_cena_07.grid(row=17, column=2)
    elif nazwa_07.get() == "Zestaw do artroskopii":
        entry_cena_07 = Entry(root, textvariable=cena_07, justify=CENTER, width=14)
        entry_cena_07.insert(0, "67")
        entry_cena_07.grid(row=17, column=2)
    elif nazwa_07.get() == "Zestaw do artroskopii barku":
        entry_cena_07 = Entry(root, textvariable=cena_07, justify=CENTER, width=14)
        entry_cena_07.insert(0, "108")
        entry_cena_07.grid(row=17, column=2)
    elif nazwa_07.get() == "Zestaw do drenażu":
        entry_cena_07 = Entry(root, textvariable=cena_07, justify=CENTER, width=14)
        entry_cena_07.insert(0, "14.23")
        entry_cena_07.grid(row=17, column=2)
    elif nazwa_07.get() == "Zestaw ortopedyczny":
        entry_cena_07 = Entry(root, textvariable=cena_07, justify=CENTER, width=14)
        entry_cena_07.insert(0, "28.08")
        entry_cena_07.grid(row=17, column=2)
    elif nazwa_07.get() == "Gaziki 20 x 10cm":
        entry_cena_07 = Entry(root, textvariable=cena_07, justify=CENTER, width=14)
        entry_cena_07.insert(0, "0.46")
        entry_cena_07.grid(row=17, column=2)
    else:
        entry_cena_07 = Entry(root, textvariable=cena_07, justify=CENTER, width=14, bg="#ffff00")
        entry_cena_07.insert(0, "0")
        entry_cena_07.grid(row=17, column=2)

    if nazwa_08.get() == "--puste--":
        entry_cena_08 = Entry(root, textvariable=cena_08, justify=CENTER, width=14)
        entry_cena_08.insert(0, "0")
        entry_cena_08.grid(row=18, column=2)
    elif nazwa_08.get() == "Ablator":
        entry_cena_08 = Entry(root, textvariable=cena_08, justify=CENTER, width=14)
        entry_cena_08.insert(0, "572")
        entry_cena_08.grid(row=18, column=2)
    elif nazwa_08.get() == "Anestezjolog":
        entry_cena_08 = Entry(root, textvariable=cena_08, justify=CENTER, width=14, bg="#ffff00")
        entry_cena_08.insert(0, "350")
        entry_cena_08.grid(row=18, column=2)
    elif nazwa_08.get() == "Butelka 400ml do długotrwałego odsysania ran j.u. sterylna":
        entry_cena_08 = Entry(root, textvariable=cena_08, justify=CENTER, width=14)
        entry_cena_08.insert(0, "4")
        entry_cena_08.grid(row=18, column=2)
    elif nazwa_08.get() == "Doba":
        entry_cena_08 = Entry(root, textvariable=cena_08, justify=CENTER, width=14)
        entry_cena_08.insert(0, "700")
        entry_cena_08.grid(row=18, column=2)
    elif nazwa_08.get() == "Dren łączący do ssaka Grena":
        entry_cena_08 = Entry(root, textvariable=cena_08, justify=CENTER, width=14)
        entry_cena_08.insert(0, "5")
        entry_cena_08.grid(row=18, column=2)
    elif nazwa_08.get() == "Dren Redona Ch 16 dł. 800mm z trokarem":
        entry_cena_08 = Entry(root, textvariable=cena_08, justify=CENTER, width=14)
        entry_cena_08.insert(0, "29.74")
        entry_cena_08.grid(row=18, column=2)
    elif nazwa_08.get() == "Dren do pompy Artrex":
        entry_cena_08 = Entry(root, textvariable=cena_08, justify=CENTER, width=14)
        entry_cena_08.insert(0, "108")
        entry_cena_08.grid(row=18, column=2)
    elif nazwa_08.get() == "Drut wiercący 2,4 x 311":
        entry_cena_08 = Entry(root, textvariable=cena_08, justify=CENTER, width=14)
        entry_cena_08.insert(0, "139.60")
        entry_cena_08.grid(row=18, column=2)
    elif nazwa_08.get() == "Fartuch jałowy L":
        entry_cena_08 = Entry(root, textvariable=cena_08, justify=CENTER, width=14)
        entry_cena_08.insert(0, "17")
        entry_cena_08.grid(row=18, column=2)
    elif nazwa_08.get() == "Fartuch jałowy M":
        entry_cena_08 = Entry(root, textvariable=cena_08, justify=CENTER, width=14)
        entry_cena_08.insert(0, "15.28")
        entry_cena_08.grid(row=18, column=2)
    elif nazwa_08.get() == "Fartuch jałowy XL":
        entry_cena_08 = Entry(root, textvariable=cena_08, justify=CENTER, width=14)
        entry_cena_08.insert(0, "20.84")
        entry_cena_08.grid(row=18, column=2)
    elif nazwa_08.get() == "FasatThread BioComposite Interference Screw 8x30":
        entry_cena_08 = Entry(root, textvariable=cena_08, justify=CENTER, width=14)
        entry_cena_08.insert(0, "594")
        entry_cena_08.grid(row=18, column=2)
    elif nazwa_08.get() == "Folia operacyjna, jałowa 45cm x 55cm":
        entry_cena_08 = Entry(root, textvariable=cena_08, justify=CENTER, width=14)
        entry_cena_08.insert(0, "9.99")
        entry_cena_08.grid(row=18, column=2)
    elif nazwa_08.get() == "Gaziki 10 x 10cm":
        entry_cena_08 = Entry(root, textvariable=cena_08, justify=CENTER, width=14)
        entry_cena_08.insert(0, "0.10")
        entry_cena_08.grid(row=18, column=2)
    elif nazwa_08.get() == "Igła 0,6 x 60":
        entry_cena_08 = Entry(root, textvariable=cena_08, justify=CENTER, width=14)
        entry_cena_08.insert(0, "0.09")
        entry_cena_08.grid(row=18, column=2)
    elif nazwa_08.get() == "Igła 0,7 x 40":
        entry_cena_08 = Entry(root, textvariable=cena_08, justify=CENTER, width=14)
        entry_cena_08.insert(0, "0.05")
        entry_cena_08.grid(row=18, column=2)
    elif nazwa_08.get() == "Igła 0,8 x 40":
        entry_cena_08 = Entry(root, textvariable=cena_08, justify=CENTER, width=14)
        entry_cena_08.insert(0, "0.05")
        entry_cena_08.grid(row=18, column=2)
    elif nazwa_08.get() == "Igła 1,1 x 70":
        entry_cena_08 = Entry(root, textvariable=cena_08, justify=CENTER, width=14)
        entry_cena_08.insert(0, "0.16")
        entry_cena_08.grid(row=18, column=2)
    elif nazwa_08.get() == "Kaniulowana śruba int. biokompozytowa z osłonką jednoraz.":
        entry_cena_08 = Entry(root, textvariable=cena_08, justify=CENTER, width=14)
        entry_cena_08.insert(0, "594")
        entry_cena_08.grid(row=18, column=2)
    elif nazwa_08.get() == "Kaniulowana śruba int. biokompozytowa z pełnym gwintem":
        entry_cena_08 = Entry(root, textvariable=cena_08, justify=CENTER, width=14)
        entry_cena_08.insert(0, "594")
        entry_cena_08.grid(row=18, column=2)
    elif nazwa_08.get() == "Końcówka do Shavera":
        entry_cena_08 = Entry(root, textvariable=cena_08, justify=CENTER, width=14)
        entry_cena_08.insert(0, "270")
        entry_cena_08.grid(row=18, column=2)
    elif nazwa_08.get() == "Kotwica biokompozytowa SwiveLock":
        entry_cena_08 = Entry(root, textvariable=cena_08, justify=CENTER, width=14)
        entry_cena_08.insert(0, "918")
        entry_cena_08.grid(row=18, column=2)
    elif nazwa_08.get() == "Kotwica Corkscrew":
        entry_cena_08 = Entry(root, textvariable=cena_08, justify=CENTER, width=14)
        entry_cena_08.insert(0, "604")
        entry_cena_08.grid(row=18, column=2)
    elif nazwa_08.get() == "Kotwica FASTak":
        entry_cena_08 = Entry(root, textvariable=cena_08, justify=CENTER, width=14)
        entry_cena_08.insert(0, "432")
        entry_cena_08.grid(row=18, column=2)
    elif nazwa_08.get() == "Kotwica PEEK SwiveLock":
        entry_cena_08 = Entry(root, textvariable=cena_08, justify=CENTER, width=14)
        entry_cena_08.insert(0, "885.60")
        entry_cena_08.grid(row=18, column=2)
    elif nazwa_08.get() == "NaCl 3000ml":
        entry_cena_08 = Entry(root, textvariable=cena_08, justify=CENTER, width=14)
        entry_cena_08.insert(0, "29.72")
        entry_cena_08.grid(row=18, column=2)
    elif nazwa_08.get() == "NaCl 5000ml":
        entry_cena_08 = Entry(root, textvariable=cena_08, justify=CENTER, width=14)
        entry_cena_08.insert(0, "58.33")
        entry_cena_08.grid(row=18, column=2)
    elif nazwa_08.get() == "Nici Dafilon 2-0":
        entry_cena_08 = Entry(root, textvariable=cena_08, justify=CENTER, width=14)
        entry_cena_08.insert(0, "6.60")
        entry_cena_08.grid(row=18, column=2)
    elif nazwa_08.get() == "Nici Novosyn 2":
        entry_cena_08 = Entry(root, textvariable=cena_08, justify=CENTER, width=14)
        entry_cena_08.insert(0, "13")
        entry_cena_08.grid(row=18, column=2)
    elif nazwa_08.get() == "Nici Novosyn 2-0":
        entry_cena_08 = Entry(root, textvariable=cena_08, justify=CENTER, width=14)
        entry_cena_08.insert(0, "7.70")
        entry_cena_08.grid(row=18, column=2)
    elif nazwa_08.get() == "Nici Novosyn 3-0":
        entry_cena_08 = Entry(root, textvariable=cena_08, justify=CENTER, width=14)
        entry_cena_08.insert(0, "7.70")
        entry_cena_08.grid(row=18, column=2)
    elif nazwa_08.get() == "Nici Nylon 2-0":
        entry_cena_08 = Entry(root, textvariable=cena_08, justify=CENTER, width=14)
        entry_cena_08.insert(0, "2.50")
        entry_cena_08.grid(row=18, column=2)
    elif nazwa_08.get() == "Nici Nylon 3-0":
        entry_cena_08 = Entry(root, textvariable=cena_08, justify=CENTER, width=14)
        entry_cena_08.insert(0, "2")
        entry_cena_08.grid(row=18, column=2)
    elif nazwa_08.get() == "Nici PGLA":
        entry_cena_08 = Entry(root, textvariable=cena_08, justify=CENTER, width=14)
        entry_cena_08.insert(0, "11.60")
        entry_cena_08.grid(row=18, column=2)
    elif nazwa_08.get() == "Nici PremiCron 3":
        entry_cena_08 = Entry(root, textvariable=cena_08, justify=CENTER, width=14)
        entry_cena_08.insert(0, "6.50")
        entry_cena_08.grid(row=18, column=2)
    elif nazwa_08.get() == "Nici Vicryl 4-0":
        entry_cena_08 = Entry(root, textvariable=cena_08, justify=CENTER, width=14)
        entry_cena_08.insert(0, "7.50")
        entry_cena_08.grid(row=18, column=2)
    elif nazwa_08.get() == "Nitinol Guide Pin 1.1":
        entry_cena_08 = Entry(root, textvariable=cena_08, justify=CENTER, width=14)
        entry_cena_08.insert(0, "145.80")
        entry_cena_08.grid(row=18, column=2)
    elif nazwa_08.get() == "Osłona na przewody":
        entry_cena_08 = Entry(root, textvariable=cena_08, justify=CENTER, width=14)
        entry_cena_08.insert(0, "2.50")
        entry_cena_08.grid(row=18, column=2)
    elif nazwa_08.get() == "Ostrze Arthrex 90(86)x19x1,27":
        entry_cena_08 = Entry(root, textvariable=cena_08, justify=CENTER, width=14)
        entry_cena_08.insert(0, "216")
        entry_cena_08.grid(row=18, column=2)
    elif nazwa_08.get() == "Ostrze piły":
        entry_cena_08 = Entry(root, textvariable=cena_08, justify=CENTER, width=14)
        entry_cena_08.insert(0, "108")
        entry_cena_08.grid(row=18, column=2)
    elif nazwa_08.get() == "Pielęgniarka anest.":
        entry_cena_08 = Entry(root, textvariable=cena_08, justify=CENTER, width=14)
        entry_cena_08.insert(0, "50")
        entry_cena_08.grid(row=18, column=2)
    elif nazwa_08.get() == "Pielęgniarka instr.":
        entry_cena_08 = Entry(root, textvariable=cena_08, justify=CENTER, width=14)
        entry_cena_08.insert(0, "50")
        entry_cena_08.grid(row=18, column=2)
    elif nazwa_08.get() == "Pielęgniarka 'Noviline'":
        entry_cena_08 = Entry(root, textvariable=cena_08, justify=CENTER, width=14)
        entry_cena_08.insert(0, "30")
        entry_cena_08.grid(row=18, column=2)
    elif nazwa_08.get() == "Płytka PeekPower do osteotomii klinowej":
        entry_cena_08 = Entry(root, textvariable=cena_08, justify=CENTER, width=14)
        entry_cena_08.insert(0, "2160")
        entry_cena_08.grid(row=18, column=2)
    elif nazwa_08.get() == "Rękawice jałowe 6,5":
        entry_cena_08 = Entry(root, textvariable=cena_08, justify=CENTER, width=14)
        entry_cena_08.insert(0, "1.20")
        entry_cena_08.grid(row=18, column=2)
    elif nazwa_08.get() == "Rękawice jałowe 7,0":
        entry_cena_08 = Entry(root, textvariable=cena_08, justify=CENTER, width=14)
        entry_cena_08.insert(0, "1.20")
        entry_cena_08.grid(row=18, column=2)
    elif nazwa_08.get() == "Rękawice jałowe 7,5":
        entry_cena_08 = Entry(root, textvariable=cena_08, justify=CENTER, width=14)
        entry_cena_08.insert(0, "1.20")
        entry_cena_08.grid(row=18, column=2)
    elif nazwa_08.get() == "Rękawice jałowe 8,00":
        entry_cena_08 = Entry(root, textvariable=cena_08, justify=CENTER, width=14)
        entry_cena_08.insert(0, "1.20")
        entry_cena_08.grid(row=18, column=2)
    elif nazwa_08.get() == "Rękojeść Interpulse wysokoprzepływowa":
        entry_cena_08 = Entry(root, textvariable=cena_08, justify=CENTER, width=14)
        entry_cena_08.insert(0, "216")
        entry_cena_08.grid(row=18, column=2)
    elif nazwa_08.get() == "Serweta":
        entry_cena_08 = Entry(root, textvariable=cena_08, justify=CENTER, width=14)
        entry_cena_08.insert(0, "6")
        entry_cena_08.grid(row=18, column=2)
    elif nazwa_08.get() == "Simplex Hv z Gentamycyna 10x40g":
        entry_cena_08 = Entry(root, textvariable=cena_08, justify=CENTER, width=14)
        entry_cena_08.insert(0, "162")
        entry_cena_08.grid(row=18, column=2)
    elif nazwa_08.get() == "Skalpel 11":
        entry_cena_08 = Entry(root, textvariable=cena_08, justify=CENTER, width=14)
        entry_cena_08.insert(0, "0.38")
        entry_cena_08.grid(row=18, column=2)
    elif nazwa_08.get() == "Skalpel 13":
        entry_cena_08 = Entry(root, textvariable=cena_08, justify=CENTER, width=14)
        entry_cena_08.insert(0, "1")
        entry_cena_08.grid(row=18, column=2)
    elif nazwa_08.get() == "Skalpel 22":
        entry_cena_08 = Entry(root, textvariable=cena_08, justify=CENTER, width=14)
        entry_cena_08.insert(0, "00000")
        entry_cena_08.grid(row=18, column=2)
    elif nazwa_08.get() == "Śruba blokująca PeekPower do osteotomii":
        entry_cena_08 = Entry(root, textvariable=cena_08, justify=CENTER, width=14)
        entry_cena_08.insert(0, "194")
        entry_cena_08.grid(row=18, column=2)
    elif nazwa_08.get() == "System do mieszania próżniowego":
        entry_cena_08 = Entry(root, textvariable=cena_08, justify=CENTER, width=14)
        entry_cena_08.insert(0, "216")
        entry_cena_08.grid(row=18, column=2)
    elif nazwa_08.get() == "System wprowadzania implantów ACL TightRope":
        entry_cena_08 = Entry(root, textvariable=cena_08, justify=CENTER, width=14)
        entry_cena_08.insert(0, "702")
        entry_cena_08.grid(row=18, column=2)
    elif nazwa_08.get() == "Szew FiberWire 2":
        entry_cena_08 = Entry(root, textvariable=cena_08, justify=CENTER, width=14)
        entry_cena_08.insert(0, "86.40")
        entry_cena_08.grid(row=18, column=2)
    elif nazwa_08.get() == "Taśma przylepna 10x50":
        entry_cena_08 = Entry(root, textvariable=cena_08, justify=CENTER, width=14)
        entry_cena_08.insert(0, "1.04")
        entry_cena_08.grid(row=18, column=2)
    elif nazwa_08.get() == "Triathlon elem. udowy lewy":
        entry_cena_08 = Entry(root, textvariable=cena_08, justify=CENTER, width=14)
        entry_cena_08.insert(0, "3132")
        entry_cena_08.grid(row=18, column=2)
    elif nazwa_08.get() == "Triathlon PS wkładka x3-9mm #4":
        entry_cena_08 = Entry(root, textvariable=cena_08, justify=CENTER, width=14)
        entry_cena_08.insert(0, "756")
        entry_cena_08.grid(row=18, column=2)
    elif nazwa_08.get() == "Triathlon taca piszczelowa":
        entry_cena_08 = Entry(root, textvariable=cena_08, justify=CENTER, width=14)
        entry_cena_08.insert(0, "1296")
        entry_cena_08.grid(row=18, column=2)
    elif nazwa_08.get() == "Wkłady 3L z żelem":
        entry_cena_08 = Entry(root, textvariable=cena_08, justify=CENTER, width=14)
        entry_cena_08.insert(0, "10.26")
        entry_cena_08.grid(row=18, column=2)
    elif nazwa_08.get() == "Zestaw do artroskopii":
        entry_cena_08 = Entry(root, textvariable=cena_08, justify=CENTER, width=14)
        entry_cena_08.insert(0, "67")
        entry_cena_08.grid(row=18, column=2)
    elif nazwa_08.get() == "Zestaw do artroskopii barku":
        entry_cena_08 = Entry(root, textvariable=cena_08, justify=CENTER, width=14)
        entry_cena_08.insert(0, "108")
        entry_cena_08.grid(row=18, column=2)
    elif nazwa_08.get() == "Zestaw do drenażu":
        entry_cena_08 = Entry(root, textvariable=cena_08, justify=CENTER, width=14)
        entry_cena_08.insert(0, "14.23")
        entry_cena_08.grid(row=18, column=2)
    elif nazwa_08.get() == "Zestaw ortopedyczny":
        entry_cena_08 = Entry(root, textvariable=cena_08, justify=CENTER, width=14)
        entry_cena_08.insert(0, "28.08")
        entry_cena_08.grid(row=18, column=2)
    elif nazwa_08.get() == "Gaziki 20 x 10cm":
        entry_cena_08 = Entry(root, textvariable=cena_08, justify=CENTER, width=14)
        entry_cena_08.insert(0, "0.46")
        entry_cena_08.grid(row=18, column=2)
    else:
        entry_cena_08 = Entry(root, textvariable=cena_08, justify=CENTER, width=14, bg="#ffff00")
        entry_cena_08.insert(0, "0")
        entry_cena_08.grid(row=18, column=2)

    if nazwa_09.get() == "--puste--":
        entry_cena_09 = Entry(root, textvariable=cena_09, justify=CENTER, width=14)
        entry_cena_09.insert(0, "0")
        entry_cena_09.grid(row=19, column=2)
    elif nazwa_09.get() == "Ablator":
        entry_cena_09 = Entry(root, textvariable=cena_09, justify=CENTER, width=14)
        entry_cena_09.insert(0, "572")
        entry_cena_09.grid(row=19, column=2)
    elif nazwa_09.get() == "Anestezjolog":
        entry_cena_09 = Entry(root, textvariable=cena_09, justify=CENTER, width=14, bg="#ffff00")
        entry_cena_09.insert(0, "350")
        entry_cena_09.grid(row=19, column=2)
    elif nazwa_09.get() == "Butelka 400ml do długotrwałego odsysania ran j.u. sterylna":
        entry_cena_09 = Entry(root, textvariable=cena_09, justify=CENTER, width=14)
        entry_cena_09.insert(0, "4")
        entry_cena_09.grid(row=19, column=2)
    elif nazwa_09.get() == "Doba":
        entry_cena_09 = Entry(root, textvariable=cena_09, justify=CENTER, width=14)
        entry_cena_09.insert(0, "700")
        entry_cena_09.grid(row=19, column=2)
    elif nazwa_09.get() == "Dren łączący do ssaka Grena":
        entry_cena_09 = Entry(root, textvariable=cena_09, justify=CENTER, width=14)
        entry_cena_09.insert(0, "5")
        entry_cena_09.grid(row=19, column=2)
    elif nazwa_09.get() == "Dren Redona Ch 16 dł. 800mm z trokarem":
        entry_cena_09 = Entry(root, textvariable=cena_09, justify=CENTER, width=14)
        entry_cena_09.insert(0, "29.74")
        entry_cena_09.grid(row=19, column=2)
    elif nazwa_09.get() == "Dren do pompy Artrex":
        entry_cena_09 = Entry(root, textvariable=cena_09, justify=CENTER, width=14)
        entry_cena_09.insert(0, "108")
        entry_cena_09.grid(row=19, column=2)
    elif nazwa_09.get() == "Drut wiercący 2,4 x 311":
        entry_cena_09 = Entry(root, textvariable=cena_09, justify=CENTER, width=14)
        entry_cena_09.insert(0, "139.60")
        entry_cena_09.grid(row=19, column=2)
    elif nazwa_09.get() == "Fartuch jałowy L":
        entry_cena_09 = Entry(root, textvariable=cena_09, justify=CENTER, width=14)
        entry_cena_09.insert(0, "17")
        entry_cena_09.grid(row=19, column=2)
    elif nazwa_09.get() == "Fartuch jałowy M":
        entry_cena_09 = Entry(root, textvariable=cena_09, justify=CENTER, width=14)
        entry_cena_09.insert(0, "15.28")
        entry_cena_09.grid(row=19, column=2)
    elif nazwa_09.get() == "Fartuch jałowy XL":
        entry_cena_09 = Entry(root, textvariable=cena_09, justify=CENTER, width=14)
        entry_cena_09.insert(0, "20.84")
        entry_cena_09.grid(row=19, column=2)
    elif nazwa_09.get() == "FasatThread BioComposite Interference Screw 8x30":
        entry_cena_09 = Entry(root, textvariable=cena_09, justify=CENTER, width=14)
        entry_cena_09.insert(0, "594")
        entry_cena_09.grid(row=19, column=2)
    elif nazwa_09.get() == "Folia operacyjna, jałowa 45cm x 55cm":
        entry_cena_09 = Entry(root, textvariable=cena_09, justify=CENTER, width=14)
        entry_cena_09.insert(0, "9.99")
        entry_cena_09.grid(row=19, column=2)
    elif nazwa_09.get() == "Gaziki 10 x 10cm":
        entry_cena_09 = Entry(root, textvariable=cena_09, justify=CENTER, width=14)
        entry_cena_09.insert(0, "0.10")
        entry_cena_09.grid(row=19, column=2)
    elif nazwa_09.get() == "Igła 0,6 x 60":
        entry_cena_09 = Entry(root, textvariable=cena_09, justify=CENTER, width=14)
        entry_cena_09.insert(0, "0.09")
        entry_cena_09.grid(row=19, column=2)
    elif nazwa_09.get() == "Igła 0,7 x 40":
        entry_cena_09 = Entry(root, textvariable=cena_09, justify=CENTER, width=14)
        entry_cena_09.insert(0, "0.05")
        entry_cena_09.grid(row=19, column=2)
    elif nazwa_09.get() == "Igła 0,8 x 40":
        entry_cena_09 = Entry(root, textvariable=cena_09, justify=CENTER, width=14)
        entry_cena_09.insert(0, "0.05")
        entry_cena_09.grid(row=19, column=2)
    elif nazwa_09.get() == "Igła 1,1 x 70":
        entry_cena_09 = Entry(root, textvariable=cena_09, justify=CENTER, width=14)
        entry_cena_09.insert(0, "0.16")
        entry_cena_09.grid(row=19, column=2)
    elif nazwa_09.get() == "Kaniulowana śruba int. biokompozytowa z osłonką jednoraz.":
        entry_cena_09 = Entry(root, textvariable=cena_09, justify=CENTER, width=14)
        entry_cena_09.insert(0, "594")
        entry_cena_09.grid(row=19, column=2)
    elif nazwa_09.get() == "Kaniulowana śruba int. biokompozytowa z pełnym gwintem":
        entry_cena_09 = Entry(root, textvariable=cena_09, justify=CENTER, width=14)
        entry_cena_09.insert(0, "594")
        entry_cena_09.grid(row=19, column=2)
    elif nazwa_09.get() == "Końcówka do Shavera":
        entry_cena_09 = Entry(root, textvariable=cena_09, justify=CENTER, width=14)
        entry_cena_09.insert(0, "270")
        entry_cena_09.grid(row=19, column=2)
    elif nazwa_09.get() == "Kotwica biokompozytowa SwiveLock":
        entry_cena_09 = Entry(root, textvariable=cena_09, justify=CENTER, width=14)
        entry_cena_09.insert(0, "918")
        entry_cena_09.grid(row=19, column=2)
    elif nazwa_09.get() == "Kotwica Corkscrew":
        entry_cena_09 = Entry(root, textvariable=cena_09, justify=CENTER, width=14)
        entry_cena_09.insert(0, "604")
        entry_cena_09.grid(row=19, column=2)
    elif nazwa_09.get() == "Kotwica FASTak":
        entry_cena_09 = Entry(root, textvariable=cena_09, justify=CENTER, width=14)
        entry_cena_09.insert(0, "432")
        entry_cena_09.grid(row=19, column=2)
    elif nazwa_09.get() == "Kotwica PEEK SwiveLock":
        entry_cena_09 = Entry(root, textvariable=cena_09, justify=CENTER, width=14)
        entry_cena_09.insert(0, "885.60")
        entry_cena_09.grid(row=19, column=2)
    elif nazwa_09.get() == "NaCl 3000ml":
        entry_cena_09 = Entry(root, textvariable=cena_09, justify=CENTER, width=14)
        entry_cena_09.insert(0, "29.72")
        entry_cena_09.grid(row=19, column=2)
    elif nazwa_09.get() == "NaCl 5000ml":
        entry_cena_09 = Entry(root, textvariable=cena_09, justify=CENTER, width=14)
        entry_cena_09.insert(0, "58.33")
        entry_cena_09.grid(row=19, column=2)
    elif nazwa_09.get() == "Nici Dafilon 2-0":
        entry_cena_09 = Entry(root, textvariable=cena_09, justify=CENTER, width=14)
        entry_cena_09.insert(0, "6.60")
        entry_cena_09.grid(row=19, column=2)
    elif nazwa_09.get() == "Nici Novosyn 2":
        entry_cena_09 = Entry(root, textvariable=cena_09, justify=CENTER, width=14)
        entry_cena_09.insert(0, "13")
        entry_cena_09.grid(row=19, column=2)
    elif nazwa_09.get() == "Nici Novosyn 2-0":
        entry_cena_09 = Entry(root, textvariable=cena_09, justify=CENTER, width=14)
        entry_cena_09.insert(0, "7.70")
        entry_cena_09.grid(row=19, column=2)
    elif nazwa_09.get() == "Nici Novosyn 3-0":
        entry_cena_09 = Entry(root, textvariable=cena_09, justify=CENTER, width=14)
        entry_cena_09.insert(0, "7.70")
        entry_cena_09.grid(row=19, column=2)
    elif nazwa_09.get() == "Nici Nylon 2-0":
        entry_cena_09 = Entry(root, textvariable=cena_09, justify=CENTER, width=14)
        entry_cena_09.insert(0, "2.50")
        entry_cena_09.grid(row=19, column=2)
    elif nazwa_09.get() == "Nici Nylon 3-0":
        entry_cena_09 = Entry(root, textvariable=cena_09, justify=CENTER, width=14)
        entry_cena_09.insert(0, "2")
        entry_cena_09.grid(row=19, column=2)
    elif nazwa_09.get() == "Nici PGLA":
        entry_cena_09 = Entry(root, textvariable=cena_09, justify=CENTER, width=14)
        entry_cena_09.insert(0, "11.60")
        entry_cena_09.grid(row=19, column=2)
    elif nazwa_09.get() == "Nici PremiCron 3":
        entry_cena_09 = Entry(root, textvariable=cena_09, justify=CENTER, width=14)
        entry_cena_09.insert(0, "6.50")
        entry_cena_09.grid(row=19, column=2)
    elif nazwa_09.get() == "Nici Vicryl 4-0":
        entry_cena_09 = Entry(root, textvariable=cena_09, justify=CENTER, width=14)
        entry_cena_09.insert(0, "7.50")
        entry_cena_09.grid(row=19, column=2)
    elif nazwa_09.get() == "Nitinol Guide Pin 1.1":
        entry_cena_09 = Entry(root, textvariable=cena_09, justify=CENTER, width=14)
        entry_cena_09.insert(0, "145.80")
        entry_cena_09.grid(row=19, column=2)
    elif nazwa_09.get() == "Osłona na przewody":
        entry_cena_09 = Entry(root, textvariable=cena_09, justify=CENTER, width=14)
        entry_cena_09.insert(0, "2.50")
        entry_cena_09.grid(row=19, column=2)
    elif nazwa_09.get() == "Ostrze Arthrex 90(86)x19x1,27":
        entry_cena_09 = Entry(root, textvariable=cena_09, justify=CENTER, width=14)
        entry_cena_09.insert(0, "216")
        entry_cena_09.grid(row=19, column=2)
    elif nazwa_09.get() == "Ostrze piły":
        entry_cena_09 = Entry(root, textvariable=cena_09, justify=CENTER, width=14)
        entry_cena_09.insert(0, "108")
        entry_cena_09.grid(row=19, column=2)
    elif nazwa_09.get() == "Pielęgniarka anest.":
        entry_cena_09 = Entry(root, textvariable=cena_09, justify=CENTER, width=14)
        entry_cena_09.insert(0, "50")
        entry_cena_09.grid(row=19, column=2)
    elif nazwa_09.get() == "Pielęgniarka instr.":
        entry_cena_09 = Entry(root, textvariable=cena_09, justify=CENTER, width=14)
        entry_cena_09.insert(0, "50")
        entry_cena_09.grid(row=19, column=2)
    elif nazwa_09.get() == "Pielęgniarka 'Noviline'":
        entry_cena_09 = Entry(root, textvariable=cena_09, justify=CENTER, width=14)
        entry_cena_09.insert(0, "30")
        entry_cena_09.grid(row=19, column=2)
    elif nazwa_09.get() == "Płytka PeekPower do osteotomii klinowej":
        entry_cena_09 = Entry(root, textvariable=cena_09, justify=CENTER, width=14)
        entry_cena_09.insert(0, "2160")
        entry_cena_09.grid(row=19, column=2)
    elif nazwa_09.get() == "Rękawice jałowe 6,5":
        entry_cena_09 = Entry(root, textvariable=cena_09, justify=CENTER, width=14)
        entry_cena_09.insert(0, "1.20")
        entry_cena_09.grid(row=19, column=2)
    elif nazwa_09.get() == "Rękawice jałowe 7,0":
        entry_cena_09 = Entry(root, textvariable=cena_09, justify=CENTER, width=14)
        entry_cena_09.insert(0, "1.20")
        entry_cena_09.grid(row=19, column=2)
    elif nazwa_09.get() == "Rękawice jałowe 7,5":
        entry_cena_09 = Entry(root, textvariable=cena_09, justify=CENTER, width=14)
        entry_cena_09.insert(0, "1.20")
        entry_cena_09.grid(row=19, column=2)
    elif nazwa_09.get() == "Rękawice jałowe 8,00":
        entry_cena_09 = Entry(root, textvariable=cena_09, justify=CENTER, width=14)
        entry_cena_09.insert(0, "1.20")
        entry_cena_09.grid(row=19, column=2)
    elif nazwa_09.get() == "Rękojeść Interpulse wysokoprzepływowa":
        entry_cena_09 = Entry(root, textvariable=cena_09, justify=CENTER, width=14)
        entry_cena_09.insert(0, "216")
        entry_cena_09.grid(row=19, column=2)
    elif nazwa_09.get() == "Serweta":
        entry_cena_09 = Entry(root, textvariable=cena_09, justify=CENTER, width=14)
        entry_cena_09.insert(0, "6")
        entry_cena_09.grid(row=19, column=2)
    elif nazwa_09.get() == "Simplex Hv z Gentamycyna 10x40g":
        entry_cena_09 = Entry(root, textvariable=cena_09, justify=CENTER, width=14)
        entry_cena_09.insert(0, "162")
        entry_cena_09.grid(row=19, column=2)
    elif nazwa_09.get() == "Skalpel 11":
        entry_cena_09 = Entry(root, textvariable=cena_09, justify=CENTER, width=14)
        entry_cena_09.insert(0, "0.38")
        entry_cena_09.grid(row=19, column=2)
    elif nazwa_09.get() == "Skalpel 13":
        entry_cena_09 = Entry(root, textvariable=cena_09, justify=CENTER, width=14)
        entry_cena_09.insert(0, "1")
        entry_cena_09.grid(row=19, column=2)
    elif nazwa_09.get() == "Skalpel 22":
        entry_cena_09 = Entry(root, textvariable=cena_09, justify=CENTER, width=14)
        entry_cena_09.insert(0, "00000")
        entry_cena_09.grid(row=19, column=2)
    elif nazwa_09.get() == "Śruba blokująca PeekPower do osteotomii":
        entry_cena_09 = Entry(root, textvariable=cena_09, justify=CENTER, width=14)
        entry_cena_09.insert(0, "194")
        entry_cena_09.grid(row=19, column=2)
    elif nazwa_09.get() == "System do mieszania próżniowego":
        entry_cena_09 = Entry(root, textvariable=cena_09, justify=CENTER, width=14)
        entry_cena_09.insert(0, "216")
        entry_cena_09.grid(row=19, column=2)
    elif nazwa_09.get() == "System wprowadzania implantów ACL TightRope":
        entry_cena_09 = Entry(root, textvariable=cena_09, justify=CENTER, width=14)
        entry_cena_09.insert(0, "702")
        entry_cena_09.grid(row=19, column=2)
    elif nazwa_09.get() == "Szew FiberWire 2":
        entry_cena_09 = Entry(root, textvariable=cena_09, justify=CENTER, width=14)
        entry_cena_09.insert(0, "86.40")
        entry_cena_09.grid(row=19, column=2)
    elif nazwa_09.get() == "Taśma przylepna 10x50":
        entry_cena_09 = Entry(root, textvariable=cena_09, justify=CENTER, width=14)
        entry_cena_09.insert(0, "1.04")
        entry_cena_09.grid(row=19, column=2)
    elif nazwa_09.get() == "Triathlon elem. udowy lewy":
        entry_cena_09 = Entry(root, textvariable=cena_09, justify=CENTER, width=14)
        entry_cena_09.insert(0, "3132")
        entry_cena_09.grid(row=19, column=2)
    elif nazwa_09.get() == "Triathlon PS wkładka x3-9mm #4":
        entry_cena_09 = Entry(root, textvariable=cena_09, justify=CENTER, width=14)
        entry_cena_09.insert(0, "756")
        entry_cena_09.grid(row=19, column=2)
    elif nazwa_09.get() == "Triathlon taca piszczelowa":
        entry_cena_09 = Entry(root, textvariable=cena_09, justify=CENTER, width=14)
        entry_cena_09.insert(0, "1296")
        entry_cena_09.grid(row=19, column=2)
    elif nazwa_09.get() == "Wkłady 3L z żelem":
        entry_cena_09 = Entry(root, textvariable=cena_09, justify=CENTER, width=14)
        entry_cena_09.insert(0, "10.26")
        entry_cena_09.grid(row=19, column=2)
    elif nazwa_09.get() == "Zestaw do artroskopii":
        entry_cena_09 = Entry(root, textvariable=cena_09, justify=CENTER, width=14)
        entry_cena_09.insert(0, "67")
        entry_cena_09.grid(row=19, column=2)
    elif nazwa_09.get() == "Zestaw do artroskopii barku":
        entry_cena_09 = Entry(root, textvariable=cena_09, justify=CENTER, width=14)
        entry_cena_09.insert(0, "108")
        entry_cena_09.grid(row=19, column=2)
    elif nazwa_09.get() == "Zestaw do drenażu":
        entry_cena_09 = Entry(root, textvariable=cena_09, justify=CENTER, width=14)
        entry_cena_09.insert(0, "14.23")
        entry_cena_09.grid(row=19, column=2)
    elif nazwa_09.get() == "Zestaw ortopedyczny":
        entry_cena_09 = Entry(root, textvariable=cena_09, justify=CENTER, width=14)
        entry_cena_09.insert(0, "28.08")
        entry_cena_09.grid(row=19, column=2)
    elif nazwa_09.get() == "Gaziki 20 x 10cm":
        entry_cena_09 = Entry(root, textvariable=cena_09, justify=CENTER, width=14)
        entry_cena_09.insert(0, "0.46")
        entry_cena_09.grid(row=19, column=2)
    else:
        entry_cena_09 = Entry(root, textvariable=cena_09, justify=CENTER, width=14, bg="#ffff00")
        entry_cena_09.insert(0, "0")
        entry_cena_09.grid(row=19, column=2)

    if nazwa_10.get() == "--puste--":
        entry_cena_10 = Entry(root, textvariable=cena_10, justify=CENTER, width=14)
        entry_cena_10.insert(0, "0")
        entry_cena_10.grid(row=20, column=2)
    elif nazwa_10.get() == "Ablator":
        entry_cena_10 = Entry(root, textvariable=cena_10, justify=CENTER, width=14)
        entry_cena_10.insert(0, "572")
        entry_cena_10.grid(row=20, column=2)
    elif nazwa_10.get() == "Anestezjolog":
        entry_cena_10 = Entry(root, textvariable=cena_10, justify=CENTER, width=14, bg="#ffff00")
        entry_cena_10.insert(0, "350")
        entry_cena_10.grid(row=20, column=2)
    elif nazwa_10.get() == "Butelka 400ml do długotrwałego odsysania ran j.u. sterylna":
        entry_cena_10 = Entry(root, textvariable=cena_10, justify=CENTER, width=14)
        entry_cena_10.insert(0, "4")
        entry_cena_10.grid(row=20, column=2)
    elif nazwa_10.get() == "Doba":
        entry_cena_10 = Entry(root, textvariable=cena_10, justify=CENTER, width=14)
        entry_cena_10.insert(0, "700")
        entry_cena_10.grid(row=20, column=2)
    elif nazwa_10.get() == "Dren łączący do ssaka Grena":
        entry_cena_10 = Entry(root, textvariable=cena_10, justify=CENTER, width=14)
        entry_cena_10.insert(0, "5")
        entry_cena_10.grid(row=20, column=2)
    elif nazwa_10.get() == "Dren Redona Ch 16 dł. 800mm z trokarem":
        entry_cena_10 = Entry(root, textvariable=cena_10, justify=CENTER, width=14)
        entry_cena_10.insert(0, "29.74")
        entry_cena_10.grid(row=20, column=2)
    elif nazwa_10.get() == "Dren do pompy Artrex":
        entry_cena_10 = Entry(root, textvariable=cena_10, justify=CENTER, width=14)
        entry_cena_10.insert(0, "108")
        entry_cena_10.grid(row=20, column=2)
    elif nazwa_10.get() == "Drut wiercący 2,4 x 311":
        entry_cena_10 = Entry(root, textvariable=cena_10, justify=CENTER, width=14)
        entry_cena_10.insert(0, "139.60")
        entry_cena_10.grid(row=20, column=2)
    elif nazwa_10.get() == "Fartuch jałowy L":
        entry_cena_10 = Entry(root, textvariable=cena_10, justify=CENTER, width=14)
        entry_cena_10.insert(0, "17")
        entry_cena_10.grid(row=20, column=2)
    elif nazwa_10.get() == "Fartuch jałowy M":
        entry_cena_10 = Entry(root, textvariable=cena_10, justify=CENTER, width=14)
        entry_cena_10.insert(0, "15.28")
        entry_cena_10.grid(row=20, column=2)
    elif nazwa_10.get() == "Fartuch jałowy XL":
        entry_cena_10 = Entry(root, textvariable=cena_10, justify=CENTER, width=14)
        entry_cena_10.insert(0, "20.84")
        entry_cena_10.grid(row=20, column=2)
    elif nazwa_10.get() == "FasatThread BioComposite Interference Screw 8x30":
        entry_cena_10 = Entry(root, textvariable=cena_10, justify=CENTER, width=14)
        entry_cena_10.insert(0, "594")
        entry_cena_10.grid(row=20, column=2)
    elif nazwa_10.get() == "Folia operacyjna, jałowa 45cm x 55cm":
        entry_cena_10 = Entry(root, textvariable=cena_10, justify=CENTER, width=14)
        entry_cena_10.insert(0, "9.99")
        entry_cena_10.grid(row=20, column=2)
    elif nazwa_10.get() == "Gaziki 10 x 10cm":
        entry_cena_10 = Entry(root, textvariable=cena_10, justify=CENTER, width=14)
        entry_cena_10.insert(0, "0.10")
        entry_cena_10.grid(row=20, column=2)
    elif nazwa_10.get() == "Igła 0,6 x 60":
        entry_cena_10 = Entry(root, textvariable=cena_10, justify=CENTER, width=14)
        entry_cena_10.insert(0, "0.09")
        entry_cena_10.grid(row=20, column=2)
    elif nazwa_10.get() == "Igła 0,7 x 40":
        entry_cena_10 = Entry(root, textvariable=cena_10, justify=CENTER, width=14)
        entry_cena_10.insert(0, "0.05")
        entry_cena_10.grid(row=20, column=2)
    elif nazwa_10.get() == "Igła 0,8 x 40":
        entry_cena_10 = Entry(root, textvariable=cena_10, justify=CENTER, width=14)
        entry_cena_10.insert(0, "0.05")
        entry_cena_10.grid(row=20, column=2)
    elif nazwa_10.get() == "Igła 1,1 x 70":
        entry_cena_10 = Entry(root, textvariable=cena_10, justify=CENTER, width=14)
        entry_cena_10.insert(0, "0.16")
        entry_cena_10.grid(row=20, column=2)
    elif nazwa_10.get() == "Kaniulowana śruba int. biokompozytowa z osłonką jednoraz.":
        entry_cena_10 = Entry(root, textvariable=cena_10, justify=CENTER, width=14)
        entry_cena_10.insert(0, "594")
        entry_cena_10.grid(row=20, column=2)
    elif nazwa_10.get() == "Kaniulowana śruba int. biokompozytowa z pełnym gwintem":
        entry_cena_10 = Entry(root, textvariable=cena_10, justify=CENTER, width=14)
        entry_cena_10.insert(0, "594")
        entry_cena_10.grid(row=20, column=2)
    elif nazwa_10.get() == "Końcówka do Shavera":
        entry_cena_10 = Entry(root, textvariable=cena_10, justify=CENTER, width=14)
        entry_cena_10.insert(0, "270")
        entry_cena_10.grid(row=20, column=2)
    elif nazwa_10.get() == "Kotwica biokompozytowa SwiveLock":
        entry_cena_10 = Entry(root, textvariable=cena_10, justify=CENTER, width=14)
        entry_cena_10.insert(0, "918")
        entry_cena_10.grid(row=20, column=2)
    elif nazwa_10.get() == "Kotwica Corkscrew":
        entry_cena_10 = Entry(root, textvariable=cena_10, justify=CENTER, width=14)
        entry_cena_10.insert(0, "604")
        entry_cena_10.grid(row=20, column=2)
    elif nazwa_10.get() == "Kotwica FASTak":
        entry_cena_10 = Entry(root, textvariable=cena_10, justify=CENTER, width=14)
        entry_cena_10.insert(0, "432")
        entry_cena_10.grid(row=20, column=2)
    elif nazwa_10.get() == "Kotwica PEEK SwiveLock":
        entry_cena_10 = Entry(root, textvariable=cena_10, justify=CENTER, width=14)
        entry_cena_10.insert(0, "885.60")
        entry_cena_10.grid(row=20, column=2)
    elif nazwa_10.get() == "NaCl 3000ml":
        entry_cena_10 = Entry(root, textvariable=cena_10, justify=CENTER, width=14)
        entry_cena_10.insert(0, "29.72")
        entry_cena_10.grid(row=20, column=2)
    elif nazwa_10.get() == "NaCl 5000ml":
        entry_cena_10 = Entry(root, textvariable=cena_10, justify=CENTER, width=14)
        entry_cena_10.insert(0, "58.33")
        entry_cena_10.grid(row=20, column=2)
    elif nazwa_10.get() == "Nici Dafilon 2-0":
        entry_cena_10 = Entry(root, textvariable=cena_10, justify=CENTER, width=14)
        entry_cena_10.insert(0, "6.60")
        entry_cena_10.grid(row=20, column=2)
    elif nazwa_10.get() == "Nici Novosyn 2":
        entry_cena_10 = Entry(root, textvariable=cena_10, justify=CENTER, width=14)
        entry_cena_10.insert(0, "13")
        entry_cena_10.grid(row=20, column=2)
    elif nazwa_10.get() == "Nici Novosyn 2-0":
        entry_cena_10 = Entry(root, textvariable=cena_10, justify=CENTER, width=14)
        entry_cena_10.insert(0, "7.70")
        entry_cena_10.grid(row=20, column=2)
    elif nazwa_10.get() == "Nici Novosyn 3-0":
        entry_cena_10 = Entry(root, textvariable=cena_10, justify=CENTER, width=14)
        entry_cena_10.insert(0, "7.70")
        entry_cena_10.grid(row=20, column=2)
    elif nazwa_10.get() == "Nici Nylon 2-0":
        entry_cena_10 = Entry(root, textvariable=cena_10, justify=CENTER, width=14)
        entry_cena_10.insert(0, "2.50")
        entry_cena_10.grid(row=20, column=2)
    elif nazwa_10.get() == "Nici Nylon 3-0":
        entry_cena_10 = Entry(root, textvariable=cena_10, justify=CENTER, width=14)
        entry_cena_10.insert(0, "2")
        entry_cena_10.grid(row=20, column=2)
    elif nazwa_10.get() == "Nici PGLA":
        entry_cena_10 = Entry(root, textvariable=cena_10, justify=CENTER, width=14)
        entry_cena_10.insert(0, "11.60")
        entry_cena_10.grid(row=20, column=2)
    elif nazwa_10.get() == "Nici PremiCron 3":
        entry_cena_10 = Entry(root, textvariable=cena_10, justify=CENTER, width=14)
        entry_cena_10.insert(0, "6.50")
        entry_cena_10.grid(row=20, column=2)
    elif nazwa_10.get() == "Nici Vicryl 4-0":
        entry_cena_10 = Entry(root, textvariable=cena_10, justify=CENTER, width=14)
        entry_cena_10.insert(0, "7.50")
        entry_cena_10.grid(row=20, column=2)
    elif nazwa_10.get() == "Nitinol Guide Pin 1.1":
        entry_cena_10 = Entry(root, textvariable=cena_10, justify=CENTER, width=14)
        entry_cena_10.insert(0, "145.80")
        entry_cena_10.grid(row=20, column=2)
    elif nazwa_10.get() == "Osłona na przewody":
        entry_cena_10 = Entry(root, textvariable=cena_10, justify=CENTER, width=14)
        entry_cena_10.insert(0, "2.50")
        entry_cena_10.grid(row=20, column=2)
    elif nazwa_10.get() == "Ostrze Arthrex 90(86)x19x1,27":
        entry_cena_10 = Entry(root, textvariable=cena_10, justify=CENTER, width=14)
        entry_cena_10.insert(0, "216")
        entry_cena_10.grid(row=20, column=2)
    elif nazwa_10.get() == "Ostrze piły":
        entry_cena_10 = Entry(root, textvariable=cena_10, justify=CENTER, width=14)
        entry_cena_10.insert(0, "108")
        entry_cena_10.grid(row=20, column=2)
    elif nazwa_10.get() == "Pielęgniarka anest.":
        entry_cena_10 = Entry(root, textvariable=cena_10, justify=CENTER, width=14)
        entry_cena_10.insert(0, "50")
        entry_cena_10.grid(row=20, column=2)
    elif nazwa_10.get() == "Pielęgniarka instr.":
        entry_cena_10 = Entry(root, textvariable=cena_10, justify=CENTER, width=14)
        entry_cena_10.insert(0, "50")
        entry_cena_10.grid(row=20, column=2)
    elif nazwa_10.get() == "Pielęgniarka 'Noviline'":
        entry_cena_10 = Entry(root, textvariable=cena_10, justify=CENTER, width=14)
        entry_cena_10.insert(0, "30")
        entry_cena_10.grid(row=20, column=2)
    elif nazwa_10.get() == "Płytka PeekPower do osteotomii klinowej":
        entry_cena_10 = Entry(root, textvariable=cena_10, justify=CENTER, width=14)
        entry_cena_10.insert(0, "2160")
        entry_cena_10.grid(row=20, column=2)
    elif nazwa_10.get() == "Rękawice jałowe 6,5":
        entry_cena_10 = Entry(root, textvariable=cena_10, justify=CENTER, width=14)
        entry_cena_10.insert(0, "1.20")
        entry_cena_10.grid(row=20, column=2)
    elif nazwa_10.get() == "Rękawice jałowe 7,0":
        entry_cena_10 = Entry(root, textvariable=cena_10, justify=CENTER, width=14)
        entry_cena_10.insert(0, "1.20")
        entry_cena_10.grid(row=20, column=2)
    elif nazwa_10.get() == "Rękawice jałowe 7,5":
        entry_cena_10 = Entry(root, textvariable=cena_10, justify=CENTER, width=14)
        entry_cena_10.insert(0, "1.20")
        entry_cena_10.grid(row=20, column=2)
    elif nazwa_10.get() == "Rękawice jałowe 8,00":
        entry_cena_10 = Entry(root, textvariable=cena_10, justify=CENTER, width=14)
        entry_cena_10.insert(0, "1.20")
        entry_cena_10.grid(row=20, column=2)
    elif nazwa_10.get() == "Rękojeść Interpulse wysokoprzepływowa":
        entry_cena_10 = Entry(root, textvariable=cena_10, justify=CENTER, width=14)
        entry_cena_10.insert(0, "216")
        entry_cena_10.grid(row=20, column=2)
    elif nazwa_10.get() == "Serweta":
        entry_cena_10 = Entry(root, textvariable=cena_10, justify=CENTER, width=14)
        entry_cena_10.insert(0, "6")
        entry_cena_10.grid(row=20, column=2)
    elif nazwa_10.get() == "Simplex Hv z Gentamycyna 10x40g":
        entry_cena_10 = Entry(root, textvariable=cena_10, justify=CENTER, width=14)
        entry_cena_10.insert(0, "162")
        entry_cena_10.grid(row=20, column=2)
    elif nazwa_10.get() == "Skalpel 11":
        entry_cena_10 = Entry(root, textvariable=cena_10, justify=CENTER, width=14)
        entry_cena_10.insert(0, "0.38")
        entry_cena_10.grid(row=20, column=2)
    elif nazwa_10.get() == "Skalpel 13":
        entry_cena_10 = Entry(root, textvariable=cena_10, justify=CENTER, width=14)
        entry_cena_10.insert(0, "1")
        entry_cena_10.grid(row=20, column=2)
    elif nazwa_10.get() == "Skalpel 22":
        entry_cena_10 = Entry(root, textvariable=cena_10, justify=CENTER, width=14)
        entry_cena_10.insert(0, "00000")
        entry_cena_10.grid(row=20, column=2)
    elif nazwa_10.get() == "Śruba blokująca PeekPower do osteotomii":
        entry_cena_10 = Entry(root, textvariable=cena_10, justify=CENTER, width=14)
        entry_cena_10.insert(0, "194")
        entry_cena_10.grid(row=20, column=2)
    elif nazwa_10.get() == "System do mieszania próżniowego":
        entry_cena_10 = Entry(root, textvariable=cena_10, justify=CENTER, width=14)
        entry_cena_10.insert(0, "216")
        entry_cena_10.grid(row=20, column=2)
    elif nazwa_10.get() == "System wprowadzania implantów ACL TightRope":
        entry_cena_10 = Entry(root, textvariable=cena_10, justify=CENTER, width=14)
        entry_cena_10.insert(0, "702")
        entry_cena_10.grid(row=20, column=2)
    elif nazwa_10.get() == "Szew FiberWire 2":
        entry_cena_10 = Entry(root, textvariable=cena_10, justify=CENTER, width=14)
        entry_cena_10.insert(0, "86.40")
        entry_cena_10.grid(row=20, column=2)
    elif nazwa_10.get() == "Taśma przylepna 10x50":
        entry_cena_10 = Entry(root, textvariable=cena_10, justify=CENTER, width=14)
        entry_cena_10.insert(0, "1.04")
        entry_cena_10.grid(row=20, column=2)
    elif nazwa_10.get() == "Triathlon elem. udowy lewy":
        entry_cena_10 = Entry(root, textvariable=cena_10, justify=CENTER, width=14)
        entry_cena_10.insert(0, "3132")
        entry_cena_10.grid(row=20, column=2)
    elif nazwa_10.get() == "Triathlon PS wkładka x3-9mm #4":
        entry_cena_10 = Entry(root, textvariable=cena_10, justify=CENTER, width=14)
        entry_cena_10.insert(0, "756")
        entry_cena_10.grid(row=20, column=2)
    elif nazwa_10.get() == "Triathlon taca piszczelowa":
        entry_cena_10 = Entry(root, textvariable=cena_10, justify=CENTER, width=14)
        entry_cena_10.insert(0, "1296")
        entry_cena_10.grid(row=20, column=2)
    elif nazwa_10.get() == "Wkłady 3L z żelem":
        entry_cena_10 = Entry(root, textvariable=cena_10, justify=CENTER, width=14)
        entry_cena_10.insert(0, "10.26")
        entry_cena_10.grid(row=20, column=2)
    elif nazwa_10.get() == "Zestaw do artroskopii":
        entry_cena_10 = Entry(root, textvariable=cena_10, justify=CENTER, width=14)
        entry_cena_10.insert(0, "67")
        entry_cena_10.grid(row=20, column=2)
    elif nazwa_10.get() == "Zestaw do artroskopii barku":
        entry_cena_10 = Entry(root, textvariable=cena_10, justify=CENTER, width=14)
        entry_cena_10.insert(0, "108")
        entry_cena_10.grid(row=20, column=2)
    elif nazwa_10.get() == "Zestaw do drenażu":
        entry_cena_10 = Entry(root, textvariable=cena_10, justify=CENTER, width=14)
        entry_cena_10.insert(0, "14.23")
        entry_cena_10.grid(row=20, column=2)
    elif nazwa_10.get() == "Zestaw ortopedyczny":
        entry_cena_10 = Entry(root, textvariable=cena_10, justify=CENTER, width=14)
        entry_cena_10.insert(0, "28.08")
        entry_cena_10.grid(row=20, column=2)
    elif nazwa_10.get() == "Gaziki 20 x 10cm":
        entry_cena_10 = Entry(root, textvariable=cena_10, justify=CENTER, width=14)
        entry_cena_10.insert(0, "0.46")
        entry_cena_10.grid(row=20, column=2)
    else:
        entry_cena_10 = Entry(root, textvariable=cena_10, justify=CENTER, width=14, bg="#ffff00")
        entry_cena_10.insert(0, "0")
        entry_cena_10.grid(row=20, column=2)

    if nazwa_11.get() == "--puste--":
        entry_cena_11 = Entry(root, textvariable=cena_11, justify=CENTER, width=14)
        entry_cena_11.insert(0, "0")
        entry_cena_11.grid(row=21, column=2)
    elif nazwa_11.get() == "Ablator":
        entry_cena_11 = Entry(root, textvariable=cena_11, justify=CENTER, width=14)
        entry_cena_11.insert(0, "572")
        entry_cena_11.grid(row=21, column=2)
    elif nazwa_11.get() == "Anestezjolog":
        entry_cena_11 = Entry(root, textvariable=cena_11, justify=CENTER, width=14, bg="#ffff00")
        entry_cena_11.insert(0, "350")
        entry_cena_11.grid(row=21, column=2)
    elif nazwa_11.get() == "Butelka 400ml do długotrwałego odsysania ran j.u. sterylna":
        entry_cena_11 = Entry(root, textvariable=cena_11, justify=CENTER, width=14)
        entry_cena_11.insert(0, "4")
        entry_cena_11.grid(row=21, column=2)
    elif nazwa_11.get() == "Doba":
        entry_cena_11 = Entry(root, textvariable=cena_11, justify=CENTER, width=14)
        entry_cena_11.insert(0, "700")
        entry_cena_11.grid(row=21, column=2)
    elif nazwa_11.get() == "Dren łączący do ssaka Grena":
        entry_cena_11 = Entry(root, textvariable=cena_11, justify=CENTER, width=14)
        entry_cena_11.insert(0, "5")
        entry_cena_11.grid(row=21, column=2)
    elif nazwa_11.get() == "Dren Redona Ch 16 dł. 800mm z trokarem":
        entry_cena_11 = Entry(root, textvariable=cena_11, justify=CENTER, width=14)
        entry_cena_11.insert(0, "29.74")
        entry_cena_11.grid(row=21, column=2)
    elif nazwa_11.get() == "Dren do pompy Artrex":
        entry_cena_11 = Entry(root, textvariable=cena_11, justify=CENTER, width=14)
        entry_cena_11.insert(0, "108")
        entry_cena_11.grid(row=21, column=2)
    elif nazwa_11.get() == "Drut wiercący 2,4 x 311":
        entry_cena_11 = Entry(root, textvariable=cena_11, justify=CENTER, width=14)
        entry_cena_11.insert(0, "139.60")
        entry_cena_11.grid(row=21, column=2)
    elif nazwa_11.get() == "Fartuch jałowy L":
        entry_cena_11 = Entry(root, textvariable=cena_11, justify=CENTER, width=14)
        entry_cena_11.insert(0, "17")
        entry_cena_11.grid(row=21, column=2)
    elif nazwa_11.get() == "Fartuch jałowy M":
        entry_cena_11 = Entry(root, textvariable=cena_11, justify=CENTER, width=14)
        entry_cena_11.insert(0, "15.28")
        entry_cena_11.grid(row=21, column=2)
    elif nazwa_11.get() == "Fartuch jałowy XL":
        entry_cena_11 = Entry(root, textvariable=cena_11, justify=CENTER, width=14)
        entry_cena_11.insert(0, "20.84")
        entry_cena_11.grid(row=21, column=2)
    elif nazwa_11.get() == "FasatThread BioComposite Interference Screw 8x30":
        entry_cena_11 = Entry(root, textvariable=cena_11, justify=CENTER, width=14)
        entry_cena_11.insert(0, "594")
        entry_cena_11.grid(row=21, column=2)
    elif nazwa_11.get() == "Folia operacyjna, jałowa 45cm x 55cm":
        entry_cena_11 = Entry(root, textvariable=cena_11, justify=CENTER, width=14)
        entry_cena_11.insert(0, "9.99")
        entry_cena_11.grid(row=21, column=2)
    elif nazwa_11.get() == "Gaziki 10 x 10cm":
        entry_cena_11 = Entry(root, textvariable=cena_11, justify=CENTER, width=14)
        entry_cena_11.insert(0, "0.10")
        entry_cena_11.grid(row=21, column=2)
    elif nazwa_11.get() == "Igła 0,6 x 60":
        entry_cena_11 = Entry(root, textvariable=cena_11, justify=CENTER, width=14)
        entry_cena_11.insert(0, "0.09")
        entry_cena_11.grid(row=21, column=2)
    elif nazwa_11.get() == "Igła 0,7 x 40":
        entry_cena_11 = Entry(root, textvariable=cena_11, justify=CENTER, width=14)
        entry_cena_11.insert(0, "0.05")
        entry_cena_11.grid(row=21, column=2)
    elif nazwa_11.get() == "Igła 0,8 x 40":
        entry_cena_11 = Entry(root, textvariable=cena_11, justify=CENTER, width=14)
        entry_cena_11.insert(0, "0.05")
        entry_cena_11.grid(row=21, column=2)
    elif nazwa_11.get() == "Igła 1,1 x 70":
        entry_cena_11 = Entry(root, textvariable=cena_11, justify=CENTER, width=14)
        entry_cena_11.insert(0, "0.16")
        entry_cena_11.grid(row=21, column=2)
    elif nazwa_11.get() == "Kaniulowana śruba int. biokompozytowa z osłonką jednoraz.":
        entry_cena_11 = Entry(root, textvariable=cena_11, justify=CENTER, width=14)
        entry_cena_11.insert(0, "594")
        entry_cena_11.grid(row=21, column=2)
    elif nazwa_11.get() == "Kaniulowana śruba int. biokompozytowa z pełnym gwintem":
        entry_cena_11 = Entry(root, textvariable=cena_11, justify=CENTER, width=14)
        entry_cena_11.insert(0, "594")
        entry_cena_11.grid(row=21, column=2)
    elif nazwa_11.get() == "Końcówka do Shavera":
        entry_cena_11 = Entry(root, textvariable=cena_11, justify=CENTER, width=14)
        entry_cena_11.insert(0, "270")
        entry_cena_11.grid(row=21, column=2)
    elif nazwa_11.get() == "Kotwica biokompozytowa SwiveLock":
        entry_cena_11 = Entry(root, textvariable=cena_11, justify=CENTER, width=14)
        entry_cena_11.insert(0, "918")
        entry_cena_11.grid(row=21, column=2)
    elif nazwa_11.get() == "Kotwica Corkscrew":
        entry_cena_11 = Entry(root, textvariable=cena_11, justify=CENTER, width=14)
        entry_cena_11.insert(0, "604")
        entry_cena_11.grid(row=21, column=2)
    elif nazwa_11.get() == "Kotwica FASTak":
        entry_cena_11 = Entry(root, textvariable=cena_11, justify=CENTER, width=14)
        entry_cena_11.insert(0, "432")
        entry_cena_11.grid(row=21, column=2)
    elif nazwa_11.get() == "Kotwica PEEK SwiveLock":
        entry_cena_11 = Entry(root, textvariable=cena_11, justify=CENTER, width=14)
        entry_cena_11.insert(0, "885.60")
        entry_cena_11.grid(row=21, column=2)
    elif nazwa_11.get() == "NaCl 3000ml":
        entry_cena_11 = Entry(root, textvariable=cena_11, justify=CENTER, width=14)
        entry_cena_11.insert(0, "29.72")
        entry_cena_11.grid(row=21, column=2)
    elif nazwa_11.get() == "NaCl 5000ml":
        entry_cena_11 = Entry(root, textvariable=cena_11, justify=CENTER, width=14)
        entry_cena_11.insert(0, "58.33")
        entry_cena_11.grid(row=21, column=2)
    elif nazwa_11.get() == "Nici Dafilon 2-0":
        entry_cena_11 = Entry(root, textvariable=cena_11, justify=CENTER, width=14)
        entry_cena_11.insert(0, "6.60")
        entry_cena_11.grid(row=21, column=2)
    elif nazwa_11.get() == "Nici Novosyn 2":
        entry_cena_11 = Entry(root, textvariable=cena_11, justify=CENTER, width=14)
        entry_cena_11.insert(0, "13")
        entry_cena_11.grid(row=21, column=2)
    elif nazwa_11.get() == "Nici Novosyn 2-0":
        entry_cena_11 = Entry(root, textvariable=cena_11, justify=CENTER, width=14)
        entry_cena_11.insert(0, "7.70")
        entry_cena_11.grid(row=21, column=2)
    elif nazwa_11.get() == "Nici Novosyn 3-0":
        entry_cena_11 = Entry(root, textvariable=cena_11, justify=CENTER, width=14)
        entry_cena_11.insert(0, "7.70")
        entry_cena_11.grid(row=21, column=2)
    elif nazwa_11.get() == "Nici Nylon 2-0":
        entry_cena_11 = Entry(root, textvariable=cena_11, justify=CENTER, width=14)
        entry_cena_11.insert(0, "2.50")
        entry_cena_11.grid(row=21, column=2)
    elif nazwa_11.get() == "Nici Nylon 3-0":
        entry_cena_11 = Entry(root, textvariable=cena_11, justify=CENTER, width=14)
        entry_cena_11.insert(0, "2")
        entry_cena_11.grid(row=21, column=2)
    elif nazwa_11.get() == "Nici PGLA":
        entry_cena_11 = Entry(root, textvariable=cena_11, justify=CENTER, width=14)
        entry_cena_11.insert(0, "11.60")
        entry_cena_11.grid(row=21, column=2)
    elif nazwa_11.get() == "Nici PremiCron 3":
        entry_cena_11 = Entry(root, textvariable=cena_11, justify=CENTER, width=14)
        entry_cena_11.insert(0, "6.50")
        entry_cena_11.grid(row=21, column=2)
    elif nazwa_11.get() == "Nici Vicryl 4-0":
        entry_cena_11 = Entry(root, textvariable=cena_11, justify=CENTER, width=14)
        entry_cena_11.insert(0, "7.50")
        entry_cena_11.grid(row=21, column=2)
    elif nazwa_11.get() == "Nitinol Guide Pin 1.1":
        entry_cena_11 = Entry(root, textvariable=cena_11, justify=CENTER, width=14)
        entry_cena_11.insert(0, "145.80")
        entry_cena_11.grid(row=21, column=2)
    elif nazwa_11.get() == "Osłona na przewody":
        entry_cena_11 = Entry(root, textvariable=cena_11, justify=CENTER, width=14)
        entry_cena_11.insert(0, "2.50")
        entry_cena_11.grid(row=21, column=2)
    elif nazwa_11.get() == "Ostrze Arthrex 90(86)x19x1,27":
        entry_cena_11 = Entry(root, textvariable=cena_11, justify=CENTER, width=14)
        entry_cena_11.insert(0, "216")
        entry_cena_11.grid(row=21, column=2)
    elif nazwa_11.get() == "Ostrze piły":
        entry_cena_11 = Entry(root, textvariable=cena_11, justify=CENTER, width=14)
        entry_cena_11.insert(0, "108")
        entry_cena_11.grid(row=21, column=2)
    elif nazwa_11.get() == "Pielęgniarka anest.":
        entry_cena_11 = Entry(root, textvariable=cena_11, justify=CENTER, width=14)
        entry_cena_11.insert(0, "50")
        entry_cena_11.grid(row=21, column=2)
    elif nazwa_11.get() == "Pielęgniarka instr.":
        entry_cena_11 = Entry(root, textvariable=cena_11, justify=CENTER, width=14)
        entry_cena_11.insert(0, "50")
        entry_cena_11.grid(row=21, column=2)
    elif nazwa_11.get() == "Pielęgniarka 'Noviline'":
        entry_cena_11 = Entry(root, textvariable=cena_11, justify=CENTER, width=14)
        entry_cena_11.insert(0, "30")
        entry_cena_11.grid(row=21, column=2)
    elif nazwa_11.get() == "Płytka PeekPower do osteotomii klinowej":
        entry_cena_11 = Entry(root, textvariable=cena_11, justify=CENTER, width=14)
        entry_cena_11.insert(0, "2160")
        entry_cena_11.grid(row=21, column=2)
    elif nazwa_11.get() == "Rękawice jałowe 6,5":
        entry_cena_11 = Entry(root, textvariable=cena_11, justify=CENTER, width=14)
        entry_cena_11.insert(0, "1.20")
        entry_cena_11.grid(row=21, column=2)
    elif nazwa_11.get() == "Rękawice jałowe 7,0":
        entry_cena_11 = Entry(root, textvariable=cena_11, justify=CENTER, width=14)
        entry_cena_11.insert(0, "1.20")
        entry_cena_11.grid(row=21, column=2)
    elif nazwa_11.get() == "Rękawice jałowe 7,5":
        entry_cena_11 = Entry(root, textvariable=cena_11, justify=CENTER, width=14)
        entry_cena_11.insert(0, "1.20")
        entry_cena_11.grid(row=21, column=2)
    elif nazwa_11.get() == "Rękawice jałowe 8,00":
        entry_cena_11 = Entry(root, textvariable=cena_11, justify=CENTER, width=14)
        entry_cena_11.insert(0, "1.20")
        entry_cena_11.grid(row=21, column=2)
    elif nazwa_11.get() == "Rękojeść Interpulse wysokoprzepływowa":
        entry_cena_11 = Entry(root, textvariable=cena_11, justify=CENTER, width=14)
        entry_cena_11.insert(0, "216")
        entry_cena_11.grid(row=21, column=2)
    elif nazwa_11.get() == "Serweta":
        entry_cena_11 = Entry(root, textvariable=cena_11, justify=CENTER, width=14)
        entry_cena_11.insert(0, "6")
        entry_cena_11.grid(row=21, column=2)
    elif nazwa_11.get() == "Simplex Hv z Gentamycyna 10x40g":
        entry_cena_11 = Entry(root, textvariable=cena_11, justify=CENTER, width=14)
        entry_cena_11.insert(0, "162")
        entry_cena_11.grid(row=21, column=2)
    elif nazwa_11.get() == "Skalpel 11":
        entry_cena_11 = Entry(root, textvariable=cena_11, justify=CENTER, width=14)
        entry_cena_11.insert(0, "0.38")
        entry_cena_11.grid(row=21, column=2)
    elif nazwa_11.get() == "Skalpel 13":
        entry_cena_11 = Entry(root, textvariable=cena_11, justify=CENTER, width=14)
        entry_cena_11.insert(0, "1")
        entry_cena_11.grid(row=21, column=2)
    elif nazwa_11.get() == "Skalpel 22":
        entry_cena_11 = Entry(root, textvariable=cena_11, justify=CENTER, width=14)
        entry_cena_11.insert(0, "00000")
        entry_cena_11.grid(row=21, column=2)
    elif nazwa_11.get() == "Śruba blokująca PeekPower do osteotomii":
        entry_cena_11 = Entry(root, textvariable=cena_11, justify=CENTER, width=14)
        entry_cena_11.insert(0, "194")
        entry_cena_11.grid(row=21, column=2)
    elif nazwa_11.get() == "System do mieszania próżniowego":
        entry_cena_11 = Entry(root, textvariable=cena_11, justify=CENTER, width=14)
        entry_cena_11.insert(0, "216")
        entry_cena_11.grid(row=21, column=2)
    elif nazwa_11.get() == "System wprowadzania implantów ACL TightRope":
        entry_cena_11 = Entry(root, textvariable=cena_11, justify=CENTER, width=14)
        entry_cena_11.insert(0, "702")
        entry_cena_11.grid(row=21, column=2)
    elif nazwa_11.get() == "Szew FiberWire 2":
        entry_cena_11 = Entry(root, textvariable=cena_11, justify=CENTER, width=14)
        entry_cena_11.insert(0, "86.40")
        entry_cena_11.grid(row=21, column=2)
    elif nazwa_11.get() == "Taśma przylepna 10x50":
        entry_cena_11 = Entry(root, textvariable=cena_11, justify=CENTER, width=14)
        entry_cena_11.insert(0, "1.04")
        entry_cena_11.grid(row=21, column=2)
    elif nazwa_11.get() == "Triathlon elem. udowy lewy":
        entry_cena_11 = Entry(root, textvariable=cena_11, justify=CENTER, width=14)
        entry_cena_11.insert(0, "3132")
        entry_cena_11.grid(row=21, column=2)
    elif nazwa_11.get() == "Triathlon PS wkładka x3-9mm #4":
        entry_cena_11 = Entry(root, textvariable=cena_11, justify=CENTER, width=14)
        entry_cena_11.insert(0, "756")
        entry_cena_11.grid(row=21, column=2)
    elif nazwa_11.get() == "Triathlon taca piszczelowa":
        entry_cena_11 = Entry(root, textvariable=cena_11, justify=CENTER, width=14)
        entry_cena_11.insert(0, "1296")
        entry_cena_11.grid(row=21, column=2)
    elif nazwa_11.get() == "Wkłady 3L z żelem":
        entry_cena_11 = Entry(root, textvariable=cena_11, justify=CENTER, width=14)
        entry_cena_11.insert(0, "10.26")
        entry_cena_11.grid(row=21, column=2)
    elif nazwa_11.get() == "Zestaw do artroskopii":
        entry_cena_11 = Entry(root, textvariable=cena_11, justify=CENTER, width=14)
        entry_cena_11.insert(0, "67")
        entry_cena_11.grid(row=21, column=2)
    elif nazwa_11.get() == "Zestaw do artroskopii barku":
        entry_cena_11 = Entry(root, textvariable=cena_11, justify=CENTER, width=14)
        entry_cena_11.insert(0, "108")
        entry_cena_11.grid(row=21, column=2)
    elif nazwa_11.get() == "Zestaw do drenażu":
        entry_cena_11 = Entry(root, textvariable=cena_11, justify=CENTER, width=14)
        entry_cena_11.insert(0, "14.23")
        entry_cena_11.grid(row=21, column=2)
    elif nazwa_11.get() == "Zestaw ortopedyczny":
        entry_cena_11 = Entry(root, textvariable=cena_11, justify=CENTER, width=14)
        entry_cena_11.insert(0, "28.08")
        entry_cena_11.grid(row=21, column=2)
    elif nazwa_11.get() == "Gaziki 20 x 10cm":
        entry_cena_11 = Entry(root, textvariable=cena_11, justify=CENTER, width=14)
        entry_cena_11.insert(0, "0.46")
        entry_cena_11.grid(row=21, column=2)
    else:
        entry_cena_11 = Entry(root, textvariable=cena_11, justify=CENTER, width=14, bg="#ffff00")
        entry_cena_11.insert(0, "0")
        entry_cena_11.grid(row=21, column=2)

    if nazwa_12.get() == "--puste--":
        entry_cena_12 = Entry(root, textvariable=cena_12, justify=CENTER, width=14)
        entry_cena_12.insert(0, "0")
        entry_cena_12.grid(row=22, column=2)
    elif nazwa_12.get() == "Ablator":
        entry_cena_12 = Entry(root, textvariable=cena_12, justify=CENTER, width=14)
        entry_cena_12.insert(0, "572")
        entry_cena_12.grid(row=22, column=2)
    elif nazwa_12.get() == "Anestezjolog":
        entry_cena_12 = Entry(root, textvariable=cena_12, justify=CENTER, width=14, bg="#ffff00")
        entry_cena_12.insert(0, "350")
        entry_cena_12.grid(row=22, column=2)
    elif nazwa_12.get() == "Butelka 400ml do długotrwałego odsysania ran j.u. sterylna":
        entry_cena_12 = Entry(root, textvariable=cena_12, justify=CENTER, width=14)
        entry_cena_12.insert(0, "4")
        entry_cena_12.grid(row=22, column=2)
    elif nazwa_12.get() == "Doba":
        entry_cena_12 = Entry(root, textvariable=cena_12, justify=CENTER, width=14)
        entry_cena_12.insert(0, "700")
        entry_cena_12.grid(row=22, column=2)
    elif nazwa_12.get() == "Dren łączący do ssaka Grena":
        entry_cena_12 = Entry(root, textvariable=cena_12, justify=CENTER, width=14)
        entry_cena_12.insert(0, "5")
        entry_cena_12.grid(row=22, column=2)
    elif nazwa_12.get() == "Dren Redona Ch 16 dł. 800mm z trokarem":
        entry_cena_12 = Entry(root, textvariable=cena_12, justify=CENTER, width=14)
        entry_cena_12.insert(0, "29.74")
        entry_cena_12.grid(row=22, column=2)
    elif nazwa_12.get() == "Dren do pompy Artrex":
        entry_cena_12 = Entry(root, textvariable=cena_12, justify=CENTER, width=14)
        entry_cena_12.insert(0, "108")
        entry_cena_12.grid(row=22, column=2)
    elif nazwa_12.get() == "Drut wiercący 2,4 x 311":
        entry_cena_12 = Entry(root, textvariable=cena_12, justify=CENTER, width=14)
        entry_cena_12.insert(0, "139.60")
        entry_cena_12.grid(row=22, column=2)
    elif nazwa_12.get() == "Fartuch jałowy L":
        entry_cena_12 = Entry(root, textvariable=cena_12, justify=CENTER, width=14)
        entry_cena_12.insert(0, "17")
        entry_cena_12.grid(row=22, column=2)
    elif nazwa_12.get() == "Fartuch jałowy M":
        entry_cena_12 = Entry(root, textvariable=cena_12, justify=CENTER, width=14)
        entry_cena_12.insert(0, "15.28")
        entry_cena_12.grid(row=22, column=2)
    elif nazwa_12.get() == "Fartuch jałowy XL":
        entry_cena_12 = Entry(root, textvariable=cena_12, justify=CENTER, width=14)
        entry_cena_12.insert(0, "20.84")
        entry_cena_12.grid(row=22, column=2)
    elif nazwa_12.get() == "FasatThread BioComposite Interference Screw 8x30":
        entry_cena_12 = Entry(root, textvariable=cena_12, justify=CENTER, width=14)
        entry_cena_12.insert(0, "594")
        entry_cena_12.grid(row=22, column=2)
    elif nazwa_12.get() == "Folia operacyjna, jałowa 45cm x 55cm":
        entry_cena_12 = Entry(root, textvariable=cena_12, justify=CENTER, width=14)
        entry_cena_12.insert(0, "9.99")
        entry_cena_12.grid(row=22, column=2)
    elif nazwa_12.get() == "Gaziki 10 x 10cm":
        entry_cena_12 = Entry(root, textvariable=cena_12, justify=CENTER, width=14)
        entry_cena_12.insert(0, "0.10")
        entry_cena_12.grid(row=22, column=2)
    elif nazwa_12.get() == "Igła 0,6 x 60":
        entry_cena_12 = Entry(root, textvariable=cena_12, justify=CENTER, width=14)
        entry_cena_12.insert(0, "0.09")
        entry_cena_12.grid(row=22, column=2)
    elif nazwa_12.get() == "Igła 0,7 x 40":
        entry_cena_12 = Entry(root, textvariable=cena_12, justify=CENTER, width=14)
        entry_cena_12.insert(0, "0.05")
        entry_cena_12.grid(row=22, column=2)
    elif nazwa_12.get() == "Igła 0,8 x 40":
        entry_cena_12 = Entry(root, textvariable=cena_12, justify=CENTER, width=14)
        entry_cena_12.insert(0, "0.05")
        entry_cena_12.grid(row=22, column=2)
    elif nazwa_12.get() == "Igła 1,1 x 70":
        entry_cena_12 = Entry(root, textvariable=cena_12, justify=CENTER, width=14)
        entry_cena_12.insert(0, "0.16")
        entry_cena_12.grid(row=22, column=2)
    elif nazwa_12.get() == "Kaniulowana śruba int. biokompozytowa z osłonką jednoraz.":
        entry_cena_12 = Entry(root, textvariable=cena_12, justify=CENTER, width=14)
        entry_cena_12.insert(0, "594")
        entry_cena_12.grid(row=22, column=2)
    elif nazwa_12.get() == "Kaniulowana śruba int. biokompozytowa z pełnym gwintem":
        entry_cena_12 = Entry(root, textvariable=cena_12, justify=CENTER, width=14)
        entry_cena_12.insert(0, "594")
        entry_cena_12.grid(row=22, column=2)
    elif nazwa_12.get() == "Końcówka do Shavera":
        entry_cena_12 = Entry(root, textvariable=cena_12, justify=CENTER, width=14)
        entry_cena_12.insert(0, "270")
        entry_cena_12.grid(row=22, column=2)
    elif nazwa_12.get() == "Kotwica biokompozytowa SwiveLock":
        entry_cena_12 = Entry(root, textvariable=cena_12, justify=CENTER, width=14)
        entry_cena_12.insert(0, "918")
        entry_cena_12.grid(row=22, column=2)
    elif nazwa_12.get() == "Kotwica Corkscrew":
        entry_cena_12 = Entry(root, textvariable=cena_12, justify=CENTER, width=14)
        entry_cena_12.insert(0, "604")
        entry_cena_12.grid(row=22, column=2)
    elif nazwa_12.get() == "Kotwica FASTak":
        entry_cena_12 = Entry(root, textvariable=cena_12, justify=CENTER, width=14)
        entry_cena_12.insert(0, "432")
        entry_cena_12.grid(row=22, column=2)
    elif nazwa_12.get() == "Kotwica PEEK SwiveLock":
        entry_cena_12 = Entry(root, textvariable=cena_12, justify=CENTER, width=14)
        entry_cena_12.insert(0, "885.60")
        entry_cena_12.grid(row=22, column=2)
    elif nazwa_12.get() == "NaCl 3000ml":
        entry_cena_12 = Entry(root, textvariable=cena_12, justify=CENTER, width=14)
        entry_cena_12.insert(0, "29.72")
        entry_cena_12.grid(row=22, column=2)
    elif nazwa_12.get() == "NaCl 5000ml":
        entry_cena_12 = Entry(root, textvariable=cena_12, justify=CENTER, width=14)
        entry_cena_12.insert(0, "58.33")
        entry_cena_12.grid(row=22, column=2)
    elif nazwa_12.get() == "Nici Dafilon 2-0":
        entry_cena_12 = Entry(root, textvariable=cena_12, justify=CENTER, width=14)
        entry_cena_12.insert(0, "6.60")
        entry_cena_12.grid(row=22, column=2)
    elif nazwa_12.get() == "Nici Novosyn 2":
        entry_cena_12 = Entry(root, textvariable=cena_12, justify=CENTER, width=14)
        entry_cena_12.insert(0, "13")
        entry_cena_12.grid(row=22, column=2)
    elif nazwa_12.get() == "Nici Novosyn 2-0":
        entry_cena_12 = Entry(root, textvariable=cena_12, justify=CENTER, width=14)
        entry_cena_12.insert(0, "7.70")
        entry_cena_12.grid(row=22, column=2)
    elif nazwa_12.get() == "Nici Novosyn 3-0":
        entry_cena_12 = Entry(root, textvariable=cena_12, justify=CENTER, width=14)
        entry_cena_12.insert(0, "7.70")
        entry_cena_12.grid(row=22, column=2)
    elif nazwa_12.get() == "Nici Nylon 2-0":
        entry_cena_12 = Entry(root, textvariable=cena_12, justify=CENTER, width=14)
        entry_cena_12.insert(0, "2.50")
        entry_cena_12.grid(row=22, column=2)
    elif nazwa_12.get() == "Nici Nylon 3-0":
        entry_cena_12 = Entry(root, textvariable=cena_12, justify=CENTER, width=14)
        entry_cena_12.insert(0, "2")
        entry_cena_12.grid(row=22, column=2)
    elif nazwa_12.get() == "Nici PGLA":
        entry_cena_12 = Entry(root, textvariable=cena_12, justify=CENTER, width=14)
        entry_cena_12.insert(0, "11.60")
        entry_cena_12.grid(row=22, column=2)
    elif nazwa_12.get() == "Nici PremiCron 3":
        entry_cena_12 = Entry(root, textvariable=cena_12, justify=CENTER, width=14)
        entry_cena_12.insert(0, "6.50")
        entry_cena_12.grid(row=22, column=2)
    elif nazwa_12.get() == "Nici Vicryl 4-0":
        entry_cena_12 = Entry(root, textvariable=cena_12, justify=CENTER, width=14)
        entry_cena_12.insert(0, "7.50")
        entry_cena_12.grid(row=22, column=2)
    elif nazwa_12.get() == "Nitinol Guide Pin 1.1":
        entry_cena_12 = Entry(root, textvariable=cena_12, justify=CENTER, width=14)
        entry_cena_12.insert(0, "145.80")
        entry_cena_12.grid(row=22, column=2)
    elif nazwa_12.get() == "Osłona na przewody":
        entry_cena_12 = Entry(root, textvariable=cena_12, justify=CENTER, width=14)
        entry_cena_12.insert(0, "2.50")
        entry_cena_12.grid(row=22, column=2)
    elif nazwa_12.get() == "Ostrze Arthrex 90(86)x19x1,27":
        entry_cena_12 = Entry(root, textvariable=cena_12, justify=CENTER, width=14)
        entry_cena_12.insert(0, "216")
        entry_cena_12.grid(row=22, column=2)
    elif nazwa_12.get() == "Ostrze piły":
        entry_cena_12 = Entry(root, textvariable=cena_12, justify=CENTER, width=14)
        entry_cena_12.insert(0, "108")
        entry_cena_12.grid(row=22, column=2)
    elif nazwa_12.get() == "Pielęgniarka anest.":
        entry_cena_12 = Entry(root, textvariable=cena_12, justify=CENTER, width=14)
        entry_cena_12.insert(0, "50")
        entry_cena_12.grid(row=22, column=2)
    elif nazwa_12.get() == "Pielęgniarka instr.":
        entry_cena_12 = Entry(root, textvariable=cena_12, justify=CENTER, width=14)
        entry_cena_12.insert(0, "50")
        entry_cena_12.grid(row=22, column=2)
    elif nazwa_12.get() == "Pielęgniarka 'Noviline'":
        entry_cena_12 = Entry(root, textvariable=cena_12, justify=CENTER, width=14)
        entry_cena_12.insert(0, "30")
        entry_cena_12.grid(row=22, column=2)
    elif nazwa_12.get() == "Płytka PeekPower do osteotomii klinowej":
        entry_cena_12 = Entry(root, textvariable=cena_12, justify=CENTER, width=14)
        entry_cena_12.insert(0, "2160")
        entry_cena_12.grid(row=22, column=2)
    elif nazwa_12.get() == "Rękawice jałowe 6,5":
        entry_cena_12 = Entry(root, textvariable=cena_12, justify=CENTER, width=14)
        entry_cena_12.insert(0, "1.20")
        entry_cena_12.grid(row=22, column=2)
    elif nazwa_12.get() == "Rękawice jałowe 7,0":
        entry_cena_12 = Entry(root, textvariable=cena_12, justify=CENTER, width=14)
        entry_cena_12.insert(0, "1.20")
        entry_cena_12.grid(row=22, column=2)
    elif nazwa_12.get() == "Rękawice jałowe 7,5":
        entry_cena_12 = Entry(root, textvariable=cena_12, justify=CENTER, width=14)
        entry_cena_12.insert(0, "1.20")
        entry_cena_12.grid(row=22, column=2)
    elif nazwa_12.get() == "Rękawice jałowe 8,00":
        entry_cena_12 = Entry(root, textvariable=cena_12, justify=CENTER, width=14)
        entry_cena_12.insert(0, "1.20")
        entry_cena_12.grid(row=22, column=2)
    elif nazwa_12.get() == "Rękojeść Interpulse wysokoprzepływowa":
        entry_cena_12 = Entry(root, textvariable=cena_12, justify=CENTER, width=14)
        entry_cena_12.insert(0, "216")
        entry_cena_12.grid(row=22, column=2)
    elif nazwa_12.get() == "Serweta":
        entry_cena_12 = Entry(root, textvariable=cena_12, justify=CENTER, width=14)
        entry_cena_12.insert(0, "6")
        entry_cena_12.grid(row=22, column=2)
    elif nazwa_12.get() == "Simplex Hv z Gentamycyna 10x40g":
        entry_cena_12 = Entry(root, textvariable=cena_12, justify=CENTER, width=14)
        entry_cena_12.insert(0, "162")
        entry_cena_12.grid(row=22, column=2)
    elif nazwa_12.get() == "Skalpel 11":
        entry_cena_12 = Entry(root, textvariable=cena_12, justify=CENTER, width=14)
        entry_cena_12.insert(0, "0.38")
        entry_cena_12.grid(row=22, column=2)
    elif nazwa_12.get() == "Skalpel 13":
        entry_cena_12 = Entry(root, textvariable=cena_12, justify=CENTER, width=14)
        entry_cena_12.insert(0, "1")
        entry_cena_12.grid(row=22, column=2)
    elif nazwa_12.get() == "Skalpel 22":
        entry_cena_12 = Entry(root, textvariable=cena_12, justify=CENTER, width=14)
        entry_cena_12.insert(0, "00000")
        entry_cena_12.grid(row=22, column=2)
    elif nazwa_12.get() == "Śruba blokująca PeekPower do osteotomii":
        entry_cena_12 = Entry(root, textvariable=cena_12, justify=CENTER, width=14)
        entry_cena_12.insert(0, "194")
        entry_cena_12.grid(row=22, column=2)
    elif nazwa_12.get() == "System do mieszania próżniowego":
        entry_cena_12 = Entry(root, textvariable=cena_12, justify=CENTER, width=14)
        entry_cena_12.insert(0, "216")
        entry_cena_12.grid(row=22, column=2)
    elif nazwa_12.get() == "System wprowadzania implantów ACL TightRope":
        entry_cena_12 = Entry(root, textvariable=cena_12, justify=CENTER, width=14)
        entry_cena_12.insert(0, "702")
        entry_cena_12.grid(row=22, column=2)
    elif nazwa_12.get() == "Szew FiberWire 2":
        entry_cena_12 = Entry(root, textvariable=cena_12, justify=CENTER, width=14)
        entry_cena_12.insert(0, "86.40")
        entry_cena_12.grid(row=22, column=2)
    elif nazwa_12.get() == "Taśma przylepna 10x50":
        entry_cena_12 = Entry(root, textvariable=cena_12, justify=CENTER, width=14)
        entry_cena_12.insert(0, "1.04")
        entry_cena_12.grid(row=22, column=2)
    elif nazwa_12.get() == "Triathlon elem. udowy lewy":
        entry_cena_12 = Entry(root, textvariable=cena_12, justify=CENTER, width=14)
        entry_cena_12.insert(0, "3132")
        entry_cena_12.grid(row=22, column=2)
    elif nazwa_12.get() == "Triathlon PS wkładka x3-9mm #4":
        entry_cena_12 = Entry(root, textvariable=cena_12, justify=CENTER, width=14)
        entry_cena_12.insert(0, "756")
        entry_cena_12.grid(row=22, column=2)
    elif nazwa_12.get() == "Triathlon taca piszczelowa":
        entry_cena_12 = Entry(root, textvariable=cena_12, justify=CENTER, width=14)
        entry_cena_12.insert(0, "1296")
        entry_cena_12.grid(row=22, column=2)
    elif nazwa_12.get() == "Wkłady 3L z żelem":
        entry_cena_12 = Entry(root, textvariable=cena_12, justify=CENTER, width=14)
        entry_cena_12.insert(0, "10.26")
        entry_cena_12.grid(row=22, column=2)
    elif nazwa_12.get() == "Zestaw do artroskopii":
        entry_cena_12 = Entry(root, textvariable=cena_12, justify=CENTER, width=14)
        entry_cena_12.insert(0, "67")
        entry_cena_12.grid(row=22, column=2)
    elif nazwa_12.get() == "Zestaw do artroskopii barku":
        entry_cena_12 = Entry(root, textvariable=cena_12, justify=CENTER, width=14)
        entry_cena_12.insert(0, "108")
        entry_cena_12.grid(row=22, column=2)
    elif nazwa_12.get() == "Zestaw do drenażu":
        entry_cena_12 = Entry(root, textvariable=cena_12, justify=CENTER, width=14)
        entry_cena_12.insert(0, "14.23")
        entry_cena_12.grid(row=22, column=2)
    elif nazwa_12.get() == "Zestaw ortopedyczny":
        entry_cena_12 = Entry(root, textvariable=cena_12, justify=CENTER, width=14)
        entry_cena_12.insert(0, "28.08")
        entry_cena_12.grid(row=22, column=2)
    elif nazwa_12.get() == "Gaziki 20 x 10cm":
        entry_cena_12 = Entry(root, textvariable=cena_12, justify=CENTER, width=14)
        entry_cena_12.insert(0, "0.46")
        entry_cena_12.grid(row=22, column=2)
    else:
        entry_cena_12 = Entry(root, textvariable=cena_12, justify=CENTER, width=14, bg="#ffff00")
        entry_cena_12.insert(0, "0")
        entry_cena_12.grid(row=22, column=2)

    if nazwa_13.get() == "--puste--":
        entry_cena_13 = Entry(root, textvariable=cena_13, justify=CENTER, width=14)
        entry_cena_13.insert(0, "0")
        entry_cena_13.grid(row=23, column=2)
    elif nazwa_13.get() == "Ablator":
        entry_cena_13 = Entry(root, textvariable=cena_13, justify=CENTER, width=14)
        entry_cena_13.insert(0, "572")
        entry_cena_13.grid(row=23, column=2)
    elif nazwa_13.get() == "Anestezjolog":
        entry_cena_13 = Entry(root, textvariable=cena_13, justify=CENTER, width=14, bg="#ffff00")
        entry_cena_13.insert(0, "350")
        entry_cena_13.grid(row=23, column=2)
    elif nazwa_13.get() == "Butelka 400ml do długotrwałego odsysania ran j.u. sterylna":
        entry_cena_13 = Entry(root, textvariable=cena_13, justify=CENTER, width=14)
        entry_cena_13.insert(0, "4")
        entry_cena_13.grid(row=23, column=2)
    elif nazwa_13.get() == "Doba":
        entry_cena_13 = Entry(root, textvariable=cena_13, justify=CENTER, width=14)
        entry_cena_13.insert(0, "700")
        entry_cena_13.grid(row=23, column=2)
    elif nazwa_13.get() == "Dren łączący do ssaka Grena":
        entry_cena_13 = Entry(root, textvariable=cena_13, justify=CENTER, width=14)
        entry_cena_13.insert(0, "5")
        entry_cena_13.grid(row=23, column=2)
    elif nazwa_13.get() == "Dren Redona Ch 16 dł. 800mm z trokarem":
        entry_cena_13 = Entry(root, textvariable=cena_13, justify=CENTER, width=14)
        entry_cena_13.insert(0, "29.74")
        entry_cena_13.grid(row=23, column=2)
    elif nazwa_13.get() == "Dren do pompy Artrex":
        entry_cena_13 = Entry(root, textvariable=cena_13, justify=CENTER, width=14)
        entry_cena_13.insert(0, "108")
        entry_cena_13.grid(row=23, column=2)
    elif nazwa_13.get() == "Drut wiercący 2,4 x 311":
        entry_cena_13 = Entry(root, textvariable=cena_13, justify=CENTER, width=14)
        entry_cena_13.insert(0, "139.60")
        entry_cena_13.grid(row=23, column=2)
    elif nazwa_13.get() == "Fartuch jałowy L":
        entry_cena_13 = Entry(root, textvariable=cena_13, justify=CENTER, width=14)
        entry_cena_13.insert(0, "17")
        entry_cena_13.grid(row=23, column=2)
    elif nazwa_13.get() == "Fartuch jałowy M":
        entry_cena_13 = Entry(root, textvariable=cena_13, justify=CENTER, width=14)
        entry_cena_13.insert(0, "15.28")
        entry_cena_13.grid(row=23, column=2)
    elif nazwa_13.get() == "Fartuch jałowy XL":
        entry_cena_13 = Entry(root, textvariable=cena_13, justify=CENTER, width=14)
        entry_cena_13.insert(0, "20.84")
        entry_cena_13.grid(row=23, column=2)
    elif nazwa_13.get() == "FasatThread BioComposite Interference Screw 8x30":
        entry_cena_13 = Entry(root, textvariable=cena_13, justify=CENTER, width=14)
        entry_cena_13.insert(0, "594")
        entry_cena_13.grid(row=23, column=2)
    elif nazwa_13.get() == "Folia operacyjna, jałowa 45cm x 55cm":
        entry_cena_13 = Entry(root, textvariable=cena_13, justify=CENTER, width=14)
        entry_cena_13.insert(0, "9.99")
        entry_cena_13.grid(row=23, column=2)
    elif nazwa_13.get() == "Gaziki 10 x 10cm":
        entry_cena_13 = Entry(root, textvariable=cena_13, justify=CENTER, width=14)
        entry_cena_13.insert(0, "0.10")
        entry_cena_13.grid(row=23, column=2)
    elif nazwa_13.get() == "Igła 0,6 x 60":
        entry_cena_13 = Entry(root, textvariable=cena_13, justify=CENTER, width=14)
        entry_cena_13.insert(0, "0.09")
        entry_cena_13.grid(row=23, column=2)
    elif nazwa_13.get() == "Igła 0,7 x 40":
        entry_cena_13 = Entry(root, textvariable=cena_13, justify=CENTER, width=14)
        entry_cena_13.insert(0, "0.05")
        entry_cena_13.grid(row=23, column=2)
    elif nazwa_13.get() == "Igła 0,8 x 40":
        entry_cena_13 = Entry(root, textvariable=cena_13, justify=CENTER, width=14)
        entry_cena_13.insert(0, "0.05")
        entry_cena_13.grid(row=23, column=2)
    elif nazwa_13.get() == "Igła 1,1 x 70":
        entry_cena_13 = Entry(root, textvariable=cena_13, justify=CENTER, width=14)
        entry_cena_13.insert(0, "0.16")
        entry_cena_13.grid(row=23, column=2)
    elif nazwa_13.get() == "Kaniulowana śruba int. biokompozytowa z osłonką jednoraz.":
        entry_cena_13 = Entry(root, textvariable=cena_13, justify=CENTER, width=14)
        entry_cena_13.insert(0, "594")
        entry_cena_13.grid(row=23, column=2)
    elif nazwa_13.get() == "Kaniulowana śruba int. biokompozytowa z pełnym gwintem":
        entry_cena_13 = Entry(root, textvariable=cena_13, justify=CENTER, width=14)
        entry_cena_13.insert(0, "594")
        entry_cena_13.grid(row=23, column=2)
    elif nazwa_13.get() == "Końcówka do Shavera":
        entry_cena_13 = Entry(root, textvariable=cena_13, justify=CENTER, width=14)
        entry_cena_13.insert(0, "270")
        entry_cena_13.grid(row=23, column=2)
    elif nazwa_13.get() == "Kotwica biokompozytowa SwiveLock":
        entry_cena_13 = Entry(root, textvariable=cena_13, justify=CENTER, width=14)
        entry_cena_13.insert(0, "918")
        entry_cena_13.grid(row=23, column=2)
    elif nazwa_13.get() == "Kotwica Corkscrew":
        entry_cena_13 = Entry(root, textvariable=cena_13, justify=CENTER, width=14)
        entry_cena_13.insert(0, "604")
        entry_cena_13.grid(row=23, column=2)
    elif nazwa_13.get() == "Kotwica FASTak":
        entry_cena_13 = Entry(root, textvariable=cena_13, justify=CENTER, width=14)
        entry_cena_13.insert(0, "432")
        entry_cena_13.grid(row=23, column=2)
    elif nazwa_13.get() == "Kotwica PEEK SwiveLock":
        entry_cena_13 = Entry(root, textvariable=cena_13, justify=CENTER, width=14)
        entry_cena_13.insert(0, "885.60")
        entry_cena_13.grid(row=23, column=2)
    elif nazwa_13.get() == "NaCl 3000ml":
        entry_cena_13 = Entry(root, textvariable=cena_13, justify=CENTER, width=14)
        entry_cena_13.insert(0, "29.72")
        entry_cena_13.grid(row=23, column=2)
    elif nazwa_13.get() == "NaCl 5000ml":
        entry_cena_13 = Entry(root, textvariable=cena_13, justify=CENTER, width=14)
        entry_cena_13.insert(0, "58.33")
        entry_cena_13.grid(row=23, column=2)
    elif nazwa_13.get() == "Nici Dafilon 2-0":
        entry_cena_13 = Entry(root, textvariable=cena_13, justify=CENTER, width=14)
        entry_cena_13.insert(0, "6.60")
        entry_cena_13.grid(row=23, column=2)
    elif nazwa_13.get() == "Nici Novosyn 2":
        entry_cena_13 = Entry(root, textvariable=cena_13, justify=CENTER, width=14)
        entry_cena_13.insert(0, "13")
        entry_cena_13.grid(row=23, column=2)
    elif nazwa_13.get() == "Nici Novosyn 2-0":
        entry_cena_13 = Entry(root, textvariable=cena_13, justify=CENTER, width=14)
        entry_cena_13.insert(0, "7.70")
        entry_cena_13.grid(row=23, column=2)
    elif nazwa_13.get() == "Nici Novosyn 3-0":
        entry_cena_13 = Entry(root, textvariable=cena_13, justify=CENTER, width=14)
        entry_cena_13.insert(0, "7.70")
        entry_cena_13.grid(row=23, column=2)
    elif nazwa_13.get() == "Nici Nylon 2-0":
        entry_cena_13 = Entry(root, textvariable=cena_13, justify=CENTER, width=14)
        entry_cena_13.insert(0, "2.50")
        entry_cena_13.grid(row=23, column=2)
    elif nazwa_13.get() == "Nici Nylon 3-0":
        entry_cena_13 = Entry(root, textvariable=cena_13, justify=CENTER, width=14)
        entry_cena_13.insert(0, "2")
        entry_cena_13.grid(row=23, column=2)
    elif nazwa_13.get() == "Nici PGLA":
        entry_cena_13 = Entry(root, textvariable=cena_13, justify=CENTER, width=14)
        entry_cena_13.insert(0, "11.60")
        entry_cena_13.grid(row=23, column=2)
    elif nazwa_13.get() == "Nici PremiCron 3":
        entry_cena_13 = Entry(root, textvariable=cena_13, justify=CENTER, width=14)
        entry_cena_13.insert(0, "6.50")
        entry_cena_13.grid(row=23, column=2)
    elif nazwa_13.get() == "Nici Vicryl 4-0":
        entry_cena_13 = Entry(root, textvariable=cena_13, justify=CENTER, width=14)
        entry_cena_13.insert(0, "7.50")
        entry_cena_13.grid(row=23, column=2)
    elif nazwa_13.get() == "Nitinol Guide Pin 1.1":
        entry_cena_13 = Entry(root, textvariable=cena_13, justify=CENTER, width=14)
        entry_cena_13.insert(0, "145.80")
        entry_cena_13.grid(row=23, column=2)
    elif nazwa_13.get() == "Osłona na przewody":
        entry_cena_13 = Entry(root, textvariable=cena_13, justify=CENTER, width=14)
        entry_cena_13.insert(0, "2.50")
        entry_cena_13.grid(row=23, column=2)
    elif nazwa_13.get() == "Ostrze Arthrex 90(86)x19x1,27":
        entry_cena_13 = Entry(root, textvariable=cena_13, justify=CENTER, width=14)
        entry_cena_13.insert(0, "216")
        entry_cena_13.grid(row=23, column=2)
    elif nazwa_13.get() == "Ostrze piły":
        entry_cena_13 = Entry(root, textvariable=cena_13, justify=CENTER, width=14)
        entry_cena_13.insert(0, "108")
        entry_cena_13.grid(row=23, column=2)
    elif nazwa_13.get() == "Pielęgniarka anest.":
        entry_cena_13 = Entry(root, textvariable=cena_13, justify=CENTER, width=14)
        entry_cena_13.insert(0, "50")
        entry_cena_13.grid(row=23, column=2)
    elif nazwa_13.get() == "Pielęgniarka instr.":
        entry_cena_13 = Entry(root, textvariable=cena_13, justify=CENTER, width=14)
        entry_cena_13.insert(0, "50")
        entry_cena_13.grid(row=23, column=2)
    elif nazwa_13.get() == "Pielęgniarka 'Noviline'":
        entry_cena_13 = Entry(root, textvariable=cena_13, justify=CENTER, width=14)
        entry_cena_13.insert(0, "30")
        entry_cena_13.grid(row=23, column=2)
    elif nazwa_13.get() == "Płytka PeekPower do osteotomii klinowej":
        entry_cena_13 = Entry(root, textvariable=cena_13, justify=CENTER, width=14)
        entry_cena_13.insert(0, "2160")
        entry_cena_13.grid(row=23, column=2)
    elif nazwa_13.get() == "Rękawice jałowe 6,5":
        entry_cena_13 = Entry(root, textvariable=cena_13, justify=CENTER, width=14)
        entry_cena_13.insert(0, "1.20")
        entry_cena_13.grid(row=23, column=2)
    elif nazwa_13.get() == "Rękawice jałowe 7,0":
        entry_cena_13 = Entry(root, textvariable=cena_13, justify=CENTER, width=14)
        entry_cena_13.insert(0, "1.20")
        entry_cena_13.grid(row=23, column=2)
    elif nazwa_13.get() == "Rękawice jałowe 7,5":
        entry_cena_13 = Entry(root, textvariable=cena_13, justify=CENTER, width=14)
        entry_cena_13.insert(0, "1.20")
        entry_cena_13.grid(row=23, column=2)
    elif nazwa_13.get() == "Rękawice jałowe 8,00":
        entry_cena_13 = Entry(root, textvariable=cena_13, justify=CENTER, width=14)
        entry_cena_13.insert(0, "1.20")
        entry_cena_13.grid(row=23, column=2)
    elif nazwa_13.get() == "Rękojeść Interpulse wysokoprzepływowa":
        entry_cena_13 = Entry(root, textvariable=cena_13, justify=CENTER, width=14)
        entry_cena_13.insert(0, "216")
        entry_cena_13.grid(row=23, column=2)
    elif nazwa_13.get() == "Serweta":
        entry_cena_13 = Entry(root, textvariable=cena_13, justify=CENTER, width=14)
        entry_cena_13.insert(0, "6")
        entry_cena_13.grid(row=23, column=2)
    elif nazwa_13.get() == "Simplex Hv z Gentamycyna 10x40g":
        entry_cena_13 = Entry(root, textvariable=cena_13, justify=CENTER, width=14)
        entry_cena_13.insert(0, "162")
        entry_cena_13.grid(row=23, column=2)
    elif nazwa_13.get() == "Skalpel 11":
        entry_cena_13 = Entry(root, textvariable=cena_13, justify=CENTER, width=14)
        entry_cena_13.insert(0, "0.38")
        entry_cena_13.grid(row=23, column=2)
    elif nazwa_13.get() == "Skalpel 13":
        entry_cena_13 = Entry(root, textvariable=cena_13, justify=CENTER, width=14)
        entry_cena_13.insert(0, "1")
        entry_cena_13.grid(row=23, column=2)
    elif nazwa_13.get() == "Skalpel 22":
        entry_cena_13 = Entry(root, textvariable=cena_13, justify=CENTER, width=14)
        entry_cena_13.insert(0, "00000")
        entry_cena_13.grid(row=23, column=2)
    elif nazwa_13.get() == "Śruba blokująca PeekPower do osteotomii":
        entry_cena_13 = Entry(root, textvariable=cena_13, justify=CENTER, width=14)
        entry_cena_13.insert(0, "194")
        entry_cena_13.grid(row=23, column=2)
    elif nazwa_13.get() == "System do mieszania próżniowego":
        entry_cena_13 = Entry(root, textvariable=cena_13, justify=CENTER, width=14)
        entry_cena_13.insert(0, "216")
        entry_cena_13.grid(row=23, column=2)
    elif nazwa_13.get() == "System wprowadzania implantów ACL TightRope":
        entry_cena_13 = Entry(root, textvariable=cena_13, justify=CENTER, width=14)
        entry_cena_13.insert(0, "702")
        entry_cena_13.grid(row=23, column=2)
    elif nazwa_13.get() == "Szew FiberWire 2":
        entry_cena_13 = Entry(root, textvariable=cena_13, justify=CENTER, width=14)
        entry_cena_13.insert(0, "86.40")
        entry_cena_13.grid(row=23, column=2)
    elif nazwa_13.get() == "Taśma przylepna 10x50":
        entry_cena_13 = Entry(root, textvariable=cena_13, justify=CENTER, width=14)
        entry_cena_13.insert(0, "1.04")
        entry_cena_13.grid(row=23, column=2)
    elif nazwa_13.get() == "Triathlon elem. udowy lewy":
        entry_cena_13 = Entry(root, textvariable=cena_13, justify=CENTER, width=14)
        entry_cena_13.insert(0, "3132")
        entry_cena_13.grid(row=23, column=2)
    elif nazwa_13.get() == "Triathlon PS wkładka x3-9mm #4":
        entry_cena_13 = Entry(root, textvariable=cena_13, justify=CENTER, width=14)
        entry_cena_13.insert(0, "756")
        entry_cena_13.grid(row=23, column=2)
    elif nazwa_13.get() == "Triathlon taca piszczelowa":
        entry_cena_13 = Entry(root, textvariable=cena_13, justify=CENTER, width=14)
        entry_cena_13.insert(0, "1296")
        entry_cena_13.grid(row=23, column=2)
    elif nazwa_13.get() == "Wkłady 3L z żelem":
        entry_cena_13 = Entry(root, textvariable=cena_13, justify=CENTER, width=14)
        entry_cena_13.insert(0, "10.26")
        entry_cena_13.grid(row=23, column=2)
    elif nazwa_13.get() == "Zestaw do artroskopii":
        entry_cena_13 = Entry(root, textvariable=cena_13, justify=CENTER, width=14)
        entry_cena_13.insert(0, "67")
        entry_cena_13.grid(row=23, column=2)
    elif nazwa_13.get() == "Zestaw do artroskopii barku":
        entry_cena_13 = Entry(root, textvariable=cena_13, justify=CENTER, width=14)
        entry_cena_13.insert(0, "108")
        entry_cena_13.grid(row=23, column=2)
    elif nazwa_13.get() == "Zestaw do drenażu":
        entry_cena_13 = Entry(root, textvariable=cena_13, justify=CENTER, width=14)
        entry_cena_13.insert(0, "14.23")
        entry_cena_13.grid(row=23, column=2)
    elif nazwa_13.get() == "Zestaw ortopedyczny":
        entry_cena_13 = Entry(root, textvariable=cena_13, justify=CENTER, width=14)
        entry_cena_13.insert(0, "28.08")
        entry_cena_13.grid(row=23, column=2)
    elif nazwa_13.get() == "Gaziki 20 x 10cm":
        entry_cena_13 = Entry(root, textvariable=cena_13, justify=CENTER, width=14)
        entry_cena_13.insert(0, "0.46")
        entry_cena_13.grid(row=23, column=2)
    else:
        entry_cena_13 = Entry(root, textvariable=cena_13, justify=CENTER, width=14, bg="#ffff00")
        entry_cena_13.insert(0, "0")
        entry_cena_13.grid(row=23, column=2)

    if nazwa_14.get() == "--puste--":
        entry_cena_14 = Entry(root, textvariable=cena_14, justify=CENTER, width=14)
        entry_cena_14.insert(0, "0")
        entry_cena_14.grid(row=24, column=2)
    elif nazwa_14.get() == "Ablator":
        entry_cena_14 = Entry(root, textvariable=cena_14, justify=CENTER, width=14)
        entry_cena_14.insert(0, "572")
        entry_cena_14.grid(row=24, column=2)
    elif nazwa_14.get() == "Anestezjolog":
        entry_cena_14 = Entry(root, textvariable=cena_14, justify=CENTER, width=14, bg="#ffff00")
        entry_cena_14.insert(0, "350")
        entry_cena_14.grid(row=24, column=2)
    elif nazwa_14.get() == "Butelka 400ml do długotrwałego odsysania ran j.u. sterylna":
        entry_cena_14 = Entry(root, textvariable=cena_14, justify=CENTER, width=14)
        entry_cena_14.insert(0, "4")
        entry_cena_14.grid(row=24, column=2)
    elif nazwa_14.get() == "Doba":
        entry_cena_14 = Entry(root, textvariable=cena_14, justify=CENTER, width=14)
        entry_cena_14.insert(0, "700")
        entry_cena_14.grid(row=24, column=2)
    elif nazwa_14.get() == "Dren łączący do ssaka Grena":
        entry_cena_14 = Entry(root, textvariable=cena_14, justify=CENTER, width=14)
        entry_cena_14.insert(0, "5")
        entry_cena_14.grid(row=24, column=2)
    elif nazwa_14.get() == "Dren Redona Ch 16 dł. 800mm z trokarem":
        entry_cena_14 = Entry(root, textvariable=cena_14, justify=CENTER, width=14)
        entry_cena_14.insert(0, "29.74")
        entry_cena_14.grid(row=24, column=2)
    elif nazwa_14.get() == "Dren do pompy Artrex":
        entry_cena_14 = Entry(root, textvariable=cena_14, justify=CENTER, width=14)
        entry_cena_14.insert(0, "108")
        entry_cena_14.grid(row=24, column=2)
    elif nazwa_14.get() == "Drut wiercący 2,4 x 311":
        entry_cena_14 = Entry(root, textvariable=cena_14, justify=CENTER, width=14)
        entry_cena_14.insert(0, "139.60")
        entry_cena_14.grid(row=24, column=2)
    elif nazwa_14.get() == "Fartuch jałowy L":
        entry_cena_14 = Entry(root, textvariable=cena_14, justify=CENTER, width=14)
        entry_cena_14.insert(0, "17")
        entry_cena_14.grid(row=24, column=2)
    elif nazwa_14.get() == "Fartuch jałowy M":
        entry_cena_14 = Entry(root, textvariable=cena_14, justify=CENTER, width=14)
        entry_cena_14.insert(0, "15.28")
        entry_cena_14.grid(row=24, column=2)
    elif nazwa_14.get() == "Fartuch jałowy XL":
        entry_cena_14 = Entry(root, textvariable=cena_14, justify=CENTER, width=14)
        entry_cena_14.insert(0, "20.84")
        entry_cena_14.grid(row=24, column=2)
    elif nazwa_14.get() == "FasatThread BioComposite Interference Screw 8x30":
        entry_cena_14 = Entry(root, textvariable=cena_14, justify=CENTER, width=14)
        entry_cena_14.insert(0, "594")
        entry_cena_14.grid(row=24, column=2)
    elif nazwa_14.get() == "Folia operacyjna, jałowa 45cm x 55cm":
        entry_cena_14 = Entry(root, textvariable=cena_14, justify=CENTER, width=14)
        entry_cena_14.insert(0, "9.99")
        entry_cena_14.grid(row=24, column=2)
    elif nazwa_14.get() == "Gaziki 10 x 10cm":
        entry_cena_14 = Entry(root, textvariable=cena_14, justify=CENTER, width=14)
        entry_cena_14.insert(0, "0.10")
        entry_cena_14.grid(row=24, column=2)
    elif nazwa_14.get() == "Igła 0,6 x 60":
        entry_cena_14 = Entry(root, textvariable=cena_14, justify=CENTER, width=14)
        entry_cena_14.insert(0, "0.09")
        entry_cena_14.grid(row=24, column=2)
    elif nazwa_14.get() == "Igła 0,7 x 40":
        entry_cena_14 = Entry(root, textvariable=cena_14, justify=CENTER, width=14)
        entry_cena_14.insert(0, "0.05")
        entry_cena_14.grid(row=24, column=2)
    elif nazwa_14.get() == "Igła 0,8 x 40":
        entry_cena_14 = Entry(root, textvariable=cena_14, justify=CENTER, width=14)
        entry_cena_14.insert(0, "0.05")
        entry_cena_14.grid(row=24, column=2)
    elif nazwa_14.get() == "Igła 1,1 x 70":
        entry_cena_14 = Entry(root, textvariable=cena_14, justify=CENTER, width=14)
        entry_cena_14.insert(0, "0.16")
        entry_cena_14.grid(row=24, column=2)
    elif nazwa_14.get() == "Kaniulowana śruba int. biokompozytowa z osłonką jednoraz.":
        entry_cena_14 = Entry(root, textvariable=cena_14, justify=CENTER, width=14)
        entry_cena_14.insert(0, "594")
        entry_cena_14.grid(row=24, column=2)
    elif nazwa_14.get() == "Kaniulowana śruba int. biokompozytowa z pełnym gwintem":
        entry_cena_14 = Entry(root, textvariable=cena_14, justify=CENTER, width=14)
        entry_cena_14.insert(0, "594")
        entry_cena_14.grid(row=24, column=2)
    elif nazwa_14.get() == "Końcówka do Shavera":
        entry_cena_14 = Entry(root, textvariable=cena_14, justify=CENTER, width=14)
        entry_cena_14.insert(0, "270")
        entry_cena_14.grid(row=24, column=2)
    elif nazwa_14.get() == "Kotwica biokompozytowa SwiveLock":
        entry_cena_14 = Entry(root, textvariable=cena_14, justify=CENTER, width=14)
        entry_cena_14.insert(0, "918")
        entry_cena_14.grid(row=24, column=2)
    elif nazwa_14.get() == "Kotwica Corkscrew":
        entry_cena_14 = Entry(root, textvariable=cena_14, justify=CENTER, width=14)
        entry_cena_14.insert(0, "604")
        entry_cena_14.grid(row=24, column=2)
    elif nazwa_14.get() == "Kotwica FASTak":
        entry_cena_14 = Entry(root, textvariable=cena_14, justify=CENTER, width=14)
        entry_cena_14.insert(0, "432")
        entry_cena_14.grid(row=24, column=2)
    elif nazwa_14.get() == "Kotwica PEEK SwiveLock":
        entry_cena_14 = Entry(root, textvariable=cena_14, justify=CENTER, width=14)
        entry_cena_14.insert(0, "885.60")
        entry_cena_14.grid(row=24, column=2)
    elif nazwa_14.get() == "NaCl 3000ml":
        entry_cena_14 = Entry(root, textvariable=cena_14, justify=CENTER, width=14)
        entry_cena_14.insert(0, "29.72")
        entry_cena_14.grid(row=24, column=2)
    elif nazwa_14.get() == "NaCl 5000ml":
        entry_cena_14 = Entry(root, textvariable=cena_14, justify=CENTER, width=14)
        entry_cena_14.insert(0, "58.33")
        entry_cena_14.grid(row=24, column=2)
    elif nazwa_14.get() == "Nici Dafilon 2-0":
        entry_cena_14 = Entry(root, textvariable=cena_14, justify=CENTER, width=14)
        entry_cena_14.insert(0, "6.60")
        entry_cena_14.grid(row=24, column=2)
    elif nazwa_14.get() == "Nici Novosyn 2":
        entry_cena_14 = Entry(root, textvariable=cena_14, justify=CENTER, width=14)
        entry_cena_14.insert(0, "13")
        entry_cena_14.grid(row=24, column=2)
    elif nazwa_14.get() == "Nici Novosyn 2-0":
        entry_cena_14 = Entry(root, textvariable=cena_14, justify=CENTER, width=14)
        entry_cena_14.insert(0, "7.70")
        entry_cena_14.grid(row=24, column=2)
    elif nazwa_14.get() == "Nici Novosyn 3-0":
        entry_cena_14 = Entry(root, textvariable=cena_14, justify=CENTER, width=14)
        entry_cena_14.insert(0, "7.70")
        entry_cena_14.grid(row=24, column=2)
    elif nazwa_14.get() == "Nici Nylon 2-0":
        entry_cena_14 = Entry(root, textvariable=cena_14, justify=CENTER, width=14)
        entry_cena_14.insert(0, "2.50")
        entry_cena_14.grid(row=24, column=2)
    elif nazwa_14.get() == "Nici Nylon 3-0":
        entry_cena_14 = Entry(root, textvariable=cena_14, justify=CENTER, width=14)
        entry_cena_14.insert(0, "2")
        entry_cena_14.grid(row=24, column=2)
    elif nazwa_14.get() == "Nici PGLA":
        entry_cena_14 = Entry(root, textvariable=cena_14, justify=CENTER, width=14)
        entry_cena_14.insert(0, "11.60")
        entry_cena_14.grid(row=24, column=2)
    elif nazwa_14.get() == "Nici PremiCron 3":
        entry_cena_14 = Entry(root, textvariable=cena_14, justify=CENTER, width=14)
        entry_cena_14.insert(0, "6.50")
        entry_cena_14.grid(row=24, column=2)
    elif nazwa_14.get() == "Nici Vicryl 4-0":
        entry_cena_14 = Entry(root, textvariable=cena_14, justify=CENTER, width=14)
        entry_cena_14.insert(0, "7.50")
        entry_cena_14.grid(row=24, column=2)
    elif nazwa_14.get() == "Nitinol Guide Pin 1.1":
        entry_cena_14 = Entry(root, textvariable=cena_14, justify=CENTER, width=14)
        entry_cena_14.insert(0, "145.80")
        entry_cena_14.grid(row=24, column=2)
    elif nazwa_14.get() == "Osłona na przewody":
        entry_cena_14 = Entry(root, textvariable=cena_14, justify=CENTER, width=14)
        entry_cena_14.insert(0, "2.50")
        entry_cena_14.grid(row=24, column=2)
    elif nazwa_14.get() == "Ostrze Arthrex 90(86)x19x1,27":
        entry_cena_14 = Entry(root, textvariable=cena_14, justify=CENTER, width=14)
        entry_cena_14.insert(0, "216")
        entry_cena_14.grid(row=24, column=2)
    elif nazwa_14.get() == "Ostrze piły":
        entry_cena_14 = Entry(root, textvariable=cena_14, justify=CENTER, width=14)
        entry_cena_14.insert(0, "108")
        entry_cena_14.grid(row=24, column=2)
    elif nazwa_14.get() == "Pielęgniarka anest.":
        entry_cena_14 = Entry(root, textvariable=cena_14, justify=CENTER, width=14)
        entry_cena_14.insert(0, "50")
        entry_cena_14.grid(row=24, column=2)
    elif nazwa_14.get() == "Pielęgniarka instr.":
        entry_cena_14 = Entry(root, textvariable=cena_14, justify=CENTER, width=14)
        entry_cena_14.insert(0, "50")
        entry_cena_14.grid(row=24, column=2)
    elif nazwa_14.get() == "Pielęgniarka 'Noviline'":
        entry_cena_14 = Entry(root, textvariable=cena_14, justify=CENTER, width=14)
        entry_cena_14.insert(0, "30")
        entry_cena_14.grid(row=24, column=2)
    elif nazwa_14.get() == "Płytka PeekPower do osteotomii klinowej":
        entry_cena_14 = Entry(root, textvariable=cena_14, justify=CENTER, width=14)
        entry_cena_14.insert(0, "2160")
        entry_cena_14.grid(row=24, column=2)
    elif nazwa_14.get() == "Rękawice jałowe 6,5":
        entry_cena_14 = Entry(root, textvariable=cena_14, justify=CENTER, width=14)
        entry_cena_14.insert(0, "1.20")
        entry_cena_14.grid(row=24, column=2)
    elif nazwa_14.get() == "Rękawice jałowe 7,0":
        entry_cena_14 = Entry(root, textvariable=cena_14, justify=CENTER, width=14)
        entry_cena_14.insert(0, "1.20")
        entry_cena_14.grid(row=24, column=2)
    elif nazwa_14.get() == "Rękawice jałowe 7,5":
        entry_cena_14 = Entry(root, textvariable=cena_14, justify=CENTER, width=14)
        entry_cena_14.insert(0, "1.20")
        entry_cena_14.grid(row=24, column=2)
    elif nazwa_14.get() == "Rękawice jałowe 8,00":
        entry_cena_14 = Entry(root, textvariable=cena_14, justify=CENTER, width=14)
        entry_cena_14.insert(0, "1.20")
        entry_cena_14.grid(row=24, column=2)
    elif nazwa_14.get() == "Rękojeść Interpulse wysokoprzepływowa":
        entry_cena_14 = Entry(root, textvariable=cena_14, justify=CENTER, width=14)
        entry_cena_14.insert(0, "216")
        entry_cena_14.grid(row=24, column=2)
    elif nazwa_14.get() == "Serweta":
        entry_cena_14 = Entry(root, textvariable=cena_14, justify=CENTER, width=14)
        entry_cena_14.insert(0, "6")
        entry_cena_14.grid(row=24, column=2)
    elif nazwa_14.get() == "Simplex Hv z Gentamycyna 10x40g":
        entry_cena_14 = Entry(root, textvariable=cena_14, justify=CENTER, width=14)
        entry_cena_14.insert(0, "162")
        entry_cena_14.grid(row=24, column=2)
    elif nazwa_14.get() == "Skalpel 11":
        entry_cena_14 = Entry(root, textvariable=cena_14, justify=CENTER, width=14)
        entry_cena_14.insert(0, "0.38")
        entry_cena_14.grid(row=24, column=2)
    elif nazwa_14.get() == "Skalpel 13":
        entry_cena_14 = Entry(root, textvariable=cena_14, justify=CENTER, width=14)
        entry_cena_14.insert(0, "1")
        entry_cena_14.grid(row=24, column=2)
    elif nazwa_14.get() == "Skalpel 22":
        entry_cena_14 = Entry(root, textvariable=cena_14, justify=CENTER, width=14)
        entry_cena_14.insert(0, "00000")
        entry_cena_14.grid(row=24, column=2)
    elif nazwa_14.get() == "Śruba blokująca PeekPower do osteotomii":
        entry_cena_14 = Entry(root, textvariable=cena_14, justify=CENTER, width=14)
        entry_cena_14.insert(0, "194")
        entry_cena_14.grid(row=24, column=2)
    elif nazwa_14.get() == "System do mieszania próżniowego":
        entry_cena_14 = Entry(root, textvariable=cena_14, justify=CENTER, width=14)
        entry_cena_14.insert(0, "216")
        entry_cena_14.grid(row=24, column=2)
    elif nazwa_14.get() == "System wprowadzania implantów ACL TightRope":
        entry_cena_14 = Entry(root, textvariable=cena_14, justify=CENTER, width=14)
        entry_cena_14.insert(0, "702")
        entry_cena_14.grid(row=24, column=2)
    elif nazwa_14.get() == "Szew FiberWire 2":
        entry_cena_14 = Entry(root, textvariable=cena_14, justify=CENTER, width=14)
        entry_cena_14.insert(0, "86.40")
        entry_cena_14.grid(row=24, column=2)
    elif nazwa_14.get() == "Taśma przylepna 10x50":
        entry_cena_14 = Entry(root, textvariable=cena_14, justify=CENTER, width=14)
        entry_cena_14.insert(0, "1.04")
        entry_cena_14.grid(row=24, column=2)
    elif nazwa_14.get() == "Triathlon elem. udowy lewy":
        entry_cena_14 = Entry(root, textvariable=cena_14, justify=CENTER, width=14)
        entry_cena_14.insert(0, "3132")
        entry_cena_14.grid(row=24, column=2)
    elif nazwa_14.get() == "Triathlon PS wkładka x3-9mm #4":
        entry_cena_14 = Entry(root, textvariable=cena_14, justify=CENTER, width=14)
        entry_cena_14.insert(0, "756")
        entry_cena_14.grid(row=24, column=2)
    elif nazwa_14.get() == "Triathlon taca piszczelowa":
        entry_cena_14 = Entry(root, textvariable=cena_14, justify=CENTER, width=14)
        entry_cena_14.insert(0, "1296")
        entry_cena_14.grid(row=24, column=2)
    elif nazwa_14.get() == "Wkłady 3L z żelem":
        entry_cena_14 = Entry(root, textvariable=cena_14, justify=CENTER, width=14)
        entry_cena_14.insert(0, "10.26")
        entry_cena_14.grid(row=24, column=2)
    elif nazwa_14.get() == "Zestaw do artroskopii":
        entry_cena_14 = Entry(root, textvariable=cena_14, justify=CENTER, width=14)
        entry_cena_14.insert(0, "67")
        entry_cena_14.grid(row=24, column=2)
    elif nazwa_14.get() == "Zestaw do artroskopii barku":
        entry_cena_14 = Entry(root, textvariable=cena_14, justify=CENTER, width=14)
        entry_cena_14.insert(0, "108")
        entry_cena_14.grid(row=24, column=2)
    elif nazwa_14.get() == "Zestaw do drenażu":
        entry_cena_14 = Entry(root, textvariable=cena_14, justify=CENTER, width=14)
        entry_cena_14.insert(0, "14.23")
        entry_cena_14.grid(row=24, column=2)
    elif nazwa_14.get() == "Zestaw ortopedyczny":
        entry_cena_14 = Entry(root, textvariable=cena_14, justify=CENTER, width=14)
        entry_cena_14.insert(0, "28.08")
        entry_cena_14.grid(row=24, column=2)
    elif nazwa_14.get() == "Gaziki 20 x 10cm":
        entry_cena_14 = Entry(root, textvariable=cena_14, justify=CENTER, width=14)
        entry_cena_14.insert(0, "0.46")
        entry_cena_14.grid(row=24, column=2)
    else:
        entry_cena_14 = Entry(root, textvariable=cena_14, justify=CENTER, width=14, bg="#ffff00")
        entry_cena_14.insert(0, "0")
        entry_cena_14.grid(row=24, column=2)

    if nazwa_15.get() == "--puste--":
        entry_cena_15 = Entry(root, textvariable=cena_15, justify=CENTER, width=14)
        entry_cena_15.insert(0, "0")
        entry_cena_15.grid(row=25, column=2)
    elif nazwa_15.get() == "Ablator":
        entry_cena_15 = Entry(root, textvariable=cena_15, justify=CENTER, width=14)
        entry_cena_15.insert(0, "572")
        entry_cena_15.grid(row=25, column=2)
    elif nazwa_15.get() == "Anestezjolog":
        entry_cena_15 = Entry(root, textvariable=cena_15, justify=CENTER, width=14, bg="#ffff00")
        entry_cena_15.insert(0, "350")
        entry_cena_15.grid(row=25, column=2)
    elif nazwa_15.get() == "Butelka 400ml do długotrwałego odsysania ran j.u. sterylna":
        entry_cena_15 = Entry(root, textvariable=cena_15, justify=CENTER, width=14)
        entry_cena_15.insert(0, "4")
        entry_cena_15.grid(row=25, column=2)
    elif nazwa_15.get() == "Doba":
        entry_cena_15 = Entry(root, textvariable=cena_15, justify=CENTER, width=14)
        entry_cena_15.insert(0, "700")
        entry_cena_15.grid(row=25, column=2)
    elif nazwa_15.get() == "Dren łączący do ssaka Grena":
        entry_cena_15 = Entry(root, textvariable=cena_15, justify=CENTER, width=14)
        entry_cena_15.insert(0, "5")
        entry_cena_15.grid(row=25, column=2)
    elif nazwa_15.get() == "Dren Redona Ch 16 dł. 800mm z trokarem":
        entry_cena_15 = Entry(root, textvariable=cena_15, justify=CENTER, width=14)
        entry_cena_15.insert(0, "29.74")
        entry_cena_15.grid(row=25, column=2)
    elif nazwa_15.get() == "Dren do pompy Artrex":
        entry_cena_15 = Entry(root, textvariable=cena_15, justify=CENTER, width=14)
        entry_cena_15.insert(0, "108")
        entry_cena_15.grid(row=25, column=2)
    elif nazwa_15.get() == "Drut wiercący 2,4 x 311":
        entry_cena_15 = Entry(root, textvariable=cena_15, justify=CENTER, width=14)
        entry_cena_15.insert(0, "139.60")
        entry_cena_15.grid(row=25, column=2)
    elif nazwa_15.get() == "Fartuch jałowy L":
        entry_cena_15 = Entry(root, textvariable=cena_15, justify=CENTER, width=14)
        entry_cena_15.insert(0, "17")
        entry_cena_15.grid(row=25, column=2)
    elif nazwa_15.get() == "Fartuch jałowy M":
        entry_cena_15 = Entry(root, textvariable=cena_15, justify=CENTER, width=14)
        entry_cena_15.insert(0, "15.28")
        entry_cena_15.grid(row=25, column=2)
    elif nazwa_15.get() == "Fartuch jałowy XL":
        entry_cena_15 = Entry(root, textvariable=cena_15, justify=CENTER, width=14)
        entry_cena_15.insert(0, "20.84")
        entry_cena_15.grid(row=25, column=2)
    elif nazwa_15.get() == "FasatThread BioComposite Interference Screw 8x30":
        entry_cena_15 = Entry(root, textvariable=cena_15, justify=CENTER, width=14)
        entry_cena_15.insert(0, "594")
        entry_cena_15.grid(row=25, column=2)
    elif nazwa_15.get() == "Folia operacyjna, jałowa 45cm x 55cm":
        entry_cena_15 = Entry(root, textvariable=cena_15, justify=CENTER, width=14)
        entry_cena_15.insert(0, "9.99")
        entry_cena_15.grid(row=25, column=2)
    elif nazwa_15.get() == "Gaziki 10 x 10cm":
        entry_cena_15 = Entry(root, textvariable=cena_15, justify=CENTER, width=14)
        entry_cena_15.insert(0, "0.10")
        entry_cena_15.grid(row=25, column=2)
    elif nazwa_15.get() == "Igła 0,6 x 60":
        entry_cena_15 = Entry(root, textvariable=cena_15, justify=CENTER, width=14)
        entry_cena_15.insert(0, "0.09")
        entry_cena_15.grid(row=25, column=2)
    elif nazwa_15.get() == "Igła 0,7 x 40":
        entry_cena_15 = Entry(root, textvariable=cena_15, justify=CENTER, width=14)
        entry_cena_15.insert(0, "0.05")
        entry_cena_15.grid(row=25, column=2)
    elif nazwa_15.get() == "Igła 0,8 x 40":
        entry_cena_15 = Entry(root, textvariable=cena_15, justify=CENTER, width=14)
        entry_cena_15.insert(0, "0.05")
        entry_cena_15.grid(row=25, column=2)
    elif nazwa_15.get() == "Igła 1,1 x 70":
        entry_cena_15 = Entry(root, textvariable=cena_15, justify=CENTER, width=14)
        entry_cena_15.insert(0, "0.16")
        entry_cena_15.grid(row=25, column=2)
    elif nazwa_15.get() == "Kaniulowana śruba int. biokompozytowa z osłonką jednoraz.":
        entry_cena_15 = Entry(root, textvariable=cena_15, justify=CENTER, width=14)
        entry_cena_15.insert(0, "594")
        entry_cena_15.grid(row=25, column=2)
    elif nazwa_15.get() == "Kaniulowana śruba int. biokompozytowa z pełnym gwintem":
        entry_cena_15 = Entry(root, textvariable=cena_15, justify=CENTER, width=14)
        entry_cena_15.insert(0, "594")
        entry_cena_15.grid(row=25, column=2)
    elif nazwa_15.get() == "Końcówka do Shavera":
        entry_cena_15 = Entry(root, textvariable=cena_15, justify=CENTER, width=14)
        entry_cena_15.insert(0, "270")
        entry_cena_15.grid(row=25, column=2)
    elif nazwa_15.get() == "Kotwica biokompozytowa SwiveLock":
        entry_cena_15 = Entry(root, textvariable=cena_15, justify=CENTER, width=14)
        entry_cena_15.insert(0, "918")
        entry_cena_15.grid(row=25, column=2)
    elif nazwa_15.get() == "Kotwica Corkscrew":
        entry_cena_15 = Entry(root, textvariable=cena_15, justify=CENTER, width=14)
        entry_cena_15.insert(0, "604")
        entry_cena_15.grid(row=25, column=2)
    elif nazwa_15.get() == "Kotwica FASTak":
        entry_cena_15 = Entry(root, textvariable=cena_15, justify=CENTER, width=14)
        entry_cena_15.insert(0, "432")
        entry_cena_15.grid(row=25, column=2)
    elif nazwa_15.get() == "Kotwica PEEK SwiveLock":
        entry_cena_15 = Entry(root, textvariable=cena_15, justify=CENTER, width=14)
        entry_cena_15.insert(0, "885.60")
        entry_cena_15.grid(row=25, column=2)
    elif nazwa_15.get() == "NaCl 3000ml":
        entry_cena_15 = Entry(root, textvariable=cena_15, justify=CENTER, width=14)
        entry_cena_15.insert(0, "29.72")
        entry_cena_15.grid(row=25, column=2)
    elif nazwa_15.get() == "NaCl 5000ml":
        entry_cena_15 = Entry(root, textvariable=cena_15, justify=CENTER, width=14)
        entry_cena_15.insert(0, "58.33")
        entry_cena_15.grid(row=25, column=2)
    elif nazwa_15.get() == "Nici Dafilon 2-0":
        entry_cena_15 = Entry(root, textvariable=cena_15, justify=CENTER, width=14)
        entry_cena_15.insert(0, "6.60")
        entry_cena_15.grid(row=25, column=2)
    elif nazwa_15.get() == "Nici Novosyn 2":
        entry_cena_15 = Entry(root, textvariable=cena_15, justify=CENTER, width=14)
        entry_cena_15.insert(0, "13")
        entry_cena_15.grid(row=25, column=2)
    elif nazwa_15.get() == "Nici Novosyn 2-0":
        entry_cena_15 = Entry(root, textvariable=cena_15, justify=CENTER, width=14)
        entry_cena_15.insert(0, "7.70")
        entry_cena_15.grid(row=25, column=2)
    elif nazwa_15.get() == "Nici Novosyn 3-0":
        entry_cena_15 = Entry(root, textvariable=cena_15, justify=CENTER, width=14)
        entry_cena_15.insert(0, "7.70")
        entry_cena_15.grid(row=25, column=2)
    elif nazwa_15.get() == "Nici Nylon 2-0":
        entry_cena_15 = Entry(root, textvariable=cena_15, justify=CENTER, width=14)
        entry_cena_15.insert(0, "2.50")
        entry_cena_15.grid(row=25, column=2)
    elif nazwa_15.get() == "Nici Nylon 3-0":
        entry_cena_15 = Entry(root, textvariable=cena_15, justify=CENTER, width=14)
        entry_cena_15.insert(0, "2")
        entry_cena_15.grid(row=25, column=2)
    elif nazwa_15.get() == "Nici PGLA":
        entry_cena_15 = Entry(root, textvariable=cena_15, justify=CENTER, width=14)
        entry_cena_15.insert(0, "11.60")
        entry_cena_15.grid(row=25, column=2)
    elif nazwa_15.get() == "Nici PremiCron 3":
        entry_cena_15 = Entry(root, textvariable=cena_15, justify=CENTER, width=14)
        entry_cena_15.insert(0, "6.50")
        entry_cena_15.grid(row=25, column=2)
    elif nazwa_15.get() == "Nici Vicryl 4-0":
        entry_cena_15 = Entry(root, textvariable=cena_15, justify=CENTER, width=14)
        entry_cena_15.insert(0, "7.50")
        entry_cena_15.grid(row=25, column=2)
    elif nazwa_15.get() == "Nitinol Guide Pin 1.1":
        entry_cena_15 = Entry(root, textvariable=cena_15, justify=CENTER, width=14)
        entry_cena_15.insert(0, "145.80")
        entry_cena_15.grid(row=25, column=2)
    elif nazwa_15.get() == "Osłona na przewody":
        entry_cena_15 = Entry(root, textvariable=cena_15, justify=CENTER, width=14)
        entry_cena_15.insert(0, "2.50")
        entry_cena_15.grid(row=25, column=2)
    elif nazwa_15.get() == "Ostrze Arthrex 90(86)x19x1,27":
        entry_cena_15 = Entry(root, textvariable=cena_15, justify=CENTER, width=14)
        entry_cena_15.insert(0, "216")
        entry_cena_15.grid(row=25, column=2)
    elif nazwa_15.get() == "Ostrze piły":
        entry_cena_15 = Entry(root, textvariable=cena_15, justify=CENTER, width=14)
        entry_cena_15.insert(0, "108")
        entry_cena_15.grid(row=25, column=2)
    elif nazwa_15.get() == "Pielęgniarka anest.":
        entry_cena_15 = Entry(root, textvariable=cena_15, justify=CENTER, width=14)
        entry_cena_15.insert(0, "50")
        entry_cena_15.grid(row=25, column=2)
    elif nazwa_15.get() == "Pielęgniarka instr.":
        entry_cena_15 = Entry(root, textvariable=cena_15, justify=CENTER, width=14)
        entry_cena_15.insert(0, "50")
        entry_cena_15.grid(row=25, column=2)
    elif nazwa_15.get() == "Pielęgniarka 'Noviline'":
        entry_cena_15 = Entry(root, textvariable=cena_15, justify=CENTER, width=14)
        entry_cena_15.insert(0, "30")
        entry_cena_15.grid(row=25, column=2)
    elif nazwa_15.get() == "Płytka PeekPower do osteotomii klinowej":
        entry_cena_15 = Entry(root, textvariable=cena_15, justify=CENTER, width=14)
        entry_cena_15.insert(0, "2160")
        entry_cena_15.grid(row=25, column=2)
    elif nazwa_15.get() == "Rękawice jałowe 6,5":
        entry_cena_15 = Entry(root, textvariable=cena_15, justify=CENTER, width=14)
        entry_cena_15.insert(0, "1.20")
        entry_cena_15.grid(row=25, column=2)
    elif nazwa_15.get() == "Rękawice jałowe 7,0":
        entry_cena_15 = Entry(root, textvariable=cena_15, justify=CENTER, width=14)
        entry_cena_15.insert(0, "1.20")
        entry_cena_15.grid(row=25, column=2)
    elif nazwa_15.get() == "Rękawice jałowe 7,5":
        entry_cena_15 = Entry(root, textvariable=cena_15, justify=CENTER, width=14)
        entry_cena_15.insert(0, "1.20")
        entry_cena_15.grid(row=25, column=2)
    elif nazwa_15.get() == "Rękawice jałowe 8,00":
        entry_cena_15 = Entry(root, textvariable=cena_15, justify=CENTER, width=14)
        entry_cena_15.insert(0, "1.20")
        entry_cena_15.grid(row=25, column=2)
    elif nazwa_15.get() == "Rękojeść Interpulse wysokoprzepływowa":
        entry_cena_15 = Entry(root, textvariable=cena_15, justify=CENTER, width=14)
        entry_cena_15.insert(0, "216")
        entry_cena_15.grid(row=25, column=2)
    elif nazwa_15.get() == "Serweta":
        entry_cena_15 = Entry(root, textvariable=cena_15, justify=CENTER, width=14)
        entry_cena_15.insert(0, "6")
        entry_cena_15.grid(row=25, column=2)
    elif nazwa_15.get() == "Simplex Hv z Gentamycyna 10x40g":
        entry_cena_15 = Entry(root, textvariable=cena_15, justify=CENTER, width=14)
        entry_cena_15.insert(0, "162")
        entry_cena_15.grid(row=25, column=2)
    elif nazwa_15.get() == "Skalpel 11":
        entry_cena_15 = Entry(root, textvariable=cena_15, justify=CENTER, width=14)
        entry_cena_15.insert(0, "0.38")
        entry_cena_15.grid(row=25, column=2)
    elif nazwa_15.get() == "Skalpel 13":
        entry_cena_15 = Entry(root, textvariable=cena_15, justify=CENTER, width=14)
        entry_cena_15.insert(0, "1")
        entry_cena_15.grid(row=25, column=2)
    elif nazwa_15.get() == "Skalpel 22":
        entry_cena_15 = Entry(root, textvariable=cena_15, justify=CENTER, width=14)
        entry_cena_15.insert(0, "00000")
        entry_cena_15.grid(row=25, column=2)
    elif nazwa_15.get() == "Śruba blokująca PeekPower do osteotomii":
        entry_cena_15 = Entry(root, textvariable=cena_15, justify=CENTER, width=14)
        entry_cena_15.insert(0, "194")
        entry_cena_15.grid(row=25, column=2)
    elif nazwa_15.get() == "System do mieszania próżniowego":
        entry_cena_15 = Entry(root, textvariable=cena_15, justify=CENTER, width=14)
        entry_cena_15.insert(0, "216")
        entry_cena_15.grid(row=25, column=2)
    elif nazwa_15.get() == "System wprowadzania implantów ACL TightRope":
        entry_cena_15 = Entry(root, textvariable=cena_15, justify=CENTER, width=14)
        entry_cena_15.insert(0, "702")
        entry_cena_15.grid(row=25, column=2)
    elif nazwa_15.get() == "Szew FiberWire 2":
        entry_cena_15 = Entry(root, textvariable=cena_15, justify=CENTER, width=14)
        entry_cena_15.insert(0, "86.40")
        entry_cena_15.grid(row=25, column=2)
    elif nazwa_15.get() == "Taśma przylepna 10x50":
        entry_cena_15 = Entry(root, textvariable=cena_15, justify=CENTER, width=14)
        entry_cena_15.insert(0, "1.04")
        entry_cena_15.grid(row=25, column=2)
    elif nazwa_15.get() == "Triathlon elem. udowy lewy":
        entry_cena_15 = Entry(root, textvariable=cena_15, justify=CENTER, width=14)
        entry_cena_15.insert(0, "3132")
        entry_cena_15.grid(row=25, column=2)
    elif nazwa_15.get() == "Triathlon PS wkładka x3-9mm #4":
        entry_cena_15 = Entry(root, textvariable=cena_15, justify=CENTER, width=14)
        entry_cena_15.insert(0, "756")
        entry_cena_15.grid(row=25, column=2)
    elif nazwa_15.get() == "Triathlon taca piszczelowa":
        entry_cena_15 = Entry(root, textvariable=cena_15, justify=CENTER, width=14)
        entry_cena_15.insert(0, "1296")
        entry_cena_15.grid(row=25, column=2)
    elif nazwa_15.get() == "Wkłady 3L z żelem":
        entry_cena_15 = Entry(root, textvariable=cena_15, justify=CENTER, width=14)
        entry_cena_15.insert(0, "10.26")
        entry_cena_15.grid(row=25, column=2)
    elif nazwa_15.get() == "Zestaw do artroskopii":
        entry_cena_15 = Entry(root, textvariable=cena_15, justify=CENTER, width=14)
        entry_cena_15.insert(0, "67")
        entry_cena_15.grid(row=25, column=2)
    elif nazwa_15.get() == "Zestaw do artroskopii barku":
        entry_cena_15 = Entry(root, textvariable=cena_15, justify=CENTER, width=14)
        entry_cena_15.insert(0, "108")
        entry_cena_15.grid(row=25, column=2)
    elif nazwa_15.get() == "Zestaw do drenażu":
        entry_cena_15 = Entry(root, textvariable=cena_15, justify=CENTER, width=14)
        entry_cena_15.insert(0, "14.23")
        entry_cena_15.grid(row=25, column=2)
    elif nazwa_15.get() == "Zestaw ortopedyczny":
        entry_cena_15 = Entry(root, textvariable=cena_15, justify=CENTER, width=14)
        entry_cena_15.insert(0, "28.08")
        entry_cena_15.grid(row=25, column=2)
    elif nazwa_15.get() == "Gaziki 20 x 10cm":
        entry_cena_15 = Entry(root, textvariable=cena_15, justify=CENTER, width=14)
        entry_cena_15.insert(0, "0.46")
        entry_cena_15.grid(row=25, column=2)
    else:
        entry_cena_15 = Entry(root, textvariable=cena_15, justify=CENTER, width=14, bg="#ffff00")
        entry_cena_15.insert(0, "0")
        entry_cena_15.grid(row=25, column=2)

    if nazwa_16.get() == "--puste--":
        entry_cena_16 = Entry(root, textvariable=cena_16, justify=CENTER, width=14)
        entry_cena_16.insert(0, "0")
        entry_cena_16.grid(row=26, column=2)
    elif nazwa_16.get() == "Ablator":
        entry_cena_16 = Entry(root, textvariable=cena_16, justify=CENTER, width=14)
        entry_cena_16.insert(0, "572")
        entry_cena_16.grid(row=26, column=2)
    elif nazwa_16.get() == "Anestezjolog":
        entry_cena_16 = Entry(root, textvariable=cena_16, justify=CENTER, width=14, bg="#ffff00")
        entry_cena_16.insert(0, "350")
        entry_cena_16.grid(row=26, column=2)
    elif nazwa_16.get() == "Butelka 400ml do długotrwałego odsysania ran j.u. sterylna":
        entry_cena_16 = Entry(root, textvariable=cena_16, justify=CENTER, width=14)
        entry_cena_16.insert(0, "4")
        entry_cena_16.grid(row=26, column=2)
    elif nazwa_16.get() == "Doba":
        entry_cena_16 = Entry(root, textvariable=cena_16, justify=CENTER, width=14)
        entry_cena_16.insert(0, "700")
        entry_cena_16.grid(row=26, column=2)
    elif nazwa_16.get() == "Dren łączący do ssaka Grena":
        entry_cena_16 = Entry(root, textvariable=cena_16, justify=CENTER, width=14)
        entry_cena_16.insert(0, "5")
        entry_cena_16.grid(row=26, column=2)
    elif nazwa_16.get() == "Dren Redona Ch 16 dł. 800mm z trokarem":
        entry_cena_16 = Entry(root, textvariable=cena_16, justify=CENTER, width=14)
        entry_cena_16.insert(0, "29.74")
        entry_cena_16.grid(row=26, column=2)
    elif nazwa_16.get() == "Dren do pompy Artrex":
        entry_cena_16 = Entry(root, textvariable=cena_16, justify=CENTER, width=14)
        entry_cena_16.insert(0, "108")
        entry_cena_16.grid(row=26, column=2)
    elif nazwa_16.get() == "Drut wiercący 2,4 x 311":
        entry_cena_16 = Entry(root, textvariable=cena_16, justify=CENTER, width=14)
        entry_cena_16.insert(0, "139.60")
        entry_cena_16.grid(row=26, column=2)
    elif nazwa_16.get() == "Fartuch jałowy L":
        entry_cena_16 = Entry(root, textvariable=cena_16, justify=CENTER, width=14)
        entry_cena_16.insert(0, "17")
        entry_cena_16.grid(row=26, column=2)
    elif nazwa_16.get() == "Fartuch jałowy M":
        entry_cena_16 = Entry(root, textvariable=cena_16, justify=CENTER, width=14)
        entry_cena_16.insert(0, "15.28")
        entry_cena_16.grid(row=26, column=2)
    elif nazwa_16.get() == "Fartuch jałowy XL":
        entry_cena_16 = Entry(root, textvariable=cena_16, justify=CENTER, width=14)
        entry_cena_16.insert(0, "20.84")
        entry_cena_16.grid(row=26, column=2)
    elif nazwa_16.get() == "FasatThread BioComposite Interference Screw 8x30":
        entry_cena_16 = Entry(root, textvariable=cena_16, justify=CENTER, width=14)
        entry_cena_16.insert(0, "594")
        entry_cena_16.grid(row=26, column=2)
    elif nazwa_16.get() == "Folia operacyjna, jałowa 45cm x 55cm":
        entry_cena_16 = Entry(root, textvariable=cena_16, justify=CENTER, width=14)
        entry_cena_16.insert(0, "9.99")
        entry_cena_16.grid(row=26, column=2)
    elif nazwa_16.get() == "Gaziki 10 x 10cm":
        entry_cena_16 = Entry(root, textvariable=cena_16, justify=CENTER, width=14)
        entry_cena_16.insert(0, "0.10")
        entry_cena_16.grid(row=26, column=2)
    elif nazwa_16.get() == "Igła 0,6 x 60":
        entry_cena_16 = Entry(root, textvariable=cena_16, justify=CENTER, width=14)
        entry_cena_16.insert(0, "0.09")
        entry_cena_16.grid(row=26, column=2)
    elif nazwa_16.get() == "Igła 0,7 x 40":
        entry_cena_16 = Entry(root, textvariable=cena_16, justify=CENTER, width=14)
        entry_cena_16.insert(0, "0.05")
        entry_cena_16.grid(row=26, column=2)
    elif nazwa_16.get() == "Igła 0,8 x 40":
        entry_cena_16 = Entry(root, textvariable=cena_16, justify=CENTER, width=14)
        entry_cena_16.insert(0, "0.05")
        entry_cena_16.grid(row=26, column=2)
    elif nazwa_16.get() == "Igła 1,1 x 70":
        entry_cena_16 = Entry(root, textvariable=cena_16, justify=CENTER, width=14)
        entry_cena_16.insert(0, "0.16")
        entry_cena_16.grid(row=26, column=2)
    elif nazwa_16.get() == "Kaniulowana śruba int. biokompozytowa z osłonką jednoraz.":
        entry_cena_16 = Entry(root, textvariable=cena_16, justify=CENTER, width=14)
        entry_cena_16.insert(0, "594")
        entry_cena_16.grid(row=26, column=2)
    elif nazwa_16.get() == "Kaniulowana śruba int. biokompozytowa z pełnym gwintem":
        entry_cena_16 = Entry(root, textvariable=cena_16, justify=CENTER, width=14)
        entry_cena_16.insert(0, "594")
        entry_cena_16.grid(row=26, column=2)
    elif nazwa_16.get() == "Końcówka do Shavera":
        entry_cena_16 = Entry(root, textvariable=cena_16, justify=CENTER, width=14)
        entry_cena_16.insert(0, "270")
        entry_cena_16.grid(row=26, column=2)
    elif nazwa_16.get() == "Kotwica biokompozytowa SwiveLock":
        entry_cena_16 = Entry(root, textvariable=cena_16, justify=CENTER, width=14)
        entry_cena_16.insert(0, "918")
        entry_cena_16.grid(row=26, column=2)
    elif nazwa_16.get() == "Kotwica Corkscrew":
        entry_cena_16 = Entry(root, textvariable=cena_16, justify=CENTER, width=14)
        entry_cena_16.insert(0, "604")
        entry_cena_16.grid(row=26, column=2)
    elif nazwa_16.get() == "Kotwica FASTak":
        entry_cena_16 = Entry(root, textvariable=cena_16, justify=CENTER, width=14)
        entry_cena_16.insert(0, "432")
        entry_cena_16.grid(row=26, column=2)
    elif nazwa_16.get() == "Kotwica PEEK SwiveLock":
        entry_cena_16 = Entry(root, textvariable=cena_16, justify=CENTER, width=14)
        entry_cena_16.insert(0, "885.60")
        entry_cena_16.grid(row=26, column=2)
    elif nazwa_16.get() == "NaCl 3000ml":
        entry_cena_16 = Entry(root, textvariable=cena_16, justify=CENTER, width=14)
        entry_cena_16.insert(0, "29.72")
        entry_cena_16.grid(row=26, column=2)
    elif nazwa_16.get() == "NaCl 5000ml":
        entry_cena_16 = Entry(root, textvariable=cena_16, justify=CENTER, width=14)
        entry_cena_16.insert(0, "58.33")
        entry_cena_16.grid(row=26, column=2)
    elif nazwa_16.get() == "Nici Dafilon 2-0":
        entry_cena_16 = Entry(root, textvariable=cena_16, justify=CENTER, width=14)
        entry_cena_16.insert(0, "6.60")
        entry_cena_16.grid(row=26, column=2)
    elif nazwa_16.get() == "Nici Novosyn 2":
        entry_cena_16 = Entry(root, textvariable=cena_16, justify=CENTER, width=14)
        entry_cena_16.insert(0, "13")
        entry_cena_16.grid(row=26, column=2)
    elif nazwa_16.get() == "Nici Novosyn 2-0":
        entry_cena_16 = Entry(root, textvariable=cena_16, justify=CENTER, width=14)
        entry_cena_16.insert(0, "7.70")
        entry_cena_16.grid(row=26, column=2)
    elif nazwa_16.get() == "Nici Novosyn 3-0":
        entry_cena_16 = Entry(root, textvariable=cena_16, justify=CENTER, width=14)
        entry_cena_16.insert(0, "7.70")
        entry_cena_16.grid(row=26, column=2)
    elif nazwa_16.get() == "Nici Nylon 2-0":
        entry_cena_16 = Entry(root, textvariable=cena_16, justify=CENTER, width=14)
        entry_cena_16.insert(0, "2.50")
        entry_cena_16.grid(row=26, column=2)
    elif nazwa_16.get() == "Nici Nylon 3-0":
        entry_cena_16 = Entry(root, textvariable=cena_16, justify=CENTER, width=14)
        entry_cena_16.insert(0, "2")
        entry_cena_16.grid(row=26, column=2)
    elif nazwa_16.get() == "Nici PGLA":
        entry_cena_16 = Entry(root, textvariable=cena_16, justify=CENTER, width=14)
        entry_cena_16.insert(0, "11.60")
        entry_cena_16.grid(row=26, column=2)
    elif nazwa_16.get() == "Nici PremiCron 3":
        entry_cena_16 = Entry(root, textvariable=cena_16, justify=CENTER, width=14)
        entry_cena_16.insert(0, "6.50")
        entry_cena_16.grid(row=26, column=2)
    elif nazwa_16.get() == "Nici Vicryl 4-0":
        entry_cena_16 = Entry(root, textvariable=cena_16, justify=CENTER, width=14)
        entry_cena_16.insert(0, "7.50")
        entry_cena_16.grid(row=26, column=2)
    elif nazwa_16.get() == "Nitinol Guide Pin 1.1":
        entry_cena_16 = Entry(root, textvariable=cena_16, justify=CENTER, width=14)
        entry_cena_16.insert(0, "145.80")
        entry_cena_16.grid(row=26, column=2)
    elif nazwa_16.get() == "Osłona na przewody":
        entry_cena_16 = Entry(root, textvariable=cena_16, justify=CENTER, width=14)
        entry_cena_16.insert(0, "2.50")
        entry_cena_16.grid(row=26, column=2)
    elif nazwa_16.get() == "Ostrze Arthrex 90(86)x19x1,27":
        entry_cena_16 = Entry(root, textvariable=cena_16, justify=CENTER, width=14)
        entry_cena_16.insert(0, "216")
        entry_cena_16.grid(row=26, column=2)
    elif nazwa_16.get() == "Ostrze piły":
        entry_cena_16 = Entry(root, textvariable=cena_16, justify=CENTER, width=14)
        entry_cena_16.insert(0, "108")
        entry_cena_16.grid(row=26, column=2)
    elif nazwa_16.get() == "Pielęgniarka anest.":
        entry_cena_16 = Entry(root, textvariable=cena_16, justify=CENTER, width=14)
        entry_cena_16.insert(0, "50")
        entry_cena_16.grid(row=26, column=2)
    elif nazwa_16.get() == "Pielęgniarka instr.":
        entry_cena_16 = Entry(root, textvariable=cena_16, justify=CENTER, width=14)
        entry_cena_16.insert(0, "50")
        entry_cena_16.grid(row=26, column=2)
    elif nazwa_16.get() == "Pielęgniarka 'Noviline'":
        entry_cena_16 = Entry(root, textvariable=cena_16, justify=CENTER, width=14)
        entry_cena_16.insert(0, "30")
        entry_cena_16.grid(row=26, column=2)
    elif nazwa_16.get() == "Płytka PeekPower do osteotomii klinowej":
        entry_cena_16 = Entry(root, textvariable=cena_16, justify=CENTER, width=14)
        entry_cena_16.insert(0, "2160")
        entry_cena_16.grid(row=26, column=2)
    elif nazwa_16.get() == "Rękawice jałowe 6,5":
        entry_cena_16 = Entry(root, textvariable=cena_16, justify=CENTER, width=14)
        entry_cena_16.insert(0, "1.20")
        entry_cena_16.grid(row=26, column=2)
    elif nazwa_16.get() == "Rękawice jałowe 7,0":
        entry_cena_16 = Entry(root, textvariable=cena_16, justify=CENTER, width=14)
        entry_cena_16.insert(0, "1.20")
        entry_cena_16.grid(row=26, column=2)
    elif nazwa_16.get() == "Rękawice jałowe 7,5":
        entry_cena_16 = Entry(root, textvariable=cena_16, justify=CENTER, width=14)
        entry_cena_16.insert(0, "1.20")
        entry_cena_16.grid(row=26, column=2)
    elif nazwa_16.get() == "Rękawice jałowe 8,00":
        entry_cena_16 = Entry(root, textvariable=cena_16, justify=CENTER, width=14)
        entry_cena_16.insert(0, "1.20")
        entry_cena_16.grid(row=26, column=2)
    elif nazwa_16.get() == "Rękojeść Interpulse wysokoprzepływowa":
        entry_cena_16 = Entry(root, textvariable=cena_16, justify=CENTER, width=14)
        entry_cena_16.insert(0, "216")
        entry_cena_16.grid(row=26, column=2)
    elif nazwa_16.get() == "Serweta":
        entry_cena_16 = Entry(root, textvariable=cena_16, justify=CENTER, width=14)
        entry_cena_16.insert(0, "6")
        entry_cena_16.grid(row=26, column=2)
    elif nazwa_16.get() == "Simplex Hv z Gentamycyna 10x40g":
        entry_cena_16 = Entry(root, textvariable=cena_16, justify=CENTER, width=14)
        entry_cena_16.insert(0, "162")
        entry_cena_16.grid(row=26, column=2)
    elif nazwa_16.get() == "Skalpel 11":
        entry_cena_16 = Entry(root, textvariable=cena_16, justify=CENTER, width=14)
        entry_cena_16.insert(0, "0.38")
        entry_cena_16.grid(row=26, column=2)
    elif nazwa_16.get() == "Skalpel 13":
        entry_cena_16 = Entry(root, textvariable=cena_16, justify=CENTER, width=14)
        entry_cena_16.insert(0, "1")
        entry_cena_16.grid(row=26, column=2)
    elif nazwa_16.get() == "Skalpel 22":
        entry_cena_16 = Entry(root, textvariable=cena_16, justify=CENTER, width=14)
        entry_cena_16.insert(0, "00000")
        entry_cena_16.grid(row=26, column=2)
    elif nazwa_16.get() == "Śruba blokująca PeekPower do osteotomii":
        entry_cena_16 = Entry(root, textvariable=cena_16, justify=CENTER, width=14)
        entry_cena_16.insert(0, "194")
        entry_cena_16.grid(row=26, column=2)
    elif nazwa_16.get() == "System do mieszania próżniowego":
        entry_cena_16 = Entry(root, textvariable=cena_16, justify=CENTER, width=14)
        entry_cena_16.insert(0, "216")
        entry_cena_16.grid(row=26, column=2)
    elif nazwa_16.get() == "System wprowadzania implantów ACL TightRope":
        entry_cena_16 = Entry(root, textvariable=cena_16, justify=CENTER, width=14)
        entry_cena_16.insert(0, "702")
        entry_cena_16.grid(row=26, column=2)
    elif nazwa_16.get() == "Szew FiberWire 2":
        entry_cena_16 = Entry(root, textvariable=cena_16, justify=CENTER, width=14)
        entry_cena_16.insert(0, "86.40")
        entry_cena_16.grid(row=26, column=2)
    elif nazwa_16.get() == "Taśma przylepna 10x50":
        entry_cena_16 = Entry(root, textvariable=cena_16, justify=CENTER, width=14)
        entry_cena_16.insert(0, "1.04")
        entry_cena_16.grid(row=26, column=2)
    elif nazwa_16.get() == "Triathlon elem. udowy lewy":
        entry_cena_16 = Entry(root, textvariable=cena_16, justify=CENTER, width=14)
        entry_cena_16.insert(0, "3132")
        entry_cena_16.grid(row=26, column=2)
    elif nazwa_16.get() == "Triathlon PS wkładka x3-9mm #4":
        entry_cena_16 = Entry(root, textvariable=cena_16, justify=CENTER, width=14)
        entry_cena_16.insert(0, "756")
        entry_cena_16.grid(row=26, column=2)
    elif nazwa_16.get() == "Triathlon taca piszczelowa":
        entry_cena_16 = Entry(root, textvariable=cena_16, justify=CENTER, width=14)
        entry_cena_16.insert(0, "1296")
        entry_cena_16.grid(row=26, column=2)
    elif nazwa_16.get() == "Wkłady 3L z żelem":
        entry_cena_16 = Entry(root, textvariable=cena_16, justify=CENTER, width=14)
        entry_cena_16.insert(0, "10.26")
        entry_cena_16.grid(row=26, column=2)
    elif nazwa_16.get() == "Zestaw do artroskopii":
        entry_cena_16 = Entry(root, textvariable=cena_16, justify=CENTER, width=14)
        entry_cena_16.insert(0, "67")
        entry_cena_16.grid(row=26, column=2)
    elif nazwa_16.get() == "Zestaw do artroskopii barku":
        entry_cena_16 = Entry(root, textvariable=cena_16, justify=CENTER, width=14)
        entry_cena_16.insert(0, "108")
        entry_cena_16.grid(row=26, column=2)
    elif nazwa_16.get() == "Zestaw do drenażu":
        entry_cena_16 = Entry(root, textvariable=cena_16, justify=CENTER, width=14)
        entry_cena_16.insert(0, "14.23")
        entry_cena_16.grid(row=26, column=2)
    elif nazwa_16.get() == "Zestaw ortopedyczny":
        entry_cena_16 = Entry(root, textvariable=cena_16, justify=CENTER, width=14)
        entry_cena_16.insert(0, "28.08")
        entry_cena_16.grid(row=26, column=2)
    elif nazwa_16.get() == "Gaziki 20 x 10cm":
        entry_cena_16 = Entry(root, textvariable=cena_16, justify=CENTER, width=14)
        entry_cena_16.insert(0, "0.46")
        entry_cena_16.grid(row=26, column=2)
    else:
        entry_cena_16 = Entry(root, textvariable=cena_16, justify=CENTER, width=14, bg="#ffff00")
        entry_cena_16.insert(0, "0")
        entry_cena_16.grid(row=26, column=2)

    if nazwa_17.get() == "--puste--":
        entry_cena_17 = Entry(root, textvariable=cena_17, justify=CENTER, width=14)
        entry_cena_17.insert(0, "0")
        entry_cena_17.grid(row=27, column=2)
    elif nazwa_17.get() == "Ablator":
        entry_cena_17 = Entry(root, textvariable=cena_17, justify=CENTER, width=14)
        entry_cena_17.insert(0, "572")
        entry_cena_17.grid(row=27, column=2)
    elif nazwa_17.get() == "Anestezjolog":
        entry_cena_17 = Entry(root, textvariable=cena_17, justify=CENTER, width=14, bg="#ffff00")
        entry_cena_17.insert(0, "350")
        entry_cena_17.grid(row=27, column=2)
    elif nazwa_17.get() == "Butelka 400ml do długotrwałego odsysania ran j.u. sterylna":
        entry_cena_17 = Entry(root, textvariable=cena_17, justify=CENTER, width=14)
        entry_cena_17.insert(0, "4")
        entry_cena_17.grid(row=27, column=2)
    elif nazwa_17.get() == "Doba":
        entry_cena_17 = Entry(root, textvariable=cena_17, justify=CENTER, width=14)
        entry_cena_17.insert(0, "700")
        entry_cena_17.grid(row=27, column=2)
    elif nazwa_17.get() == "Dren łączący do ssaka Grena":
        entry_cena_17 = Entry(root, textvariable=cena_17, justify=CENTER, width=14)
        entry_cena_17.insert(0, "5")
        entry_cena_17.grid(row=27, column=2)
    elif nazwa_17.get() == "Dren Redona Ch 16 dł. 800mm z trokarem":
        entry_cena_17 = Entry(root, textvariable=cena_17, justify=CENTER, width=14)
        entry_cena_17.insert(0, "29.74")
        entry_cena_17.grid(row=27, column=2)
    elif nazwa_17.get() == "Dren do pompy Artrex":
        entry_cena_17 = Entry(root, textvariable=cena_17, justify=CENTER, width=14)
        entry_cena_17.insert(0, "108")
        entry_cena_17.grid(row=27, column=2)
    elif nazwa_17.get() == "Drut wiercący 2,4 x 311":
        entry_cena_17 = Entry(root, textvariable=cena_17, justify=CENTER, width=14)
        entry_cena_17.insert(0, "139.60")
        entry_cena_17.grid(row=27, column=2)
    elif nazwa_17.get() == "Fartuch jałowy L":
        entry_cena_17 = Entry(root, textvariable=cena_17, justify=CENTER, width=14)
        entry_cena_17.insert(0, "17")
        entry_cena_17.grid(row=27, column=2)
    elif nazwa_17.get() == "Fartuch jałowy M":
        entry_cena_17 = Entry(root, textvariable=cena_17, justify=CENTER, width=14)
        entry_cena_17.insert(0, "15.28")
        entry_cena_17.grid(row=27, column=2)
    elif nazwa_17.get() == "Fartuch jałowy XL":
        entry_cena_17 = Entry(root, textvariable=cena_17, justify=CENTER, width=14)
        entry_cena_17.insert(0, "20.84")
        entry_cena_17.grid(row=27, column=2)
    elif nazwa_17.get() == "FasatThread BioComposite Interference Screw 8x30":
        entry_cena_17 = Entry(root, textvariable=cena_17, justify=CENTER, width=14)
        entry_cena_17.insert(0, "594")
        entry_cena_17.grid(row=27, column=2)
    elif nazwa_17.get() == "Folia operacyjna, jałowa 45cm x 55cm":
        entry_cena_17 = Entry(root, textvariable=cena_17, justify=CENTER, width=14)
        entry_cena_17.insert(0, "9.99")
        entry_cena_17.grid(row=27, column=2)
    elif nazwa_17.get() == "Gaziki 10 x 10cm":
        entry_cena_17 = Entry(root, textvariable=cena_17, justify=CENTER, width=14)
        entry_cena_17.insert(0, "0.10")
        entry_cena_17.grid(row=27, column=2)
    elif nazwa_17.get() == "Igła 0,6 x 60":
        entry_cena_17 = Entry(root, textvariable=cena_17, justify=CENTER, width=14)
        entry_cena_17.insert(0, "0.09")
        entry_cena_17.grid(row=27, column=2)
    elif nazwa_17.get() == "Igła 0,7 x 40":
        entry_cena_17 = Entry(root, textvariable=cena_17, justify=CENTER, width=14)
        entry_cena_17.insert(0, "0.05")
        entry_cena_17.grid(row=27, column=2)
    elif nazwa_17.get() == "Igła 0,8 x 40":
        entry_cena_17 = Entry(root, textvariable=cena_17, justify=CENTER, width=14)
        entry_cena_17.insert(0, "0.05")
        entry_cena_17.grid(row=27, column=2)
    elif nazwa_17.get() == "Igła 1,1 x 70":
        entry_cena_17 = Entry(root, textvariable=cena_17, justify=CENTER, width=14)
        entry_cena_17.insert(0, "0.16")
        entry_cena_17.grid(row=27, column=2)
    elif nazwa_17.get() == "Kaniulowana śruba int. biokompozytowa z osłonką jednoraz.":
        entry_cena_17 = Entry(root, textvariable=cena_17, justify=CENTER, width=14)
        entry_cena_17.insert(0, "594")
        entry_cena_17.grid(row=27, column=2)
    elif nazwa_17.get() == "Kaniulowana śruba int. biokompozytowa z pełnym gwintem":
        entry_cena_17 = Entry(root, textvariable=cena_17, justify=CENTER, width=14)
        entry_cena_17.insert(0, "594")
        entry_cena_17.grid(row=27, column=2)
    elif nazwa_17.get() == "Końcówka do Shavera":
        entry_cena_17 = Entry(root, textvariable=cena_17, justify=CENTER, width=14)
        entry_cena_17.insert(0, "270")
        entry_cena_17.grid(row=27, column=2)
    elif nazwa_17.get() == "Kotwica biokompozytowa SwiveLock":
        entry_cena_17 = Entry(root, textvariable=cena_17, justify=CENTER, width=14)
        entry_cena_17.insert(0, "918")
        entry_cena_17.grid(row=27, column=2)
    elif nazwa_17.get() == "Kotwica Corkscrew":
        entry_cena_17 = Entry(root, textvariable=cena_17, justify=CENTER, width=14)
        entry_cena_17.insert(0, "604")
        entry_cena_17.grid(row=27, column=2)
    elif nazwa_17.get() == "Kotwica FASTak":
        entry_cena_17 = Entry(root, textvariable=cena_17, justify=CENTER, width=14)
        entry_cena_17.insert(0, "432")
        entry_cena_17.grid(row=27, column=2)
    elif nazwa_17.get() == "Kotwica PEEK SwiveLock":
        entry_cena_17 = Entry(root, textvariable=cena_17, justify=CENTER, width=14)
        entry_cena_17.insert(0, "885.60")
        entry_cena_17.grid(row=27, column=2)
    elif nazwa_17.get() == "NaCl 3000ml":
        entry_cena_17 = Entry(root, textvariable=cena_17, justify=CENTER, width=14)
        entry_cena_17.insert(0, "29.72")
        entry_cena_17.grid(row=27, column=2)
    elif nazwa_17.get() == "NaCl 5000ml":
        entry_cena_17 = Entry(root, textvariable=cena_17, justify=CENTER, width=14)
        entry_cena_17.insert(0, "58.33")
        entry_cena_17.grid(row=27, column=2)
    elif nazwa_17.get() == "Nici Dafilon 2-0":
        entry_cena_17 = Entry(root, textvariable=cena_17, justify=CENTER, width=14)
        entry_cena_17.insert(0, "6.60")
        entry_cena_17.grid(row=27, column=2)
    elif nazwa_17.get() == "Nici Novosyn 2":
        entry_cena_17 = Entry(root, textvariable=cena_17, justify=CENTER, width=14)
        entry_cena_17.insert(0, "13")
        entry_cena_17.grid(row=27, column=2)
    elif nazwa_17.get() == "Nici Novosyn 2-0":
        entry_cena_17 = Entry(root, textvariable=cena_17, justify=CENTER, width=14)
        entry_cena_17.insert(0, "7.70")
        entry_cena_17.grid(row=27, column=2)
    elif nazwa_17.get() == "Nici Novosyn 3-0":
        entry_cena_17 = Entry(root, textvariable=cena_17, justify=CENTER, width=14)
        entry_cena_17.insert(0, "7.70")
        entry_cena_17.grid(row=27, column=2)
    elif nazwa_17.get() == "Nici Nylon 2-0":
        entry_cena_17 = Entry(root, textvariable=cena_17, justify=CENTER, width=14)
        entry_cena_17.insert(0, "2.50")
        entry_cena_17.grid(row=27, column=2)
    elif nazwa_17.get() == "Nici Nylon 3-0":
        entry_cena_17 = Entry(root, textvariable=cena_17, justify=CENTER, width=14)
        entry_cena_17.insert(0, "2")
        entry_cena_17.grid(row=27, column=2)
    elif nazwa_17.get() == "Nici PGLA":
        entry_cena_17 = Entry(root, textvariable=cena_17, justify=CENTER, width=14)
        entry_cena_17.insert(0, "11.60")
        entry_cena_17.grid(row=27, column=2)
    elif nazwa_17.get() == "Nici PremiCron 3":
        entry_cena_17 = Entry(root, textvariable=cena_17, justify=CENTER, width=14)
        entry_cena_17.insert(0, "6.50")
        entry_cena_17.grid(row=27, column=2)
    elif nazwa_17.get() == "Nici Vicryl 4-0":
        entry_cena_17 = Entry(root, textvariable=cena_17, justify=CENTER, width=14)
        entry_cena_17.insert(0, "7.50")
        entry_cena_17.grid(row=27, column=2)
    elif nazwa_17.get() == "Nitinol Guide Pin 1.1":
        entry_cena_17 = Entry(root, textvariable=cena_17, justify=CENTER, width=14)
        entry_cena_17.insert(0, "145.80")
        entry_cena_17.grid(row=27, column=2)
    elif nazwa_17.get() == "Osłona na przewody":
        entry_cena_17 = Entry(root, textvariable=cena_17, justify=CENTER, width=14)
        entry_cena_17.insert(0, "2.50")
        entry_cena_17.grid(row=27, column=2)
    elif nazwa_17.get() == "Ostrze Arthrex 90(86)x19x1,27":
        entry_cena_17 = Entry(root, textvariable=cena_17, justify=CENTER, width=14)
        entry_cena_17.insert(0, "216")
        entry_cena_17.grid(row=27, column=2)
    elif nazwa_17.get() == "Ostrze piły":
        entry_cena_17 = Entry(root, textvariable=cena_17, justify=CENTER, width=14)
        entry_cena_17.insert(0, "108")
        entry_cena_17.grid(row=27, column=2)
    elif nazwa_17.get() == "Pielęgniarka anest.":
        entry_cena_17 = Entry(root, textvariable=cena_17, justify=CENTER, width=14)
        entry_cena_17.insert(0, "50")
        entry_cena_17.grid(row=27, column=2)
    elif nazwa_17.get() == "Pielęgniarka instr.":
        entry_cena_17 = Entry(root, textvariable=cena_17, justify=CENTER, width=14)
        entry_cena_17.insert(0, "50")
        entry_cena_17.grid(row=27, column=2)
    elif nazwa_17.get() == "Pielęgniarka 'Noviline'":
        entry_cena_17 = Entry(root, textvariable=cena_17, justify=CENTER, width=14)
        entry_cena_17.insert(0, "30")
        entry_cena_17.grid(row=27, column=2)
    elif nazwa_17.get() == "Płytka PeekPower do osteotomii klinowej":
        entry_cena_17 = Entry(root, textvariable=cena_17, justify=CENTER, width=14)
        entry_cena_17.insert(0, "2160")
        entry_cena_17.grid(row=27, column=2)
    elif nazwa_17.get() == "Rękawice jałowe 6,5":
        entry_cena_17 = Entry(root, textvariable=cena_17, justify=CENTER, width=14)
        entry_cena_17.insert(0, "1.20")
        entry_cena_17.grid(row=27, column=2)
    elif nazwa_17.get() == "Rękawice jałowe 7,0":
        entry_cena_17 = Entry(root, textvariable=cena_17, justify=CENTER, width=14)
        entry_cena_17.insert(0, "1.20")
        entry_cena_17.grid(row=27, column=2)
    elif nazwa_17.get() == "Rękawice jałowe 7,5":
        entry_cena_17 = Entry(root, textvariable=cena_17, justify=CENTER, width=14)
        entry_cena_17.insert(0, "1.20")
        entry_cena_17.grid(row=27, column=2)
    elif nazwa_17.get() == "Rękawice jałowe 8,00":
        entry_cena_17 = Entry(root, textvariable=cena_17, justify=CENTER, width=14)
        entry_cena_17.insert(0, "1.20")
        entry_cena_17.grid(row=27, column=2)
    elif nazwa_17.get() == "Rękojeść Interpulse wysokoprzepływowa":
        entry_cena_17 = Entry(root, textvariable=cena_17, justify=CENTER, width=14)
        entry_cena_17.insert(0, "216")
        entry_cena_17.grid(row=27, column=2)
    elif nazwa_17.get() == "Serweta":
        entry_cena_17 = Entry(root, textvariable=cena_17, justify=CENTER, width=14)
        entry_cena_17.insert(0, "6")
        entry_cena_17.grid(row=27, column=2)
    elif nazwa_17.get() == "Simplex Hv z Gentamycyna 10x40g":
        entry_cena_17 = Entry(root, textvariable=cena_17, justify=CENTER, width=14)
        entry_cena_17.insert(0, "162")
        entry_cena_17.grid(row=27, column=2)
    elif nazwa_17.get() == "Skalpel 11":
        entry_cena_17 = Entry(root, textvariable=cena_17, justify=CENTER, width=14)
        entry_cena_17.insert(0, "0.38")
        entry_cena_17.grid(row=27, column=2)
    elif nazwa_17.get() == "Skalpel 13":
        entry_cena_17 = Entry(root, textvariable=cena_17, justify=CENTER, width=14)
        entry_cena_17.insert(0, "1")
        entry_cena_17.grid(row=27, column=2)
    elif nazwa_17.get() == "Skalpel 22":
        entry_cena_17 = Entry(root, textvariable=cena_17, justify=CENTER, width=14)
        entry_cena_17.insert(0, "00000")
        entry_cena_17.grid(row=27, column=2)
    elif nazwa_17.get() == "Śruba blokująca PeekPower do osteotomii":
        entry_cena_17 = Entry(root, textvariable=cena_17, justify=CENTER, width=14)
        entry_cena_17.insert(0, "194")
        entry_cena_17.grid(row=27, column=2)
    elif nazwa_17.get() == "System do mieszania próżniowego":
        entry_cena_17 = Entry(root, textvariable=cena_17, justify=CENTER, width=14)
        entry_cena_17.insert(0, "216")
        entry_cena_17.grid(row=27, column=2)
    elif nazwa_17.get() == "System wprowadzania implantów ACL TightRope":
        entry_cena_17 = Entry(root, textvariable=cena_17, justify=CENTER, width=14)
        entry_cena_17.insert(0, "702")
        entry_cena_17.grid(row=27, column=2)
    elif nazwa_17.get() == "Szew FiberWire 2":
        entry_cena_17 = Entry(root, textvariable=cena_17, justify=CENTER, width=14)
        entry_cena_17.insert(0, "86.40")
        entry_cena_17.grid(row=27, column=2)
    elif nazwa_17.get() == "Taśma przylepna 10x50":
        entry_cena_17 = Entry(root, textvariable=cena_17, justify=CENTER, width=14)
        entry_cena_17.insert(0, "1.04")
        entry_cena_17.grid(row=27, column=2)
    elif nazwa_17.get() == "Triathlon elem. udowy lewy":
        entry_cena_17 = Entry(root, textvariable=cena_17, justify=CENTER, width=14)
        entry_cena_17.insert(0, "3132")
        entry_cena_17.grid(row=27, column=2)
    elif nazwa_17.get() == "Triathlon PS wkładka x3-9mm #4":
        entry_cena_17 = Entry(root, textvariable=cena_17, justify=CENTER, width=14)
        entry_cena_17.insert(0, "756")
        entry_cena_17.grid(row=27, column=2)
    elif nazwa_17.get() == "Triathlon taca piszczelowa":
        entry_cena_17 = Entry(root, textvariable=cena_17, justify=CENTER, width=14)
        entry_cena_17.insert(0, "1296")
        entry_cena_17.grid(row=27, column=2)
    elif nazwa_17.get() == "Wkłady 3L z żelem":
        entry_cena_17 = Entry(root, textvariable=cena_17, justify=CENTER, width=14)
        entry_cena_17.insert(0, "10.26")
        entry_cena_17.grid(row=27, column=2)
    elif nazwa_17.get() == "Zestaw do artroskopii":
        entry_cena_17 = Entry(root, textvariable=cena_17, justify=CENTER, width=14)
        entry_cena_17.insert(0, "67")
        entry_cena_17.grid(row=27, column=2)
    elif nazwa_17.get() == "Zestaw do artroskopii barku":
        entry_cena_17 = Entry(root, textvariable=cena_17, justify=CENTER, width=14)
        entry_cena_17.insert(0, "108")
        entry_cena_17.grid(row=27, column=2)
    elif nazwa_17.get() == "Zestaw do drenażu":
        entry_cena_17 = Entry(root, textvariable=cena_17, justify=CENTER, width=14)
        entry_cena_17.insert(0, "14.23")
        entry_cena_17.grid(row=27, column=2)
    elif nazwa_17.get() == "Zestaw ortopedyczny":
        entry_cena_17 = Entry(root, textvariable=cena_17, justify=CENTER, width=14)
        entry_cena_17.insert(0, "28.08")
        entry_cena_17.grid(row=27, column=2)
    elif nazwa_17.get() == "Gaziki 20 x 10cm":
        entry_cena_17 = Entry(root, textvariable=cena_17, justify=CENTER, width=14)
        entry_cena_17.insert(0, "0.46")
        entry_cena_17.grid(row=27, column=2)
    else:
        entry_cena_17 = Entry(root, textvariable=cena_17, justify=CENTER, width=14, bg="#ffff00")
        entry_cena_17.insert(0, "0")
        entry_cena_17.grid(row=27, column=2)

    if nazwa_18.get() == "--puste--":
        entry_cena_18 = Entry(root, textvariable=cena_18, justify=CENTER, width=14)
        entry_cena_18.insert(0, "0")
        entry_cena_18.grid(row=28, column=2)
    elif nazwa_18.get() == "Ablator":
        entry_cena_18 = Entry(root, textvariable=cena_18, justify=CENTER, width=14)
        entry_cena_18.insert(0, "572")
        entry_cena_18.grid(row=28, column=2)
    elif nazwa_18.get() == "Anestezjolog":
        entry_cena_18 = Entry(root, textvariable=cena_18, justify=CENTER, width=14, bg="#ffff00")
        entry_cena_18.insert(0, "350")
        entry_cena_18.grid(row=28, column=2)
    elif nazwa_18.get() == "Butelka 400ml do długotrwałego odsysania ran j.u. sterylna":
        entry_cena_18 = Entry(root, textvariable=cena_18, justify=CENTER, width=14)
        entry_cena_18.insert(0, "4")
        entry_cena_18.grid(row=28, column=2)
    elif nazwa_18.get() == "Doba":
        entry_cena_18 = Entry(root, textvariable=cena_18, justify=CENTER, width=14)
        entry_cena_18.insert(0, "700")
        entry_cena_18.grid(row=28, column=2)
    elif nazwa_18.get() == "Dren łączący do ssaka Grena":
        entry_cena_18 = Entry(root, textvariable=cena_18, justify=CENTER, width=14)
        entry_cena_18.insert(0, "5")
        entry_cena_18.grid(row=28, column=2)
    elif nazwa_18.get() == "Dren Redona Ch 16 dł. 800mm z trokarem":
        entry_cena_18 = Entry(root, textvariable=cena_18, justify=CENTER, width=14)
        entry_cena_18.insert(0, "29.74")
        entry_cena_18.grid(row=28, column=2)
    elif nazwa_18.get() == "Dren do pompy Artrex":
        entry_cena_18 = Entry(root, textvariable=cena_18, justify=CENTER, width=14)
        entry_cena_18.insert(0, "108")
        entry_cena_18.grid(row=28, column=2)
    elif nazwa_18.get() == "Drut wiercący 2,4 x 311":
        entry_cena_18 = Entry(root, textvariable=cena_18, justify=CENTER, width=14)
        entry_cena_18.insert(0, "139.60")
        entry_cena_18.grid(row=28, column=2)
    elif nazwa_18.get() == "Fartuch jałowy L":
        entry_cena_18 = Entry(root, textvariable=cena_18, justify=CENTER, width=14)
        entry_cena_18.insert(0, "17")
        entry_cena_18.grid(row=28, column=2)
    elif nazwa_18.get() == "Fartuch jałowy M":
        entry_cena_18 = Entry(root, textvariable=cena_18, justify=CENTER, width=14)
        entry_cena_18.insert(0, "15.28")
        entry_cena_18.grid(row=28, column=2)
    elif nazwa_18.get() == "Fartuch jałowy XL":
        entry_cena_18 = Entry(root, textvariable=cena_18, justify=CENTER, width=14)
        entry_cena_18.insert(0, "20.84")
        entry_cena_18.grid(row=28, column=2)
    elif nazwa_18.get() == "FasatThread BioComposite Interference Screw 8x30":
        entry_cena_18 = Entry(root, textvariable=cena_18, justify=CENTER, width=14)
        entry_cena_18.insert(0, "594")
        entry_cena_18.grid(row=28, column=2)
    elif nazwa_18.get() == "Folia operacyjna, jałowa 45cm x 55cm":
        entry_cena_18 = Entry(root, textvariable=cena_18, justify=CENTER, width=14)
        entry_cena_18.insert(0, "9.99")
        entry_cena_18.grid(row=28, column=2)
    elif nazwa_18.get() == "Gaziki 10 x 10cm":
        entry_cena_18 = Entry(root, textvariable=cena_18, justify=CENTER, width=14)
        entry_cena_18.insert(0, "0.10")
        entry_cena_18.grid(row=28, column=2)
    elif nazwa_18.get() == "Igła 0,6 x 60":
        entry_cena_18 = Entry(root, textvariable=cena_18, justify=CENTER, width=14)
        entry_cena_18.insert(0, "0.09")
        entry_cena_18.grid(row=28, column=2)
    elif nazwa_18.get() == "Igła 0,7 x 40":
        entry_cena_18 = Entry(root, textvariable=cena_18, justify=CENTER, width=14)
        entry_cena_18.insert(0, "0.05")
        entry_cena_18.grid(row=28, column=2)
    elif nazwa_18.get() == "Igła 0,8 x 40":
        entry_cena_18 = Entry(root, textvariable=cena_18, justify=CENTER, width=14)
        entry_cena_18.insert(0, "0.05")
        entry_cena_18.grid(row=28, column=2)
    elif nazwa_18.get() == "Igła 1,1 x 70":
        entry_cena_18 = Entry(root, textvariable=cena_18, justify=CENTER, width=14)
        entry_cena_18.insert(0, "0.16")
        entry_cena_18.grid(row=28, column=2)
    elif nazwa_18.get() == "Kaniulowana śruba int. biokompozytowa z osłonką jednoraz.":
        entry_cena_18 = Entry(root, textvariable=cena_18, justify=CENTER, width=14)
        entry_cena_18.insert(0, "594")
        entry_cena_18.grid(row=28, column=2)
    elif nazwa_18.get() == "Kaniulowana śruba int. biokompozytowa z pełnym gwintem":
        entry_cena_18 = Entry(root, textvariable=cena_18, justify=CENTER, width=14)
        entry_cena_18.insert(0, "594")
        entry_cena_18.grid(row=28, column=2)
    elif nazwa_18.get() == "Końcówka do Shavera":
        entry_cena_18 = Entry(root, textvariable=cena_18, justify=CENTER, width=14)
        entry_cena_18.insert(0, "270")
        entry_cena_18.grid(row=28, column=2)
    elif nazwa_18.get() == "Kotwica biokompozytowa SwiveLock":
        entry_cena_18 = Entry(root, textvariable=cena_18, justify=CENTER, width=14)
        entry_cena_18.insert(0, "918")
        entry_cena_18.grid(row=28, column=2)
    elif nazwa_18.get() == "Kotwica Corkscrew":
        entry_cena_18 = Entry(root, textvariable=cena_18, justify=CENTER, width=14)
        entry_cena_18.insert(0, "604")
        entry_cena_18.grid(row=28, column=2)
    elif nazwa_18.get() == "Kotwica FASTak":
        entry_cena_18 = Entry(root, textvariable=cena_18, justify=CENTER, width=14)
        entry_cena_18.insert(0, "432")
        entry_cena_18.grid(row=28, column=2)
    elif nazwa_18.get() == "Kotwica PEEK SwiveLock":
        entry_cena_18 = Entry(root, textvariable=cena_18, justify=CENTER, width=14)
        entry_cena_18.insert(0, "885.60")
        entry_cena_18.grid(row=28, column=2)
    elif nazwa_18.get() == "NaCl 3000ml":
        entry_cena_18 = Entry(root, textvariable=cena_18, justify=CENTER, width=14)
        entry_cena_18.insert(0, "29.72")
        entry_cena_18.grid(row=28, column=2)
    elif nazwa_18.get() == "NaCl 5000ml":
        entry_cena_18 = Entry(root, textvariable=cena_18, justify=CENTER, width=14)
        entry_cena_18.insert(0, "58.33")
        entry_cena_18.grid(row=28, column=2)
    elif nazwa_18.get() == "Nici Dafilon 2-0":
        entry_cena_18 = Entry(root, textvariable=cena_18, justify=CENTER, width=14)
        entry_cena_18.insert(0, "6.60")
        entry_cena_18.grid(row=28, column=2)
    elif nazwa_18.get() == "Nici Novosyn 2":
        entry_cena_18 = Entry(root, textvariable=cena_18, justify=CENTER, width=14)
        entry_cena_18.insert(0, "13")
        entry_cena_18.grid(row=28, column=2)
    elif nazwa_18.get() == "Nici Novosyn 2-0":
        entry_cena_18 = Entry(root, textvariable=cena_18, justify=CENTER, width=14)
        entry_cena_18.insert(0, "7.70")
        entry_cena_18.grid(row=28, column=2)
    elif nazwa_18.get() == "Nici Novosyn 3-0":
        entry_cena_18 = Entry(root, textvariable=cena_18, justify=CENTER, width=14)
        entry_cena_18.insert(0, "7.70")
        entry_cena_18.grid(row=28, column=2)
    elif nazwa_18.get() == "Nici Nylon 2-0":
        entry_cena_18 = Entry(root, textvariable=cena_18, justify=CENTER, width=14)
        entry_cena_18.insert(0, "2.50")
        entry_cena_18.grid(row=28, column=2)
    elif nazwa_18.get() == "Nici Nylon 3-0":
        entry_cena_18 = Entry(root, textvariable=cena_18, justify=CENTER, width=14)
        entry_cena_18.insert(0, "2")
        entry_cena_18.grid(row=28, column=2)
    elif nazwa_18.get() == "Nici PGLA":
        entry_cena_18 = Entry(root, textvariable=cena_18, justify=CENTER, width=14)
        entry_cena_18.insert(0, "11.60")
        entry_cena_18.grid(row=28, column=2)
    elif nazwa_18.get() == "Nici PremiCron 3":
        entry_cena_18 = Entry(root, textvariable=cena_18, justify=CENTER, width=14)
        entry_cena_18.insert(0, "6.50")
        entry_cena_18.grid(row=28, column=2)
    elif nazwa_18.get() == "Nici Vicryl 4-0":
        entry_cena_18 = Entry(root, textvariable=cena_18, justify=CENTER, width=14)
        entry_cena_18.insert(0, "7.50")
        entry_cena_18.grid(row=28, column=2)
    elif nazwa_18.get() == "Nitinol Guide Pin 1.1":
        entry_cena_18 = Entry(root, textvariable=cena_18, justify=CENTER, width=14)
        entry_cena_18.insert(0, "145.80")
        entry_cena_18.grid(row=28, column=2)
    elif nazwa_18.get() == "Osłona na przewody":
        entry_cena_18 = Entry(root, textvariable=cena_18, justify=CENTER, width=14)
        entry_cena_18.insert(0, "2.50")
        entry_cena_18.grid(row=28, column=2)
    elif nazwa_18.get() == "Ostrze Arthrex 90(86)x19x1,27":
        entry_cena_18 = Entry(root, textvariable=cena_18, justify=CENTER, width=14)
        entry_cena_18.insert(0, "216")
        entry_cena_18.grid(row=28, column=2)
    elif nazwa_18.get() == "Ostrze piły":
        entry_cena_18 = Entry(root, textvariable=cena_18, justify=CENTER, width=14)
        entry_cena_18.insert(0, "108")
        entry_cena_18.grid(row=28, column=2)
    elif nazwa_18.get() == "Pielęgniarka anest.":
        entry_cena_18 = Entry(root, textvariable=cena_18, justify=CENTER, width=14)
        entry_cena_18.insert(0, "50")
        entry_cena_18.grid(row=28, column=2)
    elif nazwa_18.get() == "Pielęgniarka instr.":
        entry_cena_18 = Entry(root, textvariable=cena_18, justify=CENTER, width=14)
        entry_cena_18.insert(0, "50")
        entry_cena_18.grid(row=28, column=2)
    elif nazwa_18.get() == "Pielęgniarka 'Noviline'":
        entry_cena_18 = Entry(root, textvariable=cena_18, justify=CENTER, width=14)
        entry_cena_18.insert(0, "30")
        entry_cena_18.grid(row=28, column=2)
    elif nazwa_18.get() == "Płytka PeekPower do osteotomii klinowej":
        entry_cena_18 = Entry(root, textvariable=cena_18, justify=CENTER, width=14)
        entry_cena_18.insert(0, "2160")
        entry_cena_18.grid(row=28, column=2)
    elif nazwa_18.get() == "Rękawice jałowe 6,5":
        entry_cena_18 = Entry(root, textvariable=cena_18, justify=CENTER, width=14)
        entry_cena_18.insert(0, "1.20")
        entry_cena_18.grid(row=28, column=2)
    elif nazwa_18.get() == "Rękawice jałowe 7,0":
        entry_cena_18 = Entry(root, textvariable=cena_18, justify=CENTER, width=14)
        entry_cena_18.insert(0, "1.20")
        entry_cena_18.grid(row=28, column=2)
    elif nazwa_18.get() == "Rękawice jałowe 7,5":
        entry_cena_18 = Entry(root, textvariable=cena_18, justify=CENTER, width=14)
        entry_cena_18.insert(0, "1.20")
        entry_cena_18.grid(row=28, column=2)
    elif nazwa_18.get() == "Rękawice jałowe 8,00":
        entry_cena_18 = Entry(root, textvariable=cena_18, justify=CENTER, width=14)
        entry_cena_18.insert(0, "1.20")
        entry_cena_18.grid(row=28, column=2)
    elif nazwa_18.get() == "Rękojeść Interpulse wysokoprzepływowa":
        entry_cena_18 = Entry(root, textvariable=cena_18, justify=CENTER, width=14)
        entry_cena_18.insert(0, "216")
        entry_cena_18.grid(row=28, column=2)
    elif nazwa_18.get() == "Serweta":
        entry_cena_18 = Entry(root, textvariable=cena_18, justify=CENTER, width=14)
        entry_cena_18.insert(0, "6")
        entry_cena_18.grid(row=28, column=2)
    elif nazwa_18.get() == "Simplex Hv z Gentamycyna 10x40g":
        entry_cena_18 = Entry(root, textvariable=cena_18, justify=CENTER, width=14)
        entry_cena_18.insert(0, "162")
        entry_cena_18.grid(row=28, column=2)
    elif nazwa_18.get() == "Skalpel 11":
        entry_cena_18 = Entry(root, textvariable=cena_18, justify=CENTER, width=14)
        entry_cena_18.insert(0, "0.38")
        entry_cena_18.grid(row=28, column=2)
    elif nazwa_18.get() == "Skalpel 13":
        entry_cena_18 = Entry(root, textvariable=cena_18, justify=CENTER, width=14)
        entry_cena_18.insert(0, "1")
        entry_cena_18.grid(row=28, column=2)
    elif nazwa_18.get() == "Skalpel 22":
        entry_cena_18 = Entry(root, textvariable=cena_18, justify=CENTER, width=14)
        entry_cena_18.insert(0, "00000")
        entry_cena_18.grid(row=28, column=2)
    elif nazwa_18.get() == "Śruba blokująca PeekPower do osteotomii":
        entry_cena_18 = Entry(root, textvariable=cena_18, justify=CENTER, width=14)
        entry_cena_18.insert(0, "194")
        entry_cena_18.grid(row=28, column=2)
    elif nazwa_18.get() == "System do mieszania próżniowego":
        entry_cena_18 = Entry(root, textvariable=cena_18, justify=CENTER, width=14)
        entry_cena_18.insert(0, "216")
        entry_cena_18.grid(row=28, column=2)
    elif nazwa_18.get() == "System wprowadzania implantów ACL TightRope":
        entry_cena_18 = Entry(root, textvariable=cena_18, justify=CENTER, width=14)
        entry_cena_18.insert(0, "702")
        entry_cena_18.grid(row=28, column=2)
    elif nazwa_18.get() == "Szew FiberWire 2":
        entry_cena_18 = Entry(root, textvariable=cena_18, justify=CENTER, width=14)
        entry_cena_18.insert(0, "86.40")
        entry_cena_18.grid(row=28, column=2)
    elif nazwa_18.get() == "Taśma przylepna 10x50":
        entry_cena_18 = Entry(root, textvariable=cena_18, justify=CENTER, width=14)
        entry_cena_18.insert(0, "1.04")
        entry_cena_18.grid(row=28, column=2)
    elif nazwa_18.get() == "Triathlon elem. udowy lewy":
        entry_cena_18 = Entry(root, textvariable=cena_18, justify=CENTER, width=14)
        entry_cena_18.insert(0, "3132")
        entry_cena_18.grid(row=28, column=2)
    elif nazwa_18.get() == "Triathlon PS wkładka x3-9mm #4":
        entry_cena_18 = Entry(root, textvariable=cena_18, justify=CENTER, width=14)
        entry_cena_18.insert(0, "756")
        entry_cena_18.grid(row=28, column=2)
    elif nazwa_18.get() == "Triathlon taca piszczelowa":
        entry_cena_18 = Entry(root, textvariable=cena_18, justify=CENTER, width=14)
        entry_cena_18.insert(0, "1296")
        entry_cena_18.grid(row=28, column=2)
    elif nazwa_18.get() == "Wkłady 3L z żelem":
        entry_cena_18 = Entry(root, textvariable=cena_18, justify=CENTER, width=14)
        entry_cena_18.insert(0, "10.26")
        entry_cena_18.grid(row=28, column=2)
    elif nazwa_18.get() == "Zestaw do artroskopii":
        entry_cena_18 = Entry(root, textvariable=cena_18, justify=CENTER, width=14)
        entry_cena_18.insert(0, "67")
        entry_cena_18.grid(row=28, column=2)
    elif nazwa_18.get() == "Zestaw do artroskopii barku":
        entry_cena_18 = Entry(root, textvariable=cena_18, justify=CENTER, width=14)
        entry_cena_18.insert(0, "108")
        entry_cena_18.grid(row=28, column=2)
    elif nazwa_18.get() == "Zestaw do drenażu":
        entry_cena_18 = Entry(root, textvariable=cena_18, justify=CENTER, width=14)
        entry_cena_18.insert(0, "14.23")
        entry_cena_18.grid(row=28, column=2)
    elif nazwa_18.get() == "Zestaw ortopedyczny":
        entry_cena_18 = Entry(root, textvariable=cena_18, justify=CENTER, width=14)
        entry_cena_18.insert(0, "28.08")
        entry_cena_18.grid(row=28, column=2)
    elif nazwa_18.get() == "Gaziki 20 x 10cm":
        entry_cena_18 = Entry(root, textvariable=cena_18, justify=CENTER, width=14)
        entry_cena_18.insert(0, "0.46")
        entry_cena_18.grid(row=28, column=2)
    else:
        entry_cena_18 = Entry(root, textvariable=cena_18, justify=CENTER, width=14, bg="#ffff00")
        entry_cena_18.insert(0, "0")
        entry_cena_18.grid(row=28, column=2)

    if nazwa_19.get() == "--puste--":
        entry_cena_19 = Entry(root, textvariable=cena_19, justify=CENTER, width=14)
        entry_cena_19.insert(0, "0")
        entry_cena_19.grid(row=29, column=2)
    elif nazwa_19.get() == "Ablator":
        entry_cena_19 = Entry(root, textvariable=cena_19, justify=CENTER, width=14)
        entry_cena_19.insert(0, "572")
        entry_cena_19.grid(row=29, column=2)
    elif nazwa_19.get() == "Anestezjolog":
        entry_cena_19 = Entry(root, textvariable=cena_19, justify=CENTER, width=14, bg="#ffff00")
        entry_cena_19.insert(0, "350")
        entry_cena_19.grid(row=29, column=2)
    elif nazwa_19.get() == "Butelka 400ml do długotrwałego odsysania ran j.u. sterylna":
        entry_cena_19 = Entry(root, textvariable=cena_19, justify=CENTER, width=14)
        entry_cena_19.insert(0, "4")
        entry_cena_19.grid(row=29, column=2)
    elif nazwa_19.get() == "Doba":
        entry_cena_19 = Entry(root, textvariable=cena_19, justify=CENTER, width=14)
        entry_cena_19.insert(0, "700")
        entry_cena_19.grid(row=29, column=2)
    elif nazwa_19.get() == "Dren łączący do ssaka Grena":
        entry_cena_19 = Entry(root, textvariable=cena_19, justify=CENTER, width=14)
        entry_cena_19.insert(0, "5")
        entry_cena_19.grid(row=29, column=2)
    elif nazwa_19.get() == "Dren Redona Ch 16 dł. 800mm z trokarem":
        entry_cena_19 = Entry(root, textvariable=cena_19, justify=CENTER, width=14)
        entry_cena_19.insert(0, "29.74")
        entry_cena_19.grid(row=29, column=2)
    elif nazwa_19.get() == "Dren do pompy Artrex":
        entry_cena_19 = Entry(root, textvariable=cena_19, justify=CENTER, width=14)
        entry_cena_19.insert(0, "108")
        entry_cena_19.grid(row=29, column=2)
    elif nazwa_19.get() == "Drut wiercący 2,4 x 311":
        entry_cena_19 = Entry(root, textvariable=cena_19, justify=CENTER, width=14)
        entry_cena_19.insert(0, "139.60")
        entry_cena_19.grid(row=29, column=2)
    elif nazwa_19.get() == "Fartuch jałowy L":
        entry_cena_19 = Entry(root, textvariable=cena_19, justify=CENTER, width=14)
        entry_cena_19.insert(0, "17")
        entry_cena_19.grid(row=29, column=2)
    elif nazwa_19.get() == "Fartuch jałowy M":
        entry_cena_19 = Entry(root, textvariable=cena_19, justify=CENTER, width=14)
        entry_cena_19.insert(0, "15.28")
        entry_cena_19.grid(row=29, column=2)
    elif nazwa_19.get() == "Fartuch jałowy XL":
        entry_cena_19 = Entry(root, textvariable=cena_19, justify=CENTER, width=14)
        entry_cena_19.insert(0, "20.84")
        entry_cena_19.grid(row=29, column=2)
    elif nazwa_19.get() == "FasatThread BioComposite Interference Screw 8x30":
        entry_cena_19 = Entry(root, textvariable=cena_19, justify=CENTER, width=14)
        entry_cena_19.insert(0, "594")
        entry_cena_19.grid(row=29, column=2)
    elif nazwa_19.get() == "Folia operacyjna, jałowa 45cm x 55cm":
        entry_cena_19 = Entry(root, textvariable=cena_19, justify=CENTER, width=14)
        entry_cena_19.insert(0, "9.99")
        entry_cena_19.grid(row=29, column=2)
    elif nazwa_19.get() == "Gaziki 10 x 10cm":
        entry_cena_19 = Entry(root, textvariable=cena_19, justify=CENTER, width=14)
        entry_cena_19.insert(0, "0.10")
        entry_cena_19.grid(row=29, column=2)
    elif nazwa_19.get() == "Igła 0,6 x 60":
        entry_cena_19 = Entry(root, textvariable=cena_19, justify=CENTER, width=14)
        entry_cena_19.insert(0, "0.09")
        entry_cena_19.grid(row=29, column=2)
    elif nazwa_19.get() == "Igła 0,7 x 40":
        entry_cena_19 = Entry(root, textvariable=cena_19, justify=CENTER, width=14)
        entry_cena_19.insert(0, "0.05")
        entry_cena_19.grid(row=29, column=2)
    elif nazwa_19.get() == "Igła 0,8 x 40":
        entry_cena_19 = Entry(root, textvariable=cena_19, justify=CENTER, width=14)
        entry_cena_19.insert(0, "0.05")
        entry_cena_19.grid(row=29, column=2)
    elif nazwa_19.get() == "Igła 1,1 x 70":
        entry_cena_19 = Entry(root, textvariable=cena_19, justify=CENTER, width=14)
        entry_cena_19.insert(0, "0.16")
        entry_cena_19.grid(row=29, column=2)
    elif nazwa_19.get() == "Kaniulowana śruba int. biokompozytowa z osłonką jednoraz.":
        entry_cena_19 = Entry(root, textvariable=cena_19, justify=CENTER, width=14)
        entry_cena_19.insert(0, "594")
        entry_cena_19.grid(row=29, column=2)
    elif nazwa_19.get() == "Kaniulowana śruba int. biokompozytowa z pełnym gwintem":
        entry_cena_19 = Entry(root, textvariable=cena_19, justify=CENTER, width=14)
        entry_cena_19.insert(0, "594")
        entry_cena_19.grid(row=29, column=2)
    elif nazwa_19.get() == "Końcówka do Shavera":
        entry_cena_19 = Entry(root, textvariable=cena_19, justify=CENTER, width=14)
        entry_cena_19.insert(0, "270")
        entry_cena_19.grid(row=29, column=2)
    elif nazwa_19.get() == "Kotwica biokompozytowa SwiveLock":
        entry_cena_19 = Entry(root, textvariable=cena_19, justify=CENTER, width=14)
        entry_cena_19.insert(0, "918")
        entry_cena_19.grid(row=29, column=2)
    elif nazwa_19.get() == "Kotwica Corkscrew":
        entry_cena_19 = Entry(root, textvariable=cena_19, justify=CENTER, width=14)
        entry_cena_19.insert(0, "604")
        entry_cena_19.grid(row=29, column=2)
    elif nazwa_19.get() == "Kotwica FASTak":
        entry_cena_19 = Entry(root, textvariable=cena_19, justify=CENTER, width=14)
        entry_cena_19.insert(0, "432")
        entry_cena_19.grid(row=29, column=2)
    elif nazwa_19.get() == "Kotwica PEEK SwiveLock":
        entry_cena_19 = Entry(root, textvariable=cena_19, justify=CENTER, width=14)
        entry_cena_19.insert(0, "885.60")
        entry_cena_19.grid(row=29, column=2)
    elif nazwa_19.get() == "NaCl 3000ml":
        entry_cena_19 = Entry(root, textvariable=cena_19, justify=CENTER, width=14)
        entry_cena_19.insert(0, "29.72")
        entry_cena_19.grid(row=29, column=2)
    elif nazwa_19.get() == "NaCl 5000ml":
        entry_cena_19 = Entry(root, textvariable=cena_19, justify=CENTER, width=14)
        entry_cena_19.insert(0, "58.33")
        entry_cena_19.grid(row=29, column=2)
    elif nazwa_19.get() == "Nici Dafilon 2-0":
        entry_cena_19 = Entry(root, textvariable=cena_19, justify=CENTER, width=14)
        entry_cena_19.insert(0, "6.60")
        entry_cena_19.grid(row=29, column=2)
    elif nazwa_19.get() == "Nici Novosyn 2":
        entry_cena_19 = Entry(root, textvariable=cena_19, justify=CENTER, width=14)
        entry_cena_19.insert(0, "13")
        entry_cena_19.grid(row=29, column=2)
    elif nazwa_19.get() == "Nici Novosyn 2-0":
        entry_cena_19 = Entry(root, textvariable=cena_19, justify=CENTER, width=14)
        entry_cena_19.insert(0, "7.70")
        entry_cena_19.grid(row=29, column=2)
    elif nazwa_19.get() == "Nici Novosyn 3-0":
        entry_cena_19 = Entry(root, textvariable=cena_19, justify=CENTER, width=14)
        entry_cena_19.insert(0, "7.70")
        entry_cena_19.grid(row=29, column=2)
    elif nazwa_19.get() == "Nici Nylon 2-0":
        entry_cena_19 = Entry(root, textvariable=cena_19, justify=CENTER, width=14)
        entry_cena_19.insert(0, "2.50")
        entry_cena_19.grid(row=29, column=2)
    elif nazwa_19.get() == "Nici Nylon 3-0":
        entry_cena_19 = Entry(root, textvariable=cena_19, justify=CENTER, width=14)
        entry_cena_19.insert(0, "2")
        entry_cena_19.grid(row=29, column=2)
    elif nazwa_19.get() == "Nici PGLA":
        entry_cena_19 = Entry(root, textvariable=cena_19, justify=CENTER, width=14)
        entry_cena_19.insert(0, "11.60")
        entry_cena_19.grid(row=29, column=2)
    elif nazwa_19.get() == "Nici PremiCron 3":
        entry_cena_19 = Entry(root, textvariable=cena_19, justify=CENTER, width=14)
        entry_cena_19.insert(0, "6.50")
        entry_cena_19.grid(row=29, column=2)
    elif nazwa_19.get() == "Nici Vicryl 4-0":
        entry_cena_19 = Entry(root, textvariable=cena_19, justify=CENTER, width=14)
        entry_cena_19.insert(0, "7.50")
        entry_cena_19.grid(row=29, column=2)
    elif nazwa_19.get() == "Nitinol Guide Pin 1.1":
        entry_cena_19 = Entry(root, textvariable=cena_19, justify=CENTER, width=14)
        entry_cena_19.insert(0, "145.80")
        entry_cena_19.grid(row=29, column=2)
    elif nazwa_19.get() == "Osłona na przewody":
        entry_cena_19 = Entry(root, textvariable=cena_19, justify=CENTER, width=14)
        entry_cena_19.insert(0, "2.50")
        entry_cena_19.grid(row=29, column=2)
    elif nazwa_19.get() == "Ostrze Arthrex 90(86)x19x1,27":
        entry_cena_19 = Entry(root, textvariable=cena_19, justify=CENTER, width=14)
        entry_cena_19.insert(0, "216")
        entry_cena_19.grid(row=29, column=2)
    elif nazwa_19.get() == "Ostrze piły":
        entry_cena_19 = Entry(root, textvariable=cena_19, justify=CENTER, width=14)
        entry_cena_19.insert(0, "108")
        entry_cena_19.grid(row=29, column=2)
    elif nazwa_19.get() == "Pielęgniarka anest.":
        entry_cena_19 = Entry(root, textvariable=cena_19, justify=CENTER, width=14)
        entry_cena_19.insert(0, "50")
        entry_cena_19.grid(row=29, column=2)
    elif nazwa_19.get() == "Pielęgniarka instr.":
        entry_cena_19 = Entry(root, textvariable=cena_19, justify=CENTER, width=14)
        entry_cena_19.insert(0, "50")
        entry_cena_19.grid(row=29, column=2)
    elif nazwa_19.get() == "Pielęgniarka 'Noviline'":
        entry_cena_19 = Entry(root, textvariable=cena_19, justify=CENTER, width=14)
        entry_cena_19.insert(0, "30")
        entry_cena_19.grid(row=29, column=2)
    elif nazwa_19.get() == "Płytka PeekPower do osteotomii klinowej":
        entry_cena_19 = Entry(root, textvariable=cena_19, justify=CENTER, width=14)
        entry_cena_19.insert(0, "2160")
        entry_cena_19.grid(row=29, column=2)
    elif nazwa_19.get() == "Rękawice jałowe 6,5":
        entry_cena_19 = Entry(root, textvariable=cena_19, justify=CENTER, width=14)
        entry_cena_19.insert(0, "1.20")
        entry_cena_19.grid(row=29, column=2)
    elif nazwa_19.get() == "Rękawice jałowe 7,0":
        entry_cena_19 = Entry(root, textvariable=cena_19, justify=CENTER, width=14)
        entry_cena_19.insert(0, "1.20")
        entry_cena_19.grid(row=29, column=2)
    elif nazwa_19.get() == "Rękawice jałowe 7,5":
        entry_cena_19 = Entry(root, textvariable=cena_19, justify=CENTER, width=14)
        entry_cena_19.insert(0, "1.20")
        entry_cena_19.grid(row=29, column=2)
    elif nazwa_19.get() == "Rękawice jałowe 8,00":
        entry_cena_19 = Entry(root, textvariable=cena_19, justify=CENTER, width=14)
        entry_cena_19.insert(0, "1.20")
        entry_cena_19.grid(row=29, column=2)
    elif nazwa_19.get() == "Rękojeść Interpulse wysokoprzepływowa":
        entry_cena_19 = Entry(root, textvariable=cena_19, justify=CENTER, width=14)
        entry_cena_19.insert(0, "216")
        entry_cena_19.grid(row=29, column=2)
    elif nazwa_19.get() == "Serweta":
        entry_cena_19 = Entry(root, textvariable=cena_19, justify=CENTER, width=14)
        entry_cena_19.insert(0, "6")
        entry_cena_19.grid(row=29, column=2)
    elif nazwa_19.get() == "Simplex Hv z Gentamycyna 10x40g":
        entry_cena_19 = Entry(root, textvariable=cena_19, justify=CENTER, width=14)
        entry_cena_19.insert(0, "162")
        entry_cena_19.grid(row=29, column=2)
    elif nazwa_19.get() == "Skalpel 11":
        entry_cena_19 = Entry(root, textvariable=cena_19, justify=CENTER, width=14)
        entry_cena_19.insert(0, "0.38")
        entry_cena_19.grid(row=29, column=2)
    elif nazwa_19.get() == "Skalpel 13":
        entry_cena_19 = Entry(root, textvariable=cena_19, justify=CENTER, width=14)
        entry_cena_19.insert(0, "1")
        entry_cena_19.grid(row=29, column=2)
    elif nazwa_19.get() == "Skalpel 22":
        entry_cena_19 = Entry(root, textvariable=cena_19, justify=CENTER, width=14)
        entry_cena_19.insert(0, "00000")
        entry_cena_19.grid(row=29, column=2)
    elif nazwa_19.get() == "Śruba blokująca PeekPower do osteotomii":
        entry_cena_19 = Entry(root, textvariable=cena_19, justify=CENTER, width=14)
        entry_cena_19.insert(0, "194")
        entry_cena_19.grid(row=29, column=2)
    elif nazwa_19.get() == "System do mieszania próżniowego":
        entry_cena_19 = Entry(root, textvariable=cena_19, justify=CENTER, width=14)
        entry_cena_19.insert(0, "216")
        entry_cena_19.grid(row=29, column=2)
    elif nazwa_19.get() == "System wprowadzania implantów ACL TightRope":
        entry_cena_19 = Entry(root, textvariable=cena_19, justify=CENTER, width=14)
        entry_cena_19.insert(0, "702")
        entry_cena_19.grid(row=29, column=2)
    elif nazwa_19.get() == "Szew FiberWire 2":
        entry_cena_19 = Entry(root, textvariable=cena_19, justify=CENTER, width=14)
        entry_cena_19.insert(0, "86.40")
        entry_cena_19.grid(row=29, column=2)
    elif nazwa_19.get() == "Taśma przylepna 10x50":
        entry_cena_19 = Entry(root, textvariable=cena_19, justify=CENTER, width=14)
        entry_cena_19.insert(0, "1.04")
        entry_cena_19.grid(row=29, column=2)
    elif nazwa_19.get() == "Triathlon elem. udowy lewy":
        entry_cena_19 = Entry(root, textvariable=cena_19, justify=CENTER, width=14)
        entry_cena_19.insert(0, "3132")
        entry_cena_19.grid(row=29, column=2)
    elif nazwa_19.get() == "Triathlon PS wkładka x3-9mm #4":
        entry_cena_19 = Entry(root, textvariable=cena_19, justify=CENTER, width=14)
        entry_cena_19.insert(0, "756")
        entry_cena_19.grid(row=29, column=2)
    elif nazwa_19.get() == "Triathlon taca piszczelowa":
        entry_cena_19 = Entry(root, textvariable=cena_19, justify=CENTER, width=14)
        entry_cena_19.insert(0, "1296")
        entry_cena_19.grid(row=29, column=2)
    elif nazwa_19.get() == "Wkłady 3L z żelem":
        entry_cena_19 = Entry(root, textvariable=cena_19, justify=CENTER, width=14)
        entry_cena_19.insert(0, "10.26")
        entry_cena_19.grid(row=29, column=2)
    elif nazwa_19.get() == "Zestaw do artroskopii":
        entry_cena_19 = Entry(root, textvariable=cena_19, justify=CENTER, width=14)
        entry_cena_19.insert(0, "67")
        entry_cena_19.grid(row=29, column=2)
    elif nazwa_19.get() == "Zestaw do artroskopii barku":
        entry_cena_19 = Entry(root, textvariable=cena_19, justify=CENTER, width=14)
        entry_cena_19.insert(0, "108")
        entry_cena_19.grid(row=29, column=2)
    elif nazwa_19.get() == "Zestaw do drenażu":
        entry_cena_19 = Entry(root, textvariable=cena_19, justify=CENTER, width=14)
        entry_cena_19.insert(0, "14.23")
        entry_cena_19.grid(row=29, column=2)
    elif nazwa_19.get() == "Zestaw ortopedyczny":
        entry_cena_19 = Entry(root, textvariable=cena_19, justify=CENTER, width=14)
        entry_cena_19.insert(0, "28.08")
        entry_cena_19.grid(row=29, column=2)
    elif nazwa_19.get() == "Gaziki 20 x 10cm":
        entry_cena_19 = Entry(root, textvariable=cena_19, justify=CENTER, width=14)
        entry_cena_19.insert(0, "0.46")
        entry_cena_19.grid(row=29, column=2)
    else:
        entry_cena_19 = Entry(root, textvariable=cena_19, justify=CENTER, width=14, bg="#ffff00")
        entry_cena_19.insert(0, "0")
        entry_cena_19.grid(row=29, column=2)

    if nazwa_20.get() == "--puste--":
        entry_cena_20 = Entry(root, textvariable=cena_20, justify=CENTER, width=14)
        entry_cena_20.insert(0, "0")
        entry_cena_20.grid(row=30, column=2)
    elif nazwa_20.get() == "Ablator":
        entry_cena_20 = Entry(root, textvariable=cena_20, justify=CENTER, width=14)
        entry_cena_20.insert(0, "572")
        entry_cena_20.grid(row=30, column=2)
    elif nazwa_20.get() == "Anestezjolog":
        entry_cena_20 = Entry(root, textvariable=cena_20, justify=CENTER, width=14, bg="#ffff00")
        entry_cena_20.insert(0, "350")
        entry_cena_20.grid(row=30, column=2)
    elif nazwa_20.get() == "Butelka 400ml do długotrwałego odsysania ran j.u. sterylna":
        entry_cena_20 = Entry(root, textvariable=cena_20, justify=CENTER, width=14)
        entry_cena_20.insert(0, "4")
        entry_cena_20.grid(row=30, column=2)
    elif nazwa_20.get() == "Doba":
        entry_cena_20 = Entry(root, textvariable=cena_20, justify=CENTER, width=14)
        entry_cena_20.insert(0, "700")
        entry_cena_20.grid(row=30, column=2)
    elif nazwa_20.get() == "Dren łączący do ssaka Grena":
        entry_cena_20 = Entry(root, textvariable=cena_20, justify=CENTER, width=14)
        entry_cena_20.insert(0, "5")
        entry_cena_20.grid(row=30, column=2)
    elif nazwa_20.get() == "Dren Redona Ch 16 dł. 800mm z trokarem":
        entry_cena_20 = Entry(root, textvariable=cena_20, justify=CENTER, width=14)
        entry_cena_20.insert(0, "29.74")
        entry_cena_20.grid(row=30, column=2)
    elif nazwa_20.get() == "Dren do pompy Artrex":
        entry_cena_20 = Entry(root, textvariable=cena_20, justify=CENTER, width=14)
        entry_cena_20.insert(0, "108")
        entry_cena_20.grid(row=30, column=2)
    elif nazwa_20.get() == "Drut wiercący 2,4 x 311":
        entry_cena_20 = Entry(root, textvariable=cena_20, justify=CENTER, width=14)
        entry_cena_20.insert(0, "139.60")
        entry_cena_20.grid(row=30, column=2)
    elif nazwa_20.get() == "Fartuch jałowy L":
        entry_cena_20 = Entry(root, textvariable=cena_20, justify=CENTER, width=14)
        entry_cena_20.insert(0, "17")
        entry_cena_20.grid(row=30, column=2)
    elif nazwa_20.get() == "Fartuch jałowy M":
        entry_cena_20 = Entry(root, textvariable=cena_20, justify=CENTER, width=14)
        entry_cena_20.insert(0, "15.28")
        entry_cena_20.grid(row=30, column=2)
    elif nazwa_20.get() == "Fartuch jałowy XL":
        entry_cena_20 = Entry(root, textvariable=cena_20, justify=CENTER, width=14)
        entry_cena_20.insert(0, "20.84")
        entry_cena_20.grid(row=30, column=2)
    elif nazwa_20.get() == "FasatThread BioComposite Interference Screw 8x30":
        entry_cena_20 = Entry(root, textvariable=cena_20, justify=CENTER, width=14)
        entry_cena_20.insert(0, "594")
        entry_cena_20.grid(row=30, column=2)
    elif nazwa_20.get() == "Folia operacyjna, jałowa 45cm x 55cm":
        entry_cena_20 = Entry(root, textvariable=cena_20, justify=CENTER, width=14)
        entry_cena_20.insert(0, "9.99")
        entry_cena_20.grid(row=30, column=2)
    elif nazwa_20.get() == "Gaziki 10 x 10cm":
        entry_cena_20 = Entry(root, textvariable=cena_20, justify=CENTER, width=14)
        entry_cena_20.insert(0, "0.10")
        entry_cena_20.grid(row=30, column=2)
    elif nazwa_20.get() == "Igła 0,6 x 60":
        entry_cena_20 = Entry(root, textvariable=cena_20, justify=CENTER, width=14)
        entry_cena_20.insert(0, "0.09")
        entry_cena_20.grid(row=30, column=2)
    elif nazwa_20.get() == "Igła 0,7 x 40":
        entry_cena_20 = Entry(root, textvariable=cena_20, justify=CENTER, width=14)
        entry_cena_20.insert(0, "0.05")
        entry_cena_20.grid(row=30, column=2)
    elif nazwa_20.get() == "Igła 0,8 x 40":
        entry_cena_20 = Entry(root, textvariable=cena_20, justify=CENTER, width=14)
        entry_cena_20.insert(0, "0.05")
        entry_cena_20.grid(row=30, column=2)
    elif nazwa_20.get() == "Igła 1,1 x 70":
        entry_cena_20 = Entry(root, textvariable=cena_20, justify=CENTER, width=14)
        entry_cena_20.insert(0, "0.16")
        entry_cena_20.grid(row=30, column=2)
    elif nazwa_20.get() == "Kaniulowana śruba int. biokompozytowa z osłonką jednoraz.":
        entry_cena_20 = Entry(root, textvariable=cena_20, justify=CENTER, width=14)
        entry_cena_20.insert(0, "594")
        entry_cena_20.grid(row=30, column=2)
    elif nazwa_20.get() == "Kaniulowana śruba int. biokompozytowa z pełnym gwintem":
        entry_cena_20 = Entry(root, textvariable=cena_20, justify=CENTER, width=14)
        entry_cena_20.insert(0, "594")
        entry_cena_20.grid(row=30, column=2)
    elif nazwa_20.get() == "Końcówka do Shavera":
        entry_cena_20 = Entry(root, textvariable=cena_20, justify=CENTER, width=14)
        entry_cena_20.insert(0, "270")
        entry_cena_20.grid(row=30, column=2)
    elif nazwa_20.get() == "Kotwica biokompozytowa SwiveLock":
        entry_cena_20 = Entry(root, textvariable=cena_20, justify=CENTER, width=14)
        entry_cena_20.insert(0, "918")
        entry_cena_20.grid(row=30, column=2)
    elif nazwa_20.get() == "Kotwica Corkscrew":
        entry_cena_20 = Entry(root, textvariable=cena_20, justify=CENTER, width=14)
        entry_cena_20.insert(0, "604")
        entry_cena_20.grid(row=30, column=2)
    elif nazwa_20.get() == "Kotwica FASTak":
        entry_cena_20 = Entry(root, textvariable=cena_20, justify=CENTER, width=14)
        entry_cena_20.insert(0, "432")
        entry_cena_20.grid(row=30, column=2)
    elif nazwa_20.get() == "Kotwica PEEK SwiveLock":
        entry_cena_20 = Entry(root, textvariable=cena_20, justify=CENTER, width=14)
        entry_cena_20.insert(0, "885.60")
        entry_cena_20.grid(row=30, column=2)
    elif nazwa_20.get() == "NaCl 3000ml":
        entry_cena_20 = Entry(root, textvariable=cena_20, justify=CENTER, width=14)
        entry_cena_20.insert(0, "29.72")
        entry_cena_20.grid(row=30, column=2)
    elif nazwa_20.get() == "NaCl 5000ml":
        entry_cena_20 = Entry(root, textvariable=cena_20, justify=CENTER, width=14)
        entry_cena_20.insert(0, "58.33")
        entry_cena_20.grid(row=30, column=2)
    elif nazwa_20.get() == "Nici Dafilon 2-0":
        entry_cena_20 = Entry(root, textvariable=cena_20, justify=CENTER, width=14)
        entry_cena_20.insert(0, "6.60")
        entry_cena_20.grid(row=30, column=2)
    elif nazwa_20.get() == "Nici Novosyn 2":
        entry_cena_20 = Entry(root, textvariable=cena_20, justify=CENTER, width=14)
        entry_cena_20.insert(0, "13")
        entry_cena_20.grid(row=30, column=2)
    elif nazwa_20.get() == "Nici Novosyn 2-0":
        entry_cena_20 = Entry(root, textvariable=cena_20, justify=CENTER, width=14)
        entry_cena_20.insert(0, "7.70")
        entry_cena_20.grid(row=30, column=2)
    elif nazwa_20.get() == "Nici Novosyn 3-0":
        entry_cena_20 = Entry(root, textvariable=cena_20, justify=CENTER, width=14)
        entry_cena_20.insert(0, "7.70")
        entry_cena_20.grid(row=30, column=2)
    elif nazwa_20.get() == "Nici Nylon 2-0":
        entry_cena_20 = Entry(root, textvariable=cena_20, justify=CENTER, width=14)
        entry_cena_20.insert(0, "2.50")
        entry_cena_20.grid(row=30, column=2)
    elif nazwa_20.get() == "Nici Nylon 3-0":
        entry_cena_20 = Entry(root, textvariable=cena_20, justify=CENTER, width=14)
        entry_cena_20.insert(0, "2")
        entry_cena_20.grid(row=30, column=2)
    elif nazwa_20.get() == "Nici PGLA":
        entry_cena_20 = Entry(root, textvariable=cena_20, justify=CENTER, width=14)
        entry_cena_20.insert(0, "11.60")
        entry_cena_20.grid(row=30, column=2)
    elif nazwa_20.get() == "Nici PremiCron 3":
        entry_cena_20 = Entry(root, textvariable=cena_20, justify=CENTER, width=14)
        entry_cena_20.insert(0, "6.50")
        entry_cena_20.grid(row=30, column=2)
    elif nazwa_20.get() == "Nici Vicryl 4-0":
        entry_cena_20 = Entry(root, textvariable=cena_20, justify=CENTER, width=14)
        entry_cena_20.insert(0, "7.50")
        entry_cena_20.grid(row=30, column=2)
    elif nazwa_20.get() == "Nitinol Guide Pin 1.1":
        entry_cena_20 = Entry(root, textvariable=cena_20, justify=CENTER, width=14)
        entry_cena_20.insert(0, "145.80")
        entry_cena_20.grid(row=30, column=2)
    elif nazwa_20.get() == "Osłona na przewody":
        entry_cena_20 = Entry(root, textvariable=cena_20, justify=CENTER, width=14)
        entry_cena_20.insert(0, "2.50")
        entry_cena_20.grid(row=30, column=2)
    elif nazwa_20.get() == "Ostrze Arthrex 90(86)x19x1,27":
        entry_cena_20 = Entry(root, textvariable=cena_20, justify=CENTER, width=14)
        entry_cena_20.insert(0, "216")
        entry_cena_20.grid(row=30, column=2)
    elif nazwa_20.get() == "Ostrze piły":
        entry_cena_20 = Entry(root, textvariable=cena_20, justify=CENTER, width=14)
        entry_cena_20.insert(0, "108")
        entry_cena_20.grid(row=30, column=2)
    elif nazwa_20.get() == "Pielęgniarka anest.":
        entry_cena_20 = Entry(root, textvariable=cena_20, justify=CENTER, width=14)
        entry_cena_20.insert(0, "50")
        entry_cena_20.grid(row=30, column=2)
    elif nazwa_20.get() == "Pielęgniarka instr.":
        entry_cena_20 = Entry(root, textvariable=cena_20, justify=CENTER, width=14)
        entry_cena_20.insert(0, "50")
        entry_cena_20.grid(row=30, column=2)
    elif nazwa_20.get() == "Pielęgniarka 'Noviline'":
        entry_cena_20 = Entry(root, textvariable=cena_20, justify=CENTER, width=14)
        entry_cena_20.insert(0, "30")
        entry_cena_20.grid(row=30, column=2)
    elif nazwa_20.get() == "Płytka PeekPower do osteotomii klinowej":
        entry_cena_20 = Entry(root, textvariable=cena_20, justify=CENTER, width=14)
        entry_cena_20.insert(0, "2160")
        entry_cena_20.grid(row=30, column=2)
    elif nazwa_20.get() == "Rękawice jałowe 6,5":
        entry_cena_20 = Entry(root, textvariable=cena_20, justify=CENTER, width=14)
        entry_cena_20.insert(0, "1.20")
        entry_cena_20.grid(row=30, column=2)
    elif nazwa_20.get() == "Rękawice jałowe 7,0":
        entry_cena_20 = Entry(root, textvariable=cena_20, justify=CENTER, width=14)
        entry_cena_20.insert(0, "1.20")
        entry_cena_20.grid(row=30, column=2)
    elif nazwa_20.get() == "Rękawice jałowe 7,5":
        entry_cena_20 = Entry(root, textvariable=cena_20, justify=CENTER, width=14)
        entry_cena_20.insert(0, "1.20")
        entry_cena_20.grid(row=30, column=2)
    elif nazwa_20.get() == "Rękawice jałowe 8,00":
        entry_cena_20 = Entry(root, textvariable=cena_20, justify=CENTER, width=14)
        entry_cena_20.insert(0, "1.20")
        entry_cena_20.grid(row=30, column=2)
    elif nazwa_20.get() == "Rękojeść Interpulse wysokoprzepływowa":
        entry_cena_20 = Entry(root, textvariable=cena_20, justify=CENTER, width=14)
        entry_cena_20.insert(0, "216")
        entry_cena_20.grid(row=30, column=2)
    elif nazwa_20.get() == "Serweta":
        entry_cena_20 = Entry(root, textvariable=cena_20, justify=CENTER, width=14)
        entry_cena_20.insert(0, "6")
        entry_cena_20.grid(row=30, column=2)
    elif nazwa_20.get() == "Simplex Hv z Gentamycyna 10x40g":
        entry_cena_20 = Entry(root, textvariable=cena_20, justify=CENTER, width=14)
        entry_cena_20.insert(0, "162")
        entry_cena_20.grid(row=30, column=2)
    elif nazwa_20.get() == "Skalpel 11":
        entry_cena_20 = Entry(root, textvariable=cena_20, justify=CENTER, width=14)
        entry_cena_20.insert(0, "0.38")
        entry_cena_20.grid(row=30, column=2)
    elif nazwa_20.get() == "Skalpel 13":
        entry_cena_20 = Entry(root, textvariable=cena_20, justify=CENTER, width=14)
        entry_cena_20.insert(0, "1")
        entry_cena_20.grid(row=30, column=2)
    elif nazwa_20.get() == "Skalpel 22":
        entry_cena_20 = Entry(root, textvariable=cena_20, justify=CENTER, width=14)
        entry_cena_20.insert(0, "00000")
        entry_cena_20.grid(row=30, column=2)
    elif nazwa_20.get() == "Śruba blokująca PeekPower do osteotomii":
        entry_cena_20 = Entry(root, textvariable=cena_20, justify=CENTER, width=14)
        entry_cena_20.insert(0, "194")
        entry_cena_20.grid(row=30, column=2)
    elif nazwa_20.get() == "System do mieszania próżniowego":
        entry_cena_20 = Entry(root, textvariable=cena_20, justify=CENTER, width=14)
        entry_cena_20.insert(0, "216")
        entry_cena_20.grid(row=30, column=2)
    elif nazwa_20.get() == "System wprowadzania implantów ACL TightRope":
        entry_cena_20 = Entry(root, textvariable=cena_20, justify=CENTER, width=14)
        entry_cena_20.insert(0, "702")
        entry_cena_20.grid(row=30, column=2)
    elif nazwa_20.get() == "Szew FiberWire 2":
        entry_cena_20 = Entry(root, textvariable=cena_20, justify=CENTER, width=14)
        entry_cena_20.insert(0, "86.40")
        entry_cena_20.grid(row=30, column=2)
    elif nazwa_20.get() == "Taśma przylepna 10x50":
        entry_cena_20 = Entry(root, textvariable=cena_20, justify=CENTER, width=14)
        entry_cena_20.insert(0, "1.04")
        entry_cena_20.grid(row=30, column=2)
    elif nazwa_20.get() == "Triathlon elem. udowy lewy":
        entry_cena_20 = Entry(root, textvariable=cena_20, justify=CENTER, width=14)
        entry_cena_20.insert(0, "3132")
        entry_cena_20.grid(row=30, column=2)
    elif nazwa_20.get() == "Triathlon PS wkładka x3-9mm #4":
        entry_cena_20 = Entry(root, textvariable=cena_20, justify=CENTER, width=14)
        entry_cena_20.insert(0, "756")
        entry_cena_20.grid(row=30, column=2)
    elif nazwa_20.get() == "Triathlon taca piszczelowa":
        entry_cena_20 = Entry(root, textvariable=cena_20, justify=CENTER, width=14)
        entry_cena_20.insert(0, "1296")
        entry_cena_20.grid(row=30, column=2)
    elif nazwa_20.get() == "Wkłady 3L z żelem":
        entry_cena_20 = Entry(root, textvariable=cena_20, justify=CENTER, width=14)
        entry_cena_20.insert(0, "10.26")
        entry_cena_20.grid(row=30, column=2)
    elif nazwa_20.get() == "Zestaw do artroskopii":
        entry_cena_20 = Entry(root, textvariable=cena_20, justify=CENTER, width=14)
        entry_cena_20.insert(0, "67")
        entry_cena_20.grid(row=30, column=2)
    elif nazwa_20.get() == "Zestaw do artroskopii barku":
        entry_cena_20 = Entry(root, textvariable=cena_20, justify=CENTER, width=14)
        entry_cena_20.insert(0, "108")
        entry_cena_20.grid(row=30, column=2)
    elif nazwa_20.get() == "Zestaw do drenażu":
        entry_cena_20 = Entry(root, textvariable=cena_20, justify=CENTER, width=14)
        entry_cena_20.insert(0, "14.23")
        entry_cena_20.grid(row=30, column=2)
    elif nazwa_20.get() == "Zestaw ortopedyczny":
        entry_cena_20 = Entry(root, textvariable=cena_20, justify=CENTER, width=14)
        entry_cena_20.insert(0, "28.08")
        entry_cena_20.grid(row=30, column=2)
    elif nazwa_20.get() == "Gaziki 20 x 10cm":
        entry_cena_20 = Entry(root, textvariable=cena_20, justify=CENTER, width=14)
        entry_cena_20.insert(0, "0.46")
        entry_cena_20.grid(row=30, column=2)
    else:
        entry_cena_20 = Entry(root, textvariable=cena_20, justify=CENTER, width=14, bg="#ffff00")
        entry_cena_20.insert(0, "0")
        entry_cena_20.grid(row=30, column=2)

    if nazwa_21.get() == "--puste--":
        entry_cena_21 = Entry(root, textvariable=cena_21, justify=CENTER, width=14)
        entry_cena_21.insert(0, "0")
        entry_cena_21.grid(row=11, column=6)
    elif nazwa_21.get() == "Ablator":
        entry_cena_21 = Entry(root, textvariable=cena_21, justify=CENTER, width=14)
        entry_cena_21.insert(0, "572")
        entry_cena_21.grid(row=11, column=6)
    elif nazwa_21.get() == "Anestezjolog":
        entry_cena_21 = Entry(root, textvariable=cena_21, justify=CENTER, width=14, bg="#ffff00")
        entry_cena_21.insert(0, "350")
        entry_cena_21.grid(row=11, column=6)
    elif nazwa_21.get() == "Butelka 400ml do długotrwałego odsysania ran j.u. sterylna":
        entry_cena_21 = Entry(root, textvariable=cena_21, justify=CENTER, width=14)
        entry_cena_21.insert(0, "4")
        entry_cena_21.grid(row=11, column=6)
    elif nazwa_21.get() == "Doba":
        entry_cena_21 = Entry(root, textvariable=cena_21, justify=CENTER, width=14)
        entry_cena_21.insert(0, "700")
        entry_cena_21.grid(row=11, column=6)
    elif nazwa_21.get() == "Dren łączący do ssaka Grena":
        entry_cena_21 = Entry(root, textvariable=cena_21, justify=CENTER, width=14)
        entry_cena_21.insert(0, "5")
        entry_cena_21.grid(row=11, column=6)
    elif nazwa_21.get() == "Dren Redona Ch 16 dł. 800mm z trokarem":
        entry_cena_21 = Entry(root, textvariable=cena_21, justify=CENTER, width=14)
        entry_cena_21.insert(0, "29.74")
        entry_cena_21.grid(row=11, column=6)
    elif nazwa_21.get() == "Dren do pompy Artrex":
        entry_cena_21 = Entry(root, textvariable=cena_21, justify=CENTER, width=14)
        entry_cena_21.insert(0, "108")
        entry_cena_21.grid(row=11, column=6)
    elif nazwa_21.get() == "Drut wiercący 2,4 x 311":
        entry_cena_21 = Entry(root, textvariable=cena_21, justify=CENTER, width=14)
        entry_cena_21.insert(0, "139.60")
        entry_cena_21.grid(row=11, column=6)
    elif nazwa_21.get() == "Fartuch jałowy L":
        entry_cena_21 = Entry(root, textvariable=cena_21, justify=CENTER, width=14)
        entry_cena_21.insert(0, "17")
        entry_cena_21.grid(row=11, column=6)
    elif nazwa_21.get() == "Fartuch jałowy M":
        entry_cena_21 = Entry(root, textvariable=cena_21, justify=CENTER, width=14)
        entry_cena_21.insert(0, "15.28")
        entry_cena_21.grid(row=11, column=6)
    elif nazwa_21.get() == "Fartuch jałowy XL":
        entry_cena_21 = Entry(root, textvariable=cena_21, justify=CENTER, width=14)
        entry_cena_21.insert(0, "20.84")
        entry_cena_21.grid(row=11, column=6)
    elif nazwa_21.get() == "FasatThread BioComposite Interference Screw 8x30":
        entry_cena_21 = Entry(root, textvariable=cena_21, justify=CENTER, width=14)
        entry_cena_21.insert(0, "594")
        entry_cena_21.grid(row=11, column=6)
    elif nazwa_21.get() == "Folia operacyjna, jałowa 45cm x 55cm":
        entry_cena_21 = Entry(root, textvariable=cena_21, justify=CENTER, width=14)
        entry_cena_21.insert(0, "9.99")
        entry_cena_21.grid(row=11, column=6)
    elif nazwa_21.get() == "Gaziki 10 x 10cm":
        entry_cena_21 = Entry(root, textvariable=cena_21, justify=CENTER, width=14)
        entry_cena_21.insert(0, "0.10")
        entry_cena_21.grid(row=11, column=6)
    elif nazwa_21.get() == "Igła 0,6 x 60":
        entry_cena_21 = Entry(root, textvariable=cena_21, justify=CENTER, width=14)
        entry_cena_21.insert(0, "0.09")
        entry_cena_21.grid(row=11, column=6)
    elif nazwa_21.get() == "Igła 0,7 x 40":
        entry_cena_21 = Entry(root, textvariable=cena_21, justify=CENTER, width=14)
        entry_cena_21.insert(0, "0.05")
        entry_cena_21.grid(row=11, column=6)
    elif nazwa_21.get() == "Igła 0,8 x 40":
        entry_cena_21 = Entry(root, textvariable=cena_21, justify=CENTER, width=14)
        entry_cena_21.insert(0, "0.05")
        entry_cena_21.grid(row=11, column=6)
    elif nazwa_21.get() == "Igła 1,1 x 70":
        entry_cena_21 = Entry(root, textvariable=cena_21, justify=CENTER, width=14)
        entry_cena_21.insert(0, "0.16")
        entry_cena_21.grid(row=11, column=6)
    elif nazwa_21.get() == "Kaniulowana śruba int. biokompozytowa z osłonką jednoraz.":
        entry_cena_21 = Entry(root, textvariable=cena_21, justify=CENTER, width=14)
        entry_cena_21.insert(0, "594")
        entry_cena_21.grid(row=11, column=6)
    elif nazwa_21.get() == "Kaniulowana śruba int. biokompozytowa z pełnym gwintem":
        entry_cena_21 = Entry(root, textvariable=cena_21, justify=CENTER, width=14)
        entry_cena_21.insert(0, "594")
        entry_cena_21.grid(row=11, column=6)
    elif nazwa_21.get() == "Końcówka do Shavera":
        entry_cena_21 = Entry(root, textvariable=cena_21, justify=CENTER, width=14)
        entry_cena_21.insert(0, "270")
        entry_cena_21.grid(row=11, column=6)
    elif nazwa_21.get() == "Kotwica biokompozytowa SwiveLock":
        entry_cena_21 = Entry(root, textvariable=cena_21, justify=CENTER, width=14)
        entry_cena_21.insert(0, "918")
        entry_cena_21.grid(row=11, column=6)
    elif nazwa_21.get() == "Kotwica Corkscrew":
        entry_cena_21 = Entry(root, textvariable=cena_21, justify=CENTER, width=14)
        entry_cena_21.insert(0, "604")
        entry_cena_21.grid(row=11, column=6)
    elif nazwa_21.get() == "Kotwica FASTak":
        entry_cena_21 = Entry(root, textvariable=cena_21, justify=CENTER, width=14)
        entry_cena_21.insert(0, "432")
        entry_cena_21.grid(row=11, column=6)
    elif nazwa_21.get() == "Kotwica PEEK SwiveLock":
        entry_cena_21 = Entry(root, textvariable=cena_21, justify=CENTER, width=14)
        entry_cena_21.insert(0, "885.60")
        entry_cena_21.grid(row=11, column=6)
    elif nazwa_21.get() == "NaCl 3000ml":
        entry_cena_21 = Entry(root, textvariable=cena_21, justify=CENTER, width=14)
        entry_cena_21.insert(0, "29.72")
        entry_cena_21.grid(row=11, column=6)
    elif nazwa_21.get() == "NaCl 5000ml":
        entry_cena_21 = Entry(root, textvariable=cena_21, justify=CENTER, width=14)
        entry_cena_21.insert(0, "58.33")
        entry_cena_21.grid(row=11, column=6)
    elif nazwa_21.get() == "Nici Dafilon 2-0":
        entry_cena_21 = Entry(root, textvariable=cena_21, justify=CENTER, width=14)
        entry_cena_21.insert(0, "6.60")
        entry_cena_21.grid(row=11, column=6)
    elif nazwa_21.get() == "Nici Novosyn 2":
        entry_cena_21 = Entry(root, textvariable=cena_21, justify=CENTER, width=14)
        entry_cena_21.insert(0, "13")
        entry_cena_21.grid(row=11, column=6)
    elif nazwa_21.get() == "Nici Novosyn 2-0":
        entry_cena_21 = Entry(root, textvariable=cena_21, justify=CENTER, width=14)
        entry_cena_21.insert(0, "7.70")
        entry_cena_21.grid(row=11, column=6)
    elif nazwa_21.get() == "Nici Novosyn 3-0":
        entry_cena_21 = Entry(root, textvariable=cena_21, justify=CENTER, width=14)
        entry_cena_21.insert(0, "7.70")
        entry_cena_21.grid(row=11, column=6)
    elif nazwa_21.get() == "Nici Nylon 2-0":
        entry_cena_21 = Entry(root, textvariable=cena_21, justify=CENTER, width=14)
        entry_cena_21.insert(0, "2.50")
        entry_cena_21.grid(row=11, column=6)
    elif nazwa_21.get() == "Nici Nylon 3-0":
        entry_cena_21 = Entry(root, textvariable=cena_21, justify=CENTER, width=14)
        entry_cena_21.insert(0, "2")
        entry_cena_21.grid(row=11, column=6)
    elif nazwa_21.get() == "Nici PGLA":
        entry_cena_21 = Entry(root, textvariable=cena_21, justify=CENTER, width=14)
        entry_cena_21.insert(0, "11.60")
        entry_cena_21.grid(row=11, column=6)
    elif nazwa_21.get() == "Nici PremiCron 3":
        entry_cena_21 = Entry(root, textvariable=cena_21, justify=CENTER, width=14)
        entry_cena_21.insert(0, "6.50")
        entry_cena_21.grid(row=11, column=6)
    elif nazwa_21.get() == "Nici Vicryl 4-0":
        entry_cena_21 = Entry(root, textvariable=cena_21, justify=CENTER, width=14)
        entry_cena_21.insert(0, "7.50")
        entry_cena_21.grid(row=11, column=6)
    elif nazwa_21.get() == "Nitinol Guide Pin 1.1":
        entry_cena_21 = Entry(root, textvariable=cena_21, justify=CENTER, width=14)
        entry_cena_21.insert(0, "145.80")
        entry_cena_21.grid(row=11, column=6)
    elif nazwa_21.get() == "Osłona na przewody":
        entry_cena_21 = Entry(root, textvariable=cena_21, justify=CENTER, width=14)
        entry_cena_21.insert(0, "2.50")
        entry_cena_21.grid(row=11, column=6)
    elif nazwa_21.get() == "Ostrze Arthrex 90(86)x19x1,27":
        entry_cena_21 = Entry(root, textvariable=cena_21, justify=CENTER, width=14)
        entry_cena_21.insert(0, "216")
        entry_cena_21.grid(row=11, column=6)
    elif nazwa_21.get() == "Ostrze piły":
        entry_cena_21 = Entry(root, textvariable=cena_21, justify=CENTER, width=14)
        entry_cena_21.insert(0, "108")
        entry_cena_21.grid(row=11, column=6)
    elif nazwa_21.get() == "Pielęgniarka anest.":
        entry_cena_21 = Entry(root, textvariable=cena_21, justify=CENTER, width=14)
        entry_cena_21.insert(0, "50")
        entry_cena_21.grid(row=11, column=6)
    elif nazwa_21.get() == "Pielęgniarka instr.":
        entry_cena_21 = Entry(root, textvariable=cena_21, justify=CENTER, width=14)
        entry_cena_21.insert(0, "50")
        entry_cena_21.grid(row=11, column=6)
    elif nazwa_21.get() == "Pielęgniarka 'Noviline'":
        entry_cena_21 = Entry(root, textvariable=cena_21, justify=CENTER, width=14)
        entry_cena_21.insert(0, "30")
        entry_cena_21.grid(row=11, column=6)
    elif nazwa_21.get() == "Płytka PeekPower do osteotomii klinowej":
        entry_cena_21 = Entry(root, textvariable=cena_21, justify=CENTER, width=14)
        entry_cena_21.insert(0, "2160")
        entry_cena_21.grid(row=11, column=6)
    elif nazwa_21.get() == "Rękawice jałowe 6,5":
        entry_cena_21 = Entry(root, textvariable=cena_21, justify=CENTER, width=14)
        entry_cena_21.insert(0, "1.20")
        entry_cena_21.grid(row=11, column=6)
    elif nazwa_21.get() == "Rękawice jałowe 7,0":
        entry_cena_21 = Entry(root, textvariable=cena_21, justify=CENTER, width=14)
        entry_cena_21.insert(0, "1.20")
        entry_cena_21.grid(row=11, column=6)
    elif nazwa_21.get() == "Rękawice jałowe 7,5":
        entry_cena_21 = Entry(root, textvariable=cena_21, justify=CENTER, width=14)
        entry_cena_21.insert(0, "1.20")
        entry_cena_21.grid(row=11, column=6)
    elif nazwa_21.get() == "Rękawice jałowe 8,00":
        entry_cena_21 = Entry(root, textvariable=cena_21, justify=CENTER, width=14)
        entry_cena_21.insert(0, "1.20")
        entry_cena_21.grid(row=11, column=6)
    elif nazwa_21.get() == "Rękojeść Interpulse wysokoprzepływowa":
        entry_cena_21 = Entry(root, textvariable=cena_21, justify=CENTER, width=14)
        entry_cena_21.insert(0, "216")
        entry_cena_21.grid(row=11, column=6)
    elif nazwa_21.get() == "Serweta":
        entry_cena_21 = Entry(root, textvariable=cena_21, justify=CENTER, width=14)
        entry_cena_21.insert(0, "6")
        entry_cena_21.grid(row=11, column=6)
    elif nazwa_21.get() == "Simplex Hv z Gentamycyna 10x40g":
        entry_cena_21 = Entry(root, textvariable=cena_21, justify=CENTER, width=14)
        entry_cena_21.insert(0, "162")
        entry_cena_21.grid(row=11, column=6)
    elif nazwa_21.get() == "Skalpel 11":
        entry_cena_21 = Entry(root, textvariable=cena_21, justify=CENTER, width=14)
        entry_cena_21.insert(0, "0.38")
        entry_cena_21.grid(row=11, column=6)
    elif nazwa_21.get() == "Skalpel 13":
        entry_cena_21 = Entry(root, textvariable=cena_21, justify=CENTER, width=14)
        entry_cena_21.insert(0, "1")
        entry_cena_21.grid(row=11, column=6)
    elif nazwa_21.get() == "Skalpel 22":
        entry_cena_21 = Entry(root, textvariable=cena_21, justify=CENTER, width=14)
        entry_cena_21.insert(0, "00000")
        entry_cena_21.grid(row=11, column=6)
    elif nazwa_21.get() == "Śruba blokująca PeekPower do osteotomii":
        entry_cena_21 = Entry(root, textvariable=cena_21, justify=CENTER, width=14)
        entry_cena_21.insert(0, "194")
        entry_cena_21.grid(row=11, column=6)
    elif nazwa_21.get() == "System do mieszania próżniowego":
        entry_cena_21 = Entry(root, textvariable=cena_21, justify=CENTER, width=14)
        entry_cena_21.insert(0, "216")
        entry_cena_21.grid(row=11, column=6)
    elif nazwa_21.get() == "System wprowadzania implantów ACL TightRope":
        entry_cena_21 = Entry(root, textvariable=cena_21, justify=CENTER, width=14)
        entry_cena_21.insert(0, "702")
        entry_cena_21.grid(row=11, column=6)
    elif nazwa_21.get() == "Szew FiberWire 2":
        entry_cena_21 = Entry(root, textvariable=cena_21, justify=CENTER, width=14)
        entry_cena_21.insert(0, "86.40")
        entry_cena_21.grid(row=11, column=6)
    elif nazwa_21.get() == "Taśma przylepna 10x50":
        entry_cena_21 = Entry(root, textvariable=cena_21, justify=CENTER, width=14)
        entry_cena_21.insert(0, "1.04")
        entry_cena_21.grid(row=11, column=6)
    elif nazwa_21.get() == "Triathlon elem. udowy lewy":
        entry_cena_21 = Entry(root, textvariable=cena_21, justify=CENTER, width=14)
        entry_cena_21.insert(0, "3132")
        entry_cena_21.grid(row=11, column=6)
    elif nazwa_21.get() == "Triathlon PS wkładka x3-9mm #4":
        entry_cena_21 = Entry(root, textvariable=cena_21, justify=CENTER, width=14)
        entry_cena_21.insert(0, "756")
        entry_cena_21.grid(row=11, column=6)
    elif nazwa_21.get() == "Triathlon taca piszczelowa":
        entry_cena_21 = Entry(root, textvariable=cena_21, justify=CENTER, width=14)
        entry_cena_21.insert(0, "1296")
        entry_cena_21.grid(row=11, column=6)
    elif nazwa_21.get() == "Wkłady 3L z żelem":
        entry_cena_21 = Entry(root, textvariable=cena_21, justify=CENTER, width=14)
        entry_cena_21.insert(0, "10.26")
        entry_cena_21.grid(row=11, column=6)
    elif nazwa_21.get() == "Zestaw do artroskopii":
        entry_cena_21 = Entry(root, textvariable=cena_21, justify=CENTER, width=14)
        entry_cena_21.insert(0, "67")
        entry_cena_21.grid(row=11, column=6)
    elif nazwa_21.get() == "Zestaw do artroskopii barku":
        entry_cena_21 = Entry(root, textvariable=cena_21, justify=CENTER, width=14)
        entry_cena_21.insert(0, "108")
        entry_cena_21.grid(row=11, column=6)
    elif nazwa_21.get() == "Zestaw do drenażu":
        entry_cena_21 = Entry(root, textvariable=cena_21, justify=CENTER, width=14)
        entry_cena_21.insert(0, "14.23")
        entry_cena_21.grid(row=11, column=6)
    elif nazwa_21.get() == "Zestaw ortopedyczny":
        entry_cena_21 = Entry(root, textvariable=cena_21, justify=CENTER, width=14)
        entry_cena_21.insert(0, "28.08")
        entry_cena_21.grid(row=11, column=6)
    elif nazwa_21.get() == "Gaziki 20 x 10cm":
        entry_cena_21 = Entry(root, textvariable=cena_21, justify=CENTER, width=14)
        entry_cena_21.insert(0, "0.46")
        entry_cena_21.grid(row=11, column=6)
    else:
        entry_cena_21 = Entry(root, textvariable=cena_21, justify=CENTER, width=14, bg="#ffff00")
        entry_cena_21.insert(0, "0")
        entry_cena_21.grid(row=11, column=6)

    if nazwa_22.get() == "--puste--":
        entry_cena_22 = Entry(root, textvariable=cena_22, justify=CENTER, width=14)
        entry_cena_22.insert(0, "0")
        entry_cena_22.grid(row=12, column=6)
    elif nazwa_22.get() == "Ablator":
        entry_cena_22 = Entry(root, textvariable=cena_22, justify=CENTER, width=14)
        entry_cena_22.insert(0, "572")
        entry_cena_22.grid(row=12, column=6)
    elif nazwa_22.get() == "Anestezjolog":
        entry_cena_22 = Entry(root, textvariable=cena_22, justify=CENTER, width=14, bg="#ffff00")
        entry_cena_22.insert(0, "350")
        entry_cena_22.grid(row=12, column=6)
    elif nazwa_22.get() == "Butelka 400ml do długotrwałego odsysania ran j.u. sterylna":
        entry_cena_22 = Entry(root, textvariable=cena_22, justify=CENTER, width=14)
        entry_cena_22.insert(0, "4")
        entry_cena_22.grid(row=12, column=6)
    elif nazwa_22.get() == "Doba":
        entry_cena_22 = Entry(root, textvariable=cena_22, justify=CENTER, width=14)
        entry_cena_22.insert(0, "700")
        entry_cena_22.grid(row=12, column=6)
    elif nazwa_22.get() == "Dren łączący do ssaka Grena":
        entry_cena_22 = Entry(root, textvariable=cena_22, justify=CENTER, width=14)
        entry_cena_22.insert(0, "5")
        entry_cena_22.grid(row=12, column=6)
    elif nazwa_22.get() == "Dren Redona Ch 16 dł. 800mm z trokarem":
        entry_cena_22 = Entry(root, textvariable=cena_22, justify=CENTER, width=14)
        entry_cena_22.insert(0, "29.74")
        entry_cena_22.grid(row=12, column=6)
    elif nazwa_22.get() == "Dren do pompy Artrex":
        entry_cena_22 = Entry(root, textvariable=cena_22, justify=CENTER, width=14)
        entry_cena_22.insert(0, "108")
        entry_cena_22.grid(row=12, column=6)
    elif nazwa_22.get() == "Drut wiercący 2,4 x 311":
        entry_cena_22 = Entry(root, textvariable=cena_22, justify=CENTER, width=14)
        entry_cena_22.insert(0, "139.60")
        entry_cena_22.grid(row=12, column=6)
    elif nazwa_22.get() == "Fartuch jałowy L":
        entry_cena_22 = Entry(root, textvariable=cena_22, justify=CENTER, width=14)
        entry_cena_22.insert(0, "17")
        entry_cena_22.grid(row=12, column=6)
    elif nazwa_22.get() == "Fartuch jałowy M":
        entry_cena_22 = Entry(root, textvariable=cena_22, justify=CENTER, width=14)
        entry_cena_22.insert(0, "15.28")
        entry_cena_22.grid(row=12, column=6)
    elif nazwa_22.get() == "Fartuch jałowy XL":
        entry_cena_22 = Entry(root, textvariable=cena_22, justify=CENTER, width=14)
        entry_cena_22.insert(0, "20.84")
        entry_cena_22.grid(row=12, column=6)
    elif nazwa_22.get() == "FasatThread BioComposite Interference Screw 8x30":
        entry_cena_22 = Entry(root, textvariable=cena_22, justify=CENTER, width=14)
        entry_cena_22.insert(0, "594")
        entry_cena_22.grid(row=12, column=6)
    elif nazwa_22.get() == "Folia operacyjna, jałowa 45cm x 55cm":
        entry_cena_22 = Entry(root, textvariable=cena_22, justify=CENTER, width=14)
        entry_cena_22.insert(0, "9.99")
        entry_cena_22.grid(row=12, column=6)
    elif nazwa_22.get() == "Gaziki 10 x 10cm":
        entry_cena_22 = Entry(root, textvariable=cena_22, justify=CENTER, width=14)
        entry_cena_22.insert(0, "0.10")
        entry_cena_22.grid(row=12, column=6)
    elif nazwa_22.get() == "Igła 0,6 x 60":
        entry_cena_22 = Entry(root, textvariable=cena_22, justify=CENTER, width=14)
        entry_cena_22.insert(0, "0.09")
        entry_cena_22.grid(row=12, column=6)
    elif nazwa_22.get() == "Igła 0,7 x 40":
        entry_cena_22 = Entry(root, textvariable=cena_22, justify=CENTER, width=14)
        entry_cena_22.insert(0, "0.05")
        entry_cena_22.grid(row=12, column=6)
    elif nazwa_22.get() == "Igła 0,8 x 40":
        entry_cena_22 = Entry(root, textvariable=cena_22, justify=CENTER, width=14)
        entry_cena_22.insert(0, "0.05")
        entry_cena_22.grid(row=12, column=6)
    elif nazwa_22.get() == "Igła 1,1 x 70":
        entry_cena_22 = Entry(root, textvariable=cena_22, justify=CENTER, width=14)
        entry_cena_22.insert(0, "0.16")
        entry_cena_22.grid(row=12, column=6)
    elif nazwa_22.get() == "Kaniulowana śruba int. biokompozytowa z osłonką jednoraz.":
        entry_cena_22 = Entry(root, textvariable=cena_22, justify=CENTER, width=14)
        entry_cena_22.insert(0, "594")
        entry_cena_22.grid(row=12, column=6)
    elif nazwa_22.get() == "Kaniulowana śruba int. biokompozytowa z pełnym gwintem":
        entry_cena_22 = Entry(root, textvariable=cena_22, justify=CENTER, width=14)
        entry_cena_22.insert(0, "594")
        entry_cena_22.grid(row=12, column=6)
    elif nazwa_22.get() == "Końcówka do Shavera":
        entry_cena_22 = Entry(root, textvariable=cena_22, justify=CENTER, width=14)
        entry_cena_22.insert(0, "270")
        entry_cena_22.grid(row=12, column=6)
    elif nazwa_22.get() == "Kotwica biokompozytowa SwiveLock":
        entry_cena_22 = Entry(root, textvariable=cena_22, justify=CENTER, width=14)
        entry_cena_22.insert(0, "918")
        entry_cena_22.grid(row=12, column=6)
    elif nazwa_22.get() == "Kotwica Corkscrew":
        entry_cena_22 = Entry(root, textvariable=cena_22, justify=CENTER, width=14)
        entry_cena_22.insert(0, "604")
        entry_cena_22.grid(row=12, column=6)
    elif nazwa_22.get() == "Kotwica FASTak":
        entry_cena_22 = Entry(root, textvariable=cena_22, justify=CENTER, width=14)
        entry_cena_22.insert(0, "432")
        entry_cena_22.grid(row=12, column=6)
    elif nazwa_22.get() == "Kotwica PEEK SwiveLock":
        entry_cena_22 = Entry(root, textvariable=cena_22, justify=CENTER, width=14)
        entry_cena_22.insert(0, "885.60")
        entry_cena_22.grid(row=12, column=6)
    elif nazwa_22.get() == "NaCl 3000ml":
        entry_cena_22 = Entry(root, textvariable=cena_22, justify=CENTER, width=14)
        entry_cena_22.insert(0, "29.72")
        entry_cena_22.grid(row=12, column=6)
    elif nazwa_22.get() == "NaCl 5000ml":
        entry_cena_22 = Entry(root, textvariable=cena_22, justify=CENTER, width=14)
        entry_cena_22.insert(0, "58.33")
        entry_cena_22.grid(row=12, column=6)
    elif nazwa_22.get() == "Nici Dafilon 2-0":
        entry_cena_22 = Entry(root, textvariable=cena_22, justify=CENTER, width=14)
        entry_cena_22.insert(0, "6.60")
        entry_cena_22.grid(row=12, column=6)
    elif nazwa_22.get() == "Nici Novosyn 2":
        entry_cena_22 = Entry(root, textvariable=cena_22, justify=CENTER, width=14)
        entry_cena_22.insert(0, "13")
        entry_cena_22.grid(row=12, column=6)
    elif nazwa_22.get() == "Nici Novosyn 2-0":
        entry_cena_22 = Entry(root, textvariable=cena_22, justify=CENTER, width=14)
        entry_cena_22.insert(0, "7.70")
        entry_cena_22.grid(row=12, column=6)
    elif nazwa_22.get() == "Nici Novosyn 3-0":
        entry_cena_22 = Entry(root, textvariable=cena_22, justify=CENTER, width=14)
        entry_cena_22.insert(0, "7.70")
        entry_cena_22.grid(row=12, column=6)
    elif nazwa_22.get() == "Nici Nylon 2-0":
        entry_cena_22 = Entry(root, textvariable=cena_22, justify=CENTER, width=14)
        entry_cena_22.insert(0, "2.50")
        entry_cena_22.grid(row=12, column=6)
    elif nazwa_22.get() == "Nici Nylon 3-0":
        entry_cena_22 = Entry(root, textvariable=cena_22, justify=CENTER, width=14)
        entry_cena_22.insert(0, "2")
        entry_cena_22.grid(row=12, column=6)
    elif nazwa_22.get() == "Nici PGLA":
        entry_cena_22 = Entry(root, textvariable=cena_22, justify=CENTER, width=14)
        entry_cena_22.insert(0, "11.60")
        entry_cena_22.grid(row=12, column=6)
    elif nazwa_22.get() == "Nici PremiCron 3":
        entry_cena_22 = Entry(root, textvariable=cena_22, justify=CENTER, width=14)
        entry_cena_22.insert(0, "6.50")
        entry_cena_22.grid(row=12, column=6)
    elif nazwa_22.get() == "Nici Vicryl 4-0":
        entry_cena_22 = Entry(root, textvariable=cena_22, justify=CENTER, width=14)
        entry_cena_22.insert(0, "7.50")
        entry_cena_22.grid(row=12, column=6)
    elif nazwa_22.get() == "Nitinol Guide Pin 1.1":
        entry_cena_22 = Entry(root, textvariable=cena_22, justify=CENTER, width=14)
        entry_cena_22.insert(0, "145.80")
        entry_cena_22.grid(row=12, column=6)
    elif nazwa_22.get() == "Osłona na przewody":
        entry_cena_22 = Entry(root, textvariable=cena_22, justify=CENTER, width=14)
        entry_cena_22.insert(0, "2.50")
        entry_cena_22.grid(row=12, column=6)
    elif nazwa_22.get() == "Ostrze Arthrex 90(86)x19x1,27":
        entry_cena_22 = Entry(root, textvariable=cena_22, justify=CENTER, width=14)
        entry_cena_22.insert(0, "216")
        entry_cena_22.grid(row=12, column=6)
    elif nazwa_22.get() == "Ostrze piły":
        entry_cena_22 = Entry(root, textvariable=cena_22, justify=CENTER, width=14)
        entry_cena_22.insert(0, "108")
        entry_cena_22.grid(row=12, column=6)
    elif nazwa_22.get() == "Pielęgniarka anest.":
        entry_cena_22 = Entry(root, textvariable=cena_22, justify=CENTER, width=14)
        entry_cena_22.insert(0, "50")
        entry_cena_22.grid(row=12, column=6)
    elif nazwa_22.get() == "Pielęgniarka instr.":
        entry_cena_22 = Entry(root, textvariable=cena_22, justify=CENTER, width=14)
        entry_cena_22.insert(0, "50")
        entry_cena_22.grid(row=12, column=6)
    elif nazwa_22.get() == "Pielęgniarka 'Noviline'":
        entry_cena_22 = Entry(root, textvariable=cena_22, justify=CENTER, width=14)
        entry_cena_22.insert(0, "30")
        entry_cena_22.grid(row=12, column=6)
    elif nazwa_22.get() == "Płytka PeekPower do osteotomii klinowej":
        entry_cena_22 = Entry(root, textvariable=cena_22, justify=CENTER, width=14)
        entry_cena_22.insert(0, "2160")
        entry_cena_22.grid(row=12, column=6)
    elif nazwa_22.get() == "Rękawice jałowe 6,5":
        entry_cena_22 = Entry(root, textvariable=cena_22, justify=CENTER, width=14)
        entry_cena_22.insert(0, "1.20")
        entry_cena_22.grid(row=12, column=6)
    elif nazwa_22.get() == "Rękawice jałowe 7,0":
        entry_cena_22 = Entry(root, textvariable=cena_22, justify=CENTER, width=14)
        entry_cena_22.insert(0, "1.20")
        entry_cena_22.grid(row=12, column=6)
    elif nazwa_22.get() == "Rękawice jałowe 7,5":
        entry_cena_22 = Entry(root, textvariable=cena_22, justify=CENTER, width=14)
        entry_cena_22.insert(0, "1.20")
        entry_cena_22.grid(row=12, column=6)
    elif nazwa_22.get() == "Rękawice jałowe 8,00":
        entry_cena_22 = Entry(root, textvariable=cena_22, justify=CENTER, width=14)
        entry_cena_22.insert(0, "1.20")
        entry_cena_22.grid(row=12, column=6)
    elif nazwa_22.get() == "Rękojeść Interpulse wysokoprzepływowa":
        entry_cena_22 = Entry(root, textvariable=cena_22, justify=CENTER, width=14)
        entry_cena_22.insert(0, "216")
        entry_cena_22.grid(row=12, column=6)
    elif nazwa_22.get() == "Serweta":
        entry_cena_22 = Entry(root, textvariable=cena_22, justify=CENTER, width=14)
        entry_cena_22.insert(0, "6")
        entry_cena_22.grid(row=12, column=6)
    elif nazwa_22.get() == "Simplex Hv z Gentamycyna 10x40g":
        entry_cena_22 = Entry(root, textvariable=cena_22, justify=CENTER, width=14)
        entry_cena_22.insert(0, "162")
        entry_cena_22.grid(row=12, column=6)
    elif nazwa_22.get() == "Skalpel 11":
        entry_cena_22 = Entry(root, textvariable=cena_22, justify=CENTER, width=14)
        entry_cena_22.insert(0, "0.38")
        entry_cena_22.grid(row=12, column=6)
    elif nazwa_22.get() == "Skalpel 13":
        entry_cena_22 = Entry(root, textvariable=cena_22, justify=CENTER, width=14)
        entry_cena_22.insert(0, "1")
        entry_cena_22.grid(row=12, column=6)
    elif nazwa_22.get() == "Skalpel 22":
        entry_cena_22 = Entry(root, textvariable=cena_22, justify=CENTER, width=14)
        entry_cena_22.insert(0, "00000")
        entry_cena_22.grid(row=12, column=6)
    elif nazwa_22.get() == "Śruba blokująca PeekPower do osteotomii":
        entry_cena_22 = Entry(root, textvariable=cena_22, justify=CENTER, width=14)
        entry_cena_22.insert(0, "194")
        entry_cena_22.grid(row=12, column=6)
    elif nazwa_22.get() == "System do mieszania próżniowego":
        entry_cena_22 = Entry(root, textvariable=cena_22, justify=CENTER, width=14)
        entry_cena_22.insert(0, "216")
        entry_cena_22.grid(row=12, column=6)
    elif nazwa_22.get() == "System wprowadzania implantów ACL TightRope":
        entry_cena_22 = Entry(root, textvariable=cena_22, justify=CENTER, width=14)
        entry_cena_22.insert(0, "702")
        entry_cena_22.grid(row=12, column=6)
    elif nazwa_22.get() == "Szew FiberWire 2":
        entry_cena_22 = Entry(root, textvariable=cena_22, justify=CENTER, width=14)
        entry_cena_22.insert(0, "86.40")
        entry_cena_22.grid(row=12, column=6)
    elif nazwa_22.get() == "Taśma przylepna 10x50":
        entry_cena_22 = Entry(root, textvariable=cena_22, justify=CENTER, width=14)
        entry_cena_22.insert(0, "1.04")
        entry_cena_22.grid(row=12, column=6)
    elif nazwa_22.get() == "Triathlon elem. udowy lewy":
        entry_cena_22 = Entry(root, textvariable=cena_22, justify=CENTER, width=14)
        entry_cena_22.insert(0, "3132")
        entry_cena_22.grid(row=12, column=6)
    elif nazwa_22.get() == "Triathlon PS wkładka x3-9mm #4":
        entry_cena_22 = Entry(root, textvariable=cena_22, justify=CENTER, width=14)
        entry_cena_22.insert(0, "756")
        entry_cena_22.grid(row=12, column=6)
    elif nazwa_22.get() == "Triathlon taca piszczelowa":
        entry_cena_22 = Entry(root, textvariable=cena_22, justify=CENTER, width=14)
        entry_cena_22.insert(0, "1296")
        entry_cena_22.grid(row=12, column=6)
    elif nazwa_22.get() == "Wkłady 3L z żelem":
        entry_cena_22 = Entry(root, textvariable=cena_22, justify=CENTER, width=14)
        entry_cena_22.insert(0, "10.26")
        entry_cena_22.grid(row=12, column=6)
    elif nazwa_22.get() == "Zestaw do artroskopii":
        entry_cena_22 = Entry(root, textvariable=cena_22, justify=CENTER, width=14)
        entry_cena_22.insert(0, "67")
        entry_cena_22.grid(row=12, column=6)
    elif nazwa_22.get() == "Zestaw do artroskopii barku":
        entry_cena_22 = Entry(root, textvariable=cena_22, justify=CENTER, width=14)
        entry_cena_22.insert(0, "108")
        entry_cena_22.grid(row=12, column=6)
    elif nazwa_22.get() == "Zestaw do drenażu":
        entry_cena_22 = Entry(root, textvariable=cena_22, justify=CENTER, width=14)
        entry_cena_22.insert(0, "14.23")
        entry_cena_22.grid(row=12, column=6)
    elif nazwa_22.get() == "Zestaw ortopedyczny":
        entry_cena_22 = Entry(root, textvariable=cena_22, justify=CENTER, width=14)
        entry_cena_22.insert(0, "28.08")
        entry_cena_22.grid(row=12, column=6)
    elif nazwa_22.get() == "Gaziki 20 x 10cm":
        entry_cena_22 = Entry(root, textvariable=cena_22, justify=CENTER, width=14)
        entry_cena_22.insert(0, "0.46")
        entry_cena_22.grid(row=12, column=6)
    else:
        entry_cena_22 = Entry(root, textvariable=cena_22, justify=CENTER, width=14, bg="#ffff00")
        entry_cena_22.insert(0, "0")
        entry_cena_22.grid(row=12, column=6)

    if nazwa_23.get() == "--puste--":
        entry_cena_23 = Entry(root, textvariable=cena_23, justify=CENTER, width=14)
        entry_cena_23.insert(0, "0")
        entry_cena_23.grid(row=13, column=6)
    elif nazwa_23.get() == "Ablator":
        entry_cena_23 = Entry(root, textvariable=cena_23, justify=CENTER, width=14)
        entry_cena_23.insert(0, "572")
        entry_cena_23.grid(row=13, column=6)
    elif nazwa_23.get() == "Anestezjolog":
        entry_cena_23 = Entry(root, textvariable=cena_23, justify=CENTER, width=14, bg="#ffff00")
        entry_cena_23.insert(0, "350")
        entry_cena_23.grid(row=13, column=6)
    elif nazwa_23.get() == "Butelka 400ml do długotrwałego odsysania ran j.u. sterylna":
        entry_cena_23 = Entry(root, textvariable=cena_23, justify=CENTER, width=14)
        entry_cena_23.insert(0, "4")
        entry_cena_23.grid(row=13, column=6)
    elif nazwa_23.get() == "Doba":
        entry_cena_23 = Entry(root, textvariable=cena_23, justify=CENTER, width=14)
        entry_cena_23.insert(0, "700")
        entry_cena_23.grid(row=13, column=6)
    elif nazwa_23.get() == "Dren łączący do ssaka Grena":
        entry_cena_23 = Entry(root, textvariable=cena_23, justify=CENTER, width=14)
        entry_cena_23.insert(0, "5")
        entry_cena_23.grid(row=13, column=6)
    elif nazwa_23.get() == "Dren Redona Ch 16 dł. 800mm z trokarem":
        entry_cena_23 = Entry(root, textvariable=cena_23, justify=CENTER, width=14)
        entry_cena_23.insert(0, "29.74")
        entry_cena_23.grid(row=13, column=6)
    elif nazwa_23.get() == "Dren do pompy Artrex":
        entry_cena_23 = Entry(root, textvariable=cena_23, justify=CENTER, width=14)
        entry_cena_23.insert(0, "108")
        entry_cena_23.grid(row=13, column=6)
    elif nazwa_23.get() == "Drut wiercący 2,4 x 311":
        entry_cena_23 = Entry(root, textvariable=cena_23, justify=CENTER, width=14)
        entry_cena_23.insert(0, "139.60")
        entry_cena_23.grid(row=13, column=6)
    elif nazwa_23.get() == "Fartuch jałowy L":
        entry_cena_23 = Entry(root, textvariable=cena_23, justify=CENTER, width=14)
        entry_cena_23.insert(0, "17")
        entry_cena_23.grid(row=13, column=6)
    elif nazwa_23.get() == "Fartuch jałowy M":
        entry_cena_23 = Entry(root, textvariable=cena_23, justify=CENTER, width=14)
        entry_cena_23.insert(0, "15.28")
        entry_cena_23.grid(row=13, column=6)
    elif nazwa_23.get() == "Fartuch jałowy XL":
        entry_cena_23 = Entry(root, textvariable=cena_23, justify=CENTER, width=14)
        entry_cena_23.insert(0, "20.84")
        entry_cena_23.grid(row=13, column=6)
    elif nazwa_23.get() == "FasatThread BioComposite Interference Screw 8x30":
        entry_cena_23 = Entry(root, textvariable=cena_23, justify=CENTER, width=14)
        entry_cena_23.insert(0, "594")
        entry_cena_23.grid(row=13, column=6)
    elif nazwa_23.get() == "Folia operacyjna, jałowa 45cm x 55cm":
        entry_cena_23 = Entry(root, textvariable=cena_23, justify=CENTER, width=14)
        entry_cena_23.insert(0, "9.99")
        entry_cena_23.grid(row=13, column=6)
    elif nazwa_23.get() == "Gaziki 10 x 10cm":
        entry_cena_23 = Entry(root, textvariable=cena_23, justify=CENTER, width=14)
        entry_cena_23.insert(0, "0.10")
        entry_cena_23.grid(row=13, column=6)
    elif nazwa_23.get() == "Igła 0,6 x 60":
        entry_cena_23 = Entry(root, textvariable=cena_23, justify=CENTER, width=14)
        entry_cena_23.insert(0, "0.09")
        entry_cena_23.grid(row=13, column=6)
    elif nazwa_23.get() == "Igła 0,7 x 40":
        entry_cena_23 = Entry(root, textvariable=cena_23, justify=CENTER, width=14)
        entry_cena_23.insert(0, "0.05")
        entry_cena_23.grid(row=13, column=6)
    elif nazwa_23.get() == "Igła 0,8 x 40":
        entry_cena_23 = Entry(root, textvariable=cena_23, justify=CENTER, width=14)
        entry_cena_23.insert(0, "0.05")
        entry_cena_23.grid(row=13, column=6)
    elif nazwa_23.get() == "Igła 1,1 x 70":
        entry_cena_23 = Entry(root, textvariable=cena_23, justify=CENTER, width=14)
        entry_cena_23.insert(0, "0.16")
        entry_cena_23.grid(row=13, column=6)
    elif nazwa_23.get() == "Kaniulowana śruba int. biokompozytowa z osłonką jednoraz.":
        entry_cena_23 = Entry(root, textvariable=cena_23, justify=CENTER, width=14)
        entry_cena_23.insert(0, "594")
        entry_cena_23.grid(row=13, column=6)
    elif nazwa_23.get() == "Kaniulowana śruba int. biokompozytowa z pełnym gwintem":
        entry_cena_23 = Entry(root, textvariable=cena_23, justify=CENTER, width=14)
        entry_cena_23.insert(0, "594")
        entry_cena_23.grid(row=13, column=6)
    elif nazwa_23.get() == "Końcówka do Shavera":
        entry_cena_23 = Entry(root, textvariable=cena_23, justify=CENTER, width=14)
        entry_cena_23.insert(0, "270")
        entry_cena_23.grid(row=13, column=6)
    elif nazwa_23.get() == "Kotwica biokompozytowa SwiveLock":
        entry_cena_23 = Entry(root, textvariable=cena_23, justify=CENTER, width=14)
        entry_cena_23.insert(0, "918")
        entry_cena_23.grid(row=13, column=6)
    elif nazwa_23.get() == "Kotwica Corkscrew":
        entry_cena_23 = Entry(root, textvariable=cena_23, justify=CENTER, width=14)
        entry_cena_23.insert(0, "604")
        entry_cena_23.grid(row=13, column=6)
    elif nazwa_23.get() == "Kotwica FASTak":
        entry_cena_23 = Entry(root, textvariable=cena_23, justify=CENTER, width=14)
        entry_cena_23.insert(0, "432")
        entry_cena_23.grid(row=13, column=6)
    elif nazwa_23.get() == "Kotwica PEEK SwiveLock":
        entry_cena_23 = Entry(root, textvariable=cena_23, justify=CENTER, width=14)
        entry_cena_23.insert(0, "885.60")
        entry_cena_23.grid(row=13, column=6)
    elif nazwa_23.get() == "NaCl 3000ml":
        entry_cena_23 = Entry(root, textvariable=cena_23, justify=CENTER, width=14)
        entry_cena_23.insert(0, "29.72")
        entry_cena_23.grid(row=13, column=6)
    elif nazwa_23.get() == "NaCl 5000ml":
        entry_cena_23 = Entry(root, textvariable=cena_23, justify=CENTER, width=14)
        entry_cena_23.insert(0, "58.33")
        entry_cena_23.grid(row=13, column=6)
    elif nazwa_23.get() == "Nici Dafilon 2-0":
        entry_cena_23 = Entry(root, textvariable=cena_23, justify=CENTER, width=14)
        entry_cena_23.insert(0, "6.60")
        entry_cena_23.grid(row=13, column=6)
    elif nazwa_23.get() == "Nici Novosyn 2":
        entry_cena_23 = Entry(root, textvariable=cena_23, justify=CENTER, width=14)
        entry_cena_23.insert(0, "13")
        entry_cena_23.grid(row=13, column=6)
    elif nazwa_23.get() == "Nici Novosyn 2-0":
        entry_cena_23 = Entry(root, textvariable=cena_23, justify=CENTER, width=14)
        entry_cena_23.insert(0, "7.70")
        entry_cena_23.grid(row=13, column=6)
    elif nazwa_23.get() == "Nici Novosyn 3-0":
        entry_cena_23 = Entry(root, textvariable=cena_23, justify=CENTER, width=14)
        entry_cena_23.insert(0, "7.70")
        entry_cena_23.grid(row=13, column=6)
    elif nazwa_23.get() == "Nici Nylon 2-0":
        entry_cena_23 = Entry(root, textvariable=cena_23, justify=CENTER, width=14)
        entry_cena_23.insert(0, "2.50")
        entry_cena_23.grid(row=13, column=6)
    elif nazwa_23.get() == "Nici Nylon 3-0":
        entry_cena_23 = Entry(root, textvariable=cena_23, justify=CENTER, width=14)
        entry_cena_23.insert(0, "2")
        entry_cena_23.grid(row=13, column=6)
    elif nazwa_23.get() == "Nici PGLA":
        entry_cena_23 = Entry(root, textvariable=cena_23, justify=CENTER, width=14)
        entry_cena_23.insert(0, "11.60")
        entry_cena_23.grid(row=13, column=6)
    elif nazwa_23.get() == "Nici PremiCron 3":
        entry_cena_23 = Entry(root, textvariable=cena_23, justify=CENTER, width=14)
        entry_cena_23.insert(0, "6.50")
        entry_cena_23.grid(row=13, column=6)
    elif nazwa_23.get() == "Nici Vicryl 4-0":
        entry_cena_23 = Entry(root, textvariable=cena_23, justify=CENTER, width=14)
        entry_cena_23.insert(0, "7.50")
        entry_cena_23.grid(row=13, column=6)
    elif nazwa_23.get() == "Nitinol Guide Pin 1.1":
        entry_cena_23 = Entry(root, textvariable=cena_23, justify=CENTER, width=14)
        entry_cena_23.insert(0, "145.80")
        entry_cena_23.grid(row=13, column=6)
    elif nazwa_23.get() == "Osłona na przewody":
        entry_cena_23 = Entry(root, textvariable=cena_23, justify=CENTER, width=14)
        entry_cena_23.insert(0, "2.50")
        entry_cena_23.grid(row=13, column=6)
    elif nazwa_23.get() == "Ostrze Arthrex 90(86)x19x1,27":
        entry_cena_23 = Entry(root, textvariable=cena_23, justify=CENTER, width=14)
        entry_cena_23.insert(0, "216")
        entry_cena_23.grid(row=13, column=6)
    elif nazwa_23.get() == "Ostrze piły":
        entry_cena_23 = Entry(root, textvariable=cena_23, justify=CENTER, width=14)
        entry_cena_23.insert(0, "108")
        entry_cena_23.grid(row=13, column=6)
    elif nazwa_23.get() == "Pielęgniarka anest.":
        entry_cena_23 = Entry(root, textvariable=cena_23, justify=CENTER, width=14)
        entry_cena_23.insert(0, "50")
        entry_cena_23.grid(row=13, column=6)
    elif nazwa_23.get() == "Pielęgniarka instr.":
        entry_cena_23 = Entry(root, textvariable=cena_23, justify=CENTER, width=14)
        entry_cena_23.insert(0, "50")
        entry_cena_23.grid(row=13, column=6)
    elif nazwa_23.get() == "Pielęgniarka 'Noviline'":
        entry_cena_23 = Entry(root, textvariable=cena_23, justify=CENTER, width=14)
        entry_cena_23.insert(0, "30")
        entry_cena_23.grid(row=13, column=6)
    elif nazwa_23.get() == "Płytka PeekPower do osteotomii klinowej":
        entry_cena_23 = Entry(root, textvariable=cena_23, justify=CENTER, width=14)
        entry_cena_23.insert(0, "2160")
        entry_cena_23.grid(row=13, column=6)
    elif nazwa_23.get() == "Rękawice jałowe 6,5":
        entry_cena_23 = Entry(root, textvariable=cena_23, justify=CENTER, width=14)
        entry_cena_23.insert(0, "1.20")
        entry_cena_23.grid(row=13, column=6)
    elif nazwa_23.get() == "Rękawice jałowe 7,0":
        entry_cena_23 = Entry(root, textvariable=cena_23, justify=CENTER, width=14)
        entry_cena_23.insert(0, "1.20")
        entry_cena_23.grid(row=13, column=6)
    elif nazwa_23.get() == "Rękawice jałowe 7,5":
        entry_cena_23 = Entry(root, textvariable=cena_23, justify=CENTER, width=14)
        entry_cena_23.insert(0, "1.20")
        entry_cena_23.grid(row=13, column=6)
    elif nazwa_23.get() == "Rękawice jałowe 8,00":
        entry_cena_23 = Entry(root, textvariable=cena_23, justify=CENTER, width=14)
        entry_cena_23.insert(0, "1.20")
        entry_cena_23.grid(row=13, column=6)
    elif nazwa_23.get() == "Rękojeść Interpulse wysokoprzepływowa":
        entry_cena_23 = Entry(root, textvariable=cena_23, justify=CENTER, width=14)
        entry_cena_23.insert(0, "216")
        entry_cena_23.grid(row=13, column=6)
    elif nazwa_23.get() == "Serweta":
        entry_cena_23 = Entry(root, textvariable=cena_23, justify=CENTER, width=14)
        entry_cena_23.insert(0, "6")
        entry_cena_23.grid(row=13, column=6)
    elif nazwa_23.get() == "Simplex Hv z Gentamycyna 10x40g":
        entry_cena_23 = Entry(root, textvariable=cena_23, justify=CENTER, width=14)
        entry_cena_23.insert(0, "162")
        entry_cena_23.grid(row=13, column=6)
    elif nazwa_23.get() == "Skalpel 11":
        entry_cena_23 = Entry(root, textvariable=cena_23, justify=CENTER, width=14)
        entry_cena_23.insert(0, "0.38")
        entry_cena_23.grid(row=13, column=6)
    elif nazwa_23.get() == "Skalpel 13":
        entry_cena_23 = Entry(root, textvariable=cena_23, justify=CENTER, width=14)
        entry_cena_23.insert(0, "1")
        entry_cena_23.grid(row=13, column=6)
    elif nazwa_23.get() == "Skalpel 22":
        entry_cena_23 = Entry(root, textvariable=cena_23, justify=CENTER, width=14)
        entry_cena_23.insert(0, "00000")
        entry_cena_23.grid(row=13, column=6)
    elif nazwa_23.get() == "Śruba blokująca PeekPower do osteotomii":
        entry_cena_23 = Entry(root, textvariable=cena_23, justify=CENTER, width=14)
        entry_cena_23.insert(0, "194")
        entry_cena_23.grid(row=13, column=6)
    elif nazwa_23.get() == "System do mieszania próżniowego":
        entry_cena_23 = Entry(root, textvariable=cena_23, justify=CENTER, width=14)
        entry_cena_23.insert(0, "216")
        entry_cena_23.grid(row=13, column=6)
    elif nazwa_23.get() == "System wprowadzania implantów ACL TightRope":
        entry_cena_23 = Entry(root, textvariable=cena_23, justify=CENTER, width=14)
        entry_cena_23.insert(0, "702")
        entry_cena_23.grid(row=13, column=6)
    elif nazwa_23.get() == "Szew FiberWire 2":
        entry_cena_23 = Entry(root, textvariable=cena_23, justify=CENTER, width=14)
        entry_cena_23.insert(0, "86.40")
        entry_cena_23.grid(row=13, column=6)
    elif nazwa_23.get() == "Taśma przylepna 10x50":
        entry_cena_23 = Entry(root, textvariable=cena_23, justify=CENTER, width=14)
        entry_cena_23.insert(0, "1.04")
        entry_cena_23.grid(row=13, column=6)
    elif nazwa_23.get() == "Triathlon elem. udowy lewy":
        entry_cena_23 = Entry(root, textvariable=cena_23, justify=CENTER, width=14)
        entry_cena_23.insert(0, "3132")
        entry_cena_23.grid(row=13, column=6)
    elif nazwa_23.get() == "Triathlon PS wkładka x3-9mm #4":
        entry_cena_23 = Entry(root, textvariable=cena_23, justify=CENTER, width=14)
        entry_cena_23.insert(0, "756")
        entry_cena_23.grid(row=13, column=6)
    elif nazwa_23.get() == "Triathlon taca piszczelowa":
        entry_cena_23 = Entry(root, textvariable=cena_23, justify=CENTER, width=14)
        entry_cena_23.insert(0, "1296")
        entry_cena_23.grid(row=13, column=6)
    elif nazwa_23.get() == "Wkłady 3L z żelem":
        entry_cena_23 = Entry(root, textvariable=cena_23, justify=CENTER, width=14)
        entry_cena_23.insert(0, "10.26")
        entry_cena_23.grid(row=13, column=6)
    elif nazwa_23.get() == "Zestaw do artroskopii":
        entry_cena_23 = Entry(root, textvariable=cena_23, justify=CENTER, width=14)
        entry_cena_23.insert(0, "67")
        entry_cena_23.grid(row=13, column=6)
    elif nazwa_23.get() == "Zestaw do artroskopii barku":
        entry_cena_23 = Entry(root, textvariable=cena_23, justify=CENTER, width=14)
        entry_cena_23.insert(0, "108")
        entry_cena_23.grid(row=13, column=6)
    elif nazwa_23.get() == "Zestaw do drenażu":
        entry_cena_23 = Entry(root, textvariable=cena_23, justify=CENTER, width=14)
        entry_cena_23.insert(0, "14.23")
        entry_cena_23.grid(row=13, column=6)
    elif nazwa_23.get() == "Zestaw ortopedyczny":
        entry_cena_23 = Entry(root, textvariable=cena_23, justify=CENTER, width=14)
        entry_cena_23.insert(0, "28.08")
        entry_cena_23.grid(row=13, column=6)
    elif nazwa_23.get() == "Gaziki 20 x 10cm":
        entry_cena_23 = Entry(root, textvariable=cena_23, justify=CENTER, width=14)
        entry_cena_23.insert(0, "0.46")
        entry_cena_23.grid(row=13, column=6)
    else:
        entry_cena_23 = Entry(root, textvariable=cena_23, justify=CENTER, width=14, bg="#ffff00")
        entry_cena_23.insert(0, "0")
        entry_cena_23.grid(row=13, column=6)

    if nazwa_24.get() == "--puste--":
        entry_cena_24 = Entry(root, textvariable=cena_24, justify=CENTER, width=14)
        entry_cena_24.insert(0, "0")
        entry_cena_24.grid(row=14, column=6)
    elif nazwa_24.get() == "Ablator":
        entry_cena_24 = Entry(root, textvariable=cena_24, justify=CENTER, width=14)
        entry_cena_24.insert(0, "572")
        entry_cena_24.grid(row=14, column=6)
    elif nazwa_24.get() == "Anestezjolog":
        entry_cena_24 = Entry(root, textvariable=cena_24, justify=CENTER, width=14, bg="#ffff00")
        entry_cena_24.insert(0, "350")
        entry_cena_24.grid(row=14, column=6)
    elif nazwa_24.get() == "Butelka 400ml do długotrwałego odsysania ran j.u. sterylna":
        entry_cena_24 = Entry(root, textvariable=cena_24, justify=CENTER, width=14)
        entry_cena_24.insert(0, "4")
        entry_cena_24.grid(row=14, column=6)
    elif nazwa_24.get() == "Doba":
        entry_cena_24 = Entry(root, textvariable=cena_24, justify=CENTER, width=14)
        entry_cena_24.insert(0, "700")
        entry_cena_24.grid(row=14, column=6)
    elif nazwa_24.get() == "Dren łączący do ssaka Grena":
        entry_cena_24 = Entry(root, textvariable=cena_24, justify=CENTER, width=14)
        entry_cena_24.insert(0, "5")
        entry_cena_24.grid(row=14, column=6)
    elif nazwa_24.get() == "Dren Redona Ch 16 dł. 800mm z trokarem":
        entry_cena_24 = Entry(root, textvariable=cena_24, justify=CENTER, width=14)
        entry_cena_24.insert(0, "29.74")
        entry_cena_24.grid(row=14, column=6)
    elif nazwa_24.get() == "Dren do pompy Artrex":
        entry_cena_24 = Entry(root, textvariable=cena_24, justify=CENTER, width=14)
        entry_cena_24.insert(0, "108")
        entry_cena_24.grid(row=14, column=6)
    elif nazwa_24.get() == "Drut wiercący 2,4 x 311":
        entry_cena_24 = Entry(root, textvariable=cena_24, justify=CENTER, width=14)
        entry_cena_24.insert(0, "139.60")
        entry_cena_24.grid(row=14, column=6)
    elif nazwa_24.get() == "Fartuch jałowy L":
        entry_cena_24 = Entry(root, textvariable=cena_24, justify=CENTER, width=14)
        entry_cena_24.insert(0, "17")
        entry_cena_24.grid(row=14, column=6)
    elif nazwa_24.get() == "Fartuch jałowy M":
        entry_cena_24 = Entry(root, textvariable=cena_24, justify=CENTER, width=14)
        entry_cena_24.insert(0, "15.28")
        entry_cena_24.grid(row=14, column=6)
    elif nazwa_24.get() == "Fartuch jałowy XL":
        entry_cena_24 = Entry(root, textvariable=cena_24, justify=CENTER, width=14)
        entry_cena_24.insert(0, "20.84")
        entry_cena_24.grid(row=14, column=6)
    elif nazwa_24.get() == "FasatThread BioComposite Interference Screw 8x30":
        entry_cena_24 = Entry(root, textvariable=cena_24, justify=CENTER, width=14)
        entry_cena_24.insert(0, "594")
        entry_cena_24.grid(row=14, column=6)
    elif nazwa_24.get() == "Folia operacyjna, jałowa 45cm x 55cm":
        entry_cena_24 = Entry(root, textvariable=cena_24, justify=CENTER, width=14)
        entry_cena_24.insert(0, "9.99")
        entry_cena_24.grid(row=14, column=6)
    elif nazwa_24.get() == "Gaziki 10 x 10cm":
        entry_cena_24 = Entry(root, textvariable=cena_24, justify=CENTER, width=14)
        entry_cena_24.insert(0, "0.10")
        entry_cena_24.grid(row=14, column=6)
    elif nazwa_24.get() == "Igła 0,6 x 60":
        entry_cena_24 = Entry(root, textvariable=cena_24, justify=CENTER, width=14)
        entry_cena_24.insert(0, "0.09")
        entry_cena_24.grid(row=14, column=6)
    elif nazwa_24.get() == "Igła 0,7 x 40":
        entry_cena_24 = Entry(root, textvariable=cena_24, justify=CENTER, width=14)
        entry_cena_24.insert(0, "0.05")
        entry_cena_24.grid(row=14, column=6)
    elif nazwa_24.get() == "Igła 0,8 x 40":
        entry_cena_24 = Entry(root, textvariable=cena_24, justify=CENTER, width=14)
        entry_cena_24.insert(0, "0.05")
        entry_cena_24.grid(row=14, column=6)
    elif nazwa_24.get() == "Igła 1,1 x 70":
        entry_cena_24 = Entry(root, textvariable=cena_24, justify=CENTER, width=14)
        entry_cena_24.insert(0, "0.16")
        entry_cena_24.grid(row=14, column=6)
    elif nazwa_24.get() == "Kaniulowana śruba int. biokompozytowa z osłonką jednoraz.":
        entry_cena_24 = Entry(root, textvariable=cena_24, justify=CENTER, width=14)
        entry_cena_24.insert(0, "594")
        entry_cena_24.grid(row=14, column=6)
    elif nazwa_24.get() == "Kaniulowana śruba int. biokompozytowa z pełnym gwintem":
        entry_cena_24 = Entry(root, textvariable=cena_24, justify=CENTER, width=14)
        entry_cena_24.insert(0, "594")
        entry_cena_24.grid(row=14, column=6)
    elif nazwa_24.get() == "Końcówka do Shavera":
        entry_cena_24 = Entry(root, textvariable=cena_24, justify=CENTER, width=14)
        entry_cena_24.insert(0, "270")
        entry_cena_24.grid(row=14, column=6)
    elif nazwa_24.get() == "Kotwica biokompozytowa SwiveLock":
        entry_cena_24 = Entry(root, textvariable=cena_24, justify=CENTER, width=14)
        entry_cena_24.insert(0, "918")
        entry_cena_24.grid(row=14, column=6)
    elif nazwa_24.get() == "Kotwica Corkscrew":
        entry_cena_24 = Entry(root, textvariable=cena_24, justify=CENTER, width=14)
        entry_cena_24.insert(0, "604")
        entry_cena_24.grid(row=14, column=6)
    elif nazwa_24.get() == "Kotwica FASTak":
        entry_cena_24 = Entry(root, textvariable=cena_24, justify=CENTER, width=14)
        entry_cena_24.insert(0, "432")
        entry_cena_24.grid(row=14, column=6)
    elif nazwa_24.get() == "Kotwica PEEK SwiveLock":
        entry_cena_24 = Entry(root, textvariable=cena_24, justify=CENTER, width=14)
        entry_cena_24.insert(0, "885.60")
        entry_cena_24.grid(row=14, column=6)
    elif nazwa_24.get() == "NaCl 3000ml":
        entry_cena_24 = Entry(root, textvariable=cena_24, justify=CENTER, width=14)
        entry_cena_24.insert(0, "29.72")
        entry_cena_24.grid(row=14, column=6)
    elif nazwa_24.get() == "NaCl 5000ml":
        entry_cena_24 = Entry(root, textvariable=cena_24, justify=CENTER, width=14)
        entry_cena_24.insert(0, "58.33")
        entry_cena_24.grid(row=14, column=6)
    elif nazwa_24.get() == "Nici Dafilon 2-0":
        entry_cena_24 = Entry(root, textvariable=cena_24, justify=CENTER, width=14)
        entry_cena_24.insert(0, "6.60")
        entry_cena_24.grid(row=14, column=6)
    elif nazwa_24.get() == "Nici Novosyn 2":
        entry_cena_24 = Entry(root, textvariable=cena_24, justify=CENTER, width=14)
        entry_cena_24.insert(0, "13")
        entry_cena_24.grid(row=14, column=6)
    elif nazwa_24.get() == "Nici Novosyn 2-0":
        entry_cena_24 = Entry(root, textvariable=cena_24, justify=CENTER, width=14)
        entry_cena_24.insert(0, "7.70")
        entry_cena_24.grid(row=14, column=6)
    elif nazwa_24.get() == "Nici Novosyn 3-0":
        entry_cena_24 = Entry(root, textvariable=cena_24, justify=CENTER, width=14)
        entry_cena_24.insert(0, "7.70")
        entry_cena_24.grid(row=14, column=6)
    elif nazwa_24.get() == "Nici Nylon 2-0":
        entry_cena_24 = Entry(root, textvariable=cena_24, justify=CENTER, width=14)
        entry_cena_24.insert(0, "2.50")
        entry_cena_24.grid(row=14, column=6)
    elif nazwa_24.get() == "Nici Nylon 3-0":
        entry_cena_24 = Entry(root, textvariable=cena_24, justify=CENTER, width=14)
        entry_cena_24.insert(0, "2")
        entry_cena_24.grid(row=14, column=6)
    elif nazwa_24.get() == "Nici PGLA":
        entry_cena_24 = Entry(root, textvariable=cena_24, justify=CENTER, width=14)
        entry_cena_24.insert(0, "11.60")
        entry_cena_24.grid(row=14, column=6)
    elif nazwa_24.get() == "Nici PremiCron 3":
        entry_cena_24 = Entry(root, textvariable=cena_24, justify=CENTER, width=14)
        entry_cena_24.insert(0, "6.50")
        entry_cena_24.grid(row=14, column=6)
    elif nazwa_24.get() == "Nici Vicryl 4-0":
        entry_cena_24 = Entry(root, textvariable=cena_24, justify=CENTER, width=14)
        entry_cena_24.insert(0, "7.50")
        entry_cena_24.grid(row=14, column=6)
    elif nazwa_24.get() == "Nitinol Guide Pin 1.1":
        entry_cena_24 = Entry(root, textvariable=cena_24, justify=CENTER, width=14)
        entry_cena_24.insert(0, "145.80")
        entry_cena_24.grid(row=14, column=6)
    elif nazwa_24.get() == "Osłona na przewody":
        entry_cena_24 = Entry(root, textvariable=cena_24, justify=CENTER, width=14)
        entry_cena_24.insert(0, "2.50")
        entry_cena_24.grid(row=14, column=6)
    elif nazwa_24.get() == "Ostrze Arthrex 90(86)x19x1,27":
        entry_cena_24 = Entry(root, textvariable=cena_24, justify=CENTER, width=14)
        entry_cena_24.insert(0, "216")
        entry_cena_24.grid(row=14, column=6)
    elif nazwa_24.get() == "Ostrze piły":
        entry_cena_24 = Entry(root, textvariable=cena_24, justify=CENTER, width=14)
        entry_cena_24.insert(0, "108")
        entry_cena_24.grid(row=14, column=6)
    elif nazwa_24.get() == "Pielęgniarka anest.":
        entry_cena_24 = Entry(root, textvariable=cena_24, justify=CENTER, width=14)
        entry_cena_24.insert(0, "50")
        entry_cena_24.grid(row=14, column=6)
    elif nazwa_24.get() == "Pielęgniarka instr.":
        entry_cena_24 = Entry(root, textvariable=cena_24, justify=CENTER, width=14)
        entry_cena_24.insert(0, "50")
        entry_cena_24.grid(row=14, column=6)
    elif nazwa_24.get() == "Pielęgniarka 'Noviline'":
        entry_cena_24 = Entry(root, textvariable=cena_24, justify=CENTER, width=14)
        entry_cena_24.insert(0, "30")
        entry_cena_24.grid(row=14, column=6)
    elif nazwa_24.get() == "Płytka PeekPower do osteotomii klinowej":
        entry_cena_24 = Entry(root, textvariable=cena_24, justify=CENTER, width=14)
        entry_cena_24.insert(0, "2160")
        entry_cena_24.grid(row=14, column=6)
    elif nazwa_24.get() == "Rękawice jałowe 6,5":
        entry_cena_24 = Entry(root, textvariable=cena_24, justify=CENTER, width=14)
        entry_cena_24.insert(0, "1.20")
        entry_cena_24.grid(row=14, column=6)
    elif nazwa_24.get() == "Rękawice jałowe 7,0":
        entry_cena_24 = Entry(root, textvariable=cena_24, justify=CENTER, width=14)
        entry_cena_24.insert(0, "1.20")
        entry_cena_24.grid(row=14, column=6)
    elif nazwa_24.get() == "Rękawice jałowe 7,5":
        entry_cena_24 = Entry(root, textvariable=cena_24, justify=CENTER, width=14)
        entry_cena_24.insert(0, "1.20")
        entry_cena_24.grid(row=14, column=6)
    elif nazwa_24.get() == "Rękawice jałowe 8,00":
        entry_cena_24 = Entry(root, textvariable=cena_24, justify=CENTER, width=14)
        entry_cena_24.insert(0, "1.20")
        entry_cena_24.grid(row=14, column=6)
    elif nazwa_24.get() == "Rękojeść Interpulse wysokoprzepływowa":
        entry_cena_24 = Entry(root, textvariable=cena_24, justify=CENTER, width=14)
        entry_cena_24.insert(0, "216")
        entry_cena_24.grid(row=14, column=6)
    elif nazwa_24.get() == "Serweta":
        entry_cena_24 = Entry(root, textvariable=cena_24, justify=CENTER, width=14)
        entry_cena_24.insert(0, "6")
        entry_cena_24.grid(row=14, column=6)
    elif nazwa_24.get() == "Simplex Hv z Gentamycyna 10x40g":
        entry_cena_24 = Entry(root, textvariable=cena_24, justify=CENTER, width=14)
        entry_cena_24.insert(0, "162")
        entry_cena_24.grid(row=14, column=6)
    elif nazwa_24.get() == "Skalpel 11":
        entry_cena_24 = Entry(root, textvariable=cena_24, justify=CENTER, width=14)
        entry_cena_24.insert(0, "0.38")
        entry_cena_24.grid(row=14, column=6)
    elif nazwa_24.get() == "Skalpel 13":
        entry_cena_24 = Entry(root, textvariable=cena_24, justify=CENTER, width=14)
        entry_cena_24.insert(0, "1")
        entry_cena_24.grid(row=14, column=6)
    elif nazwa_24.get() == "Skalpel 22":
        entry_cena_24 = Entry(root, textvariable=cena_24, justify=CENTER, width=14)
        entry_cena_24.insert(0, "00000")
        entry_cena_24.grid(row=14, column=6)
    elif nazwa_24.get() == "Śruba blokująca PeekPower do osteotomii":
        entry_cena_24 = Entry(root, textvariable=cena_24, justify=CENTER, width=14)
        entry_cena_24.insert(0, "194")
        entry_cena_24.grid(row=14, column=6)
    elif nazwa_24.get() == "System do mieszania próżniowego":
        entry_cena_24 = Entry(root, textvariable=cena_24, justify=CENTER, width=14)
        entry_cena_24.insert(0, "216")
        entry_cena_24.grid(row=14, column=6)
    elif nazwa_24.get() == "System wprowadzania implantów ACL TightRope":
        entry_cena_24 = Entry(root, textvariable=cena_24, justify=CENTER, width=14)
        entry_cena_24.insert(0, "702")
        entry_cena_24.grid(row=14, column=6)
    elif nazwa_24.get() == "Szew FiberWire 2":
        entry_cena_24 = Entry(root, textvariable=cena_24, justify=CENTER, width=14)
        entry_cena_24.insert(0, "86.40")
        entry_cena_24.grid(row=14, column=6)
    elif nazwa_24.get() == "Taśma przylepna 10x50":
        entry_cena_24 = Entry(root, textvariable=cena_24, justify=CENTER, width=14)
        entry_cena_24.insert(0, "1.04")
        entry_cena_24.grid(row=14, column=6)
    elif nazwa_24.get() == "Triathlon elem. udowy lewy":
        entry_cena_24 = Entry(root, textvariable=cena_24, justify=CENTER, width=14)
        entry_cena_24.insert(0, "3132")
        entry_cena_24.grid(row=14, column=6)
    elif nazwa_24.get() == "Triathlon PS wkładka x3-9mm #4":
        entry_cena_24 = Entry(root, textvariable=cena_24, justify=CENTER, width=14)
        entry_cena_24.insert(0, "756")
        entry_cena_24.grid(row=14, column=6)
    elif nazwa_24.get() == "Triathlon taca piszczelowa":
        entry_cena_24 = Entry(root, textvariable=cena_24, justify=CENTER, width=14)
        entry_cena_24.insert(0, "1296")
        entry_cena_24.grid(row=14, column=6)
    elif nazwa_24.get() == "Wkłady 3L z żelem":
        entry_cena_24 = Entry(root, textvariable=cena_24, justify=CENTER, width=14)
        entry_cena_24.insert(0, "10.26")
        entry_cena_24.grid(row=14, column=6)
    elif nazwa_24.get() == "Zestaw do artroskopii":
        entry_cena_24 = Entry(root, textvariable=cena_24, justify=CENTER, width=14)
        entry_cena_24.insert(0, "67")
        entry_cena_24.grid(row=14, column=6)
    elif nazwa_24.get() == "Zestaw do artroskopii barku":
        entry_cena_24 = Entry(root, textvariable=cena_24, justify=CENTER, width=14)
        entry_cena_24.insert(0, "108")
        entry_cena_24.grid(row=14, column=6)
    elif nazwa_24.get() == "Zestaw do drenażu":
        entry_cena_24 = Entry(root, textvariable=cena_24, justify=CENTER, width=14)
        entry_cena_24.insert(0, "14.23")
        entry_cena_24.grid(row=14, column=6)
    elif nazwa_24.get() == "Zestaw ortopedyczny":
        entry_cena_24 = Entry(root, textvariable=cena_24, justify=CENTER, width=14)
        entry_cena_24.insert(0, "28.08")
        entry_cena_24.grid(row=14, column=6)
    elif nazwa_24.get() == "Gaziki 20 x 10cm":
        entry_cena_24 = Entry(root, textvariable=cena_24, justify=CENTER, width=14)
        entry_cena_24.insert(0, "0.46")
        entry_cena_24.grid(row=14, column=6)
    else:
        entry_cena_24 = Entry(root, textvariable=cena_24, justify=CENTER, width=14, bg="#ffff00")
        entry_cena_24.insert(0, "0")
        entry_cena_24.grid(row=14, column=6)

    if nazwa_25.get() == "--puste--":
        entry_cena_25 = Entry(root, textvariable=cena_25, justify=CENTER, width=14)
        entry_cena_25.insert(0, "0")
        entry_cena_25.grid(row=15, column=6)
    elif nazwa_25.get() == "Ablator":
        entry_cena_25 = Entry(root, textvariable=cena_25, justify=CENTER, width=14)
        entry_cena_25.insert(0, "572")
        entry_cena_25.grid(row=15, column=6)
    elif nazwa_25.get() == "Anestezjolog":
        entry_cena_25 = Entry(root, textvariable=cena_25, justify=CENTER, width=14, bg="#ffff00")
        entry_cena_25.insert(0, "350")
        entry_cena_25.grid(row=15, column=6)
    elif nazwa_25.get() == "Butelka 400ml do długotrwałego odsysania ran j.u. sterylna":
        entry_cena_25 = Entry(root, textvariable=cena_25, justify=CENTER, width=14)
        entry_cena_25.insert(0, "4")
        entry_cena_25.grid(row=15, column=6)
    elif nazwa_25.get() == "Doba":
        entry_cena_25 = Entry(root, textvariable=cena_25, justify=CENTER, width=14)
        entry_cena_25.insert(0, "700")
        entry_cena_25.grid(row=15, column=6)
    elif nazwa_25.get() == "Dren łączący do ssaka Grena":
        entry_cena_25 = Entry(root, textvariable=cena_25, justify=CENTER, width=14)
        entry_cena_25.insert(0, "5")
        entry_cena_25.grid(row=15, column=6)
    elif nazwa_25.get() == "Dren Redona Ch 16 dł. 800mm z trokarem":
        entry_cena_25 = Entry(root, textvariable=cena_25, justify=CENTER, width=14)
        entry_cena_25.insert(0, "29.74")
        entry_cena_25.grid(row=15, column=6)
    elif nazwa_25.get() == "Dren do pompy Artrex":
        entry_cena_25 = Entry(root, textvariable=cena_25, justify=CENTER, width=14)
        entry_cena_25.insert(0, "108")
        entry_cena_25.grid(row=15, column=6)
    elif nazwa_25.get() == "Drut wiercący 2,4 x 311":
        entry_cena_25 = Entry(root, textvariable=cena_25, justify=CENTER, width=14)
        entry_cena_25.insert(0, "139.60")
        entry_cena_25.grid(row=15, column=6)
    elif nazwa_25.get() == "Fartuch jałowy L":
        entry_cena_25 = Entry(root, textvariable=cena_25, justify=CENTER, width=14)
        entry_cena_25.insert(0, "17")
        entry_cena_25.grid(row=15, column=6)
    elif nazwa_25.get() == "Fartuch jałowy M":
        entry_cena_25 = Entry(root, textvariable=cena_25, justify=CENTER, width=14)
        entry_cena_25.insert(0, "15.28")
        entry_cena_25.grid(row=15, column=6)
    elif nazwa_25.get() == "Fartuch jałowy XL":
        entry_cena_25 = Entry(root, textvariable=cena_25, justify=CENTER, width=14)
        entry_cena_25.insert(0, "20.84")
        entry_cena_25.grid(row=15, column=6)
    elif nazwa_25.get() == "FasatThread BioComposite Interference Screw 8x30":
        entry_cena_25 = Entry(root, textvariable=cena_25, justify=CENTER, width=14)
        entry_cena_25.insert(0, "594")
        entry_cena_25.grid(row=15, column=6)
    elif nazwa_25.get() == "Folia operacyjna, jałowa 45cm x 55cm":
        entry_cena_25 = Entry(root, textvariable=cena_25, justify=CENTER, width=14)
        entry_cena_25.insert(0, "9.99")
        entry_cena_25.grid(row=15, column=6)
    elif nazwa_25.get() == "Gaziki 10 x 10cm":
        entry_cena_25 = Entry(root, textvariable=cena_25, justify=CENTER, width=14)
        entry_cena_25.insert(0, "0.10")
        entry_cena_25.grid(row=15, column=6)
    elif nazwa_25.get() == "Igła 0,6 x 60":
        entry_cena_25 = Entry(root, textvariable=cena_25, justify=CENTER, width=14)
        entry_cena_25.insert(0, "0.09")
        entry_cena_25.grid(row=15, column=6)
    elif nazwa_25.get() == "Igła 0,7 x 40":
        entry_cena_25 = Entry(root, textvariable=cena_25, justify=CENTER, width=14)
        entry_cena_25.insert(0, "0.05")
        entry_cena_25.grid(row=15, column=6)
    elif nazwa_25.get() == "Igła 0,8 x 40":
        entry_cena_25 = Entry(root, textvariable=cena_25, justify=CENTER, width=14)
        entry_cena_25.insert(0, "0.05")
        entry_cena_25.grid(row=15, column=6)
    elif nazwa_25.get() == "Igła 1,1 x 70":
        entry_cena_25 = Entry(root, textvariable=cena_25, justify=CENTER, width=14)
        entry_cena_25.insert(0, "0.16")
        entry_cena_25.grid(row=15, column=6)
    elif nazwa_25.get() == "Kaniulowana śruba int. biokompozytowa z osłonką jednoraz.":
        entry_cena_25 = Entry(root, textvariable=cena_25, justify=CENTER, width=14)
        entry_cena_25.insert(0, "594")
        entry_cena_25.grid(row=15, column=6)
    elif nazwa_25.get() == "Kaniulowana śruba int. biokompozytowa z pełnym gwintem":
        entry_cena_25 = Entry(root, textvariable=cena_25, justify=CENTER, width=14)
        entry_cena_25.insert(0, "594")
        entry_cena_25.grid(row=15, column=6)
    elif nazwa_25.get() == "Końcówka do Shavera":
        entry_cena_25 = Entry(root, textvariable=cena_25, justify=CENTER, width=14)
        entry_cena_25.insert(0, "270")
        entry_cena_25.grid(row=15, column=6)
    elif nazwa_25.get() == "Kotwica biokompozytowa SwiveLock":
        entry_cena_25 = Entry(root, textvariable=cena_25, justify=CENTER, width=14)
        entry_cena_25.insert(0, "918")
        entry_cena_25.grid(row=15, column=6)
    elif nazwa_25.get() == "Kotwica Corkscrew":
        entry_cena_25 = Entry(root, textvariable=cena_25, justify=CENTER, width=14)
        entry_cena_25.insert(0, "604")
        entry_cena_25.grid(row=15, column=6)
    elif nazwa_25.get() == "Kotwica FASTak":
        entry_cena_25 = Entry(root, textvariable=cena_25, justify=CENTER, width=14)
        entry_cena_25.insert(0, "432")
        entry_cena_25.grid(row=15, column=6)
    elif nazwa_25.get() == "Kotwica PEEK SwiveLock":
        entry_cena_25 = Entry(root, textvariable=cena_25, justify=CENTER, width=14)
        entry_cena_25.insert(0, "885.60")
        entry_cena_25.grid(row=15, column=6)
    elif nazwa_25.get() == "NaCl 3000ml":
        entry_cena_25 = Entry(root, textvariable=cena_25, justify=CENTER, width=14)
        entry_cena_25.insert(0, "29.72")
        entry_cena_25.grid(row=15, column=6)
    elif nazwa_25.get() == "NaCl 5000ml":
        entry_cena_25 = Entry(root, textvariable=cena_25, justify=CENTER, width=14)
        entry_cena_25.insert(0, "58.33")
        entry_cena_25.grid(row=15, column=6)
    elif nazwa_25.get() == "Nici Dafilon 2-0":
        entry_cena_25 = Entry(root, textvariable=cena_25, justify=CENTER, width=14)
        entry_cena_25.insert(0, "6.60")
        entry_cena_25.grid(row=15, column=6)
    elif nazwa_25.get() == "Nici Novosyn 2":
        entry_cena_25 = Entry(root, textvariable=cena_25, justify=CENTER, width=14)
        entry_cena_25.insert(0, "13")
        entry_cena_25.grid(row=15, column=6)
    elif nazwa_25.get() == "Nici Novosyn 2-0":
        entry_cena_25 = Entry(root, textvariable=cena_25, justify=CENTER, width=14)
        entry_cena_25.insert(0, "7.70")
        entry_cena_25.grid(row=15, column=6)
    elif nazwa_25.get() == "Nici Novosyn 3-0":
        entry_cena_25 = Entry(root, textvariable=cena_25, justify=CENTER, width=14)
        entry_cena_25.insert(0, "7.70")
        entry_cena_25.grid(row=15, column=6)
    elif nazwa_25.get() == "Nici Nylon 2-0":
        entry_cena_25 = Entry(root, textvariable=cena_25, justify=CENTER, width=14)
        entry_cena_25.insert(0, "2.50")
        entry_cena_25.grid(row=15, column=6)
    elif nazwa_25.get() == "Nici Nylon 3-0":
        entry_cena_25 = Entry(root, textvariable=cena_25, justify=CENTER, width=14)
        entry_cena_25.insert(0, "2")
        entry_cena_25.grid(row=15, column=6)
    elif nazwa_25.get() == "Nici PGLA":
        entry_cena_25 = Entry(root, textvariable=cena_25, justify=CENTER, width=14)
        entry_cena_25.insert(0, "11.60")
        entry_cena_25.grid(row=15, column=6)
    elif nazwa_25.get() == "Nici PremiCron 3":
        entry_cena_25 = Entry(root, textvariable=cena_25, justify=CENTER, width=14)
        entry_cena_25.insert(0, "6.50")
        entry_cena_25.grid(row=15, column=6)
    elif nazwa_25.get() == "Nici Vicryl 4-0":
        entry_cena_25 = Entry(root, textvariable=cena_25, justify=CENTER, width=14)
        entry_cena_25.insert(0, "7.50")
        entry_cena_25.grid(row=15, column=6)
    elif nazwa_25.get() == "Nitinol Guide Pin 1.1":
        entry_cena_25 = Entry(root, textvariable=cena_25, justify=CENTER, width=14)
        entry_cena_25.insert(0, "145.80")
        entry_cena_25.grid(row=15, column=6)
    elif nazwa_25.get() == "Osłona na przewody":
        entry_cena_25 = Entry(root, textvariable=cena_25, justify=CENTER, width=14)
        entry_cena_25.insert(0, "2.50")
        entry_cena_25.grid(row=15, column=6)
    elif nazwa_25.get() == "Ostrze Arthrex 90(86)x19x1,27":
        entry_cena_25 = Entry(root, textvariable=cena_25, justify=CENTER, width=14)
        entry_cena_25.insert(0, "216")
        entry_cena_25.grid(row=15, column=6)
    elif nazwa_25.get() == "Ostrze piły":
        entry_cena_25 = Entry(root, textvariable=cena_25, justify=CENTER, width=14)
        entry_cena_25.insert(0, "108")
        entry_cena_25.grid(row=15, column=6)
    elif nazwa_25.get() == "Pielęgniarka anest.":
        entry_cena_25 = Entry(root, textvariable=cena_25, justify=CENTER, width=14)
        entry_cena_25.insert(0, "50")
        entry_cena_25.grid(row=15, column=6)
    elif nazwa_25.get() == "Pielęgniarka instr.":
        entry_cena_25 = Entry(root, textvariable=cena_25, justify=CENTER, width=14)
        entry_cena_25.insert(0, "50")
        entry_cena_25.grid(row=15, column=6)
    elif nazwa_25.get() == "Pielęgniarka 'Noviline'":
        entry_cena_25 = Entry(root, textvariable=cena_25, justify=CENTER, width=14)
        entry_cena_25.insert(0, "30")
        entry_cena_25.grid(row=15, column=6)
    elif nazwa_25.get() == "Płytka PeekPower do osteotomii klinowej":
        entry_cena_25 = Entry(root, textvariable=cena_25, justify=CENTER, width=14)
        entry_cena_25.insert(0, "2160")
        entry_cena_25.grid(row=15, column=6)
    elif nazwa_25.get() == "Rękawice jałowe 6,5":
        entry_cena_25 = Entry(root, textvariable=cena_25, justify=CENTER, width=14)
        entry_cena_25.insert(0, "1.20")
        entry_cena_25.grid(row=15, column=6)
    elif nazwa_25.get() == "Rękawice jałowe 7,0":
        entry_cena_25 = Entry(root, textvariable=cena_25, justify=CENTER, width=14)
        entry_cena_25.insert(0, "1.20")
        entry_cena_25.grid(row=15, column=6)
    elif nazwa_25.get() == "Rękawice jałowe 7,5":
        entry_cena_25 = Entry(root, textvariable=cena_25, justify=CENTER, width=14)
        entry_cena_25.insert(0, "1.20")
        entry_cena_25.grid(row=15, column=6)
    elif nazwa_25.get() == "Rękawice jałowe 8,00":
        entry_cena_25 = Entry(root, textvariable=cena_25, justify=CENTER, width=14)
        entry_cena_25.insert(0, "1.20")
        entry_cena_25.grid(row=15, column=6)
    elif nazwa_25.get() == "Rękojeść Interpulse wysokoprzepływowa":
        entry_cena_25 = Entry(root, textvariable=cena_25, justify=CENTER, width=14)
        entry_cena_25.insert(0, "216")
        entry_cena_25.grid(row=15, column=6)
    elif nazwa_25.get() == "Serweta":
        entry_cena_25 = Entry(root, textvariable=cena_25, justify=CENTER, width=14)
        entry_cena_25.insert(0, "6")
        entry_cena_25.grid(row=15, column=6)
    elif nazwa_25.get() == "Simplex Hv z Gentamycyna 10x40g":
        entry_cena_25 = Entry(root, textvariable=cena_25, justify=CENTER, width=14)
        entry_cena_25.insert(0, "162")
        entry_cena_25.grid(row=15, column=6)
    elif nazwa_25.get() == "Skalpel 11":
        entry_cena_25 = Entry(root, textvariable=cena_25, justify=CENTER, width=14)
        entry_cena_25.insert(0, "0.38")
        entry_cena_25.grid(row=15, column=6)
    elif nazwa_25.get() == "Skalpel 13":
        entry_cena_25 = Entry(root, textvariable=cena_25, justify=CENTER, width=14)
        entry_cena_25.insert(0, "1")
        entry_cena_25.grid(row=15, column=6)
    elif nazwa_25.get() == "Skalpel 22":
        entry_cena_25 = Entry(root, textvariable=cena_25, justify=CENTER, width=14)
        entry_cena_25.insert(0, "00000")
        entry_cena_25.grid(row=15, column=6)
    elif nazwa_25.get() == "Śruba blokująca PeekPower do osteotomii":
        entry_cena_25 = Entry(root, textvariable=cena_25, justify=CENTER, width=14)
        entry_cena_25.insert(0, "194")
        entry_cena_25.grid(row=15, column=6)
    elif nazwa_25.get() == "System do mieszania próżniowego":
        entry_cena_25 = Entry(root, textvariable=cena_25, justify=CENTER, width=14)
        entry_cena_25.insert(0, "216")
        entry_cena_25.grid(row=15, column=6)
    elif nazwa_25.get() == "System wprowadzania implantów ACL TightRope":
        entry_cena_25 = Entry(root, textvariable=cena_25, justify=CENTER, width=14)
        entry_cena_25.insert(0, "702")
        entry_cena_25.grid(row=15, column=6)
    elif nazwa_25.get() == "Szew FiberWire 2":
        entry_cena_25 = Entry(root, textvariable=cena_25, justify=CENTER, width=14)
        entry_cena_25.insert(0, "86.40")
        entry_cena_25.grid(row=15, column=6)
    elif nazwa_25.get() == "Taśma przylepna 10x50":
        entry_cena_25 = Entry(root, textvariable=cena_25, justify=CENTER, width=14)
        entry_cena_25.insert(0, "1.04")
        entry_cena_25.grid(row=15, column=6)
    elif nazwa_25.get() == "Triathlon elem. udowy lewy":
        entry_cena_25 = Entry(root, textvariable=cena_25, justify=CENTER, width=14)
        entry_cena_25.insert(0, "3132")
        entry_cena_25.grid(row=15, column=6)
    elif nazwa_25.get() == "Triathlon PS wkładka x3-9mm #4":
        entry_cena_25 = Entry(root, textvariable=cena_25, justify=CENTER, width=14)
        entry_cena_25.insert(0, "756")
        entry_cena_25.grid(row=15, column=6)
    elif nazwa_25.get() == "Triathlon taca piszczelowa":
        entry_cena_25 = Entry(root, textvariable=cena_25, justify=CENTER, width=14)
        entry_cena_25.insert(0, "1296")
        entry_cena_25.grid(row=15, column=6)
    elif nazwa_25.get() == "Wkłady 3L z żelem":
        entry_cena_25 = Entry(root, textvariable=cena_25, justify=CENTER, width=14)
        entry_cena_25.insert(0, "10.26")
        entry_cena_25.grid(row=15, column=6)
    elif nazwa_25.get() == "Zestaw do artroskopii":
        entry_cena_25 = Entry(root, textvariable=cena_25, justify=CENTER, width=14)
        entry_cena_25.insert(0, "67")
        entry_cena_25.grid(row=15, column=6)
    elif nazwa_25.get() == "Zestaw do artroskopii barku":
        entry_cena_25 = Entry(root, textvariable=cena_25, justify=CENTER, width=14)
        entry_cena_25.insert(0, "108")
        entry_cena_25.grid(row=15, column=6)
    elif nazwa_25.get() == "Zestaw do drenażu":
        entry_cena_25 = Entry(root, textvariable=cena_25, justify=CENTER, width=14)
        entry_cena_25.insert(0, "14.23")
        entry_cena_25.grid(row=15, column=6)
    elif nazwa_25.get() == "Zestaw ortopedyczny":
        entry_cena_25 = Entry(root, textvariable=cena_25, justify=CENTER, width=14)
        entry_cena_25.insert(0, "28.08")
        entry_cena_25.grid(row=15, column=6)
    elif nazwa_25.get() == "Gaziki 20 x 10cm":
        entry_cena_25 = Entry(root, textvariable=cena_25, justify=CENTER, width=14)
        entry_cena_25.insert(0, "0.46")
        entry_cena_25.grid(row=15, column=6)
    else:
        entry_cena_25 = Entry(root, textvariable=cena_25, justify=CENTER, width=14, bg="#ffff00")
        entry_cena_25.insert(0, "0")
        entry_cena_25.grid(row=15, column=6)

    if nazwa_26.get() == "--puste--":
        entry_cena_26 = Entry(root, textvariable=cena_26, justify=CENTER, width=14)
        entry_cena_26.insert(0, "0")
        entry_cena_26.grid(row=16, column=6)
    elif nazwa_26.get() == "Ablator":
        entry_cena_26 = Entry(root, textvariable=cena_26, justify=CENTER, width=14)
        entry_cena_26.insert(0, "572")
        entry_cena_26.grid(row=16, column=6)
    elif nazwa_26.get() == "Anestezjolog":
        entry_cena_26 = Entry(root, textvariable=cena_26, justify=CENTER, width=14, bg="#ffff00")
        entry_cena_26.insert(0, "350")
        entry_cena_26.grid(row=16, column=6)
    elif nazwa_26.get() == "Butelka 400ml do długotrwałego odsysania ran j.u. sterylna":
        entry_cena_26 = Entry(root, textvariable=cena_26, justify=CENTER, width=14)
        entry_cena_26.insert(0, "4")
        entry_cena_26.grid(row=16, column=6)
    elif nazwa_26.get() == "Doba":
        entry_cena_26 = Entry(root, textvariable=cena_26, justify=CENTER, width=14)
        entry_cena_26.insert(0, "700")
        entry_cena_26.grid(row=16, column=6)
    elif nazwa_26.get() == "Dren łączący do ssaka Grena":
        entry_cena_26 = Entry(root, textvariable=cena_26, justify=CENTER, width=14)
        entry_cena_26.insert(0, "5")
        entry_cena_26.grid(row=16, column=6)
    elif nazwa_26.get() == "Dren Redona Ch 16 dł. 800mm z trokarem":
        entry_cena_26 = Entry(root, textvariable=cena_26, justify=CENTER, width=14)
        entry_cena_26.insert(0, "29.74")
        entry_cena_26.grid(row=16, column=6)
    elif nazwa_26.get() == "Dren do pompy Artrex":
        entry_cena_26 = Entry(root, textvariable=cena_26, justify=CENTER, width=14)
        entry_cena_26.insert(0, "108")
        entry_cena_26.grid(row=16, column=6)
    elif nazwa_26.get() == "Drut wiercący 2,4 x 311":
        entry_cena_26 = Entry(root, textvariable=cena_26, justify=CENTER, width=14)
        entry_cena_26.insert(0, "139.60")
        entry_cena_26.grid(row=16, column=6)
    elif nazwa_26.get() == "Fartuch jałowy L":
        entry_cena_26 = Entry(root, textvariable=cena_26, justify=CENTER, width=14)
        entry_cena_26.insert(0, "17")
        entry_cena_26.grid(row=16, column=6)
    elif nazwa_26.get() == "Fartuch jałowy M":
        entry_cena_26 = Entry(root, textvariable=cena_26, justify=CENTER, width=14)
        entry_cena_26.insert(0, "15.28")
        entry_cena_26.grid(row=16, column=6)
    elif nazwa_26.get() == "Fartuch jałowy XL":
        entry_cena_26 = Entry(root, textvariable=cena_26, justify=CENTER, width=14)
        entry_cena_26.insert(0, "20.84")
        entry_cena_26.grid(row=16, column=6)
    elif nazwa_26.get() == "FasatThread BioComposite Interference Screw 8x30":
        entry_cena_26 = Entry(root, textvariable=cena_26, justify=CENTER, width=14)
        entry_cena_26.insert(0, "594")
        entry_cena_26.grid(row=16, column=6)
    elif nazwa_26.get() == "Folia operacyjna, jałowa 45cm x 55cm":
        entry_cena_26 = Entry(root, textvariable=cena_26, justify=CENTER, width=14)
        entry_cena_26.insert(0, "9.99")
        entry_cena_26.grid(row=16, column=6)
    elif nazwa_26.get() == "Gaziki 10 x 10cm":
        entry_cena_26 = Entry(root, textvariable=cena_26, justify=CENTER, width=14)
        entry_cena_26.insert(0, "0.10")
        entry_cena_26.grid(row=16, column=6)
    elif nazwa_26.get() == "Igła 0,6 x 60":
        entry_cena_26 = Entry(root, textvariable=cena_26, justify=CENTER, width=14)
        entry_cena_26.insert(0, "0.09")
        entry_cena_26.grid(row=16, column=6)
    elif nazwa_26.get() == "Igła 0,7 x 40":
        entry_cena_26 = Entry(root, textvariable=cena_26, justify=CENTER, width=14)
        entry_cena_26.insert(0, "0.05")
        entry_cena_26.grid(row=16, column=6)
    elif nazwa_26.get() == "Igła 0,8 x 40":
        entry_cena_26 = Entry(root, textvariable=cena_26, justify=CENTER, width=14)
        entry_cena_26.insert(0, "0.05")
        entry_cena_26.grid(row=16, column=6)
    elif nazwa_26.get() == "Igła 1,1 x 70":
        entry_cena_26 = Entry(root, textvariable=cena_26, justify=CENTER, width=14)
        entry_cena_26.insert(0, "0.16")
        entry_cena_26.grid(row=16, column=6)
    elif nazwa_26.get() == "Kaniulowana śruba int. biokompozytowa z osłonką jednoraz.":
        entry_cena_26 = Entry(root, textvariable=cena_26, justify=CENTER, width=14)
        entry_cena_26.insert(0, "594")
        entry_cena_26.grid(row=16, column=6)
    elif nazwa_26.get() == "Kaniulowana śruba int. biokompozytowa z pełnym gwintem":
        entry_cena_26 = Entry(root, textvariable=cena_26, justify=CENTER, width=14)
        entry_cena_26.insert(0, "594")
        entry_cena_26.grid(row=16, column=6)
    elif nazwa_26.get() == "Końcówka do Shavera":
        entry_cena_26 = Entry(root, textvariable=cena_26, justify=CENTER, width=14)
        entry_cena_26.insert(0, "270")
        entry_cena_26.grid(row=16, column=6)
    elif nazwa_26.get() == "Kotwica biokompozytowa SwiveLock":
        entry_cena_26 = Entry(root, textvariable=cena_26, justify=CENTER, width=14)
        entry_cena_26.insert(0, "918")
        entry_cena_26.grid(row=16, column=6)
    elif nazwa_26.get() == "Kotwica Corkscrew":
        entry_cena_26 = Entry(root, textvariable=cena_26, justify=CENTER, width=14)
        entry_cena_26.insert(0, "604")
        entry_cena_26.grid(row=16, column=6)
    elif nazwa_26.get() == "Kotwica FASTak":
        entry_cena_26 = Entry(root, textvariable=cena_26, justify=CENTER, width=14)
        entry_cena_26.insert(0, "432")
        entry_cena_26.grid(row=16, column=6)
    elif nazwa_26.get() == "Kotwica PEEK SwiveLock":
        entry_cena_26 = Entry(root, textvariable=cena_26, justify=CENTER, width=14)
        entry_cena_26.insert(0, "885.60")
        entry_cena_26.grid(row=16, column=6)
    elif nazwa_26.get() == "NaCl 3000ml":
        entry_cena_26 = Entry(root, textvariable=cena_26, justify=CENTER, width=14)
        entry_cena_26.insert(0, "29.72")
        entry_cena_26.grid(row=16, column=6)
    elif nazwa_26.get() == "NaCl 5000ml":
        entry_cena_26 = Entry(root, textvariable=cena_26, justify=CENTER, width=14)
        entry_cena_26.insert(0, "58.33")
        entry_cena_26.grid(row=16, column=6)
    elif nazwa_26.get() == "Nici Dafilon 2-0":
        entry_cena_26 = Entry(root, textvariable=cena_26, justify=CENTER, width=14)
        entry_cena_26.insert(0, "6.60")
        entry_cena_26.grid(row=16, column=6)
    elif nazwa_26.get() == "Nici Novosyn 2":
        entry_cena_26 = Entry(root, textvariable=cena_26, justify=CENTER, width=14)
        entry_cena_26.insert(0, "13")
        entry_cena_26.grid(row=16, column=6)
    elif nazwa_26.get() == "Nici Novosyn 2-0":
        entry_cena_26 = Entry(root, textvariable=cena_26, justify=CENTER, width=14)
        entry_cena_26.insert(0, "7.70")
        entry_cena_26.grid(row=16, column=6)
    elif nazwa_26.get() == "Nici Novosyn 3-0":
        entry_cena_26 = Entry(root, textvariable=cena_26, justify=CENTER, width=14)
        entry_cena_26.insert(0, "7.70")
        entry_cena_26.grid(row=16, column=6)
    elif nazwa_26.get() == "Nici Nylon 2-0":
        entry_cena_26 = Entry(root, textvariable=cena_26, justify=CENTER, width=14)
        entry_cena_26.insert(0, "2.50")
        entry_cena_26.grid(row=16, column=6)
    elif nazwa_26.get() == "Nici Nylon 3-0":
        entry_cena_26 = Entry(root, textvariable=cena_26, justify=CENTER, width=14)
        entry_cena_26.insert(0, "2")
        entry_cena_26.grid(row=16, column=6)
    elif nazwa_26.get() == "Nici PGLA":
        entry_cena_26 = Entry(root, textvariable=cena_26, justify=CENTER, width=14)
        entry_cena_26.insert(0, "11.60")
        entry_cena_26.grid(row=16, column=6)
    elif nazwa_26.get() == "Nici PremiCron 3":
        entry_cena_26 = Entry(root, textvariable=cena_26, justify=CENTER, width=14)
        entry_cena_26.insert(0, "6.50")
        entry_cena_26.grid(row=16, column=6)
    elif nazwa_26.get() == "Nici Vicryl 4-0":
        entry_cena_26 = Entry(root, textvariable=cena_26, justify=CENTER, width=14)
        entry_cena_26.insert(0, "7.50")
        entry_cena_26.grid(row=16, column=6)
    elif nazwa_26.get() == "Nitinol Guide Pin 1.1":
        entry_cena_26 = Entry(root, textvariable=cena_26, justify=CENTER, width=14)
        entry_cena_26.insert(0, "145.80")
        entry_cena_26.grid(row=16, column=6)
    elif nazwa_26.get() == "Osłona na przewody":
        entry_cena_26 = Entry(root, textvariable=cena_26, justify=CENTER, width=14)
        entry_cena_26.insert(0, "2.50")
        entry_cena_26.grid(row=16, column=6)
    elif nazwa_26.get() == "Ostrze Arthrex 90(86)x19x1,27":
        entry_cena_26 = Entry(root, textvariable=cena_26, justify=CENTER, width=14)
        entry_cena_26.insert(0, "216")
        entry_cena_26.grid(row=16, column=6)
    elif nazwa_26.get() == "Ostrze piły":
        entry_cena_26 = Entry(root, textvariable=cena_26, justify=CENTER, width=14)
        entry_cena_26.insert(0, "108")
        entry_cena_26.grid(row=16, column=6)
    elif nazwa_26.get() == "Pielęgniarka anest.":
        entry_cena_26 = Entry(root, textvariable=cena_26, justify=CENTER, width=14)
        entry_cena_26.insert(0, "50")
        entry_cena_26.grid(row=16, column=6)
    elif nazwa_26.get() == "Pielęgniarka instr.":
        entry_cena_26 = Entry(root, textvariable=cena_26, justify=CENTER, width=14)
        entry_cena_26.insert(0, "50")
        entry_cena_26.grid(row=16, column=6)
    elif nazwa_26.get() == "Pielęgniarka 'Noviline'":
        entry_cena_26 = Entry(root, textvariable=cena_26, justify=CENTER, width=14)
        entry_cena_26.insert(0, "30")
        entry_cena_26.grid(row=16, column=6)
    elif nazwa_26.get() == "Płytka PeekPower do osteotomii klinowej":
        entry_cena_26 = Entry(root, textvariable=cena_26, justify=CENTER, width=14)
        entry_cena_26.insert(0, "2160")
        entry_cena_26.grid(row=16, column=6)
    elif nazwa_26.get() == "Rękawice jałowe 6,5":
        entry_cena_26 = Entry(root, textvariable=cena_26, justify=CENTER, width=14)
        entry_cena_26.insert(0, "1.20")
        entry_cena_26.grid(row=16, column=6)
    elif nazwa_26.get() == "Rękawice jałowe 7,0":
        entry_cena_26 = Entry(root, textvariable=cena_26, justify=CENTER, width=14)
        entry_cena_26.insert(0, "1.20")
        entry_cena_26.grid(row=16, column=6)
    elif nazwa_26.get() == "Rękawice jałowe 7,5":
        entry_cena_26 = Entry(root, textvariable=cena_26, justify=CENTER, width=14)
        entry_cena_26.insert(0, "1.20")
        entry_cena_26.grid(row=16, column=6)
    elif nazwa_26.get() == "Rękawice jałowe 8,00":
        entry_cena_26 = Entry(root, textvariable=cena_26, justify=CENTER, width=14)
        entry_cena_26.insert(0, "1.20")
        entry_cena_26.grid(row=16, column=6)
    elif nazwa_26.get() == "Rękojeść Interpulse wysokoprzepływowa":
        entry_cena_26 = Entry(root, textvariable=cena_26, justify=CENTER, width=14)
        entry_cena_26.insert(0, "216")
        entry_cena_26.grid(row=16, column=6)
    elif nazwa_26.get() == "Serweta":
        entry_cena_26 = Entry(root, textvariable=cena_26, justify=CENTER, width=14)
        entry_cena_26.insert(0, "6")
        entry_cena_26.grid(row=16, column=6)
    elif nazwa_26.get() == "Simplex Hv z Gentamycyna 10x40g":
        entry_cena_26 = Entry(root, textvariable=cena_26, justify=CENTER, width=14)
        entry_cena_26.insert(0, "162")
        entry_cena_26.grid(row=16, column=6)
    elif nazwa_26.get() == "Skalpel 11":
        entry_cena_26 = Entry(root, textvariable=cena_26, justify=CENTER, width=14)
        entry_cena_26.insert(0, "0.38")
        entry_cena_26.grid(row=16, column=6)
    elif nazwa_26.get() == "Skalpel 13":
        entry_cena_26 = Entry(root, textvariable=cena_26, justify=CENTER, width=14)
        entry_cena_26.insert(0, "1")
        entry_cena_26.grid(row=16, column=6)
    elif nazwa_26.get() == "Skalpel 22":
        entry_cena_26 = Entry(root, textvariable=cena_26, justify=CENTER, width=14)
        entry_cena_26.insert(0, "00000")
        entry_cena_26.grid(row=16, column=6)
    elif nazwa_26.get() == "Śruba blokująca PeekPower do osteotomii":
        entry_cena_26 = Entry(root, textvariable=cena_26, justify=CENTER, width=14)
        entry_cena_26.insert(0, "194")
        entry_cena_26.grid(row=16, column=6)
    elif nazwa_26.get() == "System do mieszania próżniowego":
        entry_cena_26 = Entry(root, textvariable=cena_26, justify=CENTER, width=14)
        entry_cena_26.insert(0, "216")
        entry_cena_26.grid(row=16, column=6)
    elif nazwa_26.get() == "System wprowadzania implantów ACL TightRope":
        entry_cena_26 = Entry(root, textvariable=cena_26, justify=CENTER, width=14)
        entry_cena_26.insert(0, "702")
        entry_cena_26.grid(row=16, column=6)
    elif nazwa_26.get() == "Szew FiberWire 2":
        entry_cena_26 = Entry(root, textvariable=cena_26, justify=CENTER, width=14)
        entry_cena_26.insert(0, "86.40")
        entry_cena_26.grid(row=16, column=6)
    elif nazwa_26.get() == "Taśma przylepna 10x50":
        entry_cena_26 = Entry(root, textvariable=cena_26, justify=CENTER, width=14)
        entry_cena_26.insert(0, "1.04")
        entry_cena_26.grid(row=16, column=6)
    elif nazwa_26.get() == "Triathlon elem. udowy lewy":
        entry_cena_26 = Entry(root, textvariable=cena_26, justify=CENTER, width=14)
        entry_cena_26.insert(0, "3132")
        entry_cena_26.grid(row=16, column=6)
    elif nazwa_26.get() == "Triathlon PS wkładka x3-9mm #4":
        entry_cena_26 = Entry(root, textvariable=cena_26, justify=CENTER, width=14)
        entry_cena_26.insert(0, "756")
        entry_cena_26.grid(row=16, column=6)
    elif nazwa_26.get() == "Triathlon taca piszczelowa":
        entry_cena_26 = Entry(root, textvariable=cena_26, justify=CENTER, width=14)
        entry_cena_26.insert(0, "1296")
        entry_cena_26.grid(row=16, column=6)
    elif nazwa_26.get() == "Wkłady 3L z żelem":
        entry_cena_26 = Entry(root, textvariable=cena_26, justify=CENTER, width=14)
        entry_cena_26.insert(0, "10.26")
        entry_cena_26.grid(row=16, column=6)
    elif nazwa_26.get() == "Zestaw do artroskopii":
        entry_cena_26 = Entry(root, textvariable=cena_26, justify=CENTER, width=14)
        entry_cena_26.insert(0, "67")
        entry_cena_26.grid(row=16, column=6)
    elif nazwa_26.get() == "Zestaw do artroskopii barku":
        entry_cena_26 = Entry(root, textvariable=cena_26, justify=CENTER, width=14)
        entry_cena_26.insert(0, "108")
        entry_cena_26.grid(row=16, column=6)
    elif nazwa_26.get() == "Zestaw do drenażu":
        entry_cena_26 = Entry(root, textvariable=cena_26, justify=CENTER, width=14)
        entry_cena_26.insert(0, "14.23")
        entry_cena_26.grid(row=16, column=6)
    elif nazwa_26.get() == "Zestaw ortopedyczny":
        entry_cena_26 = Entry(root, textvariable=cena_26, justify=CENTER, width=14)
        entry_cena_26.insert(0, "28.08")
        entry_cena_26.grid(row=16, column=6)
    elif nazwa_26.get() == "Gaziki 20 x 10cm":
        entry_cena_26 = Entry(root, textvariable=cena_26, justify=CENTER, width=14)
        entry_cena_26.insert(0, "0.46")
        entry_cena_26.grid(row=16, column=6)
    else:
        entry_cena_26 = Entry(root, textvariable=cena_26, justify=CENTER, width=14, bg="#ffff00")
        entry_cena_26.insert(0, "0")
        entry_cena_26.grid(row=16, column=6)

    if nazwa_27.get() == "--puste--":
        entry_cena_27 = Entry(root, textvariable=cena_27, justify=CENTER, width=14)
        entry_cena_27.insert(0, "0")
        entry_cena_27.grid(row=17, column=6)
    elif nazwa_27.get() == "Ablator":
        entry_cena_27 = Entry(root, textvariable=cena_27, justify=CENTER, width=14)
        entry_cena_27.insert(0, "572")
        entry_cena_27.grid(row=17, column=6)
    elif nazwa_27.get() == "Anestezjolog":
        entry_cena_27 = Entry(root, textvariable=cena_27, justify=CENTER, width=14, bg="#ffff00")
        entry_cena_27.insert(0, "350")
        entry_cena_27.grid(row=17, column=6)
    elif nazwa_27.get() == "Butelka 400ml do długotrwałego odsysania ran j.u. sterylna":
        entry_cena_27 = Entry(root, textvariable=cena_27, justify=CENTER, width=14)
        entry_cena_27.insert(0, "4")
        entry_cena_27.grid(row=17, column=6)
    elif nazwa_27.get() == "Doba":
        entry_cena_27 = Entry(root, textvariable=cena_27, justify=CENTER, width=14)
        entry_cena_27.insert(0, "700")
        entry_cena_27.grid(row=17, column=6)
    elif nazwa_27.get() == "Dren łączący do ssaka Grena":
        entry_cena_27 = Entry(root, textvariable=cena_27, justify=CENTER, width=14)
        entry_cena_27.insert(0, "5")
        entry_cena_27.grid(row=17, column=6)
    elif nazwa_27.get() == "Dren Redona Ch 16 dł. 800mm z trokarem":
        entry_cena_27 = Entry(root, textvariable=cena_27, justify=CENTER, width=14)
        entry_cena_27.insert(0, "29.74")
        entry_cena_27.grid(row=17, column=6)
    elif nazwa_27.get() == "Dren do pompy Artrex":
        entry_cena_27 = Entry(root, textvariable=cena_27, justify=CENTER, width=14)
        entry_cena_27.insert(0, "108")
        entry_cena_27.grid(row=17, column=6)
    elif nazwa_27.get() == "Drut wiercący 2,4 x 311":
        entry_cena_27 = Entry(root, textvariable=cena_27, justify=CENTER, width=14)
        entry_cena_27.insert(0, "139.60")
        entry_cena_27.grid(row=17, column=6)
    elif nazwa_27.get() == "Fartuch jałowy L":
        entry_cena_27 = Entry(root, textvariable=cena_27, justify=CENTER, width=14)
        entry_cena_27.insert(0, "17")
        entry_cena_27.grid(row=17, column=6)
    elif nazwa_27.get() == "Fartuch jałowy M":
        entry_cena_27 = Entry(root, textvariable=cena_27, justify=CENTER, width=14)
        entry_cena_27.insert(0, "15.28")
        entry_cena_27.grid(row=17, column=6)
    elif nazwa_27.get() == "Fartuch jałowy XL":
        entry_cena_27 = Entry(root, textvariable=cena_27, justify=CENTER, width=14)
        entry_cena_27.insert(0, "20.84")
        entry_cena_27.grid(row=17, column=6)
    elif nazwa_27.get() == "FasatThread BioComposite Interference Screw 8x30":
        entry_cena_27 = Entry(root, textvariable=cena_27, justify=CENTER, width=14)
        entry_cena_27.insert(0, "594")
        entry_cena_27.grid(row=17, column=6)
    elif nazwa_27.get() == "Folia operacyjna, jałowa 45cm x 55cm":
        entry_cena_27 = Entry(root, textvariable=cena_27, justify=CENTER, width=14)
        entry_cena_27.insert(0, "9.99")
        entry_cena_27.grid(row=17, column=6)
    elif nazwa_27.get() == "Gaziki 10 x 10cm":
        entry_cena_27 = Entry(root, textvariable=cena_27, justify=CENTER, width=14)
        entry_cena_27.insert(0, "0.10")
        entry_cena_27.grid(row=17, column=6)
    elif nazwa_27.get() == "Igła 0,6 x 60":
        entry_cena_27 = Entry(root, textvariable=cena_27, justify=CENTER, width=14)
        entry_cena_27.insert(0, "0.09")
        entry_cena_27.grid(row=17, column=6)
    elif nazwa_27.get() == "Igła 0,7 x 40":
        entry_cena_27 = Entry(root, textvariable=cena_27, justify=CENTER, width=14)
        entry_cena_27.insert(0, "0.05")
        entry_cena_27.grid(row=17, column=6)
    elif nazwa_27.get() == "Igła 0,8 x 40":
        entry_cena_27 = Entry(root, textvariable=cena_27, justify=CENTER, width=14)
        entry_cena_27.insert(0, "0.05")
        entry_cena_27.grid(row=17, column=6)
    elif nazwa_27.get() == "Igła 1,1 x 70":
        entry_cena_27 = Entry(root, textvariable=cena_27, justify=CENTER, width=14)
        entry_cena_27.insert(0, "0.16")
        entry_cena_27.grid(row=17, column=6)
    elif nazwa_27.get() == "Kaniulowana śruba int. biokompozytowa z osłonką jednoraz.":
        entry_cena_27 = Entry(root, textvariable=cena_27, justify=CENTER, width=14)
        entry_cena_27.insert(0, "594")
        entry_cena_27.grid(row=17, column=6)
    elif nazwa_27.get() == "Kaniulowana śruba int. biokompozytowa z pełnym gwintem":
        entry_cena_27 = Entry(root, textvariable=cena_27, justify=CENTER, width=14)
        entry_cena_27.insert(0, "594")
        entry_cena_27.grid(row=17, column=6)
    elif nazwa_27.get() == "Końcówka do Shavera":
        entry_cena_27 = Entry(root, textvariable=cena_27, justify=CENTER, width=14)
        entry_cena_27.insert(0, "270")
        entry_cena_27.grid(row=17, column=6)
    elif nazwa_27.get() == "Kotwica biokompozytowa SwiveLock":
        entry_cena_27 = Entry(root, textvariable=cena_27, justify=CENTER, width=14)
        entry_cena_27.insert(0, "918")
        entry_cena_27.grid(row=17, column=6)
    elif nazwa_27.get() == "Kotwica Corkscrew":
        entry_cena_27 = Entry(root, textvariable=cena_27, justify=CENTER, width=14)
        entry_cena_27.insert(0, "604")
        entry_cena_27.grid(row=17, column=6)
    elif nazwa_27.get() == "Kotwica FASTak":
        entry_cena_27 = Entry(root, textvariable=cena_27, justify=CENTER, width=14)
        entry_cena_27.insert(0, "432")
        entry_cena_27.grid(row=17, column=6)
    elif nazwa_27.get() == "Kotwica PEEK SwiveLock":
        entry_cena_27 = Entry(root, textvariable=cena_27, justify=CENTER, width=14)
        entry_cena_27.insert(0, "885.60")
        entry_cena_27.grid(row=17, column=6)
    elif nazwa_27.get() == "NaCl 3000ml":
        entry_cena_27 = Entry(root, textvariable=cena_27, justify=CENTER, width=14)
        entry_cena_27.insert(0, "29.72")
        entry_cena_27.grid(row=17, column=6)
    elif nazwa_27.get() == "NaCl 5000ml":
        entry_cena_27 = Entry(root, textvariable=cena_27, justify=CENTER, width=14)
        entry_cena_27.insert(0, "58.33")
        entry_cena_27.grid(row=17, column=6)
    elif nazwa_27.get() == "Nici Dafilon 2-0":
        entry_cena_27 = Entry(root, textvariable=cena_27, justify=CENTER, width=14)
        entry_cena_27.insert(0, "6.60")
        entry_cena_27.grid(row=17, column=6)
    elif nazwa_27.get() == "Nici Novosyn 2":
        entry_cena_27 = Entry(root, textvariable=cena_27, justify=CENTER, width=14)
        entry_cena_27.insert(0, "13")
        entry_cena_27.grid(row=17, column=6)
    elif nazwa_27.get() == "Nici Novosyn 2-0":
        entry_cena_27 = Entry(root, textvariable=cena_27, justify=CENTER, width=14)
        entry_cena_27.insert(0, "7.70")
        entry_cena_27.grid(row=17, column=6)
    elif nazwa_27.get() == "Nici Novosyn 3-0":
        entry_cena_27 = Entry(root, textvariable=cena_27, justify=CENTER, width=14)
        entry_cena_27.insert(0, "7.70")
        entry_cena_27.grid(row=17, column=6)
    elif nazwa_27.get() == "Nici Nylon 2-0":
        entry_cena_27 = Entry(root, textvariable=cena_27, justify=CENTER, width=14)
        entry_cena_27.insert(0, "2.50")
        entry_cena_27.grid(row=17, column=6)
    elif nazwa_27.get() == "Nici Nylon 3-0":
        entry_cena_27 = Entry(root, textvariable=cena_27, justify=CENTER, width=14)
        entry_cena_27.insert(0, "2")
        entry_cena_27.grid(row=17, column=6)
    elif nazwa_27.get() == "Nici PGLA":
        entry_cena_27 = Entry(root, textvariable=cena_27, justify=CENTER, width=14)
        entry_cena_27.insert(0, "11.60")
        entry_cena_27.grid(row=17, column=6)
    elif nazwa_27.get() == "Nici PremiCron 3":
        entry_cena_27 = Entry(root, textvariable=cena_27, justify=CENTER, width=14)
        entry_cena_27.insert(0, "6.50")
        entry_cena_27.grid(row=17, column=6)
    elif nazwa_27.get() == "Nici Vicryl 4-0":
        entry_cena_27 = Entry(root, textvariable=cena_27, justify=CENTER, width=14)
        entry_cena_27.insert(0, "7.50")
        entry_cena_27.grid(row=17, column=6)
    elif nazwa_27.get() == "Nitinol Guide Pin 1.1":
        entry_cena_27 = Entry(root, textvariable=cena_27, justify=CENTER, width=14)
        entry_cena_27.insert(0, "145.80")
        entry_cena_27.grid(row=17, column=6)
    elif nazwa_27.get() == "Osłona na przewody":
        entry_cena_27 = Entry(root, textvariable=cena_27, justify=CENTER, width=14)
        entry_cena_27.insert(0, "2.50")
        entry_cena_27.grid(row=17, column=6)
    elif nazwa_27.get() == "Ostrze Arthrex 90(86)x19x1,27":
        entry_cena_27 = Entry(root, textvariable=cena_27, justify=CENTER, width=14)
        entry_cena_27.insert(0, "216")
        entry_cena_27.grid(row=17, column=6)
    elif nazwa_27.get() == "Ostrze piły":
        entry_cena_27 = Entry(root, textvariable=cena_27, justify=CENTER, width=14)
        entry_cena_27.insert(0, "108")
        entry_cena_27.grid(row=17, column=6)
    elif nazwa_27.get() == "Pielęgniarka anest.":
        entry_cena_27 = Entry(root, textvariable=cena_27, justify=CENTER, width=14)
        entry_cena_27.insert(0, "50")
        entry_cena_27.grid(row=17, column=6)
    elif nazwa_27.get() == "Pielęgniarka instr.":
        entry_cena_27 = Entry(root, textvariable=cena_27, justify=CENTER, width=14)
        entry_cena_27.insert(0, "50")
        entry_cena_27.grid(row=17, column=6)
    elif nazwa_27.get() == "Pielęgniarka 'Noviline'":
        entry_cena_27 = Entry(root, textvariable=cena_27, justify=CENTER, width=14)
        entry_cena_27.insert(0, "30")
        entry_cena_27.grid(row=17, column=6)
    elif nazwa_27.get() == "Płytka PeekPower do osteotomii klinowej":
        entry_cena_27 = Entry(root, textvariable=cena_27, justify=CENTER, width=14)
        entry_cena_27.insert(0, "2160")
        entry_cena_27.grid(row=17, column=6)
    elif nazwa_27.get() == "Rękawice jałowe 6,5":
        entry_cena_27 = Entry(root, textvariable=cena_27, justify=CENTER, width=14)
        entry_cena_27.insert(0, "1.20")
        entry_cena_27.grid(row=17, column=6)
    elif nazwa_27.get() == "Rękawice jałowe 7,0":
        entry_cena_27 = Entry(root, textvariable=cena_27, justify=CENTER, width=14)
        entry_cena_27.insert(0, "1.20")
        entry_cena_27.grid(row=17, column=6)
    elif nazwa_27.get() == "Rękawice jałowe 7,5":
        entry_cena_27 = Entry(root, textvariable=cena_27, justify=CENTER, width=14)
        entry_cena_27.insert(0, "1.20")
        entry_cena_27.grid(row=17, column=6)
    elif nazwa_27.get() == "Rękawice jałowe 8,00":
        entry_cena_27 = Entry(root, textvariable=cena_27, justify=CENTER, width=14)
        entry_cena_27.insert(0, "1.20")
        entry_cena_27.grid(row=17, column=6)
    elif nazwa_27.get() == "Rękojeść Interpulse wysokoprzepływowa":
        entry_cena_27 = Entry(root, textvariable=cena_27, justify=CENTER, width=14)
        entry_cena_27.insert(0, "216")
        entry_cena_27.grid(row=17, column=6)
    elif nazwa_27.get() == "Serweta":
        entry_cena_27 = Entry(root, textvariable=cena_27, justify=CENTER, width=14)
        entry_cena_27.insert(0, "6")
        entry_cena_27.grid(row=17, column=6)
    elif nazwa_27.get() == "Simplex Hv z Gentamycyna 10x40g":
        entry_cena_27 = Entry(root, textvariable=cena_27, justify=CENTER, width=14)
        entry_cena_27.insert(0, "162")
        entry_cena_27.grid(row=17, column=6)
    elif nazwa_27.get() == "Skalpel 11":
        entry_cena_27 = Entry(root, textvariable=cena_27, justify=CENTER, width=14)
        entry_cena_27.insert(0, "0.38")
        entry_cena_27.grid(row=17, column=6)
    elif nazwa_27.get() == "Skalpel 13":
        entry_cena_27 = Entry(root, textvariable=cena_27, justify=CENTER, width=14)
        entry_cena_27.insert(0, "1")
        entry_cena_27.grid(row=17, column=6)
    elif nazwa_27.get() == "Skalpel 22":
        entry_cena_27 = Entry(root, textvariable=cena_27, justify=CENTER, width=14)
        entry_cena_27.insert(0, "1")
        entry_cena_27.grid(row=17, column=6)
    elif nazwa_27.get() == "Śruba blokująca PeekPower do osteotomii":
        entry_cena_27 = Entry(root, textvariable=cena_27, justify=CENTER, width=14)
        entry_cena_27.insert(0, "194")
        entry_cena_27.grid(row=17, column=6)
    elif nazwa_27.get() == "System do mieszania próżniowego":
        entry_cena_27 = Entry(root, textvariable=cena_27, justify=CENTER, width=14)
        entry_cena_27.insert(0, "216")
        entry_cena_27.grid(row=17, column=6)
    elif nazwa_27.get() == "System wprowadzania implantów ACL TightRope":
        entry_cena_27 = Entry(root, textvariable=cena_27, justify=CENTER, width=14)
        entry_cena_27.insert(0, "702")
        entry_cena_27.grid(row=17, column=6)
    elif nazwa_27.get() == "Szew FiberWire 2":
        entry_cena_27 = Entry(root, textvariable=cena_27, justify=CENTER, width=14)
        entry_cena_27.insert(0, "86.40")
        entry_cena_27.grid(row=17, column=6)
    elif nazwa_27.get() == "Taśma przylepna 10x50":
        entry_cena_27 = Entry(root, textvariable=cena_27, justify=CENTER, width=14)
        entry_cena_27.insert(0, "1.04")
        entry_cena_27.grid(row=17, column=6)
    elif nazwa_27.get() == "Triathlon elem. udowy lewy":
        entry_cena_27 = Entry(root, textvariable=cena_27, justify=CENTER, width=14)
        entry_cena_27.insert(0, "3132")
        entry_cena_27.grid(row=17, column=6)
    elif nazwa_27.get() == "Triathlon PS wkładka x3-9mm #4":
        entry_cena_27 = Entry(root, textvariable=cena_27, justify=CENTER, width=14)
        entry_cena_27.insert(0, "756")
        entry_cena_27.grid(row=17, column=6)
    elif nazwa_27.get() == "Triathlon taca piszczelowa":
        entry_cena_27 = Entry(root, textvariable=cena_27, justify=CENTER, width=14)
        entry_cena_27.insert(0, "1296")
        entry_cena_27.grid(row=17, column=6)
    elif nazwa_27.get() == "Wkłady 3L z żelem":
        entry_cena_27 = Entry(root, textvariable=cena_27, justify=CENTER, width=14)
        entry_cena_27.insert(0, "10.26")
        entry_cena_27.grid(row=17, column=6)
    elif nazwa_27.get() == "Zestaw do artroskopii":
        entry_cena_27 = Entry(root, textvariable=cena_27, justify=CENTER, width=14)
        entry_cena_27.insert(0, "67")
        entry_cena_27.grid(row=17, column=6)
    elif nazwa_27.get() == "Zestaw do artroskopii barku":
        entry_cena_27 = Entry(root, textvariable=cena_27, justify=CENTER, width=14)
        entry_cena_27.insert(0, "108")
        entry_cena_27.grid(row=17, column=6)
    elif nazwa_27.get() == "Zestaw do drenażu":
        entry_cena_27 = Entry(root, textvariable=cena_27, justify=CENTER, width=14)
        entry_cena_27.insert(0, "14.23")
        entry_cena_27.grid(row=17, column=6)
    elif nazwa_27.get() == "Zestaw ortopedyczny":
        entry_cena_27 = Entry(root, textvariable=cena_27, justify=CENTER, width=14)
        entry_cena_27.insert(0, "28.08")
        entry_cena_27.grid(row=17, column=6)
    elif nazwa_27.get() == "Gaziki 20 x 10cm":
        entry_cena_27 = Entry(root, textvariable=cena_27, justify=CENTER, width=14)
        entry_cena_27.insert(0, "0.46")
        entry_cena_27.grid(row=17, column=6)
    else:
        entry_cena_27 = Entry(root, textvariable=cena_27, justify=CENTER, width=14, bg="#ffff00")
        entry_cena_27.insert(0, "0")
        entry_cena_27.grid(row=17, column=6)

    if nazwa_28.get() == "--puste--":
        entry_cena_28 = Entry(root, textvariable=cena_28, justify=CENTER, width=14)
        entry_cena_28.insert(0, "0")
        entry_cena_28.grid(row=18, column=6)
    elif nazwa_28.get() == "Ablator":
        entry_cena_28 = Entry(root, textvariable=cena_28, justify=CENTER, width=14)
        entry_cena_28.insert(0, "572")
        entry_cena_28.grid(row=18, column=6)
    elif nazwa_28.get() == "Anestezjolog":
        entry_cena_28 = Entry(root, textvariable=cena_28, justify=CENTER, width=14, bg="#ffff00")
        entry_cena_28.insert(0, "350")
        entry_cena_28.grid(row=18, column=6)
    elif nazwa_28.get() == "Butelka 400ml do długotrwałego odsysania ran j.u. sterylna":
        entry_cena_28 = Entry(root, textvariable=cena_28, justify=CENTER, width=14)
        entry_cena_28.insert(0, "4")
        entry_cena_28.grid(row=18, column=6)
    elif nazwa_28.get() == "Doba":
        entry_cena_28 = Entry(root, textvariable=cena_28, justify=CENTER, width=14)
        entry_cena_28.insert(0, "700")
        entry_cena_28.grid(row=18, column=6)
    elif nazwa_28.get() == "Dren łączący do ssaka Grena":
        entry_cena_28 = Entry(root, textvariable=cena_28, justify=CENTER, width=14)
        entry_cena_28.insert(0, "5")
        entry_cena_28.grid(row=18, column=6)
    elif nazwa_28.get() == "Dren Redona Ch 16 dł. 800mm z trokarem":
        entry_cena_28 = Entry(root, textvariable=cena_28, justify=CENTER, width=14)
        entry_cena_28.insert(0, "29.74")
        entry_cena_28.grid(row=18, column=6)
    elif nazwa_28.get() == "Dren do pompy Artrex":
        entry_cena_28 = Entry(root, textvariable=cena_28, justify=CENTER, width=14)
        entry_cena_28.insert(0, "108")
        entry_cena_28.grid(row=18, column=6)
    elif nazwa_28.get() == "Drut wiercący 2,4 x 311":
        entry_cena_28 = Entry(root, textvariable=cena_28, justify=CENTER, width=14)
        entry_cena_28.insert(0, "139.60")
        entry_cena_28.grid(row=18, column=6)
    elif nazwa_28.get() == "Fartuch jałowy L":
        entry_cena_28 = Entry(root, textvariable=cena_28, justify=CENTER, width=14)
        entry_cena_28.insert(0, "17")
        entry_cena_28.grid(row=18, column=6)
    elif nazwa_28.get() == "Fartuch jałowy M":
        entry_cena_28 = Entry(root, textvariable=cena_28, justify=CENTER, width=14)
        entry_cena_28.insert(0, "15.28")
        entry_cena_28.grid(row=18, column=6)
    elif nazwa_28.get() == "Fartuch jałowy XL":
        entry_cena_28 = Entry(root, textvariable=cena_28, justify=CENTER, width=14)
        entry_cena_28.insert(0, "20.84")
        entry_cena_28.grid(row=18, column=6)
    elif nazwa_28.get() == "FasatThread BioComposite Interference Screw 8x30":
        entry_cena_28 = Entry(root, textvariable=cena_28, justify=CENTER, width=14)
        entry_cena_28.insert(0, "594")
        entry_cena_28.grid(row=18, column=6)
    elif nazwa_28.get() == "Folia operacyjna, jałowa 45cm x 55cm":
        entry_cena_28 = Entry(root, textvariable=cena_28, justify=CENTER, width=14)
        entry_cena_28.insert(0, "9.99")
        entry_cena_28.grid(row=18, column=6)
    elif nazwa_28.get() == "Gaziki 10 x 10cm":
        entry_cena_28 = Entry(root, textvariable=cena_28, justify=CENTER, width=14)
        entry_cena_28.insert(0, "0.10")
        entry_cena_28.grid(row=18, column=6)
    elif nazwa_28.get() == "Igła 0,6 x 60":
        entry_cena_28 = Entry(root, textvariable=cena_28, justify=CENTER, width=14)
        entry_cena_28.insert(0, "0.09")
        entry_cena_28.grid(row=18, column=6)
    elif nazwa_28.get() == "Igła 0,7 x 40":
        entry_cena_28 = Entry(root, textvariable=cena_28, justify=CENTER, width=14)
        entry_cena_28.insert(0, "0.05")
        entry_cena_28.grid(row=18, column=6)
    elif nazwa_28.get() == "Igła 0,8 x 40":
        entry_cena_28 = Entry(root, textvariable=cena_28, justify=CENTER, width=14)
        entry_cena_28.insert(0, "0.05")
        entry_cena_28.grid(row=18, column=6)
    elif nazwa_28.get() == "Igła 1,1 x 70":
        entry_cena_28 = Entry(root, textvariable=cena_28, justify=CENTER, width=14)
        entry_cena_28.insert(0, "0.16")
        entry_cena_28.grid(row=18, column=6)
    elif nazwa_28.get() == "Kaniulowana śruba int. biokompozytowa z osłonką jednoraz.":
        entry_cena_28 = Entry(root, textvariable=cena_28, justify=CENTER, width=14)
        entry_cena_28.insert(0, "594")
        entry_cena_28.grid(row=18, column=6)
    elif nazwa_28.get() == "Kaniulowana śruba int. biokompozytowa z pełnym gwintem":
        entry_cena_28 = Entry(root, textvariable=cena_28, justify=CENTER, width=14)
        entry_cena_28.insert(0, "594")
        entry_cena_28.grid(row=18, column=6)
    elif nazwa_28.get() == "Końcówka do Shavera":
        entry_cena_28 = Entry(root, textvariable=cena_28, justify=CENTER, width=14)
        entry_cena_28.insert(0, "270")
        entry_cena_28.grid(row=18, column=6)
    elif nazwa_28.get() == "Kotwica biokompozytowa SwiveLock":
        entry_cena_28 = Entry(root, textvariable=cena_28, justify=CENTER, width=14)
        entry_cena_28.insert(0, "918")
        entry_cena_28.grid(row=18, column=6)
    elif nazwa_28.get() == "Kotwica Corkscrew":
        entry_cena_28 = Entry(root, textvariable=cena_28, justify=CENTER, width=14)
        entry_cena_28.insert(0, "604")
        entry_cena_28.grid(row=18, column=6)
    elif nazwa_28.get() == "Kotwica FASTak":
        entry_cena_28 = Entry(root, textvariable=cena_28, justify=CENTER, width=14)
        entry_cena_28.insert(0, "432")
        entry_cena_28.grid(row=18, column=6)
    elif nazwa_28.get() == "Kotwica PEEK SwiveLock":
        entry_cena_28 = Entry(root, textvariable=cena_28, justify=CENTER, width=14)
        entry_cena_28.insert(0, "885.60")
        entry_cena_28.grid(row=18, column=6)
    elif nazwa_28.get() == "NaCl 3000ml":
        entry_cena_28 = Entry(root, textvariable=cena_28, justify=CENTER, width=14)
        entry_cena_28.insert(0, "29.72")
        entry_cena_28.grid(row=18, column=6)
    elif nazwa_28.get() == "NaCl 5000ml":
        entry_cena_28 = Entry(root, textvariable=cena_28, justify=CENTER, width=14)
        entry_cena_28.insert(0, "58.33")
        entry_cena_28.grid(row=18, column=6)
    elif nazwa_28.get() == "Nici Dafilon 2-0":
        entry_cena_28 = Entry(root, textvariable=cena_28, justify=CENTER, width=14)
        entry_cena_28.insert(0, "6.60")
        entry_cena_28.grid(row=18, column=6)
    elif nazwa_28.get() == "Nici Novosyn 2":
        entry_cena_28 = Entry(root, textvariable=cena_28, justify=CENTER, width=14)
        entry_cena_28.insert(0, "13")
        entry_cena_28.grid(row=18, column=6)
    elif nazwa_28.get() == "Nici Novosyn 2-0":
        entry_cena_28 = Entry(root, textvariable=cena_28, justify=CENTER, width=14)
        entry_cena_28.insert(0, "7.70")
        entry_cena_28.grid(row=18, column=6)
    elif nazwa_28.get() == "Nici Novosyn 3-0":
        entry_cena_28 = Entry(root, textvariable=cena_28, justify=CENTER, width=14)
        entry_cena_28.insert(0, "7.70")
        entry_cena_28.grid(row=18, column=6)
    elif nazwa_28.get() == "Nici Nylon 2-0":
        entry_cena_28 = Entry(root, textvariable=cena_28, justify=CENTER, width=14)
        entry_cena_28.insert(0, "2.50")
        entry_cena_28.grid(row=18, column=6)
    elif nazwa_28.get() == "Nici Nylon 3-0":
        entry_cena_28 = Entry(root, textvariable=cena_28, justify=CENTER, width=14)
        entry_cena_28.insert(0, "2")
        entry_cena_28.grid(row=18, column=6)
    elif nazwa_28.get() == "Nici PGLA":
        entry_cena_28 = Entry(root, textvariable=cena_28, justify=CENTER, width=14)
        entry_cena_28.insert(0, "11.60")
        entry_cena_28.grid(row=18, column=6)
    elif nazwa_28.get() == "Nici PremiCron 3":
        entry_cena_28 = Entry(root, textvariable=cena_28, justify=CENTER, width=14)
        entry_cena_28.insert(0, "6.50")
        entry_cena_28.grid(row=18, column=6)
    elif nazwa_28.get() == "Nici Vicryl 4-0":
        entry_cena_28 = Entry(root, textvariable=cena_28, justify=CENTER, width=14)
        entry_cena_28.insert(0, "7.50")
        entry_cena_28.grid(row=18, column=6)
    elif nazwa_28.get() == "Nitinol Guide Pin 1.1":
        entry_cena_28 = Entry(root, textvariable=cena_28, justify=CENTER, width=14)
        entry_cena_28.insert(0, "145.80")
        entry_cena_28.grid(row=18, column=6)
    elif nazwa_28.get() == "Osłona na przewody":
        entry_cena_28 = Entry(root, textvariable=cena_28, justify=CENTER, width=14)
        entry_cena_28.insert(0, "2.50")
        entry_cena_28.grid(row=18, column=6)
    elif nazwa_28.get() == "Ostrze Arthrex 90(86)x19x1,27":
        entry_cena_28 = Entry(root, textvariable=cena_28, justify=CENTER, width=14)
        entry_cena_28.insert(0, "216")
        entry_cena_28.grid(row=18, column=6)
    elif nazwa_28.get() == "Ostrze piły":
        entry_cena_28 = Entry(root, textvariable=cena_28, justify=CENTER, width=14)
        entry_cena_28.insert(0, "108")
        entry_cena_28.grid(row=18, column=6)
    elif nazwa_28.get() == "Pielęgniarka anest.":
        entry_cena_28 = Entry(root, textvariable=cena_28, justify=CENTER, width=14)
        entry_cena_28.insert(0, "50")
        entry_cena_28.grid(row=18, column=6)
    elif nazwa_28.get() == "Pielęgniarka instr.":
        entry_cena_28 = Entry(root, textvariable=cena_28, justify=CENTER, width=14)
        entry_cena_28.insert(0, "50")
        entry_cena_28.grid(row=18, column=6)
    elif nazwa_28.get() == "Pielęgniarka 'Noviline'":
        entry_cena_28 = Entry(root, textvariable=cena_28, justify=CENTER, width=14)
        entry_cena_28.insert(0, "30")
        entry_cena_28.grid(row=18, column=6)
    elif nazwa_28.get() == "Płytka PeekPower do osteotomii klinowej":
        entry_cena_28 = Entry(root, textvariable=cena_28, justify=CENTER, width=14)
        entry_cena_28.insert(0, "2160")
        entry_cena_28.grid(row=18, column=6)
    elif nazwa_28.get() == "Rękawice jałowe 6,5":
        entry_cena_28 = Entry(root, textvariable=cena_28, justify=CENTER, width=14)
        entry_cena_28.insert(0, "1.20")
        entry_cena_28.grid(row=18, column=6)
    elif nazwa_28.get() == "Rękawice jałowe 7,0":
        entry_cena_28 = Entry(root, textvariable=cena_28, justify=CENTER, width=14)
        entry_cena_28.insert(0, "1.20")
        entry_cena_28.grid(row=18, column=6)
    elif nazwa_28.get() == "Rękawice jałowe 7,5":
        entry_cena_28 = Entry(root, textvariable=cena_28, justify=CENTER, width=14)
        entry_cena_28.insert(0, "1.20")
        entry_cena_28.grid(row=18, column=6)
    elif nazwa_28.get() == "Rękawice jałowe 8,00":
        entry_cena_28 = Entry(root, textvariable=cena_28, justify=CENTER, width=14)
        entry_cena_28.insert(0, "1.20")
        entry_cena_28.grid(row=18, column=6)
    elif nazwa_28.get() == "Rękojeść Interpulse wysokoprzepływowa":
        entry_cena_28 = Entry(root, textvariable=cena_28, justify=CENTER, width=14)
        entry_cena_28.insert(0, "216")
        entry_cena_28.grid(row=18, column=6)
    elif nazwa_28.get() == "Serweta":
        entry_cena_28 = Entry(root, textvariable=cena_28, justify=CENTER, width=14)
        entry_cena_28.insert(0, "6")
        entry_cena_28.grid(row=18, column=6)
    elif nazwa_28.get() == "Simplex Hv z Gentamycyna 10x40g":
        entry_cena_28 = Entry(root, textvariable=cena_28, justify=CENTER, width=14)
        entry_cena_28.insert(0, "162")
        entry_cena_28.grid(row=18, column=6)
    elif nazwa_28.get() == "Skalpel 11":
        entry_cena_28 = Entry(root, textvariable=cena_28, justify=CENTER, width=14)
        entry_cena_28.insert(0, "0.38")
        entry_cena_28.grid(row=18, column=6)
    elif nazwa_28.get() == "Skalpel 13":
        entry_cena_28 = Entry(root, textvariable=cena_28, justify=CENTER, width=14)
        entry_cena_28.insert(0, "1")
        entry_cena_28.grid(row=18, column=6)
    elif nazwa_28.get() == "Skalpel 22":
        entry_cena_28 = Entry(root, textvariable=cena_28, justify=CENTER, width=14)
        entry_cena_28.insert(0, "1")
        entry_cena_28.grid(row=18, column=6)
    elif nazwa_28.get() == "Śruba blokująca PeekPower do osteotomii":
        entry_cena_28 = Entry(root, textvariable=cena_28, justify=CENTER, width=14)
        entry_cena_28.insert(0, "194")
        entry_cena_28.grid(row=18, column=6)
    elif nazwa_28.get() == "System do mieszania próżniowego":
        entry_cena_28 = Entry(root, textvariable=cena_28, justify=CENTER, width=14)
        entry_cena_28.insert(0, "216")
        entry_cena_28.grid(row=18, column=6)
    elif nazwa_28.get() == "System wprowadzania implantów ACL TightRope":
        entry_cena_28 = Entry(root, textvariable=cena_28, justify=CENTER, width=14)
        entry_cena_28.insert(0, "702")
        entry_cena_28.grid(row=18, column=6)
    elif nazwa_28.get() == "Szew FiberWire 2":
        entry_cena_28 = Entry(root, textvariable=cena_28, justify=CENTER, width=14)
        entry_cena_28.insert(0, "86.40")
        entry_cena_28.grid(row=18, column=6)
    elif nazwa_28.get() == "Taśma przylepna 10x50":
        entry_cena_28 = Entry(root, textvariable=cena_28, justify=CENTER, width=14)
        entry_cena_28.insert(0, "1.04")
        entry_cena_28.grid(row=18, column=6)
    elif nazwa_28.get() == "Triathlon elem. udowy lewy":
        entry_cena_28 = Entry(root, textvariable=cena_28, justify=CENTER, width=14)
        entry_cena_28.insert(0, "3132")
        entry_cena_28.grid(row=18, column=6)
    elif nazwa_28.get() == "Triathlon PS wkładka x3-9mm #4":
        entry_cena_28 = Entry(root, textvariable=cena_28, justify=CENTER, width=14)
        entry_cena_28.insert(0, "756")
        entry_cena_28.grid(row=18, column=6)
    elif nazwa_28.get() == "Triathlon taca piszczelowa":
        entry_cena_28 = Entry(root, textvariable=cena_28, justify=CENTER, width=14)
        entry_cena_28.insert(0, "1296")
        entry_cena_28.grid(row=18, column=6)
    elif nazwa_28.get() == "Wkłady 3L z żelem":
        entry_cena_28 = Entry(root, textvariable=cena_28, justify=CENTER, width=14)
        entry_cena_28.insert(0, "10.26")
        entry_cena_28.grid(row=18, column=6)
    elif nazwa_28.get() == "Zestaw do artroskopii":
        entry_cena_28 = Entry(root, textvariable=cena_28, justify=CENTER, width=14)
        entry_cena_28.insert(0, "67")
        entry_cena_28.grid(row=18, column=6)
    elif nazwa_28.get() == "Zestaw do artroskopii barku":
        entry_cena_28 = Entry(root, textvariable=cena_28, justify=CENTER, width=14)
        entry_cena_28.insert(0, "108")
        entry_cena_28.grid(row=18, column=6)
    elif nazwa_28.get() == "Zestaw do drenażu":
        entry_cena_28 = Entry(root, textvariable=cena_28, justify=CENTER, width=14)
        entry_cena_28.insert(0, "14.23")
        entry_cena_28.grid(row=18, column=6)
    elif nazwa_28.get() == "Zestaw ortopedyczny":
        entry_cena_28 = Entry(root, textvariable=cena_28, justify=CENTER, width=14)
        entry_cena_28.insert(0, "28.08")
        entry_cena_28.grid(row=18, column=6)
    elif nazwa_28.get() == "Gaziki 20 x 10cm":
        entry_cena_28 = Entry(root, textvariable=cena_28, justify=CENTER, width=14)
        entry_cena_28.insert(0, "0.46")
        entry_cena_28.grid(row=18, column=6)
    else:
        entry_cena_28 = Entry(root, textvariable=cena_28, justify=CENTER, width=14, bg="#ffff00")
        entry_cena_28.insert(0, "0")
        entry_cena_28.grid(row=18, column=6)

    if nazwa_29.get() == "--puste--":
        entry_cena_29 = Entry(root, textvariable=cena_29, justify=CENTER, width=14)
        entry_cena_29.insert(0, "0")
        entry_cena_29.grid(row=19, column=6)
    elif nazwa_29.get() == "Ablator":
        entry_cena_29 = Entry(root, textvariable=cena_29, justify=CENTER, width=14)
        entry_cena_29.insert(0, "572")
        entry_cena_29.grid(row=19, column=6)
    elif nazwa_29.get() == "Anestezjolog":
        entry_cena_29 = Entry(root, textvariable=cena_29, justify=CENTER, width=14, bg="#ffff00")
        entry_cena_29.insert(0, "350")
        entry_cena_29.grid(row=19, column=6)
    elif nazwa_29.get() == "Butelka 400ml do długotrwałego odsysania ran j.u. sterylna":
        entry_cena_29 = Entry(root, textvariable=cena_29, justify=CENTER, width=14)
        entry_cena_29.insert(0, "4")
        entry_cena_29.grid(row=19, column=6)
    elif nazwa_29.get() == "Doba":
        entry_cena_29 = Entry(root, textvariable=cena_29, justify=CENTER, width=14)
        entry_cena_29.insert(0, "700")
        entry_cena_29.grid(row=19, column=6)
    elif nazwa_29.get() == "Dren łączący do ssaka Grena":
        entry_cena_29 = Entry(root, textvariable=cena_29, justify=CENTER, width=14)
        entry_cena_29.insert(0, "5")
        entry_cena_29.grid(row=19, column=6)
    elif nazwa_29.get() == "Dren Redona Ch 16 dł. 800mm z trokarem":
        entry_cena_29 = Entry(root, textvariable=cena_29, justify=CENTER, width=14)
        entry_cena_29.insert(0, "29.74")
        entry_cena_29.grid(row=19, column=6)
    elif nazwa_29.get() == "Dren do pompy Artrex":
        entry_cena_29 = Entry(root, textvariable=cena_29, justify=CENTER, width=14)
        entry_cena_29.insert(0, "108")
        entry_cena_29.grid(row=19, column=6)
    elif nazwa_29.get() == "Drut wiercący 2,4 x 311":
        entry_cena_29 = Entry(root, textvariable=cena_29, justify=CENTER, width=14)
        entry_cena_29.insert(0, "139.60")
        entry_cena_29.grid(row=19, column=6)
    elif nazwa_29.get() == "Fartuch jałowy L":
        entry_cena_29 = Entry(root, textvariable=cena_29, justify=CENTER, width=14)
        entry_cena_29.insert(0, "17")
        entry_cena_29.grid(row=19, column=6)
    elif nazwa_29.get() == "Fartuch jałowy M":
        entry_cena_29 = Entry(root, textvariable=cena_29, justify=CENTER, width=14)
        entry_cena_29.insert(0, "15.28")
        entry_cena_29.grid(row=19, column=6)
    elif nazwa_29.get() == "Fartuch jałowy XL":
        entry_cena_29 = Entry(root, textvariable=cena_29, justify=CENTER, width=14)
        entry_cena_29.insert(0, "20.84")
        entry_cena_29.grid(row=19, column=6)
    elif nazwa_29.get() == "FasatThread BioComposite Interference Screw 8x30":
        entry_cena_29 = Entry(root, textvariable=cena_29, justify=CENTER, width=14)
        entry_cena_29.insert(0, "594")
        entry_cena_29.grid(row=19, column=6)
    elif nazwa_29.get() == "Folia operacyjna, jałowa 45cm x 55cm":
        entry_cena_29 = Entry(root, textvariable=cena_29, justify=CENTER, width=14)
        entry_cena_29.insert(0, "9.99")
        entry_cena_29.grid(row=19, column=6)
    elif nazwa_29.get() == "Gaziki 10 x 10cm":
        entry_cena_29 = Entry(root, textvariable=cena_29, justify=CENTER, width=14)
        entry_cena_29.insert(0, "0.10")
        entry_cena_29.grid(row=19, column=6)
    elif nazwa_29.get() == "Igła 0,6 x 60":
        entry_cena_29 = Entry(root, textvariable=cena_29, justify=CENTER, width=14)
        entry_cena_29.insert(0, "0.09")
        entry_cena_29.grid(row=19, column=6)
    elif nazwa_29.get() == "Igła 0,7 x 40":
        entry_cena_29 = Entry(root, textvariable=cena_29, justify=CENTER, width=14)
        entry_cena_29.insert(0, "0.05")
        entry_cena_29.grid(row=19, column=6)
    elif nazwa_29.get() == "Igła 0,8 x 40":
        entry_cena_29 = Entry(root, textvariable=cena_29, justify=CENTER, width=14)
        entry_cena_29.insert(0, "0.05")
        entry_cena_29.grid(row=19, column=6)
    elif nazwa_29.get() == "Igła 1,1 x 70":
        entry_cena_29 = Entry(root, textvariable=cena_29, justify=CENTER, width=14)
        entry_cena_29.insert(0, "0.16")
        entry_cena_29.grid(row=19, column=6)
    elif nazwa_29.get() == "Kaniulowana śruba int. biokompozytowa z osłonką jednoraz.":
        entry_cena_29 = Entry(root, textvariable=cena_29, justify=CENTER, width=14)
        entry_cena_29.insert(0, "594")
        entry_cena_29.grid(row=19, column=6)
    elif nazwa_29.get() == "Kaniulowana śruba int. biokompozytowa z pełnym gwintem":
        entry_cena_29 = Entry(root, textvariable=cena_29, justify=CENTER, width=14)
        entry_cena_29.insert(0, "594")
        entry_cena_29.grid(row=19, column=6)
    elif nazwa_29.get() == "Końcówka do Shavera":
        entry_cena_29 = Entry(root, textvariable=cena_29, justify=CENTER, width=14)
        entry_cena_29.insert(0, "270")
        entry_cena_29.grid(row=19, column=6)
    elif nazwa_29.get() == "Kotwica biokompozytowa SwiveLock":
        entry_cena_29 = Entry(root, textvariable=cena_29, justify=CENTER, width=14)
        entry_cena_29.insert(0, "918")
        entry_cena_29.grid(row=19, column=6)
    elif nazwa_29.get() == "Kotwica Corkscrew":
        entry_cena_29 = Entry(root, textvariable=cena_29, justify=CENTER, width=14)
        entry_cena_29.insert(0, "604")
        entry_cena_29.grid(row=19, column=6)
    elif nazwa_29.get() == "Kotwica FASTak":
        entry_cena_29 = Entry(root, textvariable=cena_29, justify=CENTER, width=14)
        entry_cena_29.insert(0, "432")
        entry_cena_29.grid(row=19, column=6)
    elif nazwa_29.get() == "Kotwica PEEK SwiveLock":
        entry_cena_29 = Entry(root, textvariable=cena_29, justify=CENTER, width=14)
        entry_cena_29.insert(0, "885.60")
        entry_cena_29.grid(row=19, column=6)
    elif nazwa_29.get() == "NaCl 3000ml":
        entry_cena_29 = Entry(root, textvariable=cena_29, justify=CENTER, width=14)
        entry_cena_29.insert(0, "29.72")
        entry_cena_29.grid(row=19, column=6)
    elif nazwa_29.get() == "NaCl 5000ml":
        entry_cena_29 = Entry(root, textvariable=cena_29, justify=CENTER, width=14)
        entry_cena_29.insert(0, "58.33")
        entry_cena_29.grid(row=19, column=6)
    elif nazwa_29.get() == "Nici Dafilon 2-0":
        entry_cena_29 = Entry(root, textvariable=cena_29, justify=CENTER, width=14)
        entry_cena_29.insert(0, "6.60")
        entry_cena_29.grid(row=19, column=6)
    elif nazwa_29.get() == "Nici Novosyn 2":
        entry_cena_29 = Entry(root, textvariable=cena_29, justify=CENTER, width=14)
        entry_cena_29.insert(0, "13")
        entry_cena_29.grid(row=19, column=6)
    elif nazwa_29.get() == "Nici Novosyn 2-0":
        entry_cena_29 = Entry(root, textvariable=cena_29, justify=CENTER, width=14)
        entry_cena_29.insert(0, "7.70")
        entry_cena_29.grid(row=19, column=6)
    elif nazwa_29.get() == "Nici Novosyn 3-0":
        entry_cena_29 = Entry(root, textvariable=cena_29, justify=CENTER, width=14)
        entry_cena_29.insert(0, "7.70")
        entry_cena_29.grid(row=19, column=6)
    elif nazwa_29.get() == "Nici Nylon 2-0":
        entry_cena_29 = Entry(root, textvariable=cena_29, justify=CENTER, width=14)
        entry_cena_29.insert(0, "2.50")
        entry_cena_29.grid(row=19, column=6)
    elif nazwa_29.get() == "Nici Nylon 3-0":
        entry_cena_29 = Entry(root, textvariable=cena_29, justify=CENTER, width=14)
        entry_cena_29.insert(0, "2")
        entry_cena_29.grid(row=19, column=6)
    elif nazwa_29.get() == "Nici PGLA":
        entry_cena_29 = Entry(root, textvariable=cena_29, justify=CENTER, width=14)
        entry_cena_29.insert(0, "11.60")
        entry_cena_29.grid(row=19, column=6)
    elif nazwa_29.get() == "Nici PremiCron 3":
        entry_cena_29 = Entry(root, textvariable=cena_29, justify=CENTER, width=14)
        entry_cena_29.insert(0, "6.50")
        entry_cena_29.grid(row=19, column=6)
    elif nazwa_29.get() == "Nici Vicryl 4-0":
        entry_cena_29 = Entry(root, textvariable=cena_29, justify=CENTER, width=14)
        entry_cena_29.insert(0, "7.50")
        entry_cena_29.grid(row=19, column=6)
    elif nazwa_29.get() == "Nitinol Guide Pin 1.1":
        entry_cena_29 = Entry(root, textvariable=cena_29, justify=CENTER, width=14)
        entry_cena_29.insert(0, "145.80")
        entry_cena_29.grid(row=19, column=6)
    elif nazwa_29.get() == "Osłona na przewody":
        entry_cena_29 = Entry(root, textvariable=cena_29, justify=CENTER, width=14)
        entry_cena_29.insert(0, "2.50")
        entry_cena_29.grid(row=19, column=6)
    elif nazwa_29.get() == "Ostrze Arthrex 90(86)x19x1,27":
        entry_cena_29 = Entry(root, textvariable=cena_29, justify=CENTER, width=14)
        entry_cena_29.insert(0, "216")
        entry_cena_29.grid(row=19, column=6)
    elif nazwa_29.get() == "Ostrze piły":
        entry_cena_29 = Entry(root, textvariable=cena_29, justify=CENTER, width=14)
        entry_cena_29.insert(0, "108")
        entry_cena_29.grid(row=19, column=6)
    elif nazwa_29.get() == "Pielęgniarka anest.":
        entry_cena_29 = Entry(root, textvariable=cena_29, justify=CENTER, width=14)
        entry_cena_29.insert(0, "50")
        entry_cena_29.grid(row=19, column=6)
    elif nazwa_29.get() == "Pielęgniarka instr.":
        entry_cena_29 = Entry(root, textvariable=cena_29, justify=CENTER, width=14)
        entry_cena_29.insert(0, "50")
        entry_cena_29.grid(row=19, column=6)
    elif nazwa_29.get() == "Pielęgniarka 'Noviline'":
        entry_cena_29 = Entry(root, textvariable=cena_29, justify=CENTER, width=14)
        entry_cena_29.insert(0, "30")
        entry_cena_29.grid(row=19, column=6)
    elif nazwa_29.get() == "Płytka PeekPower do osteotomii klinowej":
        entry_cena_29 = Entry(root, textvariable=cena_29, justify=CENTER, width=14)
        entry_cena_29.insert(0, "2160")
        entry_cena_29.grid(row=19, column=6)
    elif nazwa_29.get() == "Rękawice jałowe 6,5":
        entry_cena_29 = Entry(root, textvariable=cena_29, justify=CENTER, width=14)
        entry_cena_29.insert(0, "1.20")
        entry_cena_29.grid(row=19, column=6)
    elif nazwa_29.get() == "Rękawice jałowe 7,0":
        entry_cena_29 = Entry(root, textvariable=cena_29, justify=CENTER, width=14)
        entry_cena_29.insert(0, "1.20")
        entry_cena_29.grid(row=19, column=6)
    elif nazwa_29.get() == "Rękawice jałowe 7,5":
        entry_cena_29 = Entry(root, textvariable=cena_29, justify=CENTER, width=14)
        entry_cena_29.insert(0, "1.20")
        entry_cena_29.grid(row=19, column=6)
    elif nazwa_29.get() == "Rękawice jałowe 8,00":
        entry_cena_29 = Entry(root, textvariable=cena_29, justify=CENTER, width=14)
        entry_cena_29.insert(0, "1.20")
        entry_cena_29.grid(row=19, column=6)
    elif nazwa_29.get() == "Rękojeść Interpulse wysokoprzepływowa":
        entry_cena_29 = Entry(root, textvariable=cena_29, justify=CENTER, width=14)
        entry_cena_29.insert(0, "216")
        entry_cena_29.grid(row=19, column=6)
    elif nazwa_29.get() == "Serweta":
        entry_cena_29 = Entry(root, textvariable=cena_29, justify=CENTER, width=14)
        entry_cena_29.insert(0, "6")
        entry_cena_29.grid(row=19, column=6)
    elif nazwa_29.get() == "Simplex Hv z Gentamycyna 10x40g":
        entry_cena_29 = Entry(root, textvariable=cena_29, justify=CENTER, width=14)
        entry_cena_29.insert(0, "162")
        entry_cena_29.grid(row=19, column=6)
    elif nazwa_29.get() == "Skalpel 11":
        entry_cena_29 = Entry(root, textvariable=cena_29, justify=CENTER, width=14)
        entry_cena_29.insert(0, "0.38")
        entry_cena_29.grid(row=19, column=6)
    elif nazwa_29.get() == "Skalpel 13":
        entry_cena_29 = Entry(root, textvariable=cena_29, justify=CENTER, width=14)
        entry_cena_29.insert(0, "1")
        entry_cena_29.grid(row=19, column=6)
    elif nazwa_29.get() == "Skalpel 22":
        entry_cena_29 = Entry(root, textvariable=cena_29, justify=CENTER, width=14)
        entry_cena_29.insert(0, "1")
        entry_cena_29.grid(row=19, column=6)
    elif nazwa_29.get() == "Śruba blokująca PeekPower do osteotomii":
        entry_cena_29 = Entry(root, textvariable=cena_29, justify=CENTER, width=14)
        entry_cena_29.insert(0, "194")
        entry_cena_29.grid(row=19, column=6)
    elif nazwa_29.get() == "System do mieszania próżniowego":
        entry_cena_29 = Entry(root, textvariable=cena_29, justify=CENTER, width=14)
        entry_cena_29.insert(0, "216")
        entry_cena_29.grid(row=19, column=6)
    elif nazwa_29.get() == "System wprowadzania implantów ACL TightRope":
        entry_cena_29 = Entry(root, textvariable=cena_29, justify=CENTER, width=14)
        entry_cena_29.insert(0, "702")
        entry_cena_29.grid(row=19, column=6)
    elif nazwa_29.get() == "Szew FiberWire 2":
        entry_cena_29 = Entry(root, textvariable=cena_29, justify=CENTER, width=14)
        entry_cena_29.insert(0, "86.40")
        entry_cena_29.grid(row=19, column=6)
    elif nazwa_29.get() == "Taśma przylepna 10x50":
        entry_cena_29 = Entry(root, textvariable=cena_29, justify=CENTER, width=14)
        entry_cena_29.insert(0, "1.04")
        entry_cena_29.grid(row=19, column=6)
    elif nazwa_29.get() == "Triathlon elem. udowy lewy":
        entry_cena_29 = Entry(root, textvariable=cena_29, justify=CENTER, width=14)
        entry_cena_29.insert(0, "3132")
        entry_cena_29.grid(row=19, column=6)
    elif nazwa_29.get() == "Triathlon PS wkładka x3-9mm #4":
        entry_cena_29 = Entry(root, textvariable=cena_29, justify=CENTER, width=14)
        entry_cena_29.insert(0, "756")
        entry_cena_29.grid(row=19, column=6)
    elif nazwa_29.get() == "Triathlon taca piszczelowa":
        entry_cena_29 = Entry(root, textvariable=cena_29, justify=CENTER, width=14)
        entry_cena_29.insert(0, "1296")
        entry_cena_29.grid(row=19, column=6)
    elif nazwa_29.get() == "Wkłady 3L z żelem":
        entry_cena_29 = Entry(root, textvariable=cena_29, justify=CENTER, width=14)
        entry_cena_29.insert(0, "10.26")
        entry_cena_29.grid(row=19, column=6)
    elif nazwa_29.get() == "Zestaw do artroskopii":
        entry_cena_29 = Entry(root, textvariable=cena_29, justify=CENTER, width=14)
        entry_cena_29.insert(0, "67")
        entry_cena_29.grid(row=19, column=6)
    elif nazwa_29.get() == "Zestaw do artroskopii barku":
        entry_cena_29 = Entry(root, textvariable=cena_29, justify=CENTER, width=14)
        entry_cena_29.insert(0, "108")
        entry_cena_29.grid(row=19, column=6)
    elif nazwa_29.get() == "Zestaw do drenażu":
        entry_cena_29 = Entry(root, textvariable=cena_29, justify=CENTER, width=14)
        entry_cena_29.insert(0, "14.23")
        entry_cena_29.grid(row=19, column=6)
    elif nazwa_29.get() == "Zestaw ortopedyczny":
        entry_cena_29 = Entry(root, textvariable=cena_29, justify=CENTER, width=14)
        entry_cena_29.insert(0, "28.08")
        entry_cena_29.grid(row=19, column=6)
    elif nazwa_29.get() == "Gaziki 20 x 10cm":
        entry_cena_29 = Entry(root, textvariable=cena_29, justify=CENTER, width=14)
        entry_cena_29.insert(0, "0.46")
        entry_cena_29.grid(row=19, column=6)
    else:
        entry_cena_29 = Entry(root, textvariable=cena_29, justify=CENTER, width=14, bg="#ffff00")
        entry_cena_29.insert(0, "0")
        entry_cena_29.grid(row=19, column=6)

    if nazwa_30.get() == "--puste--":
        entry_cena_30 = Entry(root, textvariable=cena_30, justify=CENTER, width=14)
        entry_cena_30.insert(0, "0")
        entry_cena_30.grid(row=20, column=6)
    elif nazwa_30.get() == "Ablator":
        entry_cena_30 = Entry(root, textvariable=cena_30, justify=CENTER, width=14)
        entry_cena_30.insert(0, "572")
        entry_cena_30.grid(row=20, column=6)
    elif nazwa_30.get() == "Anestezjolog":
        entry_cena_30 = Entry(root, textvariable=cena_30, justify=CENTER, width=14, bg="#ffff00")
        entry_cena_30.insert(0, "350")
        entry_cena_30.grid(row=20, column=6)
    elif nazwa_30.get() == "Butelka 400ml do długotrwałego odsysania ran j.u. sterylna":
        entry_cena_30 = Entry(root, textvariable=cena_30, justify=CENTER, width=14)
        entry_cena_30.insert(0, "4")
        entry_cena_30.grid(row=20, column=6)
    elif nazwa_30.get() == "Doba":
        entry_cena_30 = Entry(root, textvariable=cena_30, justify=CENTER, width=14)
        entry_cena_30.insert(0, "700")
        entry_cena_30.grid(row=20, column=6)
    elif nazwa_30.get() == "Dren łączący do ssaka Grena":
        entry_cena_30 = Entry(root, textvariable=cena_30, justify=CENTER, width=14)
        entry_cena_30.insert(0, "5")
        entry_cena_30.grid(row=20, column=6)
    elif nazwa_30.get() == "Dren Redona Ch 16 dł. 800mm z trokarem":
        entry_cena_30 = Entry(root, textvariable=cena_30, justify=CENTER, width=14)
        entry_cena_30.insert(0, "29.74")
        entry_cena_30.grid(row=20, column=6)
    elif nazwa_30.get() == "Dren do pompy Artrex":
        entry_cena_30 = Entry(root, textvariable=cena_30, justify=CENTER, width=14)
        entry_cena_30.insert(0, "108")
        entry_cena_30.grid(row=20, column=6)
    elif nazwa_30.get() == "Drut wiercący 2,4 x 311":
        entry_cena_30 = Entry(root, textvariable=cena_30, justify=CENTER, width=14)
        entry_cena_30.insert(0, "139.60")
        entry_cena_30.grid(row=20, column=6)
    elif nazwa_30.get() == "Fartuch jałowy L":
        entry_cena_30 = Entry(root, textvariable=cena_30, justify=CENTER, width=14)
        entry_cena_30.insert(0, "17")
        entry_cena_30.grid(row=20, column=6)
    elif nazwa_30.get() == "Fartuch jałowy M":
        entry_cena_30 = Entry(root, textvariable=cena_30, justify=CENTER, width=14)
        entry_cena_30.insert(0, "15.28")
        entry_cena_30.grid(row=20, column=6)
    elif nazwa_30.get() == "Fartuch jałowy XL":
        entry_cena_30 = Entry(root, textvariable=cena_30, justify=CENTER, width=14)
        entry_cena_30.insert(0, "20.84")
        entry_cena_30.grid(row=20, column=6)
    elif nazwa_30.get() == "FasatThread BioComposite Interference Screw 8x30":
        entry_cena_30 = Entry(root, textvariable=cena_30, justify=CENTER, width=14)
        entry_cena_30.insert(0, "594")
        entry_cena_30.grid(row=20, column=6)
    elif nazwa_30.get() == "Folia operacyjna, jałowa 45cm x 55cm":
        entry_cena_30 = Entry(root, textvariable=cena_30, justify=CENTER, width=14)
        entry_cena_30.insert(0, "9.99")
        entry_cena_30.grid(row=20, column=6)
    elif nazwa_30.get() == "Gaziki 10 x 10cm":
        entry_cena_30 = Entry(root, textvariable=cena_30, justify=CENTER, width=14)
        entry_cena_30.insert(0, "0.10")
        entry_cena_30.grid(row=20, column=6)
    elif nazwa_30.get() == "Igła 0,6 x 60":
        entry_cena_30 = Entry(root, textvariable=cena_30, justify=CENTER, width=14)
        entry_cena_30.insert(0, "0.09")
        entry_cena_30.grid(row=20, column=6)
    elif nazwa_30.get() == "Igła 0,7 x 40":
        entry_cena_30 = Entry(root, textvariable=cena_30, justify=CENTER, width=14)
        entry_cena_30.insert(0, "0.05")
        entry_cena_30.grid(row=20, column=6)
    elif nazwa_30.get() == "Igła 0,8 x 40":
        entry_cena_30 = Entry(root, textvariable=cena_30, justify=CENTER, width=14)
        entry_cena_30.insert(0, "0.05")
        entry_cena_30.grid(row=20, column=6)
    elif nazwa_30.get() == "Igła 1,1 x 70":
        entry_cena_30 = Entry(root, textvariable=cena_30, justify=CENTER, width=14)
        entry_cena_30.insert(0, "0.16")
        entry_cena_30.grid(row=20, column=6)
    elif nazwa_30.get() == "Kaniulowana śruba int. biokompozytowa z osłonką jednoraz.":
        entry_cena_30 = Entry(root, textvariable=cena_30, justify=CENTER, width=14)
        entry_cena_30.insert(0, "594")
        entry_cena_30.grid(row=20, column=6)
    elif nazwa_30.get() == "Kaniulowana śruba int. biokompozytowa z pełnym gwintem":
        entry_cena_30 = Entry(root, textvariable=cena_30, justify=CENTER, width=14)
        entry_cena_30.insert(0, "594")
        entry_cena_30.grid(row=20, column=6)
    elif nazwa_30.get() == "Końcówka do Shavera":
        entry_cena_30 = Entry(root, textvariable=cena_30, justify=CENTER, width=14)
        entry_cena_30.insert(0, "270")
        entry_cena_30.grid(row=20, column=6)
    elif nazwa_30.get() == "Kotwica biokompozytowa SwiveLock":
        entry_cena_30 = Entry(root, textvariable=cena_30, justify=CENTER, width=14)
        entry_cena_30.insert(0, "918")
        entry_cena_30.grid(row=20, column=6)
    elif nazwa_30.get() == "Kotwica Corkscrew":
        entry_cena_30 = Entry(root, textvariable=cena_30, justify=CENTER, width=14)
        entry_cena_30.insert(0, "604")
        entry_cena_30.grid(row=20, column=6)
    elif nazwa_30.get() == "Kotwica FASTak":
        entry_cena_30 = Entry(root, textvariable=cena_30, justify=CENTER, width=14)
        entry_cena_30.insert(0, "432")
        entry_cena_30.grid(row=20, column=6)
    elif nazwa_30.get() == "Kotwica PEEK SwiveLock":
        entry_cena_30 = Entry(root, textvariable=cena_30, justify=CENTER, width=14)
        entry_cena_30.insert(0, "885.60")
        entry_cena_30.grid(row=20, column=6)
    elif nazwa_30.get() == "NaCl 3000ml":
        entry_cena_30 = Entry(root, textvariable=cena_30, justify=CENTER, width=14)
        entry_cena_30.insert(0, "29.72")
        entry_cena_30.grid(row=20, column=6)
    elif nazwa_30.get() == "NaCl 5000ml":
        entry_cena_30 = Entry(root, textvariable=cena_30, justify=CENTER, width=14)
        entry_cena_30.insert(0, "58.33")
        entry_cena_30.grid(row=20, column=6)
    elif nazwa_30.get() == "Nici Dafilon 2-0":
        entry_cena_30 = Entry(root, textvariable=cena_30, justify=CENTER, width=14)
        entry_cena_30.insert(0, "6.60")
        entry_cena_30.grid(row=20, column=6)
    elif nazwa_30.get() == "Nici Novosyn 2":
        entry_cena_30 = Entry(root, textvariable=cena_30, justify=CENTER, width=14)
        entry_cena_30.insert(0, "13")
        entry_cena_30.grid(row=20, column=6)
    elif nazwa_30.get() == "Nici Novosyn 2-0":
        entry_cena_30 = Entry(root, textvariable=cena_30, justify=CENTER, width=14)
        entry_cena_30.insert(0, "7.70")
        entry_cena_30.grid(row=20, column=6)
    elif nazwa_30.get() == "Nici Novosyn 3-0":
        entry_cena_30 = Entry(root, textvariable=cena_30, justify=CENTER, width=14)
        entry_cena_30.insert(0, "7.70")
        entry_cena_30.grid(row=20, column=6)
    elif nazwa_30.get() == "Nici Nylon 2-0":
        entry_cena_30 = Entry(root, textvariable=cena_30, justify=CENTER, width=14)
        entry_cena_30.insert(0, "2.50")
        entry_cena_30.grid(row=20, column=6)
    elif nazwa_30.get() == "Nici Nylon 3-0":
        entry_cena_30 = Entry(root, textvariable=cena_30, justify=CENTER, width=14)
        entry_cena_30.insert(0, "2")
        entry_cena_30.grid(row=20, column=6)
    elif nazwa_30.get() == "Nici PGLA":
        entry_cena_30 = Entry(root, textvariable=cena_30, justify=CENTER, width=14)
        entry_cena_30.insert(0, "11.60")
        entry_cena_30.grid(row=20, column=6)
    elif nazwa_30.get() == "Nici PremiCron 3":
        entry_cena_30 = Entry(root, textvariable=cena_30, justify=CENTER, width=14)
        entry_cena_30.insert(0, "6.50")
        entry_cena_30.grid(row=20, column=6)
    elif nazwa_30.get() == "Nici Vicryl 4-0":
        entry_cena_30 = Entry(root, textvariable=cena_30, justify=CENTER, width=14)
        entry_cena_30.insert(0, "7.50")
        entry_cena_30.grid(row=20, column=6)
    elif nazwa_30.get() == "Nitinol Guide Pin 1.1":
        entry_cena_30 = Entry(root, textvariable=cena_30, justify=CENTER, width=14)
        entry_cena_30.insert(0, "145.80")
        entry_cena_30.grid(row=20, column=6)
    elif nazwa_30.get() == "Osłona na przewody":
        entry_cena_30 = Entry(root, textvariable=cena_30, justify=CENTER, width=14)
        entry_cena_30.insert(0, "2.50")
        entry_cena_30.grid(row=20, column=6)
    elif nazwa_30.get() == "Ostrze Arthrex 90(86)x19x1,27":
        entry_cena_30 = Entry(root, textvariable=cena_30, justify=CENTER, width=14)
        entry_cena_30.insert(0, "216")
        entry_cena_30.grid(row=20, column=6)
    elif nazwa_30.get() == "Ostrze piły":
        entry_cena_30 = Entry(root, textvariable=cena_30, justify=CENTER, width=14)
        entry_cena_30.insert(0, "108")
        entry_cena_30.grid(row=20, column=6)
    elif nazwa_30.get() == "Pielęgniarka anest.":
        entry_cena_30 = Entry(root, textvariable=cena_30, justify=CENTER, width=14)
        entry_cena_30.insert(0, "50")
        entry_cena_30.grid(row=20, column=6)
    elif nazwa_30.get() == "Pielęgniarka instr.":
        entry_cena_30 = Entry(root, textvariable=cena_30, justify=CENTER, width=14)
        entry_cena_30.insert(0, "50")
        entry_cena_30.grid(row=20, column=6)
    elif nazwa_30.get() == "Pielęgniarka 'Noviline'":
        entry_cena_30 = Entry(root, textvariable=cena_30, justify=CENTER, width=14)
        entry_cena_30.insert(0, "30")
        entry_cena_30.grid(row=20, column=6)
    elif nazwa_30.get() == "Płytka PeekPower do osteotomii klinowej":
        entry_cena_30 = Entry(root, textvariable=cena_30, justify=CENTER, width=14)
        entry_cena_30.insert(0, "2160")
        entry_cena_30.grid(row=20, column=6)
    elif nazwa_30.get() == "Rękawice jałowe 6,5":
        entry_cena_30 = Entry(root, textvariable=cena_30, justify=CENTER, width=14)
        entry_cena_30.insert(0, "1.20")
        entry_cena_30.grid(row=20, column=6)
    elif nazwa_30.get() == "Rękawice jałowe 7,0":
        entry_cena_30 = Entry(root, textvariable=cena_30, justify=CENTER, width=14)
        entry_cena_30.insert(0, "1.20")
        entry_cena_30.grid(row=20, column=6)
    elif nazwa_30.get() == "Rękawice jałowe 7,5":
        entry_cena_30 = Entry(root, textvariable=cena_30, justify=CENTER, width=14)
        entry_cena_30.insert(0, "1.20")
        entry_cena_30.grid(row=20, column=6)
    elif nazwa_30.get() == "Rękawice jałowe 8,00":
        entry_cena_30 = Entry(root, textvariable=cena_30, justify=CENTER, width=14)
        entry_cena_30.insert(0, "1.20")
        entry_cena_30.grid(row=20, column=6)
    elif nazwa_30.get() == "Rękojeść Interpulse wysokoprzepływowa":
        entry_cena_30 = Entry(root, textvariable=cena_30, justify=CENTER, width=14)
        entry_cena_30.insert(0, "216")
        entry_cena_30.grid(row=20, column=6)
    elif nazwa_30.get() == "Serweta":
        entry_cena_30 = Entry(root, textvariable=cena_30, justify=CENTER, width=14)
        entry_cena_30.insert(0, "6")
        entry_cena_30.grid(row=20, column=6)
    elif nazwa_30.get() == "Simplex Hv z Gentamycyna 10x40g":
        entry_cena_30 = Entry(root, textvariable=cena_30, justify=CENTER, width=14)
        entry_cena_30.insert(0, "162")
        entry_cena_30.grid(row=20, column=6)
    elif nazwa_30.get() == "Skalpel 11":
        entry_cena_30 = Entry(root, textvariable=cena_30, justify=CENTER, width=14)
        entry_cena_30.insert(0, "0.38")
        entry_cena_30.grid(row=20, column=6)
    elif nazwa_30.get() == "Skalpel 13":
        entry_cena_30 = Entry(root, textvariable=cena_30, justify=CENTER, width=14)
        entry_cena_30.insert(0, "1")
        entry_cena_30.grid(row=20, column=6)
    elif nazwa_30.get() == "Skalpel 22":
        entry_cena_30 = Entry(root, textvariable=cena_30, justify=CENTER, width=14)
        entry_cena_30.insert(0, "1")
        entry_cena_30.grid(row=20, column=6)
    elif nazwa_30.get() == "Śruba blokująca PeekPower do osteotomii":
        entry_cena_30 = Entry(root, textvariable=cena_30, justify=CENTER, width=14)
        entry_cena_30.insert(0, "194")
        entry_cena_30.grid(row=20, column=6)
    elif nazwa_30.get() == "System do mieszania próżniowego":
        entry_cena_30 = Entry(root, textvariable=cena_30, justify=CENTER, width=14)
        entry_cena_30.insert(0, "216")
        entry_cena_30.grid(row=20, column=6)
    elif nazwa_30.get() == "System wprowadzania implantów ACL TightRope":
        entry_cena_30 = Entry(root, textvariable=cena_30, justify=CENTER, width=14)
        entry_cena_30.insert(0, "702")
        entry_cena_30.grid(row=20, column=6)
    elif nazwa_30.get() == "Szew FiberWire 2":
        entry_cena_30 = Entry(root, textvariable=cena_30, justify=CENTER, width=14)
        entry_cena_30.insert(0, "86.40")
        entry_cena_30.grid(row=20, column=6)
    elif nazwa_30.get() == "Taśma przylepna 10x50":
        entry_cena_30 = Entry(root, textvariable=cena_30, justify=CENTER, width=14)
        entry_cena_30.insert(0, "1.04")
        entry_cena_30.grid(row=20, column=6)
    elif nazwa_30.get() == "Triathlon elem. udowy lewy":
        entry_cena_30 = Entry(root, textvariable=cena_30, justify=CENTER, width=14)
        entry_cena_30.insert(0, "3132")
        entry_cena_30.grid(row=20, column=6)
    elif nazwa_30.get() == "Triathlon PS wkładka x3-9mm #4":
        entry_cena_30 = Entry(root, textvariable=cena_30, justify=CENTER, width=14)
        entry_cena_30.insert(0, "756")
        entry_cena_30.grid(row=20, column=6)
    elif nazwa_30.get() == "Triathlon taca piszczelowa":
        entry_cena_30 = Entry(root, textvariable=cena_30, justify=CENTER, width=14)
        entry_cena_30.insert(0, "1296")
        entry_cena_30.grid(row=20, column=6)
    elif nazwa_30.get() == "Wkłady 3L z żelem":
        entry_cena_30 = Entry(root, textvariable=cena_30, justify=CENTER, width=14)
        entry_cena_30.insert(0, "10.26")
        entry_cena_30.grid(row=20, column=6)
    elif nazwa_30.get() == "Zestaw do artroskopii":
        entry_cena_30 = Entry(root, textvariable=cena_30, justify=CENTER, width=14)
        entry_cena_30.insert(0, "67")
        entry_cena_30.grid(row=20, column=6)
    elif nazwa_30.get() == "Zestaw do artroskopii barku":
        entry_cena_30 = Entry(root, textvariable=cena_30, justify=CENTER, width=14)
        entry_cena_30.insert(0, "108")
        entry_cena_30.grid(row=20, column=6)
    elif nazwa_30.get() == "Zestaw do drenażu":
        entry_cena_30 = Entry(root, textvariable=cena_30, justify=CENTER, width=14)
        entry_cena_30.insert(0, "14.23")
        entry_cena_30.grid(row=20, column=6)
    elif nazwa_30.get() == "Zestaw ortopedyczny":
        entry_cena_30 = Entry(root, textvariable=cena_30, justify=CENTER, width=14)
        entry_cena_30.insert(0, "28.08")
        entry_cena_30.grid(row=20, column=6)
    elif nazwa_30.get() == "Gaziki 20 x 10cm":
        entry_cena_30 = Entry(root, textvariable=cena_30, justify=CENTER, width=14)
        entry_cena_30.insert(0, "0.46")
        entry_cena_30.grid(row=20, column=6)
    else:
        entry_cena_30 = Entry(root, textvariable=cena_30, justify=CENTER, width=14, bg="#ffff00")
        entry_cena_30.insert(0, "0")
        entry_cena_30.grid(row=20, column=6)

    if nazwa_31.get() == "--puste--":
        entry_cena_31 = Entry(root, textvariable=cena_31, justify=CENTER, width=14)
        entry_cena_31.insert(0, "0")
        entry_cena_31.grid(row=21, column=6)
    elif nazwa_31.get() == "Ablator":
        entry_cena_31 = Entry(root, textvariable=cena_31, justify=CENTER, width=14)
        entry_cena_31.insert(0, "572")
        entry_cena_31.grid(row=21, column=6)
    elif nazwa_31.get() == "Anestezjolog":
        entry_cena_31 = Entry(root, textvariable=cena_31, justify=CENTER, width=14, bg="#ffff00")
        entry_cena_31.insert(0, "350")
        entry_cena_31.grid(row=21, column=6)
    elif nazwa_31.get() == "Butelka 400ml do długotrwałego odsysania ran j.u. sterylna":
        entry_cena_31 = Entry(root, textvariable=cena_31, justify=CENTER, width=14)
        entry_cena_31.insert(0, "4")
        entry_cena_31.grid(row=21, column=6)
    elif nazwa_31.get() == "Doba":
        entry_cena_31 = Entry(root, textvariable=cena_31, justify=CENTER, width=14)
        entry_cena_31.insert(0, "700")
        entry_cena_31.grid(row=21, column=6)
    elif nazwa_31.get() == "Dren łączący do ssaka Grena":
        entry_cena_31 = Entry(root, textvariable=cena_31, justify=CENTER, width=14)
        entry_cena_31.insert(0, "5")
        entry_cena_31.grid(row=21, column=6)
    elif nazwa_31.get() == "Dren Redona Ch 16 dł. 800mm z trokarem":
        entry_cena_31 = Entry(root, textvariable=cena_31, justify=CENTER, width=14)
        entry_cena_31.insert(0, "29.74")
        entry_cena_31.grid(row=21, column=6)
    elif nazwa_31.get() == "Dren do pompy Artrex":
        entry_cena_31 = Entry(root, textvariable=cena_31, justify=CENTER, width=14)
        entry_cena_31.insert(0, "108")
        entry_cena_31.grid(row=21, column=6)
    elif nazwa_31.get() == "Drut wiercący 2,4 x 311":
        entry_cena_31 = Entry(root, textvariable=cena_31, justify=CENTER, width=14)
        entry_cena_31.insert(0, "139.60")
        entry_cena_31.grid(row=21, column=6)
    elif nazwa_31.get() == "Fartuch jałowy L":
        entry_cena_31 = Entry(root, textvariable=cena_31, justify=CENTER, width=14)
        entry_cena_31.insert(0, "17")
        entry_cena_31.grid(row=21, column=6)
    elif nazwa_31.get() == "Fartuch jałowy M":
        entry_cena_31 = Entry(root, textvariable=cena_31, justify=CENTER, width=14)
        entry_cena_31.insert(0, "15.28")
        entry_cena_31.grid(row=21, column=6)
    elif nazwa_31.get() == "Fartuch jałowy XL":
        entry_cena_31 = Entry(root, textvariable=cena_31, justify=CENTER, width=14)
        entry_cena_31.insert(0, "20.84")
        entry_cena_31.grid(row=21, column=6)
    elif nazwa_31.get() == "FasatThread BioComposite Interference Screw 8x30":
        entry_cena_31 = Entry(root, textvariable=cena_31, justify=CENTER, width=14)
        entry_cena_31.insert(0, "594")
        entry_cena_31.grid(row=21, column=6)
    elif nazwa_31.get() == "Folia operacyjna, jałowa 45cm x 55cm":
        entry_cena_31 = Entry(root, textvariable=cena_31, justify=CENTER, width=14)
        entry_cena_31.insert(0, "9.99")
        entry_cena_31.grid(row=21, column=6)
    elif nazwa_31.get() == "Gaziki 10 x 10cm":
        entry_cena_31 = Entry(root, textvariable=cena_31, justify=CENTER, width=14)
        entry_cena_31.insert(0, "0.10")
        entry_cena_31.grid(row=21, column=6)
    elif nazwa_31.get() == "Igła 0,6 x 60":
        entry_cena_31 = Entry(root, textvariable=cena_31, justify=CENTER, width=14)
        entry_cena_31.insert(0, "0.09")
        entry_cena_31.grid(row=21, column=6)
    elif nazwa_31.get() == "Igła 0,7 x 40":
        entry_cena_31 = Entry(root, textvariable=cena_31, justify=CENTER, width=14)
        entry_cena_31.insert(0, "0.05")
        entry_cena_31.grid(row=21, column=6)
    elif nazwa_31.get() == "Igła 0,8 x 40":
        entry_cena_31 = Entry(root, textvariable=cena_31, justify=CENTER, width=14)
        entry_cena_31.insert(0, "0.05")
        entry_cena_31.grid(row=21, column=6)
    elif nazwa_31.get() == "Igła 1,1 x 70":
        entry_cena_31 = Entry(root, textvariable=cena_31, justify=CENTER, width=14)
        entry_cena_31.insert(0, "0.16")
        entry_cena_31.grid(row=21, column=6)
    elif nazwa_31.get() == "Kaniulowana śruba int. biokompozytowa z osłonką jednoraz.":
        entry_cena_31 = Entry(root, textvariable=cena_31, justify=CENTER, width=14)
        entry_cena_31.insert(0, "594")
        entry_cena_31.grid(row=21, column=6)
    elif nazwa_31.get() == "Kaniulowana śruba int. biokompozytowa z pełnym gwintem":
        entry_cena_31 = Entry(root, textvariable=cena_31, justify=CENTER, width=14)
        entry_cena_31.insert(0, "594")
        entry_cena_31.grid(row=21, column=6)
    elif nazwa_31.get() == "Końcówka do Shavera":
        entry_cena_31 = Entry(root, textvariable=cena_31, justify=CENTER, width=14)
        entry_cena_31.insert(0, "270")
        entry_cena_31.grid(row=21, column=6)
    elif nazwa_31.get() == "Kotwica biokompozytowa SwiveLock":
        entry_cena_31 = Entry(root, textvariable=cena_31, justify=CENTER, width=14)
        entry_cena_31.insert(0, "918")
        entry_cena_31.grid(row=21, column=6)
    elif nazwa_31.get() == "Kotwica Corkscrew":
        entry_cena_31 = Entry(root, textvariable=cena_31, justify=CENTER, width=14)
        entry_cena_31.insert(0, "604")
        entry_cena_31.grid(row=21, column=6)
    elif nazwa_31.get() == "Kotwica FASTak":
        entry_cena_31 = Entry(root, textvariable=cena_31, justify=CENTER, width=14)
        entry_cena_31.insert(0, "432")
        entry_cena_31.grid(row=21, column=6)
    elif nazwa_31.get() == "Kotwica PEEK SwiveLock":
        entry_cena_31 = Entry(root, textvariable=cena_31, justify=CENTER, width=14)
        entry_cena_31.insert(0, "885.60")
        entry_cena_31.grid(row=21, column=6)
    elif nazwa_31.get() == "NaCl 3000ml":
        entry_cena_31 = Entry(root, textvariable=cena_31, justify=CENTER, width=14)
        entry_cena_31.insert(0, "29.72")
        entry_cena_31.grid(row=21, column=6)
    elif nazwa_31.get() == "NaCl 5000ml":
        entry_cena_31 = Entry(root, textvariable=cena_31, justify=CENTER, width=14)
        entry_cena_31.insert(0, "58.33")
        entry_cena_31.grid(row=21, column=6)
    elif nazwa_31.get() == "Nici Dafilon 2-0":
        entry_cena_31 = Entry(root, textvariable=cena_31, justify=CENTER, width=14)
        entry_cena_31.insert(0, "6.60")
        entry_cena_31.grid(row=21, column=6)
    elif nazwa_31.get() == "Nici Novosyn 2":
        entry_cena_31 = Entry(root, textvariable=cena_31, justify=CENTER, width=14)
        entry_cena_31.insert(0, "13")
        entry_cena_31.grid(row=21, column=6)
    elif nazwa_31.get() == "Nici Novosyn 2-0":
        entry_cena_31 = Entry(root, textvariable=cena_31, justify=CENTER, width=14)
        entry_cena_31.insert(0, "7.70")
        entry_cena_31.grid(row=21, column=6)
    elif nazwa_31.get() == "Nici Novosyn 3-0":
        entry_cena_31 = Entry(root, textvariable=cena_31, justify=CENTER, width=14)
        entry_cena_31.insert(0, "7.70")
        entry_cena_31.grid(row=21, column=6)
    elif nazwa_31.get() == "Nici Nylon 2-0":
        entry_cena_31 = Entry(root, textvariable=cena_31, justify=CENTER, width=14)
        entry_cena_31.insert(0, "2.50")
        entry_cena_31.grid(row=21, column=6)
    elif nazwa_31.get() == "Nici Nylon 3-0":
        entry_cena_31 = Entry(root, textvariable=cena_31, justify=CENTER, width=14)
        entry_cena_31.insert(0, "2")
        entry_cena_31.grid(row=21, column=6)
    elif nazwa_31.get() == "Nici PGLA":
        entry_cena_31 = Entry(root, textvariable=cena_31, justify=CENTER, width=14)
        entry_cena_31.insert(0, "11.60")
        entry_cena_31.grid(row=21, column=6)
    elif nazwa_31.get() == "Nici PremiCron 3":
        entry_cena_31 = Entry(root, textvariable=cena_31, justify=CENTER, width=14)
        entry_cena_31.insert(0, "6.50")
        entry_cena_31.grid(row=21, column=6)
    elif nazwa_31.get() == "Nici Vicryl 4-0":
        entry_cena_31 = Entry(root, textvariable=cena_31, justify=CENTER, width=14)
        entry_cena_31.insert(0, "7.50")
        entry_cena_31.grid(row=21, column=6)
    elif nazwa_31.get() == "Nitinol Guide Pin 1.1":
        entry_cena_31 = Entry(root, textvariable=cena_31, justify=CENTER, width=14)
        entry_cena_31.insert(0, "145.80")
        entry_cena_31.grid(row=21, column=6)
    elif nazwa_31.get() == "Osłona na przewody":
        entry_cena_31 = Entry(root, textvariable=cena_31, justify=CENTER, width=14)
        entry_cena_31.insert(0, "2.50")
        entry_cena_31.grid(row=21, column=6)
    elif nazwa_31.get() == "Ostrze Arthrex 90(86)x19x1,27":
        entry_cena_31 = Entry(root, textvariable=cena_31, justify=CENTER, width=14)
        entry_cena_31.insert(0, "216")
        entry_cena_31.grid(row=21, column=6)
    elif nazwa_31.get() == "Ostrze piły":
        entry_cena_31 = Entry(root, textvariable=cena_31, justify=CENTER, width=14)
        entry_cena_31.insert(0, "108")
        entry_cena_31.grid(row=21, column=6)
    elif nazwa_31.get() == "Pielęgniarka anest.":
        entry_cena_31 = Entry(root, textvariable=cena_31, justify=CENTER, width=14)
        entry_cena_31.insert(0, "50")
        entry_cena_31.grid(row=21, column=6)
    elif nazwa_31.get() == "Pielęgniarka instr.":
        entry_cena_31 = Entry(root, textvariable=cena_31, justify=CENTER, width=14)
        entry_cena_31.insert(0, "50")
        entry_cena_31.grid(row=21, column=6)
    elif nazwa_31.get() == "Pielęgniarka 'Noviline'":
        entry_cena_31 = Entry(root, textvariable=cena_31, justify=CENTER, width=14)
        entry_cena_31.insert(0, "30")
        entry_cena_31.grid(row=21, column=6)
    elif nazwa_31.get() == "Płytka PeekPower do osteotomii klinowej":
        entry_cena_31 = Entry(root, textvariable=cena_31, justify=CENTER, width=14)
        entry_cena_31.insert(0, "2160")
        entry_cena_31.grid(row=21, column=6)
    elif nazwa_31.get() == "Rękawice jałowe 6,5":
        entry_cena_31 = Entry(root, textvariable=cena_31, justify=CENTER, width=14)
        entry_cena_31.insert(0, "1.20")
        entry_cena_31.grid(row=21, column=6)
    elif nazwa_31.get() == "Rękawice jałowe 7,0":
        entry_cena_31 = Entry(root, textvariable=cena_31, justify=CENTER, width=14)
        entry_cena_31.insert(0, "1.20")
        entry_cena_31.grid(row=21, column=6)
    elif nazwa_31.get() == "Rękawice jałowe 7,5":
        entry_cena_31 = Entry(root, textvariable=cena_31, justify=CENTER, width=14)
        entry_cena_31.insert(0, "1.20")
        entry_cena_31.grid(row=21, column=6)
    elif nazwa_31.get() == "Rękawice jałowe 8,00":
        entry_cena_31 = Entry(root, textvariable=cena_31, justify=CENTER, width=14)
        entry_cena_31.insert(0, "1.20")
        entry_cena_31.grid(row=21, column=6)
    elif nazwa_31.get() == "Rękojeść Interpulse wysokoprzepływowa":
        entry_cena_31 = Entry(root, textvariable=cena_31, justify=CENTER, width=14)
        entry_cena_31.insert(0, "216")
        entry_cena_31.grid(row=21, column=6)
    elif nazwa_31.get() == "Serweta":
        entry_cena_31 = Entry(root, textvariable=cena_31, justify=CENTER, width=14)
        entry_cena_31.insert(0, "6")
        entry_cena_31.grid(row=21, column=6)
    elif nazwa_31.get() == "Simplex Hv z Gentamycyna 10x40g":
        entry_cena_31 = Entry(root, textvariable=cena_31, justify=CENTER, width=14)
        entry_cena_31.insert(0, "162")
        entry_cena_31.grid(row=21, column=6)
    elif nazwa_31.get() == "Skalpel 11":
        entry_cena_31 = Entry(root, textvariable=cena_31, justify=CENTER, width=14)
        entry_cena_31.insert(0, "0.38")
        entry_cena_31.grid(row=21, column=6)
    elif nazwa_31.get() == "Skalpel 13":
        entry_cena_31 = Entry(root, textvariable=cena_31, justify=CENTER, width=14)
        entry_cena_31.insert(0, "1")
        entry_cena_31.grid(row=21, column=6)
    elif nazwa_31.get() == "Skalpel 22":
        entry_cena_31 = Entry(root, textvariable=cena_31, justify=CENTER, width=14)
        entry_cena_31.insert(0, "1")
        entry_cena_31.grid(row=21, column=6)
    elif nazwa_31.get() == "Śruba blokująca PeekPower do osteotomii":
        entry_cena_31 = Entry(root, textvariable=cena_31, justify=CENTER, width=14)
        entry_cena_31.insert(0, "194")
        entry_cena_31.grid(row=21, column=6)
    elif nazwa_31.get() == "System do mieszania próżniowego":
        entry_cena_31 = Entry(root, textvariable=cena_31, justify=CENTER, width=14)
        entry_cena_31.insert(0, "216")
        entry_cena_31.grid(row=21, column=6)
    elif nazwa_31.get() == "System wprowadzania implantów ACL TightRope":
        entry_cena_31 = Entry(root, textvariable=cena_31, justify=CENTER, width=14)
        entry_cena_31.insert(0, "702")
        entry_cena_31.grid(row=21, column=6)
    elif nazwa_31.get() == "Szew FiberWire 2":
        entry_cena_31 = Entry(root, textvariable=cena_31, justify=CENTER, width=14)
        entry_cena_31.insert(0, "86.40")
        entry_cena_31.grid(row=21, column=6)
    elif nazwa_31.get() == "Taśma przylepna 10x50":
        entry_cena_31 = Entry(root, textvariable=cena_31, justify=CENTER, width=14)
        entry_cena_31.insert(0, "1.04")
        entry_cena_31.grid(row=21, column=6)
    elif nazwa_31.get() == "Triathlon elem. udowy lewy":
        entry_cena_31 = Entry(root, textvariable=cena_31, justify=CENTER, width=14)
        entry_cena_31.insert(0, "3132")
        entry_cena_31.grid(row=21, column=6)
    elif nazwa_31.get() == "Triathlon PS wkładka x3-9mm #4":
        entry_cena_31 = Entry(root, textvariable=cena_31, justify=CENTER, width=14)
        entry_cena_31.insert(0, "756")
        entry_cena_31.grid(row=21, column=6)
    elif nazwa_31.get() == "Triathlon taca piszczelowa":
        entry_cena_31 = Entry(root, textvariable=cena_31, justify=CENTER, width=14)
        entry_cena_31.insert(0, "1296")
        entry_cena_31.grid(row=21, column=6)
    elif nazwa_31.get() == "Wkłady 3L z żelem":
        entry_cena_31 = Entry(root, textvariable=cena_31, justify=CENTER, width=14)
        entry_cena_31.insert(0, "10.26")
        entry_cena_31.grid(row=21, column=6)
    elif nazwa_31.get() == "Zestaw do artroskopii":
        entry_cena_31 = Entry(root, textvariable=cena_31, justify=CENTER, width=14)
        entry_cena_31.insert(0, "67")
        entry_cena_31.grid(row=21, column=6)
    elif nazwa_31.get() == "Zestaw do artroskopii barku":
        entry_cena_31 = Entry(root, textvariable=cena_31, justify=CENTER, width=14)
        entry_cena_31.insert(0, "108")
        entry_cena_31.grid(row=21, column=6)
    elif nazwa_31.get() == "Zestaw do drenażu":
        entry_cena_31 = Entry(root, textvariable=cena_31, justify=CENTER, width=14)
        entry_cena_31.insert(0, "14.23")
        entry_cena_31.grid(row=21, column=6)
    elif nazwa_31.get() == "Zestaw ortopedyczny":
        entry_cena_31 = Entry(root, textvariable=cena_31, justify=CENTER, width=14)
        entry_cena_31.insert(0, "28.08")
        entry_cena_31.grid(row=21, column=6)
    elif nazwa_31.get() == "Gaziki 20 x 10cm":
        entry_cena_31 = Entry(root, textvariable=cena_31, justify=CENTER, width=14)
        entry_cena_31.insert(0, "0.46")
        entry_cena_31.grid(row=21, column=6)
    else:
        entry_cena_31 = Entry(root, textvariable=cena_31, justify=CENTER, width=14, bg="#ffff00")
        entry_cena_31.insert(0, "0")
        entry_cena_31.grid(row=21, column=6)

    if nazwa_32.get() == "--puste--":
        entry_cena_32 = Entry(root, textvariable=cena_32, justify=CENTER, width=14)
        entry_cena_32.insert(0, "0")
        entry_cena_32.grid(row=22, column=6)
    elif nazwa_32.get() == "Ablator":
        entry_cena_32 = Entry(root, textvariable=cena_32, justify=CENTER, width=14)
        entry_cena_32.insert(0, "572")
        entry_cena_32.grid(row=22, column=6)
    elif nazwa_32.get() == "Anestezjolog":
        entry_cena_32 = Entry(root, textvariable=cena_32, justify=CENTER, width=14, bg="#ffff00")
        entry_cena_32.insert(0, "350")
        entry_cena_32.grid(row=22, column=6)
    elif nazwa_32.get() == "Butelka 400ml do długotrwałego odsysania ran j.u. sterylna":
        entry_cena_32 = Entry(root, textvariable=cena_32, justify=CENTER, width=14)
        entry_cena_32.insert(0, "4")
        entry_cena_32.grid(row=22, column=6)
    elif nazwa_32.get() == "Doba":
        entry_cena_32 = Entry(root, textvariable=cena_32, justify=CENTER, width=14)
        entry_cena_32.insert(0, "700")
        entry_cena_32.grid(row=22, column=6)
    elif nazwa_32.get() == "Dren łączący do ssaka Grena":
        entry_cena_32 = Entry(root, textvariable=cena_32, justify=CENTER, width=14)
        entry_cena_32.insert(0, "5")
        entry_cena_32.grid(row=22, column=6)
    elif nazwa_32.get() == "Dren Redona Ch 16 dł. 800mm z trokarem":
        entry_cena_32 = Entry(root, textvariable=cena_32, justify=CENTER, width=14)
        entry_cena_32.insert(0, "29.74")
        entry_cena_32.grid(row=22, column=6)
    elif nazwa_32.get() == "Dren do pompy Artrex":
        entry_cena_32 = Entry(root, textvariable=cena_32, justify=CENTER, width=14)
        entry_cena_32.insert(0, "108")
        entry_cena_32.grid(row=22, column=6)
    elif nazwa_32.get() == "Drut wiercący 2,4 x 311":
        entry_cena_32 = Entry(root, textvariable=cena_32, justify=CENTER, width=14)
        entry_cena_32.insert(0, "139.60")
        entry_cena_32.grid(row=22, column=6)
    elif nazwa_32.get() == "Fartuch jałowy L":
        entry_cena_32 = Entry(root, textvariable=cena_32, justify=CENTER, width=14)
        entry_cena_32.insert(0, "17")
        entry_cena_32.grid(row=22, column=6)
    elif nazwa_32.get() == "Fartuch jałowy M":
        entry_cena_32 = Entry(root, textvariable=cena_32, justify=CENTER, width=14)
        entry_cena_32.insert(0, "15.28")
        entry_cena_32.grid(row=22, column=6)
    elif nazwa_32.get() == "Fartuch jałowy XL":
        entry_cena_32 = Entry(root, textvariable=cena_32, justify=CENTER, width=14)
        entry_cena_32.insert(0, "20.84")
        entry_cena_32.grid(row=22, column=6)
    elif nazwa_32.get() == "FasatThread BioComposite Interference Screw 8x30":
        entry_cena_32 = Entry(root, textvariable=cena_32, justify=CENTER, width=14)
        entry_cena_32.insert(0, "594")
        entry_cena_32.grid(row=22, column=6)
    elif nazwa_32.get() == "Folia operacyjna, jałowa 45cm x 55cm":
        entry_cena_32 = Entry(root, textvariable=cena_32, justify=CENTER, width=14)
        entry_cena_32.insert(0, "9.99")
        entry_cena_32.grid(row=22, column=6)
    elif nazwa_32.get() == "Gaziki 10 x 10cm":
        entry_cena_32 = Entry(root, textvariable=cena_32, justify=CENTER, width=14)
        entry_cena_32.insert(0, "0.10")
        entry_cena_32.grid(row=22, column=6)
    elif nazwa_32.get() == "Igła 0,6 x 60":
        entry_cena_32 = Entry(root, textvariable=cena_32, justify=CENTER, width=14)
        entry_cena_32.insert(0, "0.09")
        entry_cena_32.grid(row=22, column=6)
    elif nazwa_32.get() == "Igła 0,7 x 40":
        entry_cena_32 = Entry(root, textvariable=cena_32, justify=CENTER, width=14)
        entry_cena_32.insert(0, "0.05")
        entry_cena_32.grid(row=22, column=6)
    elif nazwa_32.get() == "Igła 0,8 x 40":
        entry_cena_32 = Entry(root, textvariable=cena_32, justify=CENTER, width=14)
        entry_cena_32.insert(0, "0.05")
        entry_cena_32.grid(row=22, column=6)
    elif nazwa_32.get() == "Igła 1,1 x 70":
        entry_cena_32 = Entry(root, textvariable=cena_32, justify=CENTER, width=14)
        entry_cena_32.insert(0, "0.16")
        entry_cena_32.grid(row=22, column=6)
    elif nazwa_32.get() == "Kaniulowana śruba int. biokompozytowa z osłonką jednoraz.":
        entry_cena_32 = Entry(root, textvariable=cena_32, justify=CENTER, width=14)
        entry_cena_32.insert(0, "594")
        entry_cena_32.grid(row=22, column=6)
    elif nazwa_32.get() == "Kaniulowana śruba int. biokompozytowa z pełnym gwintem":
        entry_cena_32 = Entry(root, textvariable=cena_32, justify=CENTER, width=14)
        entry_cena_32.insert(0, "594")
        entry_cena_32.grid(row=22, column=6)
    elif nazwa_32.get() == "Końcówka do Shavera":
        entry_cena_32 = Entry(root, textvariable=cena_32, justify=CENTER, width=14)
        entry_cena_32.insert(0, "270")
        entry_cena_32.grid(row=22, column=6)
    elif nazwa_32.get() == "Kotwica biokompozytowa SwiveLock":
        entry_cena_32 = Entry(root, textvariable=cena_32, justify=CENTER, width=14)
        entry_cena_32.insert(0, "918")
        entry_cena_32.grid(row=22, column=6)
    elif nazwa_32.get() == "Kotwica Corkscrew":
        entry_cena_32 = Entry(root, textvariable=cena_32, justify=CENTER, width=14)
        entry_cena_32.insert(0, "604")
        entry_cena_32.grid(row=22, column=6)
    elif nazwa_32.get() == "Kotwica FASTak":
        entry_cena_32 = Entry(root, textvariable=cena_32, justify=CENTER, width=14)
        entry_cena_32.insert(0, "432")
        entry_cena_32.grid(row=22, column=6)
    elif nazwa_32.get() == "Kotwica PEEK SwiveLock":
        entry_cena_32 = Entry(root, textvariable=cena_32, justify=CENTER, width=14)
        entry_cena_32.insert(0, "885.60")
        entry_cena_32.grid(row=22, column=6)
    elif nazwa_32.get() == "NaCl 3000ml":
        entry_cena_32 = Entry(root, textvariable=cena_32, justify=CENTER, width=14)
        entry_cena_32.insert(0, "29.72")
        entry_cena_32.grid(row=22, column=6)
    elif nazwa_32.get() == "NaCl 5000ml":
        entry_cena_32 = Entry(root, textvariable=cena_32, justify=CENTER, width=14)
        entry_cena_32.insert(0, "58.33")
        entry_cena_32.grid(row=22, column=6)
    elif nazwa_32.get() == "Nici Dafilon 2-0":
        entry_cena_32 = Entry(root, textvariable=cena_32, justify=CENTER, width=14)
        entry_cena_32.insert(0, "6.60")
        entry_cena_32.grid(row=22, column=6)
    elif nazwa_32.get() == "Nici Novosyn 2":
        entry_cena_32 = Entry(root, textvariable=cena_32, justify=CENTER, width=14)
        entry_cena_32.insert(0, "13")
        entry_cena_32.grid(row=22, column=6)
    elif nazwa_32.get() == "Nici Novosyn 2-0":
        entry_cena_32 = Entry(root, textvariable=cena_32, justify=CENTER, width=14)
        entry_cena_32.insert(0, "7.70")
        entry_cena_32.grid(row=22, column=6)
    elif nazwa_32.get() == "Nici Novosyn 3-0":
        entry_cena_32 = Entry(root, textvariable=cena_32, justify=CENTER, width=14)
        entry_cena_32.insert(0, "7.70")
        entry_cena_32.grid(row=22, column=6)
    elif nazwa_32.get() == "Nici Nylon 2-0":
        entry_cena_32 = Entry(root, textvariable=cena_32, justify=CENTER, width=14)
        entry_cena_32.insert(0, "2.50")
        entry_cena_32.grid(row=22, column=6)
    elif nazwa_32.get() == "Nici Nylon 3-0":
        entry_cena_32 = Entry(root, textvariable=cena_32, justify=CENTER, width=14)
        entry_cena_32.insert(0, "2")
        entry_cena_32.grid(row=22, column=6)
    elif nazwa_32.get() == "Nici PGLA":
        entry_cena_32 = Entry(root, textvariable=cena_32, justify=CENTER, width=14)
        entry_cena_32.insert(0, "11.60")
        entry_cena_32.grid(row=22, column=6)
    elif nazwa_32.get() == "Nici PremiCron 3":
        entry_cena_32 = Entry(root, textvariable=cena_32, justify=CENTER, width=14)
        entry_cena_32.insert(0, "6.50")
        entry_cena_32.grid(row=22, column=6)
    elif nazwa_32.get() == "Nici Vicryl 4-0":
        entry_cena_32 = Entry(root, textvariable=cena_32, justify=CENTER, width=14)
        entry_cena_32.insert(0, "7.50")
        entry_cena_32.grid(row=22, column=6)
    elif nazwa_32.get() == "Nitinol Guide Pin 1.1":
        entry_cena_32 = Entry(root, textvariable=cena_32, justify=CENTER, width=14)
        entry_cena_32.insert(0, "145.80")
        entry_cena_32.grid(row=22, column=6)
    elif nazwa_32.get() == "Osłona na przewody":
        entry_cena_32 = Entry(root, textvariable=cena_32, justify=CENTER, width=14)
        entry_cena_32.insert(0, "2.50")
        entry_cena_32.grid(row=22, column=6)
    elif nazwa_32.get() == "Ostrze Arthrex 90(86)x19x1,27":
        entry_cena_32 = Entry(root, textvariable=cena_32, justify=CENTER, width=14)
        entry_cena_32.insert(0, "216")
        entry_cena_32.grid(row=22, column=6)
    elif nazwa_32.get() == "Ostrze piły":
        entry_cena_32 = Entry(root, textvariable=cena_32, justify=CENTER, width=14)
        entry_cena_32.insert(0, "108")
        entry_cena_32.grid(row=22, column=6)
    elif nazwa_32.get() == "Pielęgniarka anest.":
        entry_cena_32 = Entry(root, textvariable=cena_32, justify=CENTER, width=14)
        entry_cena_32.insert(0, "50")
        entry_cena_32.grid(row=22, column=6)
    elif nazwa_32.get() == "Pielęgniarka instr.":
        entry_cena_32 = Entry(root, textvariable=cena_32, justify=CENTER, width=14)
        entry_cena_32.insert(0, "50")
        entry_cena_32.grid(row=22, column=6)
    elif nazwa_32.get() == "Pielęgniarka 'Noviline'":
        entry_cena_32 = Entry(root, textvariable=cena_32, justify=CENTER, width=14)
        entry_cena_32.insert(0, "30")
        entry_cena_32.grid(row=22, column=6)
    elif nazwa_32.get() == "Płytka PeekPower do osteotomii klinowej":
        entry_cena_32 = Entry(root, textvariable=cena_32, justify=CENTER, width=14)
        entry_cena_32.insert(0, "2160")
        entry_cena_32.grid(row=22, column=6)
    elif nazwa_32.get() == "Rękawice jałowe 6,5":
        entry_cena_32 = Entry(root, textvariable=cena_32, justify=CENTER, width=14)
        entry_cena_32.insert(0, "1.20")
        entry_cena_32.grid(row=22, column=6)
    elif nazwa_32.get() == "Rękawice jałowe 7,0":
        entry_cena_32 = Entry(root, textvariable=cena_32, justify=CENTER, width=14)
        entry_cena_32.insert(0, "1.20")
        entry_cena_32.grid(row=22, column=6)
    elif nazwa_32.get() == "Rękawice jałowe 7,5":
        entry_cena_32 = Entry(root, textvariable=cena_32, justify=CENTER, width=14)
        entry_cena_32.insert(0, "1.20")
        entry_cena_32.grid(row=22, column=6)
    elif nazwa_32.get() == "Rękawice jałowe 8,00":
        entry_cena_32 = Entry(root, textvariable=cena_32, justify=CENTER, width=14)
        entry_cena_32.insert(0, "1.20")
        entry_cena_32.grid(row=22, column=6)
    elif nazwa_32.get() == "Rękojeść Interpulse wysokoprzepływowa":
        entry_cena_32 = Entry(root, textvariable=cena_32, justify=CENTER, width=14)
        entry_cena_32.insert(0, "216")
        entry_cena_32.grid(row=22, column=6)
    elif nazwa_32.get() == "Serweta":
        entry_cena_32 = Entry(root, textvariable=cena_32, justify=CENTER, width=14)
        entry_cena_32.insert(0, "6")
        entry_cena_32.grid(row=22, column=6)
    elif nazwa_32.get() == "Simplex Hv z Gentamycyna 10x40g":
        entry_cena_32 = Entry(root, textvariable=cena_32, justify=CENTER, width=14)
        entry_cena_32.insert(0, "162")
        entry_cena_32.grid(row=22, column=6)
    elif nazwa_32.get() == "Skalpel 11":
        entry_cena_32 = Entry(root, textvariable=cena_32, justify=CENTER, width=14)
        entry_cena_32.insert(0, "0.38")
        entry_cena_32.grid(row=22, column=6)
    elif nazwa_32.get() == "Skalpel 13":
        entry_cena_32 = Entry(root, textvariable=cena_32, justify=CENTER, width=14)
        entry_cena_32.insert(0, "1")
        entry_cena_32.grid(row=22, column=6)
    elif nazwa_32.get() == "Skalpel 22":
        entry_cena_32 = Entry(root, textvariable=cena_32, justify=CENTER, width=14)
        entry_cena_32.insert(0, "1")
        entry_cena_32.grid(row=22, column=6)
    elif nazwa_32.get() == "Śruba blokująca PeekPower do osteotomii":
        entry_cena_32 = Entry(root, textvariable=cena_32, justify=CENTER, width=14)
        entry_cena_32.insert(0, "194")
        entry_cena_32.grid(row=22, column=6)
    elif nazwa_32.get() == "System do mieszania próżniowego":
        entry_cena_32 = Entry(root, textvariable=cena_32, justify=CENTER, width=14)
        entry_cena_32.insert(0, "216")
        entry_cena_32.grid(row=22, column=6)
    elif nazwa_32.get() == "System wprowadzania implantów ACL TightRope":
        entry_cena_32 = Entry(root, textvariable=cena_32, justify=CENTER, width=14)
        entry_cena_32.insert(0, "702")
        entry_cena_32.grid(row=22, column=6)
    elif nazwa_32.get() == "Szew FiberWire 2":
        entry_cena_32 = Entry(root, textvariable=cena_32, justify=CENTER, width=14)
        entry_cena_32.insert(0, "86.40")
        entry_cena_32.grid(row=22, column=6)
    elif nazwa_32.get() == "Taśma przylepna 10x50":
        entry_cena_32 = Entry(root, textvariable=cena_32, justify=CENTER, width=14)
        entry_cena_32.insert(0, "1.04")
        entry_cena_32.grid(row=22, column=6)
    elif nazwa_32.get() == "Triathlon elem. udowy lewy":
        entry_cena_32 = Entry(root, textvariable=cena_32, justify=CENTER, width=14)
        entry_cena_32.insert(0, "3132")
        entry_cena_32.grid(row=22, column=6)
    elif nazwa_32.get() == "Triathlon PS wkładka x3-9mm #4":
        entry_cena_32 = Entry(root, textvariable=cena_32, justify=CENTER, width=14)
        entry_cena_32.insert(0, "756")
        entry_cena_32.grid(row=22, column=6)
    elif nazwa_32.get() == "Triathlon taca piszczelowa":
        entry_cena_32 = Entry(root, textvariable=cena_32, justify=CENTER, width=14)
        entry_cena_32.insert(0, "1296")
        entry_cena_32.grid(row=22, column=6)
    elif nazwa_32.get() == "Wkłady 3L z żelem":
        entry_cena_32 = Entry(root, textvariable=cena_32, justify=CENTER, width=14)
        entry_cena_32.insert(0, "10.26")
        entry_cena_32.grid(row=22, column=6)
    elif nazwa_32.get() == "Zestaw do artroskopii":
        entry_cena_32 = Entry(root, textvariable=cena_32, justify=CENTER, width=14)
        entry_cena_32.insert(0, "67")
        entry_cena_32.grid(row=22, column=6)
    elif nazwa_32.get() == "Zestaw do artroskopii barku":
        entry_cena_32 = Entry(root, textvariable=cena_32, justify=CENTER, width=14)
        entry_cena_32.insert(0, "108")
        entry_cena_32.grid(row=22, column=6)
    elif nazwa_32.get() == "Zestaw do drenażu":
        entry_cena_32 = Entry(root, textvariable=cena_32, justify=CENTER, width=14)
        entry_cena_32.insert(0, "14.23")
        entry_cena_32.grid(row=22, column=6)
    elif nazwa_32.get() == "Zestaw ortopedyczny":
        entry_cena_32 = Entry(root, textvariable=cena_32, justify=CENTER, width=14)
        entry_cena_32.insert(0, "28.08")
        entry_cena_32.grid(row=22, column=6)
    elif nazwa_32.get() == "Gaziki 20 x 10cm":
        entry_cena_32 = Entry(root, textvariable=cena_32, justify=CENTER, width=14)
        entry_cena_32.insert(0, "0.46")
        entry_cena_32.grid(row=22, column=6)
    else:
        entry_cena_32 = Entry(root, textvariable=cena_32, justify=CENTER, width=14, bg="#ffff00")
        entry_cena_32.insert(0, "0")
        entry_cena_32.grid(row=22, column=6)

    if nazwa_33.get() == "--puste--":
        entry_cena_33 = Entry(root, textvariable=cena_33, justify=CENTER, width=14)
        entry_cena_33.insert(0, "0")
        entry_cena_33.grid(row=23, column=6)
    elif nazwa_33.get() == "Ablator":
        entry_cena_33 = Entry(root, textvariable=cena_33, justify=CENTER, width=14)
        entry_cena_33.insert(0, "572")
        entry_cena_33.grid(row=23, column=6)
    elif nazwa_33.get() == "Anestezjolog":
        entry_cena_33 = Entry(root, textvariable=cena_33, justify=CENTER, width=14, bg="#ffff00")
        entry_cena_33.insert(0, "350")
        entry_cena_33.grid(row=23, column=6)
    elif nazwa_33.get() == "Butelka 400ml do długotrwałego odsysania ran j.u. sterylna":
        entry_cena_33 = Entry(root, textvariable=cena_33, justify=CENTER, width=14)
        entry_cena_33.insert(0, "4")
        entry_cena_33.grid(row=23, column=6)
    elif nazwa_33.get() == "Doba":
        entry_cena_33 = Entry(root, textvariable=cena_33, justify=CENTER, width=14)
        entry_cena_33.insert(0, "700")
        entry_cena_33.grid(row=23, column=6)
    elif nazwa_33.get() == "Dren łączący do ssaka Grena":
        entry_cena_33 = Entry(root, textvariable=cena_33, justify=CENTER, width=14)
        entry_cena_33.insert(0, "5")
        entry_cena_33.grid(row=23, column=6)
    elif nazwa_33.get() == "Dren Redona Ch 16 dł. 800mm z trokarem":
        entry_cena_33 = Entry(root, textvariable=cena_33, justify=CENTER, width=14)
        entry_cena_33.insert(0, "29.74")
        entry_cena_33.grid(row=23, column=6)
    elif nazwa_33.get() == "Dren do pompy Artrex":
        entry_cena_33 = Entry(root, textvariable=cena_33, justify=CENTER, width=14)
        entry_cena_33.insert(0, "108")
        entry_cena_33.grid(row=23, column=6)
    elif nazwa_33.get() == "Drut wiercący 2,4 x 311":
        entry_cena_33 = Entry(root, textvariable=cena_33, justify=CENTER, width=14)
        entry_cena_33.insert(0, "139.60")
        entry_cena_33.grid(row=23, column=6)
    elif nazwa_33.get() == "Fartuch jałowy L":
        entry_cena_33 = Entry(root, textvariable=cena_33, justify=CENTER, width=14)
        entry_cena_33.insert(0, "17")
        entry_cena_33.grid(row=23, column=6)
    elif nazwa_33.get() == "Fartuch jałowy M":
        entry_cena_33 = Entry(root, textvariable=cena_33, justify=CENTER, width=14)
        entry_cena_33.insert(0, "15.28")
        entry_cena_33.grid(row=23, column=6)
    elif nazwa_33.get() == "Fartuch jałowy XL":
        entry_cena_33 = Entry(root, textvariable=cena_33, justify=CENTER, width=14)
        entry_cena_33.insert(0, "20.84")
        entry_cena_33.grid(row=23, column=6)
    elif nazwa_33.get() == "FasatThread BioComposite Interference Screw 8x30":
        entry_cena_33 = Entry(root, textvariable=cena_33, justify=CENTER, width=14)
        entry_cena_33.insert(0, "594")
        entry_cena_33.grid(row=23, column=6)
    elif nazwa_33.get() == "Folia operacyjna, jałowa 45cm x 55cm":
        entry_cena_33 = Entry(root, textvariable=cena_33, justify=CENTER, width=14)
        entry_cena_33.insert(0, "9.99")
        entry_cena_33.grid(row=23, column=6)
    elif nazwa_33.get() == "Gaziki 10 x 10cm":
        entry_cena_33 = Entry(root, textvariable=cena_33, justify=CENTER, width=14)
        entry_cena_33.insert(0, "0.10")
        entry_cena_33.grid(row=23, column=6)
    elif nazwa_33.get() == "Igła 0,6 x 60":
        entry_cena_33 = Entry(root, textvariable=cena_33, justify=CENTER, width=14)
        entry_cena_33.insert(0, "0.09")
        entry_cena_33.grid(row=23, column=6)
    elif nazwa_33.get() == "Igła 0,7 x 40":
        entry_cena_33 = Entry(root, textvariable=cena_33, justify=CENTER, width=14)
        entry_cena_33.insert(0, "0.05")
        entry_cena_33.grid(row=23, column=6)
    elif nazwa_33.get() == "Igła 0,8 x 40":
        entry_cena_33 = Entry(root, textvariable=cena_33, justify=CENTER, width=14)
        entry_cena_33.insert(0, "0.05")
        entry_cena_33.grid(row=23, column=6)
    elif nazwa_33.get() == "Igła 1,1 x 70":
        entry_cena_33 = Entry(root, textvariable=cena_33, justify=CENTER, width=14)
        entry_cena_33.insert(0, "0.16")
        entry_cena_33.grid(row=23, column=6)
    elif nazwa_33.get() == "Kaniulowana śruba int. biokompozytowa z osłonką jednoraz.":
        entry_cena_33 = Entry(root, textvariable=cena_33, justify=CENTER, width=14)
        entry_cena_33.insert(0, "594")
        entry_cena_33.grid(row=23, column=6)
    elif nazwa_33.get() == "Kaniulowana śruba int. biokompozytowa z pełnym gwintem":
        entry_cena_33 = Entry(root, textvariable=cena_33, justify=CENTER, width=14)
        entry_cena_33.insert(0, "594")
        entry_cena_33.grid(row=23, column=6)
    elif nazwa_33.get() == "Końcówka do Shavera":
        entry_cena_33 = Entry(root, textvariable=cena_33, justify=CENTER, width=14)
        entry_cena_33.insert(0, "270")
        entry_cena_33.grid(row=23, column=6)
    elif nazwa_33.get() == "Kotwica biokompozytowa SwiveLock":
        entry_cena_33 = Entry(root, textvariable=cena_33, justify=CENTER, width=14)
        entry_cena_33.insert(0, "918")
        entry_cena_33.grid(row=23, column=6)
    elif nazwa_33.get() == "Kotwica Corkscrew":
        entry_cena_33 = Entry(root, textvariable=cena_33, justify=CENTER, width=14)
        entry_cena_33.insert(0, "604")
        entry_cena_33.grid(row=23, column=6)
    elif nazwa_33.get() == "Kotwica FASTak":
        entry_cena_33 = Entry(root, textvariable=cena_33, justify=CENTER, width=14)
        entry_cena_33.insert(0, "432")
        entry_cena_33.grid(row=23, column=6)
    elif nazwa_33.get() == "Kotwica PEEK SwiveLock":
        entry_cena_33 = Entry(root, textvariable=cena_33, justify=CENTER, width=14)
        entry_cena_33.insert(0, "885.60")
        entry_cena_33.grid(row=23, column=6)
    elif nazwa_33.get() == "NaCl 3000ml":
        entry_cena_33 = Entry(root, textvariable=cena_33, justify=CENTER, width=14)
        entry_cena_33.insert(0, "29.72")
        entry_cena_33.grid(row=23, column=6)
    elif nazwa_33.get() == "NaCl 5000ml":
        entry_cena_33 = Entry(root, textvariable=cena_33, justify=CENTER, width=14)
        entry_cena_33.insert(0, "58.33")
        entry_cena_33.grid(row=23, column=6)
    elif nazwa_33.get() == "Nici Dafilon 2-0":
        entry_cena_33 = Entry(root, textvariable=cena_33, justify=CENTER, width=14)
        entry_cena_33.insert(0, "6.60")
        entry_cena_33.grid(row=23, column=6)
    elif nazwa_33.get() == "Nici Novosyn 2":
        entry_cena_33 = Entry(root, textvariable=cena_33, justify=CENTER, width=14)
        entry_cena_33.insert(0, "13")
        entry_cena_33.grid(row=23, column=6)
    elif nazwa_33.get() == "Nici Novosyn 2-0":
        entry_cena_33 = Entry(root, textvariable=cena_33, justify=CENTER, width=14)
        entry_cena_33.insert(0, "7.70")
        entry_cena_33.grid(row=23, column=6)
    elif nazwa_33.get() == "Nici Novosyn 3-0":
        entry_cena_33 = Entry(root, textvariable=cena_33, justify=CENTER, width=14)
        entry_cena_33.insert(0, "7.70")
        entry_cena_33.grid(row=23, column=6)
    elif nazwa_33.get() == "Nici Nylon 2-0":
        entry_cena_33 = Entry(root, textvariable=cena_33, justify=CENTER, width=14)
        entry_cena_33.insert(0, "2.50")
        entry_cena_33.grid(row=23, column=6)
    elif nazwa_33.get() == "Nici Nylon 3-0":
        entry_cena_33 = Entry(root, textvariable=cena_33, justify=CENTER, width=14)
        entry_cena_33.insert(0, "2")
        entry_cena_33.grid(row=23, column=6)
    elif nazwa_33.get() == "Nici PGLA":
        entry_cena_33 = Entry(root, textvariable=cena_33, justify=CENTER, width=14)
        entry_cena_33.insert(0, "11.60")
        entry_cena_33.grid(row=23, column=6)
    elif nazwa_33.get() == "Nici PremiCron 3":
        entry_cena_33 = Entry(root, textvariable=cena_33, justify=CENTER, width=14)
        entry_cena_33.insert(0, "6.50")
        entry_cena_33.grid(row=23, column=6)
    elif nazwa_33.get() == "Nici Vicryl 4-0":
        entry_cena_33 = Entry(root, textvariable=cena_33, justify=CENTER, width=14)
        entry_cena_33.insert(0, "7.50")
        entry_cena_33.grid(row=23, column=6)
    elif nazwa_33.get() == "Nitinol Guide Pin 1.1":
        entry_cena_33 = Entry(root, textvariable=cena_33, justify=CENTER, width=14)
        entry_cena_33.insert(0, "145.80")
        entry_cena_33.grid(row=23, column=6)
    elif nazwa_33.get() == "Osłona na przewody":
        entry_cena_33 = Entry(root, textvariable=cena_33, justify=CENTER, width=14)
        entry_cena_33.insert(0, "2.50")
        entry_cena_33.grid(row=23, column=6)
    elif nazwa_33.get() == "Ostrze Arthrex 90(86)x19x1,27":
        entry_cena_33 = Entry(root, textvariable=cena_33, justify=CENTER, width=14)
        entry_cena_33.insert(0, "216")
        entry_cena_33.grid(row=23, column=6)
    elif nazwa_33.get() == "Ostrze piły":
        entry_cena_33 = Entry(root, textvariable=cena_33, justify=CENTER, width=14)
        entry_cena_33.insert(0, "108")
        entry_cena_33.grid(row=23, column=6)
    elif nazwa_33.get() == "Pielęgniarka anest.":
        entry_cena_33 = Entry(root, textvariable=cena_33, justify=CENTER, width=14)
        entry_cena_33.insert(0, "50")
        entry_cena_33.grid(row=23, column=6)
    elif nazwa_33.get() == "Pielęgniarka instr.":
        entry_cena_33 = Entry(root, textvariable=cena_33, justify=CENTER, width=14)
        entry_cena_33.insert(0, "50")
        entry_cena_33.grid(row=23, column=6)
    elif nazwa_33.get() == "Pielęgniarka 'Noviline'":
        entry_cena_33 = Entry(root, textvariable=cena_33, justify=CENTER, width=14)
        entry_cena_33.insert(0, "30")
        entry_cena_33.grid(row=23, column=6)
    elif nazwa_33.get() == "Płytka PeekPower do osteotomii klinowej":
        entry_cena_33 = Entry(root, textvariable=cena_33, justify=CENTER, width=14)
        entry_cena_33.insert(0, "2160")
        entry_cena_33.grid(row=23, column=6)
    elif nazwa_33.get() == "Rękawice jałowe 6,5":
        entry_cena_33 = Entry(root, textvariable=cena_33, justify=CENTER, width=14)
        entry_cena_33.insert(0, "1.20")
        entry_cena_33.grid(row=23, column=6)
    elif nazwa_33.get() == "Rękawice jałowe 7,0":
        entry_cena_33 = Entry(root, textvariable=cena_33, justify=CENTER, width=14)
        entry_cena_33.insert(0, "1.20")
        entry_cena_33.grid(row=23, column=6)
    elif nazwa_33.get() == "Rękawice jałowe 7,5":
        entry_cena_33 = Entry(root, textvariable=cena_33, justify=CENTER, width=14)
        entry_cena_33.insert(0, "1.20")
        entry_cena_33.grid(row=23, column=6)
    elif nazwa_33.get() == "Rękawice jałowe 8,00":
        entry_cena_33 = Entry(root, textvariable=cena_33, justify=CENTER, width=14)
        entry_cena_33.insert(0, "1.20")
        entry_cena_33.grid(row=23, column=6)
    elif nazwa_33.get() == "Rękojeść Interpulse wysokoprzepływowa":
        entry_cena_33 = Entry(root, textvariable=cena_33, justify=CENTER, width=14)
        entry_cena_33.insert(0, "216")
        entry_cena_33.grid(row=23, column=6)
    elif nazwa_33.get() == "Serweta":
        entry_cena_33 = Entry(root, textvariable=cena_33, justify=CENTER, width=14)
        entry_cena_33.insert(0, "6")
        entry_cena_33.grid(row=23, column=6)
    elif nazwa_33.get() == "Simplex Hv z Gentamycyna 10x40g":
        entry_cena_33 = Entry(root, textvariable=cena_33, justify=CENTER, width=14)
        entry_cena_33.insert(0, "162")
        entry_cena_33.grid(row=23, column=6)
    elif nazwa_33.get() == "Skalpel 11":
        entry_cena_33 = Entry(root, textvariable=cena_33, justify=CENTER, width=14)
        entry_cena_33.insert(0, "0.38")
        entry_cena_33.grid(row=23, column=6)
    elif nazwa_33.get() == "Skalpel 13":
        entry_cena_33 = Entry(root, textvariable=cena_33, justify=CENTER, width=14)
        entry_cena_33.insert(0, "1")
        entry_cena_33.grid(row=23, column=6)
    elif nazwa_33.get() == "Skalpel 22":
        entry_cena_33 = Entry(root, textvariable=cena_33, justify=CENTER, width=14)
        entry_cena_33.insert(0, "1")
        entry_cena_33.grid(row=23, column=6)
    elif nazwa_33.get() == "Śruba blokująca PeekPower do osteotomii":
        entry_cena_33 = Entry(root, textvariable=cena_33, justify=CENTER, width=14)
        entry_cena_33.insert(0, "194")
        entry_cena_33.grid(row=23, column=6)
    elif nazwa_33.get() == "System do mieszania próżniowego":
        entry_cena_33 = Entry(root, textvariable=cena_33, justify=CENTER, width=14)
        entry_cena_33.insert(0, "216")
        entry_cena_33.grid(row=23, column=6)
    elif nazwa_33.get() == "System wprowadzania implantów ACL TightRope":
        entry_cena_33 = Entry(root, textvariable=cena_33, justify=CENTER, width=14)
        entry_cena_33.insert(0, "702")
        entry_cena_33.grid(row=23, column=6)
    elif nazwa_33.get() == "Szew FiberWire 2":
        entry_cena_33 = Entry(root, textvariable=cena_33, justify=CENTER, width=14)
        entry_cena_33.insert(0, "86.40")
        entry_cena_33.grid(row=23, column=6)
    elif nazwa_33.get() == "Taśma przylepna 10x50":
        entry_cena_33 = Entry(root, textvariable=cena_33, justify=CENTER, width=14)
        entry_cena_33.insert(0, "1.04")
        entry_cena_33.grid(row=23, column=6)
    elif nazwa_33.get() == "Triathlon elem. udowy lewy":
        entry_cena_33 = Entry(root, textvariable=cena_33, justify=CENTER, width=14)
        entry_cena_33.insert(0, "3132")
        entry_cena_33.grid(row=23, column=6)
    elif nazwa_33.get() == "Triathlon PS wkładka x3-9mm #4":
        entry_cena_33 = Entry(root, textvariable=cena_33, justify=CENTER, width=14)
        entry_cena_33.insert(0, "756")
        entry_cena_33.grid(row=23, column=6)
    elif nazwa_33.get() == "Triathlon taca piszczelowa":
        entry_cena_33 = Entry(root, textvariable=cena_33, justify=CENTER, width=14)
        entry_cena_33.insert(0, "1296")
        entry_cena_33.grid(row=23, column=6)
    elif nazwa_33.get() == "Wkłady 3L z żelem":
        entry_cena_33 = Entry(root, textvariable=cena_33, justify=CENTER, width=14)
        entry_cena_33.insert(0, "10.26")
        entry_cena_33.grid(row=23, column=6)
    elif nazwa_33.get() == "Zestaw do artroskopii":
        entry_cena_33 = Entry(root, textvariable=cena_33, justify=CENTER, width=14)
        entry_cena_33.insert(0, "67")
        entry_cena_33.grid(row=23, column=6)
    elif nazwa_33.get() == "Zestaw do artroskopii barku":
        entry_cena_33 = Entry(root, textvariable=cena_33, justify=CENTER, width=14)
        entry_cena_33.insert(0, "108")
        entry_cena_33.grid(row=23, column=6)
    elif nazwa_33.get() == "Zestaw do drenażu":
        entry_cena_33 = Entry(root, textvariable=cena_33, justify=CENTER, width=14)
        entry_cena_33.insert(0, "14.23")
        entry_cena_33.grid(row=23, column=6)
    elif nazwa_33.get() == "Zestaw ortopedyczny":
        entry_cena_33 = Entry(root, textvariable=cena_33, justify=CENTER, width=14)
        entry_cena_33.insert(0, "28.08")
        entry_cena_33.grid(row=23, column=6)
    elif nazwa_33.get() == "Gaziki 20 x 10cm":
        entry_cena_33 = Entry(root, textvariable=cena_33, justify=CENTER, width=14)
        entry_cena_33.insert(0, "0.46")
        entry_cena_33.grid(row=23, column=6)
    else:
        entry_cena_33 = Entry(root, textvariable=cena_33, justify=CENTER, width=14, bg="#ffff00")
        entry_cena_33.insert(0, "0")
        entry_cena_33.grid(row=23, column=6)

    if nazwa_34.get() == "--puste--":
        entry_cena_34 = Entry(root, textvariable=cena_34, justify=CENTER, width=14)
        entry_cena_34.insert(0, "0")
        entry_cena_34.grid(row=24, column=6)
    elif nazwa_34.get() == "Ablator":
        entry_cena_34 = Entry(root, textvariable=cena_34, justify=CENTER, width=14)
        entry_cena_34.insert(0, "572")
        entry_cena_34.grid(row=24, column=6)
    elif nazwa_34.get() == "Anestezjolog":
        entry_cena_34 = Entry(root, textvariable=cena_34, justify=CENTER, width=14, bg="#ffff00")
        entry_cena_34.insert(0, "350")
        entry_cena_34.grid(row=24, column=6)
    elif nazwa_34.get() == "Butelka 400ml do długotrwałego odsysania ran j.u. sterylna":
        entry_cena_34 = Entry(root, textvariable=cena_34, justify=CENTER, width=14)
        entry_cena_34.insert(0, "4")
        entry_cena_34.grid(row=24, column=6)
    elif nazwa_34.get() == "Doba":
        entry_cena_34 = Entry(root, textvariable=cena_34, justify=CENTER, width=14)
        entry_cena_34.insert(0, "700")
        entry_cena_34.grid(row=24, column=6)
    elif nazwa_34.get() == "Dren łączący do ssaka Grena":
        entry_cena_34 = Entry(root, textvariable=cena_34, justify=CENTER, width=14)
        entry_cena_34.insert(0, "5")
        entry_cena_34.grid(row=24, column=6)
    elif nazwa_34.get() == "Dren Redona Ch 16 dł. 800mm z trokarem":
        entry_cena_34 = Entry(root, textvariable=cena_34, justify=CENTER, width=14)
        entry_cena_34.insert(0, "29.74")
        entry_cena_34.grid(row=24, column=6)
    elif nazwa_34.get() == "Dren do pompy Artrex":
        entry_cena_34 = Entry(root, textvariable=cena_34, justify=CENTER, width=14)
        entry_cena_34.insert(0, "108")
        entry_cena_34.grid(row=24, column=6)
    elif nazwa_34.get() == "Drut wiercący 2,4 x 311":
        entry_cena_34 = Entry(root, textvariable=cena_34, justify=CENTER, width=14)
        entry_cena_34.insert(0, "139.60")
        entry_cena_34.grid(row=24, column=6)
    elif nazwa_34.get() == "Fartuch jałowy L":
        entry_cena_34 = Entry(root, textvariable=cena_34, justify=CENTER, width=14)
        entry_cena_34.insert(0, "17")
        entry_cena_34.grid(row=24, column=6)
    elif nazwa_34.get() == "Fartuch jałowy M":
        entry_cena_34 = Entry(root, textvariable=cena_34, justify=CENTER, width=14)
        entry_cena_34.insert(0, "15.28")
        entry_cena_34.grid(row=24, column=6)
    elif nazwa_34.get() == "Fartuch jałowy XL":
        entry_cena_34 = Entry(root, textvariable=cena_34, justify=CENTER, width=14)
        entry_cena_34.insert(0, "20.84")
        entry_cena_34.grid(row=24, column=6)
    elif nazwa_34.get() == "FasatThread BioComposite Interference Screw 8x30":
        entry_cena_34 = Entry(root, textvariable=cena_34, justify=CENTER, width=14)
        entry_cena_34.insert(0, "594")
        entry_cena_34.grid(row=24, column=6)
    elif nazwa_34.get() == "Folia operacyjna, jałowa 45cm x 55cm":
        entry_cena_34 = Entry(root, textvariable=cena_34, justify=CENTER, width=14)
        entry_cena_34.insert(0, "9.99")
        entry_cena_34.grid(row=24, column=6)
    elif nazwa_34.get() == "Gaziki 10 x 10cm":
        entry_cena_34 = Entry(root, textvariable=cena_34, justify=CENTER, width=14)
        entry_cena_34.insert(0, "0.10")
        entry_cena_34.grid(row=24, column=6)
    elif nazwa_34.get() == "Igła 0,6 x 60":
        entry_cena_34 = Entry(root, textvariable=cena_34, justify=CENTER, width=14)
        entry_cena_34.insert(0, "0.09")
        entry_cena_34.grid(row=24, column=6)
    elif nazwa_34.get() == "Igła 0,7 x 40":
        entry_cena_34 = Entry(root, textvariable=cena_34, justify=CENTER, width=14)
        entry_cena_34.insert(0, "0.05")
        entry_cena_34.grid(row=24, column=6)
    elif nazwa_34.get() == "Igła 0,8 x 40":
        entry_cena_34 = Entry(root, textvariable=cena_34, justify=CENTER, width=14)
        entry_cena_34.insert(0, "0.05")
        entry_cena_34.grid(row=24, column=6)
    elif nazwa_34.get() == "Igła 1,1 x 70":
        entry_cena_34 = Entry(root, textvariable=cena_34, justify=CENTER, width=14)
        entry_cena_34.insert(0, "0.16")
        entry_cena_34.grid(row=24, column=6)
    elif nazwa_34.get() == "Kaniulowana śruba int. biokompozytowa z osłonką jednoraz.":
        entry_cena_34 = Entry(root, textvariable=cena_34, justify=CENTER, width=14)
        entry_cena_34.insert(0, "594")
        entry_cena_34.grid(row=24, column=6)
    elif nazwa_34.get() == "Kaniulowana śruba int. biokompozytowa z pełnym gwintem":
        entry_cena_34 = Entry(root, textvariable=cena_34, justify=CENTER, width=14)
        entry_cena_34.insert(0, "594")
        entry_cena_34.grid(row=24, column=6)
    elif nazwa_34.get() == "Końcówka do Shavera":
        entry_cena_34 = Entry(root, textvariable=cena_34, justify=CENTER, width=14)
        entry_cena_34.insert(0, "270")
        entry_cena_34.grid(row=24, column=6)
    elif nazwa_34.get() == "Kotwica biokompozytowa SwiveLock":
        entry_cena_34 = Entry(root, textvariable=cena_34, justify=CENTER, width=14)
        entry_cena_34.insert(0, "918")
        entry_cena_34.grid(row=24, column=6)
    elif nazwa_34.get() == "Kotwica Corkscrew":
        entry_cena_34 = Entry(root, textvariable=cena_34, justify=CENTER, width=14)
        entry_cena_34.insert(0, "604")
        entry_cena_34.grid(row=24, column=6)
    elif nazwa_34.get() == "Kotwica FASTak":
        entry_cena_34 = Entry(root, textvariable=cena_34, justify=CENTER, width=14)
        entry_cena_34.insert(0, "432")
        entry_cena_34.grid(row=24, column=6)
    elif nazwa_34.get() == "Kotwica PEEK SwiveLock":
        entry_cena_34 = Entry(root, textvariable=cena_34, justify=CENTER, width=14)
        entry_cena_34.insert(0, "885.60")
        entry_cena_34.grid(row=24, column=6)
    elif nazwa_34.get() == "NaCl 3000ml":
        entry_cena_34 = Entry(root, textvariable=cena_34, justify=CENTER, width=14)
        entry_cena_34.insert(0, "29.72")
        entry_cena_34.grid(row=24, column=6)
    elif nazwa_34.get() == "NaCl 5000ml":
        entry_cena_34 = Entry(root, textvariable=cena_34, justify=CENTER, width=14)
        entry_cena_34.insert(0, "58.33")
        entry_cena_34.grid(row=24, column=6)
    elif nazwa_34.get() == "Nici Dafilon 2-0":
        entry_cena_34 = Entry(root, textvariable=cena_34, justify=CENTER, width=14)
        entry_cena_34.insert(0, "6.60")
        entry_cena_34.grid(row=24, column=6)
    elif nazwa_34.get() == "Nici Novosyn 2":
        entry_cena_34 = Entry(root, textvariable=cena_34, justify=CENTER, width=14)
        entry_cena_34.insert(0, "13")
        entry_cena_34.grid(row=24, column=6)
    elif nazwa_34.get() == "Nici Novosyn 2-0":
        entry_cena_34 = Entry(root, textvariable=cena_34, justify=CENTER, width=14)
        entry_cena_34.insert(0, "7.70")
        entry_cena_34.grid(row=24, column=6)
    elif nazwa_34.get() == "Nici Novosyn 3-0":
        entry_cena_34 = Entry(root, textvariable=cena_34, justify=CENTER, width=14)
        entry_cena_34.insert(0, "7.70")
        entry_cena_34.grid(row=24, column=6)
    elif nazwa_34.get() == "Nici Nylon 2-0":
        entry_cena_34 = Entry(root, textvariable=cena_34, justify=CENTER, width=14)
        entry_cena_34.insert(0, "2.50")
        entry_cena_34.grid(row=24, column=6)
    elif nazwa_34.get() == "Nici Nylon 3-0":
        entry_cena_34 = Entry(root, textvariable=cena_34, justify=CENTER, width=14)
        entry_cena_34.insert(0, "2")
        entry_cena_34.grid(row=24, column=6)
    elif nazwa_34.get() == "Nici PGLA":
        entry_cena_34 = Entry(root, textvariable=cena_34, justify=CENTER, width=14)
        entry_cena_34.insert(0, "11.60")
        entry_cena_34.grid(row=24, column=6)
    elif nazwa_34.get() == "Nici PremiCron 3":
        entry_cena_34 = Entry(root, textvariable=cena_34, justify=CENTER, width=14)
        entry_cena_34.insert(0, "6.50")
        entry_cena_34.grid(row=24, column=6)
    elif nazwa_34.get() == "Nici Vicryl 4-0":
        entry_cena_34 = Entry(root, textvariable=cena_34, justify=CENTER, width=14)
        entry_cena_34.insert(0, "7.50")
        entry_cena_34.grid(row=24, column=6)
    elif nazwa_34.get() == "Nitinol Guide Pin 1.1":
        entry_cena_34 = Entry(root, textvariable=cena_34, justify=CENTER, width=14)
        entry_cena_34.insert(0, "145.80")
        entry_cena_34.grid(row=24, column=6)
    elif nazwa_34.get() == "Osłona na przewody":
        entry_cena_34 = Entry(root, textvariable=cena_34, justify=CENTER, width=14)
        entry_cena_34.insert(0, "2.50")
        entry_cena_34.grid(row=24, column=6)
    elif nazwa_34.get() == "Ostrze Arthrex 90(86)x19x1,27":
        entry_cena_34 = Entry(root, textvariable=cena_34, justify=CENTER, width=14)
        entry_cena_34.insert(0, "216")
        entry_cena_34.grid(row=24, column=6)
    elif nazwa_34.get() == "Ostrze piły":
        entry_cena_34 = Entry(root, textvariable=cena_34, justify=CENTER, width=14)
        entry_cena_34.insert(0, "108")
        entry_cena_34.grid(row=24, column=6)
    elif nazwa_34.get() == "Pielęgniarka anest.":
        entry_cena_34 = Entry(root, textvariable=cena_34, justify=CENTER, width=14)
        entry_cena_34.insert(0, "50")
        entry_cena_34.grid(row=24, column=6)
    elif nazwa_34.get() == "Pielęgniarka instr.":
        entry_cena_34 = Entry(root, textvariable=cena_34, justify=CENTER, width=14)
        entry_cena_34.insert(0, "50")
        entry_cena_34.grid(row=24, column=6)
    elif nazwa_34.get() == "Pielęgniarka 'Noviline'":
        entry_cena_34 = Entry(root, textvariable=cena_34, justify=CENTER, width=14)
        entry_cena_34.insert(0, "30")
        entry_cena_34.grid(row=24, column=6)
    elif nazwa_34.get() == "Płytka PeekPower do osteotomii klinowej":
        entry_cena_34 = Entry(root, textvariable=cena_34, justify=CENTER, width=14)
        entry_cena_34.insert(0, "2160")
        entry_cena_34.grid(row=24, column=6)
    elif nazwa_34.get() == "Rękawice jałowe 6,5":
        entry_cena_34 = Entry(root, textvariable=cena_34, justify=CENTER, width=14)
        entry_cena_34.insert(0, "1.20")
        entry_cena_34.grid(row=24, column=6)
    elif nazwa_34.get() == "Rękawice jałowe 7,0":
        entry_cena_34 = Entry(root, textvariable=cena_34, justify=CENTER, width=14)
        entry_cena_34.insert(0, "1.20")
        entry_cena_34.grid(row=24, column=6)
    elif nazwa_34.get() == "Rękawice jałowe 7,5":
        entry_cena_34 = Entry(root, textvariable=cena_34, justify=CENTER, width=14)
        entry_cena_34.insert(0, "1.20")
        entry_cena_34.grid(row=24, column=6)
    elif nazwa_34.get() == "Rękawice jałowe 8,00":
        entry_cena_34 = Entry(root, textvariable=cena_34, justify=CENTER, width=14)
        entry_cena_34.insert(0, "1.20")
        entry_cena_34.grid(row=24, column=6)
    elif nazwa_34.get() == "Rękojeść Interpulse wysokoprzepływowa":
        entry_cena_34 = Entry(root, textvariable=cena_34, justify=CENTER, width=14)
        entry_cena_34.insert(0, "216")
        entry_cena_34.grid(row=24, column=6)
    elif nazwa_34.get() == "Serweta":
        entry_cena_34 = Entry(root, textvariable=cena_34, justify=CENTER, width=14)
        entry_cena_34.insert(0, "6")
        entry_cena_34.grid(row=24, column=6)
    elif nazwa_34.get() == "Simplex Hv z Gentamycyna 10x40g":
        entry_cena_34 = Entry(root, textvariable=cena_34, justify=CENTER, width=14)
        entry_cena_34.insert(0, "162")
        entry_cena_34.grid(row=24, column=6)
    elif nazwa_34.get() == "Skalpel 11":
        entry_cena_34 = Entry(root, textvariable=cena_34, justify=CENTER, width=14)
        entry_cena_34.insert(0, "0.38")
        entry_cena_34.grid(row=24, column=6)
    elif nazwa_34.get() == "Skalpel 13":
        entry_cena_34 = Entry(root, textvariable=cena_34, justify=CENTER, width=14)
        entry_cena_34.insert(0, "1")
        entry_cena_34.grid(row=24, column=6)
    elif nazwa_34.get() == "Skalpel 22":
        entry_cena_34 = Entry(root, textvariable=cena_34, justify=CENTER, width=14)
        entry_cena_34.insert(0, "1")
        entry_cena_34.grid(row=24, column=6)
    elif nazwa_34.get() == "Śruba blokująca PeekPower do osteotomii":
        entry_cena_34 = Entry(root, textvariable=cena_34, justify=CENTER, width=14)
        entry_cena_34.insert(0, "194")
        entry_cena_34.grid(row=24, column=6)
    elif nazwa_34.get() == "System do mieszania próżniowego":
        entry_cena_34 = Entry(root, textvariable=cena_34, justify=CENTER, width=14)
        entry_cena_34.insert(0, "216")
        entry_cena_34.grid(row=24, column=6)
    elif nazwa_34.get() == "System wprowadzania implantów ACL TightRope":
        entry_cena_34 = Entry(root, textvariable=cena_34, justify=CENTER, width=14)
        entry_cena_34.insert(0, "702")
        entry_cena_34.grid(row=24, column=6)
    elif nazwa_34.get() == "Szew FiberWire 2":
        entry_cena_34 = Entry(root, textvariable=cena_34, justify=CENTER, width=14)
        entry_cena_34.insert(0, "86.40")
        entry_cena_34.grid(row=24, column=6)
    elif nazwa_34.get() == "Taśma przylepna 10x50":
        entry_cena_34 = Entry(root, textvariable=cena_34, justify=CENTER, width=14)
        entry_cena_34.insert(0, "1.04")
        entry_cena_34.grid(row=24, column=6)
    elif nazwa_34.get() == "Triathlon elem. udowy lewy":
        entry_cena_34 = Entry(root, textvariable=cena_34, justify=CENTER, width=14)
        entry_cena_34.insert(0, "3132")
        entry_cena_34.grid(row=24, column=6)
    elif nazwa_34.get() == "Triathlon PS wkładka x3-9mm #4":
        entry_cena_34 = Entry(root, textvariable=cena_34, justify=CENTER, width=14)
        entry_cena_34.insert(0, "756")
        entry_cena_34.grid(row=24, column=6)
    elif nazwa_34.get() == "Triathlon taca piszczelowa":
        entry_cena_34 = Entry(root, textvariable=cena_34, justify=CENTER, width=14)
        entry_cena_34.insert(0, "1296")
        entry_cena_34.grid(row=24, column=6)
    elif nazwa_34.get() == "Wkłady 3L z żelem":
        entry_cena_34 = Entry(root, textvariable=cena_34, justify=CENTER, width=14)
        entry_cena_34.insert(0, "10.26")
        entry_cena_34.grid(row=24, column=6)
    elif nazwa_34.get() == "Zestaw do artroskopii":
        entry_cena_34 = Entry(root, textvariable=cena_34, justify=CENTER, width=14)
        entry_cena_34.insert(0, "67")
        entry_cena_34.grid(row=24, column=6)
    elif nazwa_34.get() == "Zestaw do artroskopii barku":
        entry_cena_34 = Entry(root, textvariable=cena_34, justify=CENTER, width=14)
        entry_cena_34.insert(0, "108")
        entry_cena_34.grid(row=24, column=6)
    elif nazwa_34.get() == "Zestaw do drenażu":
        entry_cena_34 = Entry(root, textvariable=cena_34, justify=CENTER, width=14)
        entry_cena_34.insert(0, "14.23")
        entry_cena_34.grid(row=24, column=6)
    elif nazwa_34.get() == "Zestaw ortopedyczny":
        entry_cena_34 = Entry(root, textvariable=cena_34, justify=CENTER, width=14)
        entry_cena_34.insert(0, "28.08")
        entry_cena_34.grid(row=24, column=6)
    elif nazwa_34.get() == "Gaziki 20 x 10cm":
        entry_cena_34 = Entry(root, textvariable=cena_34, justify=CENTER, width=14)
        entry_cena_34.insert(0, "0.46")
        entry_cena_34.grid(row=24, column=6)
    else:
        entry_cena_34 = Entry(root, textvariable=cena_34, justify=CENTER, width=14, bg="#ffff00")
        entry_cena_34.insert(0, "0")
        entry_cena_34.grid(row=24, column=6)

    if nazwa_35.get() == "--puste--":
        entry_cena_35 = Entry(root, textvariable=cena_35, justify=CENTER, width=14)
        entry_cena_35.insert(0, "0")
        entry_cena_35.grid(row=25, column=6)
    elif nazwa_35.get() == "Ablator":
        entry_cena_35 = Entry(root, textvariable=cena_35, justify=CENTER, width=14)
        entry_cena_35.insert(0, "572")
        entry_cena_35.grid(row=25, column=6)
    elif nazwa_35.get() == "Anestezjolog":
        entry_cena_35 = Entry(root, textvariable=cena_35, justify=CENTER, width=14, bg="#ffff00")
        entry_cena_35.insert(0, "350")
        entry_cena_35.grid(row=25, column=6)
    elif nazwa_35.get() == "Butelka 400ml do długotrwałego odsysania ran j.u. sterylna":
        entry_cena_35 = Entry(root, textvariable=cena_35, justify=CENTER, width=14)
        entry_cena_35.insert(0, "4")
        entry_cena_35.grid(row=25, column=6)
    elif nazwa_35.get() == "Doba":
        entry_cena_35 = Entry(root, textvariable=cena_35, justify=CENTER, width=14)
        entry_cena_35.insert(0, "700")
        entry_cena_35.grid(row=25, column=6)
    elif nazwa_35.get() == "Dren łączący do ssaka Grena":
        entry_cena_35 = Entry(root, textvariable=cena_35, justify=CENTER, width=14)
        entry_cena_35.insert(0, "5")
        entry_cena_35.grid(row=25, column=6)
    elif nazwa_35.get() == "Dren Redona Ch 16 dł. 800mm z trokarem":
        entry_cena_35 = Entry(root, textvariable=cena_35, justify=CENTER, width=14)
        entry_cena_35.insert(0, "29.74")
        entry_cena_35.grid(row=25, column=6)
    elif nazwa_35.get() == "Dren do pompy Artrex":
        entry_cena_35 = Entry(root, textvariable=cena_35, justify=CENTER, width=14)
        entry_cena_35.insert(0, "108")
        entry_cena_35.grid(row=25, column=6)
    elif nazwa_35.get() == "Drut wiercący 2,4 x 311":
        entry_cena_35 = Entry(root, textvariable=cena_35, justify=CENTER, width=14)
        entry_cena_35.insert(0, "139.60")
        entry_cena_35.grid(row=25, column=6)
    elif nazwa_35.get() == "Fartuch jałowy L":
        entry_cena_35 = Entry(root, textvariable=cena_35, justify=CENTER, width=14)
        entry_cena_35.insert(0, "17")
        entry_cena_35.grid(row=25, column=6)
    elif nazwa_35.get() == "Fartuch jałowy M":
        entry_cena_35 = Entry(root, textvariable=cena_35, justify=CENTER, width=14)
        entry_cena_35.insert(0, "15.28")
        entry_cena_35.grid(row=25, column=6)
    elif nazwa_35.get() == "Fartuch jałowy XL":
        entry_cena_35 = Entry(root, textvariable=cena_35, justify=CENTER, width=14)
        entry_cena_35.insert(0, "20.84")
        entry_cena_35.grid(row=25, column=6)
    elif nazwa_35.get() == "FasatThread BioComposite Interference Screw 8x30":
        entry_cena_35 = Entry(root, textvariable=cena_35, justify=CENTER, width=14)
        entry_cena_35.insert(0, "594")
        entry_cena_35.grid(row=25, column=6)
    elif nazwa_35.get() == "Folia operacyjna, jałowa 45cm x 55cm":
        entry_cena_35 = Entry(root, textvariable=cena_35, justify=CENTER, width=14)
        entry_cena_35.insert(0, "9.99")
        entry_cena_35.grid(row=25, column=6)
    elif nazwa_35.get() == "Gaziki 10 x 10cm":
        entry_cena_35 = Entry(root, textvariable=cena_35, justify=CENTER, width=14)
        entry_cena_35.insert(0, "0.10")
        entry_cena_35.grid(row=25, column=6)
    elif nazwa_35.get() == "Igła 0,6 x 60":
        entry_cena_35 = Entry(root, textvariable=cena_35, justify=CENTER, width=14)
        entry_cena_35.insert(0, "0.09")
        entry_cena_35.grid(row=25, column=6)
    elif nazwa_35.get() == "Igła 0,7 x 40":
        entry_cena_35 = Entry(root, textvariable=cena_35, justify=CENTER, width=14)
        entry_cena_35.insert(0, "0.05")
        entry_cena_35.grid(row=25, column=6)
    elif nazwa_35.get() == "Igła 0,8 x 40":
        entry_cena_35 = Entry(root, textvariable=cena_35, justify=CENTER, width=14)
        entry_cena_35.insert(0, "0.05")
        entry_cena_35.grid(row=25, column=6)
    elif nazwa_35.get() == "Igła 1,1 x 70":
        entry_cena_35 = Entry(root, textvariable=cena_35, justify=CENTER, width=14)
        entry_cena_35.insert(0, "0.16")
        entry_cena_35.grid(row=25, column=6)
    elif nazwa_35.get() == "Kaniulowana śruba int. biokompozytowa z osłonką jednoraz.":
        entry_cena_35 = Entry(root, textvariable=cena_35, justify=CENTER, width=14)
        entry_cena_35.insert(0, "594")
        entry_cena_35.grid(row=25, column=6)
    elif nazwa_35.get() == "Kaniulowana śruba int. biokompozytowa z pełnym gwintem":
        entry_cena_35 = Entry(root, textvariable=cena_35, justify=CENTER, width=14)
        entry_cena_35.insert(0, "594")
        entry_cena_35.grid(row=25, column=6)
    elif nazwa_35.get() == "Końcówka do Shavera":
        entry_cena_35 = Entry(root, textvariable=cena_35, justify=CENTER, width=14)
        entry_cena_35.insert(0, "270")
        entry_cena_35.grid(row=25, column=6)
    elif nazwa_35.get() == "Kotwica biokompozytowa SwiveLock":
        entry_cena_35 = Entry(root, textvariable=cena_35, justify=CENTER, width=14)
        entry_cena_35.insert(0, "918")
        entry_cena_35.grid(row=25, column=6)
    elif nazwa_35.get() == "Kotwica Corkscrew":
        entry_cena_35 = Entry(root, textvariable=cena_35, justify=CENTER, width=14)
        entry_cena_35.insert(0, "604")
        entry_cena_35.grid(row=25, column=6)
    elif nazwa_35.get() == "Kotwica FASTak":
        entry_cena_35 = Entry(root, textvariable=cena_35, justify=CENTER, width=14)
        entry_cena_35.insert(0, "432")
        entry_cena_35.grid(row=25, column=6)
    elif nazwa_35.get() == "Kotwica PEEK SwiveLock":
        entry_cena_35 = Entry(root, textvariable=cena_35, justify=CENTER, width=14)
        entry_cena_35.insert(0, "885.60")
        entry_cena_35.grid(row=25, column=6)
    elif nazwa_35.get() == "NaCl 3000ml":
        entry_cena_35 = Entry(root, textvariable=cena_35, justify=CENTER, width=14)
        entry_cena_35.insert(0, "29.72")
        entry_cena_35.grid(row=25, column=6)
    elif nazwa_35.get() == "NaCl 5000ml":
        entry_cena_35 = Entry(root, textvariable=cena_35, justify=CENTER, width=14)
        entry_cena_35.insert(0, "58.33")
        entry_cena_35.grid(row=25, column=6)
    elif nazwa_35.get() == "Nici Dafilon 2-0":
        entry_cena_35 = Entry(root, textvariable=cena_35, justify=CENTER, width=14)
        entry_cena_35.insert(0, "6.60")
        entry_cena_35.grid(row=25, column=6)
    elif nazwa_35.get() == "Nici Novosyn 2":
        entry_cena_35 = Entry(root, textvariable=cena_35, justify=CENTER, width=14)
        entry_cena_35.insert(0, "13")
        entry_cena_35.grid(row=25, column=6)
    elif nazwa_35.get() == "Nici Novosyn 2-0":
        entry_cena_35 = Entry(root, textvariable=cena_35, justify=CENTER, width=14)
        entry_cena_35.insert(0, "7.70")
        entry_cena_35.grid(row=25, column=6)
    elif nazwa_35.get() == "Nici Novosyn 3-0":
        entry_cena_35 = Entry(root, textvariable=cena_35, justify=CENTER, width=14)
        entry_cena_35.insert(0, "7.70")
        entry_cena_35.grid(row=25, column=6)
    elif nazwa_35.get() == "Nici Nylon 2-0":
        entry_cena_35 = Entry(root, textvariable=cena_35, justify=CENTER, width=14)
        entry_cena_35.insert(0, "2.50")
        entry_cena_35.grid(row=25, column=6)
    elif nazwa_35.get() == "Nici Nylon 3-0":
        entry_cena_35 = Entry(root, textvariable=cena_35, justify=CENTER, width=14)
        entry_cena_35.insert(0, "2")
        entry_cena_35.grid(row=25, column=6)
    elif nazwa_35.get() == "Nici PGLA":
        entry_cena_35 = Entry(root, textvariable=cena_35, justify=CENTER, width=14)
        entry_cena_35.insert(0, "11.60")
        entry_cena_35.grid(row=25, column=6)
    elif nazwa_35.get() == "Nici PremiCron 3":
        entry_cena_35 = Entry(root, textvariable=cena_35, justify=CENTER, width=14)
        entry_cena_35.insert(0, "6.50")
        entry_cena_35.grid(row=25, column=6)
    elif nazwa_35.get() == "Nici Vicryl 4-0":
        entry_cena_35 = Entry(root, textvariable=cena_35, justify=CENTER, width=14)
        entry_cena_35.insert(0, "7.50")
        entry_cena_35.grid(row=25, column=6)
    elif nazwa_35.get() == "Nitinol Guide Pin 1.1":
        entry_cena_35 = Entry(root, textvariable=cena_35, justify=CENTER, width=14)
        entry_cena_35.insert(0, "145.80")
        entry_cena_35.grid(row=25, column=6)
    elif nazwa_35.get() == "Osłona na przewody":
        entry_cena_35 = Entry(root, textvariable=cena_35, justify=CENTER, width=14)
        entry_cena_35.insert(0, "2.50")
        entry_cena_35.grid(row=25, column=6)
    elif nazwa_35.get() == "Ostrze Arthrex 90(86)x19x1,27":
        entry_cena_35 = Entry(root, textvariable=cena_35, justify=CENTER, width=14)
        entry_cena_35.insert(0, "216")
        entry_cena_35.grid(row=25, column=6)
    elif nazwa_35.get() == "Ostrze piły":
        entry_cena_35 = Entry(root, textvariable=cena_35, justify=CENTER, width=14)
        entry_cena_35.insert(0, "108")
        entry_cena_35.grid(row=25, column=6)
    elif nazwa_35.get() == "Pielęgniarka anest.":
        entry_cena_35 = Entry(root, textvariable=cena_35, justify=CENTER, width=14)
        entry_cena_35.insert(0, "50")
        entry_cena_35.grid(row=25, column=6)
    elif nazwa_35.get() == "Pielęgniarka instr.":
        entry_cena_35 = Entry(root, textvariable=cena_35, justify=CENTER, width=14)
        entry_cena_35.insert(0, "50")
        entry_cena_35.grid(row=25, column=6)
    elif nazwa_35.get() == "Pielęgniarka 'Noviline'":
        entry_cena_35 = Entry(root, textvariable=cena_35, justify=CENTER, width=14)
        entry_cena_35.insert(0, "30")
        entry_cena_35.grid(row=25, column=6)
    elif nazwa_35.get() == "Płytka PeekPower do osteotomii klinowej":
        entry_cena_35 = Entry(root, textvariable=cena_35, justify=CENTER, width=14)
        entry_cena_35.insert(0, "2160")
        entry_cena_35.grid(row=25, column=6)
    elif nazwa_35.get() == "Rękawice jałowe 6,5":
        entry_cena_35 = Entry(root, textvariable=cena_35, justify=CENTER, width=14)
        entry_cena_35.insert(0, "1.20")
        entry_cena_35.grid(row=25, column=6)
    elif nazwa_35.get() == "Rękawice jałowe 7,0":
        entry_cena_35 = Entry(root, textvariable=cena_35, justify=CENTER, width=14)
        entry_cena_35.insert(0, "1.20")
        entry_cena_35.grid(row=25, column=6)
    elif nazwa_35.get() == "Rękawice jałowe 7,5":
        entry_cena_35 = Entry(root, textvariable=cena_35, justify=CENTER, width=14)
        entry_cena_35.insert(0, "1.20")
        entry_cena_35.grid(row=25, column=6)
    elif nazwa_35.get() == "Rękawice jałowe 8,00":
        entry_cena_35 = Entry(root, textvariable=cena_35, justify=CENTER, width=14)
        entry_cena_35.insert(0, "1.20")
        entry_cena_35.grid(row=25, column=6)
    elif nazwa_35.get() == "Rękojeść Interpulse wysokoprzepływowa":
        entry_cena_35 = Entry(root, textvariable=cena_35, justify=CENTER, width=14)
        entry_cena_35.insert(0, "216")
        entry_cena_35.grid(row=25, column=6)
    elif nazwa_35.get() == "Serweta":
        entry_cena_35 = Entry(root, textvariable=cena_35, justify=CENTER, width=14)
        entry_cena_35.insert(0, "6")
        entry_cena_35.grid(row=25, column=6)
    elif nazwa_35.get() == "Simplex Hv z Gentamycyna 10x40g":
        entry_cena_35 = Entry(root, textvariable=cena_35, justify=CENTER, width=14)
        entry_cena_35.insert(0, "162")
        entry_cena_35.grid(row=25, column=6)
    elif nazwa_35.get() == "Skalpel 11":
        entry_cena_35 = Entry(root, textvariable=cena_35, justify=CENTER, width=14)
        entry_cena_35.insert(0, "0.38")
        entry_cena_35.grid(row=25, column=6)
    elif nazwa_35.get() == "Skalpel 13":
        entry_cena_35 = Entry(root, textvariable=cena_35, justify=CENTER, width=14)
        entry_cena_35.insert(0, "1")
        entry_cena_35.grid(row=25, column=6)
    elif nazwa_35.get() == "Skalpel 22":
        entry_cena_35 = Entry(root, textvariable=cena_35, justify=CENTER, width=14)
        entry_cena_35.insert(0, "1")
        entry_cena_35.grid(row=25, column=6)
    elif nazwa_35.get() == "Śruba blokująca PeekPower do osteotomii":
        entry_cena_35 = Entry(root, textvariable=cena_35, justify=CENTER, width=14)
        entry_cena_35.insert(0, "194")
        entry_cena_35.grid(row=25, column=6)
    elif nazwa_35.get() == "System do mieszania próżniowego":
        entry_cena_35 = Entry(root, textvariable=cena_35, justify=CENTER, width=14)
        entry_cena_35.insert(0, "216")
        entry_cena_35.grid(row=25, column=6)
    elif nazwa_35.get() == "System wprowadzania implantów ACL TightRope":
        entry_cena_35 = Entry(root, textvariable=cena_35, justify=CENTER, width=14)
        entry_cena_35.insert(0, "702")
        entry_cena_35.grid(row=25, column=6)
    elif nazwa_35.get() == "Szew FiberWire 2":
        entry_cena_35 = Entry(root, textvariable=cena_35, justify=CENTER, width=14)
        entry_cena_35.insert(0, "86.40")
        entry_cena_35.grid(row=25, column=6)
    elif nazwa_35.get() == "Taśma przylepna 10x50":
        entry_cena_35 = Entry(root, textvariable=cena_35, justify=CENTER, width=14)
        entry_cena_35.insert(0, "1.04")
        entry_cena_35.grid(row=25, column=6)
    elif nazwa_35.get() == "Triathlon elem. udowy lewy":
        entry_cena_35 = Entry(root, textvariable=cena_35, justify=CENTER, width=14)
        entry_cena_35.insert(0, "3132")
        entry_cena_35.grid(row=25, column=6)
    elif nazwa_35.get() == "Triathlon PS wkładka x3-9mm #4":
        entry_cena_35 = Entry(root, textvariable=cena_35, justify=CENTER, width=14)
        entry_cena_35.insert(0, "756")
        entry_cena_35.grid(row=25, column=6)
    elif nazwa_35.get() == "Triathlon taca piszczelowa":
        entry_cena_35 = Entry(root, textvariable=cena_35, justify=CENTER, width=14)
        entry_cena_35.insert(0, "1296")
        entry_cena_35.grid(row=25, column=6)
    elif nazwa_35.get() == "Wkłady 3L z żelem":
        entry_cena_35 = Entry(root, textvariable=cena_35, justify=CENTER, width=14)
        entry_cena_35.insert(0, "10.26")
        entry_cena_35.grid(row=25, column=6)
    elif nazwa_35.get() == "Zestaw do artroskopii":
        entry_cena_35 = Entry(root, textvariable=cena_35, justify=CENTER, width=14)
        entry_cena_35.insert(0, "67")
        entry_cena_35.grid(row=25, column=6)
    elif nazwa_35.get() == "Zestaw do artroskopii barku":
        entry_cena_35 = Entry(root, textvariable=cena_35, justify=CENTER, width=14)
        entry_cena_35.insert(0, "108")
        entry_cena_35.grid(row=25, column=6)
    elif nazwa_35.get() == "Zestaw do drenażu":
        entry_cena_35 = Entry(root, textvariable=cena_35, justify=CENTER, width=14)
        entry_cena_35.insert(0, "14.23")
        entry_cena_35.grid(row=25, column=6)
    elif nazwa_35.get() == "Zestaw ortopedyczny":
        entry_cena_35 = Entry(root, textvariable=cena_35, justify=CENTER, width=14)
        entry_cena_35.insert(0, "28.08")
        entry_cena_35.grid(row=25, column=6)
    elif nazwa_35.get() == "Gaziki 20 x 10cm":
        entry_cena_35 = Entry(root, textvariable=cena_35, justify=CENTER, width=14)
        entry_cena_35.insert(0, "0.46")
        entry_cena_35.grid(row=25, column=6)
    else:
        entry_cena_35 = Entry(root, textvariable=cena_35, justify=CENTER, width=14, bg="#ffff00")
        entry_cena_35.insert(0, "0")
        entry_cena_35.grid(row=25, column=6)

    if nazwa_36.get() == "--puste--":
        entry_cena_36 = Entry(root, textvariable=cena_36, justify=CENTER, width=14)
        entry_cena_36.insert(0, "0")
        entry_cena_36.grid(row=26, column=6)
    elif nazwa_36.get() == "Ablator":
        entry_cena_36 = Entry(root, textvariable=cena_36, justify=CENTER, width=14)
        entry_cena_36.insert(0, "572")
        entry_cena_36.grid(row=26, column=6)
    elif nazwa_36.get() == "Anestezjolog":
        entry_cena_36 = Entry(root, textvariable=cena_36, justify=CENTER, width=14, bg="#ffff00")
        entry_cena_36.insert(0, "350")
        entry_cena_36.grid(row=26, column=6)
    elif nazwa_36.get() == "Butelka 400ml do długotrwałego odsysania ran j.u. sterylna":
        entry_cena_36 = Entry(root, textvariable=cena_36, justify=CENTER, width=14)
        entry_cena_36.insert(0, "4")
        entry_cena_36.grid(row=26, column=6)
    elif nazwa_36.get() == "Doba":
        entry_cena_36 = Entry(root, textvariable=cena_36, justify=CENTER, width=14)
        entry_cena_36.insert(0, "700")
        entry_cena_36.grid(row=26, column=6)
    elif nazwa_36.get() == "Dren łączący do ssaka Grena":
        entry_cena_36 = Entry(root, textvariable=cena_36, justify=CENTER, width=14)
        entry_cena_36.insert(0, "5")
        entry_cena_36.grid(row=26, column=6)
    elif nazwa_36.get() == "Dren Redona Ch 16 dł. 800mm z trokarem":
        entry_cena_36 = Entry(root, textvariable=cena_36, justify=CENTER, width=14)
        entry_cena_36.insert(0, "29.74")
        entry_cena_36.grid(row=26, column=6)
    elif nazwa_36.get() == "Dren do pompy Artrex":
        entry_cena_36 = Entry(root, textvariable=cena_36, justify=CENTER, width=14)
        entry_cena_36.insert(0, "108")
        entry_cena_36.grid(row=26, column=6)
    elif nazwa_36.get() == "Drut wiercący 2,4 x 311":
        entry_cena_36 = Entry(root, textvariable=cena_36, justify=CENTER, width=14)
        entry_cena_36.insert(0, "139.60")
        entry_cena_36.grid(row=26, column=6)
    elif nazwa_36.get() == "Fartuch jałowy L":
        entry_cena_36 = Entry(root, textvariable=cena_36, justify=CENTER, width=14)
        entry_cena_36.insert(0, "17")
        entry_cena_36.grid(row=26, column=6)
    elif nazwa_36.get() == "Fartuch jałowy M":
        entry_cena_36 = Entry(root, textvariable=cena_36, justify=CENTER, width=14)
        entry_cena_36.insert(0, "15.28")
        entry_cena_36.grid(row=26, column=6)
    elif nazwa_36.get() == "Fartuch jałowy XL":
        entry_cena_36 = Entry(root, textvariable=cena_36, justify=CENTER, width=14)
        entry_cena_36.insert(0, "20.84")
        entry_cena_36.grid(row=26, column=6)
    elif nazwa_36.get() == "FasatThread BioComposite Interference Screw 8x30":
        entry_cena_36 = Entry(root, textvariable=cena_36, justify=CENTER, width=14)
        entry_cena_36.insert(0, "594")
        entry_cena_36.grid(row=26, column=6)
    elif nazwa_36.get() == "Folia operacyjna, jałowa 45cm x 55cm":
        entry_cena_36 = Entry(root, textvariable=cena_36, justify=CENTER, width=14)
        entry_cena_36.insert(0, "9.99")
        entry_cena_36.grid(row=26, column=6)
    elif nazwa_36.get() == "Gaziki 10 x 10cm":
        entry_cena_36 = Entry(root, textvariable=cena_36, justify=CENTER, width=14)
        entry_cena_36.insert(0, "0.10")
        entry_cena_36.grid(row=26, column=6)
    elif nazwa_36.get() == "Igła 0,6 x 60":
        entry_cena_36 = Entry(root, textvariable=cena_36, justify=CENTER, width=14)
        entry_cena_36.insert(0, "0.09")
        entry_cena_36.grid(row=26, column=6)
    elif nazwa_36.get() == "Igła 0,7 x 40":
        entry_cena_36 = Entry(root, textvariable=cena_36, justify=CENTER, width=14)
        entry_cena_36.insert(0, "0.05")
        entry_cena_36.grid(row=26, column=6)
    elif nazwa_36.get() == "Igła 0,8 x 40":
        entry_cena_36 = Entry(root, textvariable=cena_36, justify=CENTER, width=14)
        entry_cena_36.insert(0, "0.05")
        entry_cena_36.grid(row=26, column=6)
    elif nazwa_36.get() == "Igła 1,1 x 70":
        entry_cena_36 = Entry(root, textvariable=cena_36, justify=CENTER, width=14)
        entry_cena_36.insert(0, "0.16")
        entry_cena_36.grid(row=26, column=6)
    elif nazwa_36.get() == "Kaniulowana śruba int. biokompozytowa z osłonką jednoraz.":
        entry_cena_36 = Entry(root, textvariable=cena_36, justify=CENTER, width=14)
        entry_cena_36.insert(0, "594")
        entry_cena_36.grid(row=26, column=6)
    elif nazwa_36.get() == "Kaniulowana śruba int. biokompozytowa z pełnym gwintem":
        entry_cena_36 = Entry(root, textvariable=cena_36, justify=CENTER, width=14)
        entry_cena_36.insert(0, "594")
        entry_cena_36.grid(row=26, column=6)
    elif nazwa_36.get() == "Końcówka do Shavera":
        entry_cena_36 = Entry(root, textvariable=cena_36, justify=CENTER, width=14)
        entry_cena_36.insert(0, "270")
        entry_cena_36.grid(row=26, column=6)
    elif nazwa_36.get() == "Kotwica biokompozytowa SwiveLock":
        entry_cena_36 = Entry(root, textvariable=cena_36, justify=CENTER, width=14)
        entry_cena_36.insert(0, "918")
        entry_cena_36.grid(row=26, column=6)
    elif nazwa_36.get() == "Kotwica Corkscrew":
        entry_cena_36 = Entry(root, textvariable=cena_36, justify=CENTER, width=14)
        entry_cena_36.insert(0, "604")
        entry_cena_36.grid(row=26, column=6)
    elif nazwa_36.get() == "Kotwica FASTak":
        entry_cena_36 = Entry(root, textvariable=cena_36, justify=CENTER, width=14)
        entry_cena_36.insert(0, "432")
        entry_cena_36.grid(row=26, column=6)
    elif nazwa_36.get() == "Kotwica PEEK SwiveLock":
        entry_cena_36 = Entry(root, textvariable=cena_36, justify=CENTER, width=14)
        entry_cena_36.insert(0, "885.60")
        entry_cena_36.grid(row=26, column=6)
    elif nazwa_36.get() == "NaCl 3000ml":
        entry_cena_36 = Entry(root, textvariable=cena_36, justify=CENTER, width=14)
        entry_cena_36.insert(0, "29.72")
        entry_cena_36.grid(row=26, column=6)
    elif nazwa_36.get() == "NaCl 5000ml":
        entry_cena_36 = Entry(root, textvariable=cena_36, justify=CENTER, width=14)
        entry_cena_36.insert(0, "58.33")
        entry_cena_36.grid(row=26, column=6)
    elif nazwa_36.get() == "Nici Dafilon 2-0":
        entry_cena_36 = Entry(root, textvariable=cena_36, justify=CENTER, width=14)
        entry_cena_36.insert(0, "6.60")
        entry_cena_36.grid(row=26, column=6)
    elif nazwa_36.get() == "Nici Novosyn 2":
        entry_cena_36 = Entry(root, textvariable=cena_36, justify=CENTER, width=14)
        entry_cena_36.insert(0, "13")
        entry_cena_36.grid(row=26, column=6)
    elif nazwa_36.get() == "Nici Novosyn 2-0":
        entry_cena_36 = Entry(root, textvariable=cena_36, justify=CENTER, width=14)
        entry_cena_36.insert(0, "7.70")
        entry_cena_36.grid(row=26, column=6)
    elif nazwa_36.get() == "Nici Novosyn 3-0":
        entry_cena_36 = Entry(root, textvariable=cena_36, justify=CENTER, width=14)
        entry_cena_36.insert(0, "7.70")
        entry_cena_36.grid(row=26, column=6)
    elif nazwa_36.get() == "Nici Nylon 2-0":
        entry_cena_36 = Entry(root, textvariable=cena_36, justify=CENTER, width=14)
        entry_cena_36.insert(0, "2.50")
        entry_cena_36.grid(row=26, column=6)
    elif nazwa_36.get() == "Nici Nylon 3-0":
        entry_cena_36 = Entry(root, textvariable=cena_36, justify=CENTER, width=14)
        entry_cena_36.insert(0, "2")
        entry_cena_36.grid(row=26, column=6)
    elif nazwa_36.get() == "Nici PGLA":
        entry_cena_36 = Entry(root, textvariable=cena_36, justify=CENTER, width=14)
        entry_cena_36.insert(0, "11.60")
        entry_cena_36.grid(row=26, column=6)
    elif nazwa_36.get() == "Nici PremiCron 3":
        entry_cena_36 = Entry(root, textvariable=cena_36, justify=CENTER, width=14)
        entry_cena_36.insert(0, "6.50")
        entry_cena_36.grid(row=26, column=6)
    elif nazwa_36.get() == "Nici Vicryl 4-0":
        entry_cena_36 = Entry(root, textvariable=cena_36, justify=CENTER, width=14)
        entry_cena_36.insert(0, "7.50")
        entry_cena_36.grid(row=26, column=6)
    elif nazwa_36.get() == "Nitinol Guide Pin 1.1":
        entry_cena_36 = Entry(root, textvariable=cena_36, justify=CENTER, width=14)
        entry_cena_36.insert(0, "145.80")
        entry_cena_36.grid(row=26, column=6)
    elif nazwa_36.get() == "Osłona na przewody":
        entry_cena_36 = Entry(root, textvariable=cena_36, justify=CENTER, width=14)
        entry_cena_36.insert(0, "2.50")
        entry_cena_36.grid(row=26, column=6)
    elif nazwa_36.get() == "Ostrze Arthrex 90(86)x19x1,27":
        entry_cena_36 = Entry(root, textvariable=cena_36, justify=CENTER, width=14)
        entry_cena_36.insert(0, "216")
        entry_cena_36.grid(row=26, column=6)
    elif nazwa_36.get() == "Ostrze piły":
        entry_cena_36 = Entry(root, textvariable=cena_36, justify=CENTER, width=14)
        entry_cena_36.insert(0, "108")
        entry_cena_36.grid(row=26, column=6)
    elif nazwa_36.get() == "Pielęgniarka anest.":
        entry_cena_36 = Entry(root, textvariable=cena_36, justify=CENTER, width=14)
        entry_cena_36.insert(0, "50")
        entry_cena_36.grid(row=26, column=6)
    elif nazwa_36.get() == "Pielęgniarka instr.":
        entry_cena_36 = Entry(root, textvariable=cena_36, justify=CENTER, width=14)
        entry_cena_36.insert(0, "50")
        entry_cena_36.grid(row=26, column=6)
    elif nazwa_36.get() == "Pielęgniarka 'Noviline'":
        entry_cena_36 = Entry(root, textvariable=cena_36, justify=CENTER, width=14)
        entry_cena_36.insert(0, "30")
        entry_cena_36.grid(row=26, column=6)
    elif nazwa_36.get() == "Płytka PeekPower do osteotomii klinowej":
        entry_cena_36 = Entry(root, textvariable=cena_36, justify=CENTER, width=14)
        entry_cena_36.insert(0, "2160")
        entry_cena_36.grid(row=26, column=6)
    elif nazwa_36.get() == "Rękawice jałowe 6,5":
        entry_cena_36 = Entry(root, textvariable=cena_36, justify=CENTER, width=14)
        entry_cena_36.insert(0, "1.20")
        entry_cena_36.grid(row=26, column=6)
    elif nazwa_36.get() == "Rękawice jałowe 7,0":
        entry_cena_36 = Entry(root, textvariable=cena_36, justify=CENTER, width=14)
        entry_cena_36.insert(0, "1.20")
        entry_cena_36.grid(row=26, column=6)
    elif nazwa_36.get() == "Rękawice jałowe 7,5":
        entry_cena_36 = Entry(root, textvariable=cena_36, justify=CENTER, width=14)
        entry_cena_36.insert(0, "1.20")
        entry_cena_36.grid(row=26, column=6)
    elif nazwa_36.get() == "Rękawice jałowe 8,00":
        entry_cena_36 = Entry(root, textvariable=cena_36, justify=CENTER, width=14)
        entry_cena_36.insert(0, "1.20")
        entry_cena_36.grid(row=26, column=6)
    elif nazwa_36.get() == "Rękojeść Interpulse wysokoprzepływowa":
        entry_cena_36 = Entry(root, textvariable=cena_36, justify=CENTER, width=14)
        entry_cena_36.insert(0, "216")
        entry_cena_36.grid(row=26, column=6)
    elif nazwa_36.get() == "Serweta":
        entry_cena_36 = Entry(root, textvariable=cena_36, justify=CENTER, width=14)
        entry_cena_36.insert(0, "6")
        entry_cena_36.grid(row=26, column=6)
    elif nazwa_36.get() == "Simplex Hv z Gentamycyna 10x40g":
        entry_cena_36 = Entry(root, textvariable=cena_36, justify=CENTER, width=14)
        entry_cena_36.insert(0, "162")
        entry_cena_36.grid(row=26, column=6)
    elif nazwa_36.get() == "Skalpel 11":
        entry_cena_36 = Entry(root, textvariable=cena_36, justify=CENTER, width=14)
        entry_cena_36.insert(0, "0.38")
        entry_cena_36.grid(row=26, column=6)
    elif nazwa_36.get() == "Skalpel 13":
        entry_cena_36 = Entry(root, textvariable=cena_36, justify=CENTER, width=14)
        entry_cena_36.insert(0, "1")
        entry_cena_36.grid(row=26, column=6)
    elif nazwa_36.get() == "Skalpel 22":
        entry_cena_36 = Entry(root, textvariable=cena_36, justify=CENTER, width=14)
        entry_cena_36.insert(0, "1")
        entry_cena_36.grid(row=26, column=6)
    elif nazwa_36.get() == "Śruba blokująca PeekPower do osteotomii":
        entry_cena_36 = Entry(root, textvariable=cena_36, justify=CENTER, width=14)
        entry_cena_36.insert(0, "194")
        entry_cena_36.grid(row=26, column=6)
    elif nazwa_36.get() == "System do mieszania próżniowego":
        entry_cena_36 = Entry(root, textvariable=cena_36, justify=CENTER, width=14)
        entry_cena_36.insert(0, "216")
        entry_cena_36.grid(row=26, column=6)
    elif nazwa_36.get() == "System wprowadzania implantów ACL TightRope":
        entry_cena_36 = Entry(root, textvariable=cena_36, justify=CENTER, width=14)
        entry_cena_36.insert(0, "702")
        entry_cena_36.grid(row=26, column=6)
    elif nazwa_36.get() == "Szew FiberWire 2":
        entry_cena_36 = Entry(root, textvariable=cena_36, justify=CENTER, width=14)
        entry_cena_36.insert(0, "86.40")
        entry_cena_36.grid(row=26, column=6)
    elif nazwa_36.get() == "Taśma przylepna 10x50":
        entry_cena_36 = Entry(root, textvariable=cena_36, justify=CENTER, width=14)
        entry_cena_36.insert(0, "1.04")
        entry_cena_36.grid(row=26, column=6)
    elif nazwa_36.get() == "Triathlon elem. udowy lewy":
        entry_cena_36 = Entry(root, textvariable=cena_36, justify=CENTER, width=14)
        entry_cena_36.insert(0, "3132")
        entry_cena_36.grid(row=26, column=6)
    elif nazwa_36.get() == "Triathlon PS wkładka x3-9mm #4":
        entry_cena_36 = Entry(root, textvariable=cena_36, justify=CENTER, width=14)
        entry_cena_36.insert(0, "756")
        entry_cena_36.grid(row=26, column=6)
    elif nazwa_36.get() == "Triathlon taca piszczelowa":
        entry_cena_36 = Entry(root, textvariable=cena_36, justify=CENTER, width=14)
        entry_cena_36.insert(0, "1296")
        entry_cena_36.grid(row=26, column=6)
    elif nazwa_36.get() == "Wkłady 3L z żelem":
        entry_cena_36 = Entry(root, textvariable=cena_36, justify=CENTER, width=14)
        entry_cena_36.insert(0, "10.26")
        entry_cena_36.grid(row=26, column=6)
    elif nazwa_36.get() == "Zestaw do artroskopii":
        entry_cena_36 = Entry(root, textvariable=cena_36, justify=CENTER, width=14)
        entry_cena_36.insert(0, "67")
        entry_cena_36.grid(row=26, column=6)
    elif nazwa_36.get() == "Zestaw do artroskopii barku":
        entry_cena_36 = Entry(root, textvariable=cena_36, justify=CENTER, width=14)
        entry_cena_36.insert(0, "108")
        entry_cena_36.grid(row=26, column=6)
    elif nazwa_36.get() == "Zestaw do drenażu":
        entry_cena_36 = Entry(root, textvariable=cena_36, justify=CENTER, width=14)
        entry_cena_36.insert(0, "14.23")
        entry_cena_36.grid(row=26, column=6)
    elif nazwa_36.get() == "Zestaw ortopedyczny":
        entry_cena_36 = Entry(root, textvariable=cena_36, justify=CENTER, width=14)
        entry_cena_36.insert(0, "28.08")
        entry_cena_36.grid(row=26, column=6)
    elif nazwa_36.get() == "Gaziki 20 x 10cm":
        entry_cena_36 = Entry(root, textvariable=cena_36, justify=CENTER, width=14)
        entry_cena_36.insert(0, "0.46")
        entry_cena_36.grid(row=26, column=6)
    else:
        entry_cena_36 = Entry(root, textvariable=cena_36, justify=CENTER, width=14, bg="#ffff00")
        entry_cena_36.insert(0, "0")
        entry_cena_36.grid(row=26, column=6)

    if nazwa_37.get() == "--puste--":
        entry_cena_37 = Entry(root, textvariable=cena_37, justify=CENTER, width=14)
        entry_cena_37.insert(0, "0")
        entry_cena_37.grid(row=27, column=6)
    elif nazwa_37.get() == "Ablator":
        entry_cena_37 = Entry(root, textvariable=cena_37, justify=CENTER, width=14)
        entry_cena_37.insert(0, "572")
        entry_cena_37.grid(row=27, column=6)
    elif nazwa_37.get() == "Anestezjolog":
        entry_cena_37 = Entry(root, textvariable=cena_37, justify=CENTER, width=14, bg="#ffff00")
        entry_cena_37.insert(0, "350")
        entry_cena_37.grid(row=27, column=6)
    elif nazwa_37.get() == "Butelka 400ml do długotrwałego odsysania ran j.u. sterylna":
        entry_cena_37 = Entry(root, textvariable=cena_37, justify=CENTER, width=14)
        entry_cena_37.insert(0, "4")
        entry_cena_37.grid(row=27, column=6)
    elif nazwa_37.get() == "Doba":
        entry_cena_37 = Entry(root, textvariable=cena_37, justify=CENTER, width=14)
        entry_cena_37.insert(0, "700")
        entry_cena_37.grid(row=27, column=6)
    elif nazwa_37.get() == "Dren łączący do ssaka Grena":
        entry_cena_37 = Entry(root, textvariable=cena_37, justify=CENTER, width=14)
        entry_cena_37.insert(0, "5")
        entry_cena_37.grid(row=27, column=6)
    elif nazwa_37.get() == "Dren Redona Ch 16 dł. 800mm z trokarem":
        entry_cena_37 = Entry(root, textvariable=cena_37, justify=CENTER, width=14)
        entry_cena_37.insert(0, "29.74")
        entry_cena_37.grid(row=27, column=6)
    elif nazwa_37.get() == "Dren do pompy Artrex":
        entry_cena_37 = Entry(root, textvariable=cena_37, justify=CENTER, width=14)
        entry_cena_37.insert(0, "108")
        entry_cena_37.grid(row=27, column=6)
    elif nazwa_37.get() == "Drut wiercący 2,4 x 311":
        entry_cena_37 = Entry(root, textvariable=cena_37, justify=CENTER, width=14)
        entry_cena_37.insert(0, "139.60")
        entry_cena_37.grid(row=27, column=6)
    elif nazwa_37.get() == "Fartuch jałowy L":
        entry_cena_37 = Entry(root, textvariable=cena_37, justify=CENTER, width=14)
        entry_cena_37.insert(0, "17")
        entry_cena_37.grid(row=27, column=6)
    elif nazwa_37.get() == "Fartuch jałowy M":
        entry_cena_37 = Entry(root, textvariable=cena_37, justify=CENTER, width=14)
        entry_cena_37.insert(0, "15.28")
        entry_cena_37.grid(row=27, column=6)
    elif nazwa_37.get() == "Fartuch jałowy XL":
        entry_cena_37 = Entry(root, textvariable=cena_37, justify=CENTER, width=14)
        entry_cena_37.insert(0, "20.84")
        entry_cena_37.grid(row=27, column=6)
    elif nazwa_37.get() == "FasatThread BioComposite Interference Screw 8x30":
        entry_cena_37 = Entry(root, textvariable=cena_37, justify=CENTER, width=14)
        entry_cena_37.insert(0, "594")
        entry_cena_37.grid(row=27, column=6)
    elif nazwa_37.get() == "Folia operacyjna, jałowa 45cm x 55cm":
        entry_cena_37 = Entry(root, textvariable=cena_37, justify=CENTER, width=14)
        entry_cena_37.insert(0, "9.99")
        entry_cena_37.grid(row=27, column=6)
    elif nazwa_37.get() == "Gaziki 10 x 10cm":
        entry_cena_37 = Entry(root, textvariable=cena_37, justify=CENTER, width=14)
        entry_cena_37.insert(0, "0.10")
        entry_cena_37.grid(row=27, column=6)
    elif nazwa_37.get() == "Igła 0,6 x 60":
        entry_cena_37 = Entry(root, textvariable=cena_37, justify=CENTER, width=14)
        entry_cena_37.insert(0, "0.09")
        entry_cena_37.grid(row=27, column=6)
    elif nazwa_37.get() == "Igła 0,7 x 40":
        entry_cena_37 = Entry(root, textvariable=cena_37, justify=CENTER, width=14)
        entry_cena_37.insert(0, "0.05")
        entry_cena_37.grid(row=27, column=6)
    elif nazwa_37.get() == "Igła 0,8 x 40":
        entry_cena_37 = Entry(root, textvariable=cena_37, justify=CENTER, width=14)
        entry_cena_37.insert(0, "0.05")
        entry_cena_37.grid(row=27, column=6)
    elif nazwa_37.get() == "Igła 1,1 x 70":
        entry_cena_37 = Entry(root, textvariable=cena_37, justify=CENTER, width=14)
        entry_cena_37.insert(0, "0.16")
        entry_cena_37.grid(row=27, column=6)
    elif nazwa_37.get() == "Kaniulowana śruba int. biokompozytowa z osłonką jednoraz.":
        entry_cena_37 = Entry(root, textvariable=cena_37, justify=CENTER, width=14)
        entry_cena_37.insert(0, "594")
        entry_cena_37.grid(row=27, column=6)
    elif nazwa_37.get() == "Kaniulowana śruba int. biokompozytowa z pełnym gwintem":
        entry_cena_37 = Entry(root, textvariable=cena_37, justify=CENTER, width=14)
        entry_cena_37.insert(0, "594")
        entry_cena_37.grid(row=27, column=6)
    elif nazwa_37.get() == "Końcówka do Shavera":
        entry_cena_37 = Entry(root, textvariable=cena_37, justify=CENTER, width=14)
        entry_cena_37.insert(0, "270")
        entry_cena_37.grid(row=27, column=6)
    elif nazwa_37.get() == "Kotwica biokompozytowa SwiveLock":
        entry_cena_37 = Entry(root, textvariable=cena_37, justify=CENTER, width=14)
        entry_cena_37.insert(0, "918")
        entry_cena_37.grid(row=27, column=6)
    elif nazwa_37.get() == "Kotwica Corkscrew":
        entry_cena_37 = Entry(root, textvariable=cena_37, justify=CENTER, width=14)
        entry_cena_37.insert(0, "604")
        entry_cena_37.grid(row=27, column=6)
    elif nazwa_37.get() == "Kotwica FASTak":
        entry_cena_37 = Entry(root, textvariable=cena_37, justify=CENTER, width=14)
        entry_cena_37.insert(0, "432")
        entry_cena_37.grid(row=27, column=6)
    elif nazwa_37.get() == "Kotwica PEEK SwiveLock":
        entry_cena_37 = Entry(root, textvariable=cena_37, justify=CENTER, width=14)
        entry_cena_37.insert(0, "885.60")
        entry_cena_37.grid(row=27, column=6)
    elif nazwa_37.get() == "NaCl 3000ml":
        entry_cena_37 = Entry(root, textvariable=cena_37, justify=CENTER, width=14)
        entry_cena_37.insert(0, "29.72")
        entry_cena_37.grid(row=27, column=6)
    elif nazwa_37.get() == "NaCl 5000ml":
        entry_cena_37 = Entry(root, textvariable=cena_37, justify=CENTER, width=14)
        entry_cena_37.insert(0, "58.33")
        entry_cena_37.grid(row=27, column=6)
    elif nazwa_37.get() == "Nici Dafilon 2-0":
        entry_cena_37 = Entry(root, textvariable=cena_37, justify=CENTER, width=14)
        entry_cena_37.insert(0, "6.60")
        entry_cena_37.grid(row=27, column=6)
    elif nazwa_37.get() == "Nici Novosyn 2":
        entry_cena_37 = Entry(root, textvariable=cena_37, justify=CENTER, width=14)
        entry_cena_37.insert(0, "13")
        entry_cena_37.grid(row=27, column=6)
    elif nazwa_37.get() == "Nici Novosyn 2-0":
        entry_cena_37 = Entry(root, textvariable=cena_37, justify=CENTER, width=14)
        entry_cena_37.insert(0, "7.70")
        entry_cena_37.grid(row=27, column=6)
    elif nazwa_37.get() == "Nici Novosyn 3-0":
        entry_cena_37 = Entry(root, textvariable=cena_37, justify=CENTER, width=14)
        entry_cena_37.insert(0, "7.70")
        entry_cena_37.grid(row=27, column=6)
    elif nazwa_37.get() == "Nici Nylon 2-0":
        entry_cena_37 = Entry(root, textvariable=cena_37, justify=CENTER, width=14)
        entry_cena_37.insert(0, "2.50")
        entry_cena_37.grid(row=27, column=6)
    elif nazwa_37.get() == "Nici Nylon 3-0":
        entry_cena_37 = Entry(root, textvariable=cena_37, justify=CENTER, width=14)
        entry_cena_37.insert(0, "2")
        entry_cena_37.grid(row=27, column=6)
    elif nazwa_37.get() == "Nici PGLA":
        entry_cena_37 = Entry(root, textvariable=cena_37, justify=CENTER, width=14)
        entry_cena_37.insert(0, "11.60")
        entry_cena_37.grid(row=27, column=6)
    elif nazwa_37.get() == "Nici PremiCron 3":
        entry_cena_37 = Entry(root, textvariable=cena_37, justify=CENTER, width=14)
        entry_cena_37.insert(0, "6.50")
        entry_cena_37.grid(row=27, column=6)
    elif nazwa_37.get() == "Nici Vicryl 4-0":
        entry_cena_37 = Entry(root, textvariable=cena_37, justify=CENTER, width=14)
        entry_cena_37.insert(0, "7.50")
        entry_cena_37.grid(row=27, column=6)
    elif nazwa_37.get() == "Nitinol Guide Pin 1.1":
        entry_cena_37 = Entry(root, textvariable=cena_37, justify=CENTER, width=14)
        entry_cena_37.insert(0, "145.80")
        entry_cena_37.grid(row=27, column=6)
    elif nazwa_37.get() == "Osłona na przewody":
        entry_cena_37 = Entry(root, textvariable=cena_37, justify=CENTER, width=14)
        entry_cena_37.insert(0, "2.50")
        entry_cena_37.grid(row=27, column=6)
    elif nazwa_37.get() == "Ostrze Arthrex 90(86)x19x1,27":
        entry_cena_37 = Entry(root, textvariable=cena_37, justify=CENTER, width=14)
        entry_cena_37.insert(0, "216")
        entry_cena_37.grid(row=27, column=6)
    elif nazwa_37.get() == "Ostrze piły":
        entry_cena_37 = Entry(root, textvariable=cena_37, justify=CENTER, width=14)
        entry_cena_37.insert(0, "108")
        entry_cena_37.grid(row=27, column=6)
    elif nazwa_37.get() == "Pielęgniarka anest.":
        entry_cena_37 = Entry(root, textvariable=cena_37, justify=CENTER, width=14)
        entry_cena_37.insert(0, "50")
        entry_cena_37.grid(row=27, column=6)
    elif nazwa_37.get() == "Pielęgniarka instr.":
        entry_cena_37 = Entry(root, textvariable=cena_37, justify=CENTER, width=14)
        entry_cena_37.insert(0, "50")
        entry_cena_37.grid(row=27, column=6)
    elif nazwa_37.get() == "Pielęgniarka 'Noviline'":
        entry_cena_37 = Entry(root, textvariable=cena_37, justify=CENTER, width=14)
        entry_cena_37.insert(0, "30")
        entry_cena_37.grid(row=27, column=6)
    elif nazwa_37.get() == "Płytka PeekPower do osteotomii klinowej":
        entry_cena_37 = Entry(root, textvariable=cena_37, justify=CENTER, width=14)
        entry_cena_37.insert(0, "2160")
        entry_cena_37.grid(row=27, column=6)
    elif nazwa_37.get() == "Rękawice jałowe 6,5":
        entry_cena_37 = Entry(root, textvariable=cena_37, justify=CENTER, width=14)
        entry_cena_37.insert(0, "1.20")
        entry_cena_37.grid(row=27, column=6)
    elif nazwa_37.get() == "Rękawice jałowe 7,0":
        entry_cena_37 = Entry(root, textvariable=cena_37, justify=CENTER, width=14)
        entry_cena_37.insert(0, "1.20")
        entry_cena_37.grid(row=27, column=6)
    elif nazwa_37.get() == "Rękawice jałowe 7,5":
        entry_cena_37 = Entry(root, textvariable=cena_37, justify=CENTER, width=14)
        entry_cena_37.insert(0, "1.20")
        entry_cena_37.grid(row=27, column=6)
    elif nazwa_37.get() == "Rękawice jałowe 8,00":
        entry_cena_37 = Entry(root, textvariable=cena_37, justify=CENTER, width=14)
        entry_cena_37.insert(0, "1.20")
        entry_cena_37.grid(row=27, column=6)
    elif nazwa_37.get() == "Rękojeść Interpulse wysokoprzepływowa":
        entry_cena_37 = Entry(root, textvariable=cena_37, justify=CENTER, width=14)
        entry_cena_37.insert(0, "216")
        entry_cena_37.grid(row=27, column=6)
    elif nazwa_37.get() == "Serweta":
        entry_cena_37 = Entry(root, textvariable=cena_37, justify=CENTER, width=14)
        entry_cena_37.insert(0, "6")
        entry_cena_37.grid(row=27, column=6)
    elif nazwa_37.get() == "Simplex Hv z Gentamycyna 10x40g":
        entry_cena_37 = Entry(root, textvariable=cena_37, justify=CENTER, width=14)
        entry_cena_37.insert(0, "162")
        entry_cena_37.grid(row=27, column=6)
    elif nazwa_37.get() == "Skalpel 11":
        entry_cena_37 = Entry(root, textvariable=cena_37, justify=CENTER, width=14)
        entry_cena_37.insert(0, "0.38")
        entry_cena_37.grid(row=27, column=6)
    elif nazwa_37.get() == "Skalpel 13":
        entry_cena_37 = Entry(root, textvariable=cena_37, justify=CENTER, width=14)
        entry_cena_37.insert(0, "1")
        entry_cena_37.grid(row=27, column=6)
    elif nazwa_37.get() == "Skalpel 22":
        entry_cena_37 = Entry(root, textvariable=cena_37, justify=CENTER, width=14)
        entry_cena_37.insert(0, "1")
        entry_cena_37.grid(row=27, column=6)
    elif nazwa_37.get() == "Śruba blokująca PeekPower do osteotomii":
        entry_cena_37 = Entry(root, textvariable=cena_37, justify=CENTER, width=14)
        entry_cena_37.insert(0, "194")
        entry_cena_37.grid(row=27, column=6)
    elif nazwa_37.get() == "System do mieszania próżniowego":
        entry_cena_37 = Entry(root, textvariable=cena_37, justify=CENTER, width=14)
        entry_cena_37.insert(0, "216")
        entry_cena_37.grid(row=27, column=6)
    elif nazwa_37.get() == "System wprowadzania implantów ACL TightRope":
        entry_cena_37 = Entry(root, textvariable=cena_37, justify=CENTER, width=14)
        entry_cena_37.insert(0, "702")
        entry_cena_37.grid(row=27, column=6)
    elif nazwa_37.get() == "Szew FiberWire 2":
        entry_cena_37 = Entry(root, textvariable=cena_37, justify=CENTER, width=14)
        entry_cena_37.insert(0, "86.40")
        entry_cena_37.grid(row=27, column=6)
    elif nazwa_37.get() == "Taśma przylepna 10x50":
        entry_cena_37 = Entry(root, textvariable=cena_37, justify=CENTER, width=14)
        entry_cena_37.insert(0, "1.04")
        entry_cena_37.grid(row=27, column=6)
    elif nazwa_37.get() == "Triathlon elem. udowy lewy":
        entry_cena_37 = Entry(root, textvariable=cena_37, justify=CENTER, width=14)
        entry_cena_37.insert(0, "3132")
        entry_cena_37.grid(row=27, column=6)
    elif nazwa_37.get() == "Triathlon PS wkładka x3-9mm #4":
        entry_cena_37 = Entry(root, textvariable=cena_37, justify=CENTER, width=14)
        entry_cena_37.insert(0, "756")
        entry_cena_37.grid(row=27, column=6)
    elif nazwa_37.get() == "Triathlon taca piszczelowa":
        entry_cena_37 = Entry(root, textvariable=cena_37, justify=CENTER, width=14)
        entry_cena_37.insert(0, "1296")
        entry_cena_37.grid(row=27, column=6)
    elif nazwa_37.get() == "Wkłady 3L z żelem":
        entry_cena_37 = Entry(root, textvariable=cena_37, justify=CENTER, width=14)
        entry_cena_37.insert(0, "10.26")
        entry_cena_37.grid(row=27, column=6)
    elif nazwa_37.get() == "Zestaw do artroskopii":
        entry_cena_37 = Entry(root, textvariable=cena_37, justify=CENTER, width=14)
        entry_cena_37.insert(0, "67")
        entry_cena_37.grid(row=27, column=6)
    elif nazwa_37.get() == "Zestaw do artroskopii barku":
        entry_cena_37 = Entry(root, textvariable=cena_37, justify=CENTER, width=14)
        entry_cena_37.insert(0, "108")
        entry_cena_37.grid(row=27, column=6)
    elif nazwa_37.get() == "Zestaw do drenażu":
        entry_cena_37 = Entry(root, textvariable=cena_37, justify=CENTER, width=14)
        entry_cena_37.insert(0, "14.23")
        entry_cena_37.grid(row=27, column=6)
    elif nazwa_37.get() == "Zestaw ortopedyczny":
        entry_cena_37 = Entry(root, textvariable=cena_37, justify=CENTER, width=14)
        entry_cena_37.insert(0, "28.08")
        entry_cena_37.grid(row=27, column=6)
    elif nazwa_37.get() == "Gaziki 20 x 10cm":
        entry_cena_37 = Entry(root, textvariable=cena_37, justify=CENTER, width=14)
        entry_cena_37.insert(0, "0.46")
        entry_cena_37.grid(row=27, column=6)
    else:
        entry_cena_37 = Entry(root, textvariable=cena_37, justify=CENTER, width=14, bg="#ffff00")
        entry_cena_37.insert(0, "0")
        entry_cena_37.grid(row=27, column=6)

    if nazwa_38.get() == "--puste--":
        entry_cena_38 = Entry(root, textvariable=cena_38, justify=CENTER, width=14)
        entry_cena_38.insert(0, "0")
        entry_cena_38.grid(row=28, column=6)
    elif nazwa_38.get() == "Ablator":
        entry_cena_38 = Entry(root, textvariable=cena_38, justify=CENTER, width=14)
        entry_cena_38.insert(0, "572")
        entry_cena_38.grid(row=28, column=6)
    elif nazwa_38.get() == "Anestezjolog":
        entry_cena_38 = Entry(root, textvariable=cena_38, justify=CENTER, width=14, bg="#ffff00")
        entry_cena_38.insert(0, "350")
        entry_cena_38.grid(row=28, column=6)
    elif nazwa_38.get() == "Butelka 400ml do długotrwałego odsysania ran j.u. sterylna":
        entry_cena_38 = Entry(root, textvariable=cena_38, justify=CENTER, width=14)
        entry_cena_38.insert(0, "4")
        entry_cena_38.grid(row=28, column=6)
    elif nazwa_38.get() == "Doba":
        entry_cena_38 = Entry(root, textvariable=cena_38, justify=CENTER, width=14)
        entry_cena_38.insert(0, "700")
        entry_cena_38.grid(row=28, column=6)
    elif nazwa_38.get() == "Dren łączący do ssaka Grena":
        entry_cena_38 = Entry(root, textvariable=cena_38, justify=CENTER, width=14)
        entry_cena_38.insert(0, "5")
        entry_cena_38.grid(row=28, column=6)
    elif nazwa_38.get() == "Dren Redona Ch 16 dł. 800mm z trokarem":
        entry_cena_38 = Entry(root, textvariable=cena_38, justify=CENTER, width=14)
        entry_cena_38.insert(0, "29.74")
        entry_cena_38.grid(row=28, column=6)
    elif nazwa_38.get() == "Dren do pompy Artrex":
        entry_cena_38 = Entry(root, textvariable=cena_38, justify=CENTER, width=14)
        entry_cena_38.insert(0, "108")
        entry_cena_38.grid(row=28, column=6)
    elif nazwa_38.get() == "Drut wiercący 2,4 x 311":
        entry_cena_38 = Entry(root, textvariable=cena_38, justify=CENTER, width=14)
        entry_cena_38.insert(0, "139.60")
        entry_cena_38.grid(row=28, column=6)
    elif nazwa_38.get() == "Fartuch jałowy L":
        entry_cena_38 = Entry(root, textvariable=cena_38, justify=CENTER, width=14)
        entry_cena_38.insert(0, "17")
        entry_cena_38.grid(row=28, column=6)
    elif nazwa_38.get() == "Fartuch jałowy M":
        entry_cena_38 = Entry(root, textvariable=cena_38, justify=CENTER, width=14)
        entry_cena_38.insert(0, "15.28")
        entry_cena_38.grid(row=28, column=6)
    elif nazwa_38.get() == "Fartuch jałowy XL":
        entry_cena_38 = Entry(root, textvariable=cena_38, justify=CENTER, width=14)
        entry_cena_38.insert(0, "20.84")
        entry_cena_38.grid(row=28, column=6)
    elif nazwa_38.get() == "FasatThread BioComposite Interference Screw 8x30":
        entry_cena_38 = Entry(root, textvariable=cena_38, justify=CENTER, width=14)
        entry_cena_38.insert(0, "594")
        entry_cena_38.grid(row=28, column=6)
    elif nazwa_38.get() == "Folia operacyjna, jałowa 45cm x 55cm":
        entry_cena_38 = Entry(root, textvariable=cena_38, justify=CENTER, width=14)
        entry_cena_38.insert(0, "9.99")
        entry_cena_38.grid(row=28, column=6)
    elif nazwa_38.get() == "Gaziki 10 x 10cm":
        entry_cena_38 = Entry(root, textvariable=cena_38, justify=CENTER, width=14)
        entry_cena_38.insert(0, "0.10")
        entry_cena_38.grid(row=28, column=6)
    elif nazwa_38.get() == "Igła 0,6 x 60":
        entry_cena_38 = Entry(root, textvariable=cena_38, justify=CENTER, width=14)
        entry_cena_38.insert(0, "0.09")
        entry_cena_38.grid(row=28, column=6)
    elif nazwa_38.get() == "Igła 0,7 x 40":
        entry_cena_38 = Entry(root, textvariable=cena_38, justify=CENTER, width=14)
        entry_cena_38.insert(0, "0.05")
        entry_cena_38.grid(row=28, column=6)
    elif nazwa_38.get() == "Igła 0,8 x 40":
        entry_cena_38 = Entry(root, textvariable=cena_38, justify=CENTER, width=14)
        entry_cena_38.insert(0, "0.05")
        entry_cena_38.grid(row=28, column=6)
    elif nazwa_38.get() == "Igła 1,1 x 70":
        entry_cena_38 = Entry(root, textvariable=cena_38, justify=CENTER, width=14)
        entry_cena_38.insert(0, "0.16")
        entry_cena_38.grid(row=28, column=6)
    elif nazwa_38.get() == "Kaniulowana śruba int. biokompozytowa z osłonką jednoraz.":
        entry_cena_38 = Entry(root, textvariable=cena_38, justify=CENTER, width=14)
        entry_cena_38.insert(0, "594")
        entry_cena_38.grid(row=28, column=6)
    elif nazwa_38.get() == "Kaniulowana śruba int. biokompozytowa z pełnym gwintem":
        entry_cena_38 = Entry(root, textvariable=cena_38, justify=CENTER, width=14)
        entry_cena_38.insert(0, "594")
        entry_cena_38.grid(row=28, column=6)
    elif nazwa_38.get() == "Końcówka do Shavera":
        entry_cena_38 = Entry(root, textvariable=cena_38, justify=CENTER, width=14)
        entry_cena_38.insert(0, "270")
        entry_cena_38.grid(row=28, column=6)
    elif nazwa_38.get() == "Kotwica biokompozytowa SwiveLock":
        entry_cena_38 = Entry(root, textvariable=cena_38, justify=CENTER, width=14)
        entry_cena_38.insert(0, "918")
        entry_cena_38.grid(row=28, column=6)
    elif nazwa_38.get() == "Kotwica Corkscrew":
        entry_cena_38 = Entry(root, textvariable=cena_38, justify=CENTER, width=14)
        entry_cena_38.insert(0, "604")
        entry_cena_38.grid(row=28, column=6)
    elif nazwa_38.get() == "Kotwica FASTak":
        entry_cena_38 = Entry(root, textvariable=cena_38, justify=CENTER, width=14)
        entry_cena_38.insert(0, "432")
        entry_cena_38.grid(row=28, column=6)
    elif nazwa_38.get() == "Kotwica PEEK SwiveLock":
        entry_cena_38 = Entry(root, textvariable=cena_38, justify=CENTER, width=14)
        entry_cena_38.insert(0, "885.60")
        entry_cena_38.grid(row=28, column=6)
    elif nazwa_38.get() == "NaCl 3000ml":
        entry_cena_38 = Entry(root, textvariable=cena_38, justify=CENTER, width=14)
        entry_cena_38.insert(0, "29.72")
        entry_cena_38.grid(row=28, column=6)
    elif nazwa_38.get() == "NaCl 5000ml":
        entry_cena_38 = Entry(root, textvariable=cena_38, justify=CENTER, width=14)
        entry_cena_38.insert(0, "58.33")
        entry_cena_38.grid(row=28, column=6)
    elif nazwa_38.get() == "Nici Dafilon 2-0":
        entry_cena_38 = Entry(root, textvariable=cena_38, justify=CENTER, width=14)
        entry_cena_38.insert(0, "6.60")
        entry_cena_38.grid(row=28, column=6)
    elif nazwa_38.get() == "Nici Novosyn 2":
        entry_cena_38 = Entry(root, textvariable=cena_38, justify=CENTER, width=14)
        entry_cena_38.insert(0, "13")
        entry_cena_38.grid(row=28, column=6)
    elif nazwa_38.get() == "Nici Novosyn 2-0":
        entry_cena_38 = Entry(root, textvariable=cena_38, justify=CENTER, width=14)
        entry_cena_38.insert(0, "7.70")
        entry_cena_38.grid(row=28, column=6)
    elif nazwa_38.get() == "Nici Novosyn 3-0":
        entry_cena_38 = Entry(root, textvariable=cena_38, justify=CENTER, width=14)
        entry_cena_38.insert(0, "7.70")
        entry_cena_38.grid(row=28, column=6)
    elif nazwa_38.get() == "Nici Nylon 2-0":
        entry_cena_38 = Entry(root, textvariable=cena_38, justify=CENTER, width=14)
        entry_cena_38.insert(0, "2.50")
        entry_cena_38.grid(row=28, column=6)
    elif nazwa_38.get() == "Nici Nylon 3-0":
        entry_cena_38 = Entry(root, textvariable=cena_38, justify=CENTER, width=14)
        entry_cena_38.insert(0, "2")
        entry_cena_38.grid(row=28, column=6)
    elif nazwa_38.get() == "Nici PGLA":
        entry_cena_38 = Entry(root, textvariable=cena_38, justify=CENTER, width=14)
        entry_cena_38.insert(0, "11.60")
        entry_cena_38.grid(row=28, column=6)
    elif nazwa_38.get() == "Nici PremiCron 3":
        entry_cena_38 = Entry(root, textvariable=cena_38, justify=CENTER, width=14)
        entry_cena_38.insert(0, "6.50")
        entry_cena_38.grid(row=28, column=6)
    elif nazwa_38.get() == "Nici Vicryl 4-0":
        entry_cena_38 = Entry(root, textvariable=cena_38, justify=CENTER, width=14)
        entry_cena_38.insert(0, "7.50")
        entry_cena_38.grid(row=28, column=6)
    elif nazwa_38.get() == "Nitinol Guide Pin 1.1":
        entry_cena_38 = Entry(root, textvariable=cena_38, justify=CENTER, width=14)
        entry_cena_38.insert(0, "145.80")
        entry_cena_38.grid(row=28, column=6)
    elif nazwa_38.get() == "Osłona na przewody":
        entry_cena_38 = Entry(root, textvariable=cena_38, justify=CENTER, width=14)
        entry_cena_38.insert(0, "2.50")
        entry_cena_38.grid(row=28, column=6)
    elif nazwa_38.get() == "Ostrze Arthrex 90(86)x19x1,27":
        entry_cena_38 = Entry(root, textvariable=cena_38, justify=CENTER, width=14)
        entry_cena_38.insert(0, "216")
        entry_cena_38.grid(row=28, column=6)
    elif nazwa_38.get() == "Ostrze piły":
        entry_cena_38 = Entry(root, textvariable=cena_38, justify=CENTER, width=14)
        entry_cena_38.insert(0, "108")
        entry_cena_38.grid(row=28, column=6)
    elif nazwa_38.get() == "Pielęgniarka anest.":
        entry_cena_38 = Entry(root, textvariable=cena_38, justify=CENTER, width=14)
        entry_cena_38.insert(0, "50")
        entry_cena_38.grid(row=28, column=6)
    elif nazwa_38.get() == "Pielęgniarka instr.":
        entry_cena_38 = Entry(root, textvariable=cena_38, justify=CENTER, width=14)
        entry_cena_38.insert(0, "50")
        entry_cena_38.grid(row=28, column=6)
    elif nazwa_38.get() == "Pielęgniarka 'Noviline'":
        entry_cena_38 = Entry(root, textvariable=cena_38, justify=CENTER, width=14)
        entry_cena_38.insert(0, "30")
        entry_cena_38.grid(row=28, column=6)
    elif nazwa_38.get() == "Płytka PeekPower do osteotomii klinowej":
        entry_cena_38 = Entry(root, textvariable=cena_38, justify=CENTER, width=14)
        entry_cena_38.insert(0, "2160")
        entry_cena_38.grid(row=28, column=6)
    elif nazwa_38.get() == "Rękawice jałowe 6,5":
        entry_cena_38 = Entry(root, textvariable=cena_38, justify=CENTER, width=14)
        entry_cena_38.insert(0, "1.20")
        entry_cena_38.grid(row=28, column=6)
    elif nazwa_38.get() == "Rękawice jałowe 7,0":
        entry_cena_38 = Entry(root, textvariable=cena_38, justify=CENTER, width=14)
        entry_cena_38.insert(0, "1.20")
        entry_cena_38.grid(row=28, column=6)
    elif nazwa_38.get() == "Rękawice jałowe 7,5":
        entry_cena_38 = Entry(root, textvariable=cena_38, justify=CENTER, width=14)
        entry_cena_38.insert(0, "1.20")
        entry_cena_38.grid(row=28, column=6)
    elif nazwa_38.get() == "Rękawice jałowe 8,00":
        entry_cena_38 = Entry(root, textvariable=cena_38, justify=CENTER, width=14)
        entry_cena_38.insert(0, "1.20")
        entry_cena_38.grid(row=28, column=6)
    elif nazwa_38.get() == "Rękojeść Interpulse wysokoprzepływowa":
        entry_cena_38 = Entry(root, textvariable=cena_38, justify=CENTER, width=14)
        entry_cena_38.insert(0, "216")
        entry_cena_38.grid(row=28, column=6)
    elif nazwa_38.get() == "Serweta":
        entry_cena_38 = Entry(root, textvariable=cena_38, justify=CENTER, width=14)
        entry_cena_38.insert(0, "6")
        entry_cena_38.grid(row=28, column=6)
    elif nazwa_38.get() == "Simplex Hv z Gentamycyna 10x40g":
        entry_cena_38 = Entry(root, textvariable=cena_38, justify=CENTER, width=14)
        entry_cena_38.insert(0, "162")
        entry_cena_38.grid(row=28, column=6)
    elif nazwa_38.get() == "Skalpel 11":
        entry_cena_38 = Entry(root, textvariable=cena_38, justify=CENTER, width=14)
        entry_cena_38.insert(0, "0.38")
        entry_cena_38.grid(row=28, column=6)
    elif nazwa_38.get() == "Skalpel 13":
        entry_cena_38 = Entry(root, textvariable=cena_38, justify=CENTER, width=14)
        entry_cena_38.insert(0, "1")
        entry_cena_38.grid(row=28, column=6)
    elif nazwa_38.get() == "Skalpel 22":
        entry_cena_38 = Entry(root, textvariable=cena_38, justify=CENTER, width=14)
        entry_cena_38.insert(0, "1")
        entry_cena_38.grid(row=28, column=6)
    elif nazwa_38.get() == "Śruba blokująca PeekPower do osteotomii":
        entry_cena_38 = Entry(root, textvariable=cena_38, justify=CENTER, width=14)
        entry_cena_38.insert(0, "194")
        entry_cena_38.grid(row=28, column=6)
    elif nazwa_38.get() == "System do mieszania próżniowego":
        entry_cena_38 = Entry(root, textvariable=cena_38, justify=CENTER, width=14)
        entry_cena_38.insert(0, "216")
        entry_cena_38.grid(row=28, column=6)
    elif nazwa_38.get() == "System wprowadzania implantów ACL TightRope":
        entry_cena_38 = Entry(root, textvariable=cena_38, justify=CENTER, width=14)
        entry_cena_38.insert(0, "702")
        entry_cena_38.grid(row=28, column=6)
    elif nazwa_38.get() == "Szew FiberWire 2":
        entry_cena_38 = Entry(root, textvariable=cena_38, justify=CENTER, width=14)
        entry_cena_38.insert(0, "86.40")
        entry_cena_38.grid(row=28, column=6)
    elif nazwa_38.get() == "Taśma przylepna 10x50":
        entry_cena_38 = Entry(root, textvariable=cena_38, justify=CENTER, width=14)
        entry_cena_38.insert(0, "1.04")
        entry_cena_38.grid(row=28, column=6)
    elif nazwa_38.get() == "Triathlon elem. udowy lewy":
        entry_cena_38 = Entry(root, textvariable=cena_38, justify=CENTER, width=14)
        entry_cena_38.insert(0, "3132")
        entry_cena_38.grid(row=28, column=6)
    elif nazwa_38.get() == "Triathlon PS wkładka x3-9mm #4":
        entry_cena_38 = Entry(root, textvariable=cena_38, justify=CENTER, width=14)
        entry_cena_38.insert(0, "756")
        entry_cena_38.grid(row=28, column=6)
    elif nazwa_38.get() == "Triathlon taca piszczelowa":
        entry_cena_38 = Entry(root, textvariable=cena_38, justify=CENTER, width=14)
        entry_cena_38.insert(0, "1296")
        entry_cena_38.grid(row=28, column=6)
    elif nazwa_38.get() == "Wkłady 3L z żelem":
        entry_cena_38 = Entry(root, textvariable=cena_38, justify=CENTER, width=14)
        entry_cena_38.insert(0, "10.26")
        entry_cena_38.grid(row=28, column=6)
    elif nazwa_38.get() == "Zestaw do artroskopii":
        entry_cena_38 = Entry(root, textvariable=cena_38, justify=CENTER, width=14)
        entry_cena_38.insert(0, "67")
        entry_cena_38.grid(row=28, column=6)
    elif nazwa_38.get() == "Zestaw do artroskopii barku":
        entry_cena_38 = Entry(root, textvariable=cena_38, justify=CENTER, width=14)
        entry_cena_38.insert(0, "108")
        entry_cena_38.grid(row=28, column=6)
    elif nazwa_38.get() == "Zestaw do drenażu":
        entry_cena_38 = Entry(root, textvariable=cena_38, justify=CENTER, width=14)
        entry_cena_38.insert(0, "14.23")
        entry_cena_38.grid(row=28, column=6)
    elif nazwa_38.get() == "Zestaw ortopedyczny":
        entry_cena_38 = Entry(root, textvariable=cena_38, justify=CENTER, width=14)
        entry_cena_38.insert(0, "28.08")
        entry_cena_38.grid(row=28, column=6)
    elif nazwa_38.get() == "Gaziki 20 x 10cm":
        entry_cena_38 = Entry(root, textvariable=cena_38, justify=CENTER, width=14)
        entry_cena_38.insert(0, "0.46")
        entry_cena_38.grid(row=28, column=6)
    else:
        entry_cena_38 = Entry(root, textvariable=cena_38, justify=CENTER, width=14, bg="#ffff00")
        entry_cena_38.insert(0, "0")
        entry_cena_38.grid(row=28, column=6)

    if nazwa_39.get() == "--puste--":
        entry_cena_39 = Entry(root, textvariable=cena_39, justify=CENTER, width=14)
        entry_cena_39.insert(0, "0")
        entry_cena_39.grid(row=29, column=6)
    elif nazwa_39.get() == "Ablator":
        entry_cena_39 = Entry(root, textvariable=cena_39, justify=CENTER, width=14)
        entry_cena_39.insert(0, "572")
        entry_cena_39.grid(row=29, column=6)
    elif nazwa_39.get() == "Anestezjolog":
        entry_cena_39 = Entry(root, textvariable=cena_39, justify=CENTER, width=14, bg="#ffff00")
        entry_cena_39.insert(0, "350")
        entry_cena_39.grid(row=29, column=6)
    elif nazwa_39.get() == "Butelka 400ml do długotrwałego odsysania ran j.u. sterylna":
        entry_cena_39 = Entry(root, textvariable=cena_39, justify=CENTER, width=14)
        entry_cena_39.insert(0, "4")
        entry_cena_39.grid(row=29, column=6)
    elif nazwa_39.get() == "Doba":
        entry_cena_39 = Entry(root, textvariable=cena_39, justify=CENTER, width=14)
        entry_cena_39.insert(0, "700")
        entry_cena_39.grid(row=29, column=6)
    elif nazwa_39.get() == "Dren łączący do ssaka Grena":
        entry_cena_39 = Entry(root, textvariable=cena_39, justify=CENTER, width=14)
        entry_cena_39.insert(0, "5")
        entry_cena_39.grid(row=29, column=6)
    elif nazwa_39.get() == "Dren Redona Ch 16 dł. 800mm z trokarem":
        entry_cena_39 = Entry(root, textvariable=cena_39, justify=CENTER, width=14)
        entry_cena_39.insert(0, "29.74")
        entry_cena_39.grid(row=29, column=6)
    elif nazwa_39.get() == "Dren do pompy Artrex":
        entry_cena_39 = Entry(root, textvariable=cena_39, justify=CENTER, width=14)
        entry_cena_39.insert(0, "108")
        entry_cena_39.grid(row=29, column=6)
    elif nazwa_39.get() == "Drut wiercący 2,4 x 311":
        entry_cena_39 = Entry(root, textvariable=cena_39, justify=CENTER, width=14)
        entry_cena_39.insert(0, "139.60")
        entry_cena_39.grid(row=29, column=6)
    elif nazwa_39.get() == "Fartuch jałowy L":
        entry_cena_39 = Entry(root, textvariable=cena_39, justify=CENTER, width=14)
        entry_cena_39.insert(0, "17")
        entry_cena_39.grid(row=29, column=6)
    elif nazwa_39.get() == "Fartuch jałowy M":
        entry_cena_39 = Entry(root, textvariable=cena_39, justify=CENTER, width=14)
        entry_cena_39.insert(0, "15.28")
        entry_cena_39.grid(row=29, column=6)
    elif nazwa_39.get() == "Fartuch jałowy XL":
        entry_cena_39 = Entry(root, textvariable=cena_39, justify=CENTER, width=14)
        entry_cena_39.insert(0, "20.84")
        entry_cena_39.grid(row=29, column=6)
    elif nazwa_39.get() == "FasatThread BioComposite Interference Screw 8x30":
        entry_cena_39 = Entry(root, textvariable=cena_39, justify=CENTER, width=14)
        entry_cena_39.insert(0, "594")
        entry_cena_39.grid(row=29, column=6)
    elif nazwa_39.get() == "Folia operacyjna, jałowa 45cm x 55cm":
        entry_cena_39 = Entry(root, textvariable=cena_39, justify=CENTER, width=14)
        entry_cena_39.insert(0, "9.99")
        entry_cena_39.grid(row=29, column=6)
    elif nazwa_39.get() == "Gaziki 10 x 10cm":
        entry_cena_39 = Entry(root, textvariable=cena_39, justify=CENTER, width=14)
        entry_cena_39.insert(0, "0.10")
        entry_cena_39.grid(row=29, column=6)
    elif nazwa_39.get() == "Igła 0,6 x 60":
        entry_cena_39 = Entry(root, textvariable=cena_39, justify=CENTER, width=14)
        entry_cena_39.insert(0, "0.09")
        entry_cena_39.grid(row=29, column=6)
    elif nazwa_39.get() == "Igła 0,7 x 40":
        entry_cena_39 = Entry(root, textvariable=cena_39, justify=CENTER, width=14)
        entry_cena_39.insert(0, "0.05")
        entry_cena_39.grid(row=29, column=6)
    elif nazwa_39.get() == "Igła 0,8 x 40":
        entry_cena_39 = Entry(root, textvariable=cena_39, justify=CENTER, width=14)
        entry_cena_39.insert(0, "0.05")
        entry_cena_39.grid(row=29, column=6)
    elif nazwa_39.get() == "Igła 1,1 x 70":
        entry_cena_39 = Entry(root, textvariable=cena_39, justify=CENTER, width=14)
        entry_cena_39.insert(0, "0.16")
        entry_cena_39.grid(row=29, column=6)
    elif nazwa_39.get() == "Kaniulowana śruba int. biokompozytowa z osłonką jednoraz.":
        entry_cena_39 = Entry(root, textvariable=cena_39, justify=CENTER, width=14)
        entry_cena_39.insert(0, "594")
        entry_cena_39.grid(row=29, column=6)
    elif nazwa_39.get() == "Kaniulowana śruba int. biokompozytowa z pełnym gwintem":
        entry_cena_39 = Entry(root, textvariable=cena_39, justify=CENTER, width=14)
        entry_cena_39.insert(0, "594")
        entry_cena_39.grid(row=29, column=6)
    elif nazwa_39.get() == "Końcówka do Shavera":
        entry_cena_39 = Entry(root, textvariable=cena_39, justify=CENTER, width=14)
        entry_cena_39.insert(0, "270")
        entry_cena_39.grid(row=29, column=6)
    elif nazwa_39.get() == "Kotwica biokompozytowa SwiveLock":
        entry_cena_39 = Entry(root, textvariable=cena_39, justify=CENTER, width=14)
        entry_cena_39.insert(0, "918")
        entry_cena_39.grid(row=29, column=6)
    elif nazwa_39.get() == "Kotwica Corkscrew":
        entry_cena_39 = Entry(root, textvariable=cena_39, justify=CENTER, width=14)
        entry_cena_39.insert(0, "604")
        entry_cena_39.grid(row=29, column=6)
    elif nazwa_39.get() == "Kotwica FASTak":
        entry_cena_39 = Entry(root, textvariable=cena_39, justify=CENTER, width=14)
        entry_cena_39.insert(0, "432")
        entry_cena_39.grid(row=29, column=6)
    elif nazwa_39.get() == "Kotwica PEEK SwiveLock":
        entry_cena_39 = Entry(root, textvariable=cena_39, justify=CENTER, width=14)
        entry_cena_39.insert(0, "885.60")
        entry_cena_39.grid(row=29, column=6)
    elif nazwa_39.get() == "NaCl 3000ml":
        entry_cena_39 = Entry(root, textvariable=cena_39, justify=CENTER, width=14)
        entry_cena_39.insert(0, "29.72")
        entry_cena_39.grid(row=29, column=6)
    elif nazwa_39.get() == "NaCl 5000ml":
        entry_cena_39 = Entry(root, textvariable=cena_39, justify=CENTER, width=14)
        entry_cena_39.insert(0, "58.33")
        entry_cena_39.grid(row=29, column=6)
    elif nazwa_39.get() == "Nici Dafilon 2-0":
        entry_cena_39 = Entry(root, textvariable=cena_39, justify=CENTER, width=14)
        entry_cena_39.insert(0, "6.60")
        entry_cena_39.grid(row=29, column=6)
    elif nazwa_39.get() == "Nici Novosyn 2":
        entry_cena_39 = Entry(root, textvariable=cena_39, justify=CENTER, width=14)
        entry_cena_39.insert(0, "13")
        entry_cena_39.grid(row=29, column=6)
    elif nazwa_39.get() == "Nici Novosyn 2-0":
        entry_cena_39 = Entry(root, textvariable=cena_39, justify=CENTER, width=14)
        entry_cena_39.insert(0, "7.70")
        entry_cena_39.grid(row=29, column=6)
    elif nazwa_39.get() == "Nici Novosyn 3-0":
        entry_cena_39 = Entry(root, textvariable=cena_39, justify=CENTER, width=14)
        entry_cena_39.insert(0, "7.70")
        entry_cena_39.grid(row=29, column=6)
    elif nazwa_39.get() == "Nici Nylon 2-0":
        entry_cena_39 = Entry(root, textvariable=cena_39, justify=CENTER, width=14)
        entry_cena_39.insert(0, "2.50")
        entry_cena_39.grid(row=29, column=6)
    elif nazwa_39.get() == "Nici Nylon 3-0":
        entry_cena_39 = Entry(root, textvariable=cena_39, justify=CENTER, width=14)
        entry_cena_39.insert(0, "2")
        entry_cena_39.grid(row=29, column=6)
    elif nazwa_39.get() == "Nici PGLA":
        entry_cena_39 = Entry(root, textvariable=cena_39, justify=CENTER, width=14)
        entry_cena_39.insert(0, "11.60")
        entry_cena_39.grid(row=29, column=6)
    elif nazwa_39.get() == "Nici PremiCron 3":
        entry_cena_39 = Entry(root, textvariable=cena_39, justify=CENTER, width=14)
        entry_cena_39.insert(0, "6.50")
        entry_cena_39.grid(row=29, column=6)
    elif nazwa_39.get() == "Nici Vicryl 4-0":
        entry_cena_39 = Entry(root, textvariable=cena_39, justify=CENTER, width=14)
        entry_cena_39.insert(0, "7.50")
        entry_cena_39.grid(row=29, column=6)
    elif nazwa_39.get() == "Nitinol Guide Pin 1.1":
        entry_cena_39 = Entry(root, textvariable=cena_39, justify=CENTER, width=14)
        entry_cena_39.insert(0, "145.80")
        entry_cena_39.grid(row=29, column=6)
    elif nazwa_39.get() == "Osłona na przewody":
        entry_cena_39 = Entry(root, textvariable=cena_39, justify=CENTER, width=14)
        entry_cena_39.insert(0, "2.50")
        entry_cena_39.grid(row=29, column=6)
    elif nazwa_39.get() == "Ostrze Arthrex 90(86)x19x1,27":
        entry_cena_39 = Entry(root, textvariable=cena_39, justify=CENTER, width=14)
        entry_cena_39.insert(0, "216")
        entry_cena_39.grid(row=29, column=6)
    elif nazwa_39.get() == "Ostrze piły":
        entry_cena_39 = Entry(root, textvariable=cena_39, justify=CENTER, width=14)
        entry_cena_39.insert(0, "108")
        entry_cena_39.grid(row=29, column=6)
    elif nazwa_39.get() == "Pielęgniarka anest.":
        entry_cena_39 = Entry(root, textvariable=cena_39, justify=CENTER, width=14)
        entry_cena_39.insert(0, "50")
        entry_cena_39.grid(row=29, column=6)
    elif nazwa_39.get() == "Pielęgniarka instr.":
        entry_cena_39 = Entry(root, textvariable=cena_39, justify=CENTER, width=14)
        entry_cena_39.insert(0, "50")
        entry_cena_39.grid(row=29, column=6)
    elif nazwa_39.get() == "Pielęgniarka 'Noviline'":
        entry_cena_39 = Entry(root, textvariable=cena_39, justify=CENTER, width=14)
        entry_cena_39.insert(0, "30")
        entry_cena_39.grid(row=29, column=6)
    elif nazwa_39.get() == "Płytka PeekPower do osteotomii klinowej":
        entry_cena_39 = Entry(root, textvariable=cena_39, justify=CENTER, width=14)
        entry_cena_39.insert(0, "2160")
        entry_cena_39.grid(row=29, column=6)
    elif nazwa_39.get() == "Rękawice jałowe 6,5":
        entry_cena_39 = Entry(root, textvariable=cena_39, justify=CENTER, width=14)
        entry_cena_39.insert(0, "1.20")
        entry_cena_39.grid(row=29, column=6)
    elif nazwa_39.get() == "Rękawice jałowe 7,0":
        entry_cena_39 = Entry(root, textvariable=cena_39, justify=CENTER, width=14)
        entry_cena_39.insert(0, "1.20")
        entry_cena_39.grid(row=29, column=6)
    elif nazwa_39.get() == "Rękawice jałowe 7,5":
        entry_cena_39 = Entry(root, textvariable=cena_39, justify=CENTER, width=14)
        entry_cena_39.insert(0, "1.20")
        entry_cena_39.grid(row=29, column=6)
    elif nazwa_39.get() == "Rękawice jałowe 8,00":
        entry_cena_39 = Entry(root, textvariable=cena_39, justify=CENTER, width=14)
        entry_cena_39.insert(0, "1.20")
        entry_cena_39.grid(row=29, column=6)
    elif nazwa_39.get() == "Rękojeść Interpulse wysokoprzepływowa":
        entry_cena_39 = Entry(root, textvariable=cena_39, justify=CENTER, width=14)
        entry_cena_39.insert(0, "216")
        entry_cena_39.grid(row=29, column=6)
    elif nazwa_39.get() == "Serweta":
        entry_cena_39 = Entry(root, textvariable=cena_39, justify=CENTER, width=14)
        entry_cena_39.insert(0, "6")
        entry_cena_39.grid(row=29, column=6)
    elif nazwa_39.get() == "Simplex Hv z Gentamycyna 10x40g":
        entry_cena_39 = Entry(root, textvariable=cena_39, justify=CENTER, width=14)
        entry_cena_39.insert(0, "162")
        entry_cena_39.grid(row=29, column=6)
    elif nazwa_39.get() == "Skalpel 11":
        entry_cena_39 = Entry(root, textvariable=cena_39, justify=CENTER, width=14)
        entry_cena_39.insert(0, "0.38")
        entry_cena_39.grid(row=29, column=6)
    elif nazwa_39.get() == "Skalpel 13":
        entry_cena_39 = Entry(root, textvariable=cena_39, justify=CENTER, width=14)
        entry_cena_39.insert(0, "1")
        entry_cena_39.grid(row=29, column=6)
    elif nazwa_39.get() == "Skalpel 22":
        entry_cena_39 = Entry(root, textvariable=cena_39, justify=CENTER, width=14)
        entry_cena_39.insert(0, "1")
        entry_cena_39.grid(row=29, column=6)
    elif nazwa_39.get() == "Śruba blokująca PeekPower do osteotomii":
        entry_cena_39 = Entry(root, textvariable=cena_39, justify=CENTER, width=14)
        entry_cena_39.insert(0, "194")
        entry_cena_39.grid(row=29, column=6)
    elif nazwa_39.get() == "System do mieszania próżniowego":
        entry_cena_39 = Entry(root, textvariable=cena_39, justify=CENTER, width=14)
        entry_cena_39.insert(0, "216")
        entry_cena_39.grid(row=29, column=6)
    elif nazwa_39.get() == "System wprowadzania implantów ACL TightRope":
        entry_cena_39 = Entry(root, textvariable=cena_39, justify=CENTER, width=14)
        entry_cena_39.insert(0, "702")
        entry_cena_39.grid(row=29, column=6)
    elif nazwa_39.get() == "Szew FiberWire 2":
        entry_cena_39 = Entry(root, textvariable=cena_39, justify=CENTER, width=14)
        entry_cena_39.insert(0, "86.40")
        entry_cena_39.grid(row=29, column=6)
    elif nazwa_39.get() == "Taśma przylepna 10x50":
        entry_cena_39 = Entry(root, textvariable=cena_39, justify=CENTER, width=14)
        entry_cena_39.insert(0, "1.04")
        entry_cena_39.grid(row=29, column=6)
    elif nazwa_39.get() == "Triathlon elem. udowy lewy":
        entry_cena_39 = Entry(root, textvariable=cena_39, justify=CENTER, width=14)
        entry_cena_39.insert(0, "3132")
        entry_cena_39.grid(row=29, column=6)
    elif nazwa_39.get() == "Triathlon PS wkładka x3-9mm #4":
        entry_cena_39 = Entry(root, textvariable=cena_39, justify=CENTER, width=14)
        entry_cena_39.insert(0, "756")
        entry_cena_39.grid(row=29, column=6)
    elif nazwa_39.get() == "Triathlon taca piszczelowa":
        entry_cena_39 = Entry(root, textvariable=cena_39, justify=CENTER, width=14)
        entry_cena_39.insert(0, "1296")
        entry_cena_39.grid(row=29, column=6)
    elif nazwa_39.get() == "Wkłady 3L z żelem":
        entry_cena_39 = Entry(root, textvariable=cena_39, justify=CENTER, width=14)
        entry_cena_39.insert(0, "10.26")
        entry_cena_39.grid(row=29, column=6)
    elif nazwa_39.get() == "Zestaw do artroskopii":
        entry_cena_39 = Entry(root, textvariable=cena_39, justify=CENTER, width=14)
        entry_cena_39.insert(0, "67")
        entry_cena_39.grid(row=29, column=6)
    elif nazwa_39.get() == "Zestaw do artroskopii barku":
        entry_cena_39 = Entry(root, textvariable=cena_39, justify=CENTER, width=14)
        entry_cena_39.insert(0, "108")
        entry_cena_39.grid(row=29, column=6)
    elif nazwa_39.get() == "Zestaw do drenażu":
        entry_cena_39 = Entry(root, textvariable=cena_39, justify=CENTER, width=14)
        entry_cena_39.insert(0, "14.23")
        entry_cena_39.grid(row=29, column=6)
    elif nazwa_39.get() == "Zestaw ortopedyczny":
        entry_cena_39 = Entry(root, textvariable=cena_39, justify=CENTER, width=14)
        entry_cena_39.insert(0, "28.08")
        entry_cena_39.grid(row=29, column=6)
    elif nazwa_39.get() == "Gaziki 20 x 10cm":
        entry_cena_39 = Entry(root, textvariable=cena_39, justify=CENTER, width=14)
        entry_cena_39.insert(0, "0.46")
        entry_cena_39.grid(row=29, column=6)
    else:
        entry_cena_39 = Entry(root, textvariable=cena_39, justify=CENTER, width=14, bg="#ffff00")
        entry_cena_39.insert(0, "0")
        entry_cena_39.grid(row=29, column=6)

    if nazwa_40.get() == "--puste--":
        entry_cena_40 = Entry(root, textvariable=cena_40, justify=CENTER, width=14)
        entry_cena_40.insert(0, "0")
        entry_cena_40.grid(row=30, column=6)
    elif nazwa_40.get() == "Ablator":
        entry_cena_40 = Entry(root, textvariable=cena_40, justify=CENTER, width=14)
        entry_cena_40.insert(0, "572")
        entry_cena_40.grid(row=30, column=6)
    elif nazwa_40.get() == "Anestezjolog":
        entry_cena_40 = Entry(root, textvariable=cena_40, justify=CENTER, width=14, bg="#ffff00")
        entry_cena_40.insert(0, "350")
        entry_cena_40.grid(row=30, column=6)
    elif nazwa_40.get() == "Butelka 400ml do długotrwałego odsysania ran j.u. sterylna":
        entry_cena_40 = Entry(root, textvariable=cena_40, justify=CENTER, width=14)
        entry_cena_40.insert(0, "4")
        entry_cena_40.grid(row=30, column=6)
    elif nazwa_40.get() == "Doba":
        entry_cena_40 = Entry(root, textvariable=cena_40, justify=CENTER, width=14)
        entry_cena_40.insert(0, "700")
        entry_cena_40.grid(row=30, column=6)
    elif nazwa_40.get() == "Dren łączący do ssaka Grena":
        entry_cena_40 = Entry(root, textvariable=cena_40, justify=CENTER, width=14)
        entry_cena_40.insert(0, "5")
        entry_cena_40.grid(row=30, column=6)
    elif nazwa_40.get() == "Dren Redona Ch 16 dł. 800mm z trokarem":
        entry_cena_40 = Entry(root, textvariable=cena_40, justify=CENTER, width=14)
        entry_cena_40.insert(0, "29.74")
        entry_cena_40.grid(row=30, column=6)
    elif nazwa_40.get() == "Dren do pompy Artrex":
        entry_cena_40 = Entry(root, textvariable=cena_40, justify=CENTER, width=14)
        entry_cena_40.insert(0, "108")
        entry_cena_40.grid(row=30, column=6)
    elif nazwa_40.get() == "Drut wiercący 2,4 x 311":
        entry_cena_40 = Entry(root, textvariable=cena_40, justify=CENTER, width=14)
        entry_cena_40.insert(0, "139.60")
        entry_cena_40.grid(row=30, column=6)
    elif nazwa_40.get() == "Fartuch jałowy L":
        entry_cena_40 = Entry(root, textvariable=cena_40, justify=CENTER, width=14)
        entry_cena_40.insert(0, "17")
        entry_cena_40.grid(row=30, column=6)
    elif nazwa_40.get() == "Fartuch jałowy M":
        entry_cena_40 = Entry(root, textvariable=cena_40, justify=CENTER, width=14)
        entry_cena_40.insert(0, "15.28")
        entry_cena_40.grid(row=30, column=6)
    elif nazwa_40.get() == "Fartuch jałowy XL":
        entry_cena_40 = Entry(root, textvariable=cena_40, justify=CENTER, width=14)
        entry_cena_40.insert(0, "20.84")
        entry_cena_40.grid(row=30, column=6)
    elif nazwa_40.get() == "FasatThread BioComposite Interference Screw 8x30":
        entry_cena_40 = Entry(root, textvariable=cena_40, justify=CENTER, width=14)
        entry_cena_40.insert(0, "594")
        entry_cena_40.grid(row=30, column=6)
    elif nazwa_40.get() == "Folia operacyjna, jałowa 45cm x 55cm":
        entry_cena_40 = Entry(root, textvariable=cena_40, justify=CENTER, width=14)
        entry_cena_40.insert(0, "9.99")
        entry_cena_40.grid(row=30, column=6)
    elif nazwa_40.get() == "Gaziki 10 x 10cm":
        entry_cena_40 = Entry(root, textvariable=cena_40, justify=CENTER, width=14)
        entry_cena_40.insert(0, "0.10")
        entry_cena_40.grid(row=30, column=6)
    elif nazwa_40.get() == "Igła 0,6 x 60":
        entry_cena_40 = Entry(root, textvariable=cena_40, justify=CENTER, width=14)
        entry_cena_40.insert(0, "0.09")
        entry_cena_40.grid(row=30, column=6)
    elif nazwa_40.get() == "Igła 0,7 x 40":
        entry_cena_40 = Entry(root, textvariable=cena_40, justify=CENTER, width=14)
        entry_cena_40.insert(0, "0.05")
        entry_cena_40.grid(row=30, column=6)
    elif nazwa_40.get() == "Igła 0,8 x 40":
        entry_cena_40 = Entry(root, textvariable=cena_40, justify=CENTER, width=14)
        entry_cena_40.insert(0, "0.05")
        entry_cena_40.grid(row=30, column=6)
    elif nazwa_40.get() == "Igła 1,1 x 70":
        entry_cena_40 = Entry(root, textvariable=cena_40, justify=CENTER, width=14)
        entry_cena_40.insert(0, "0.16")
        entry_cena_40.grid(row=30, column=6)
    elif nazwa_40.get() == "Kaniulowana śruba int. biokompozytowa z osłonką jednoraz.":
        entry_cena_40 = Entry(root, textvariable=cena_40, justify=CENTER, width=14)
        entry_cena_40.insert(0, "594")
        entry_cena_40.grid(row=30, column=6)
    elif nazwa_40.get() == "Kaniulowana śruba int. biokompozytowa z pełnym gwintem":
        entry_cena_40 = Entry(root, textvariable=cena_40, justify=CENTER, width=14)
        entry_cena_40.insert(0, "594")
        entry_cena_40.grid(row=30, column=6)
    elif nazwa_40.get() == "Końcówka do Shavera":
        entry_cena_40 = Entry(root, textvariable=cena_40, justify=CENTER, width=14)
        entry_cena_40.insert(0, "270")
        entry_cena_40.grid(row=30, column=6)
    elif nazwa_40.get() == "Kotwica biokompozytowa SwiveLock":
        entry_cena_40 = Entry(root, textvariable=cena_40, justify=CENTER, width=14)
        entry_cena_40.insert(0, "918")
        entry_cena_40.grid(row=30, column=6)
    elif nazwa_40.get() == "Kotwica Corkscrew":
        entry_cena_40 = Entry(root, textvariable=cena_40, justify=CENTER, width=14)
        entry_cena_40.insert(0, "604")
        entry_cena_40.grid(row=30, column=6)
    elif nazwa_40.get() == "Kotwica FASTak":
        entry_cena_40 = Entry(root, textvariable=cena_40, justify=CENTER, width=14)
        entry_cena_40.insert(0, "432")
        entry_cena_40.grid(row=30, column=6)
    elif nazwa_40.get() == "Kotwica PEEK SwiveLock":
        entry_cena_40 = Entry(root, textvariable=cena_40, justify=CENTER, width=14)
        entry_cena_40.insert(0, "885.60")
        entry_cena_40.grid(row=30, column=6)
    elif nazwa_40.get() == "NaCl 3000ml":
        entry_cena_40 = Entry(root, textvariable=cena_40, justify=CENTER, width=14)
        entry_cena_40.insert(0, "29.72")
        entry_cena_40.grid(row=30, column=6)
    elif nazwa_40.get() == "NaCl 5000ml":
        entry_cena_40 = Entry(root, textvariable=cena_40, justify=CENTER, width=14)
        entry_cena_40.insert(0, "58.33")
        entry_cena_40.grid(row=30, column=6)
    elif nazwa_40.get() == "Nici Dafilon 2-0":
        entry_cena_40 = Entry(root, textvariable=cena_40, justify=CENTER, width=14)
        entry_cena_40.insert(0, "6.60")
        entry_cena_40.grid(row=30, column=6)
    elif nazwa_40.get() == "Nici Novosyn 2":
        entry_cena_40 = Entry(root, textvariable=cena_40, justify=CENTER, width=14)
        entry_cena_40.insert(0, "13")
        entry_cena_40.grid(row=30, column=6)
    elif nazwa_40.get() == "Nici Novosyn 2-0":
        entry_cena_40 = Entry(root, textvariable=cena_40, justify=CENTER, width=14)
        entry_cena_40.insert(0, "7.70")
        entry_cena_40.grid(row=30, column=6)
    elif nazwa_40.get() == "Nici Novosyn 3-0":
        entry_cena_40 = Entry(root, textvariable=cena_40, justify=CENTER, width=14)
        entry_cena_40.insert(0, "7.70")
        entry_cena_40.grid(row=30, column=6)
    elif nazwa_40.get() == "Nici Nylon 2-0":
        entry_cena_40 = Entry(root, textvariable=cena_40, justify=CENTER, width=14)
        entry_cena_40.insert(0, "2.50")
        entry_cena_40.grid(row=30, column=6)
    elif nazwa_40.get() == "Nici Nylon 3-0":
        entry_cena_40 = Entry(root, textvariable=cena_40, justify=CENTER, width=14)
        entry_cena_40.insert(0, "2")
        entry_cena_40.grid(row=30, column=6)
    elif nazwa_40.get() == "Nici PGLA":
        entry_cena_40 = Entry(root, textvariable=cena_40, justify=CENTER, width=14)
        entry_cena_40.insert(0, "11.60")
        entry_cena_40.grid(row=30, column=6)
    elif nazwa_40.get() == "Nici PremiCron 3":
        entry_cena_40 = Entry(root, textvariable=cena_40, justify=CENTER, width=14)
        entry_cena_40.insert(0, "6.50")
        entry_cena_40.grid(row=30, column=6)
    elif nazwa_40.get() == "Nici Vicryl 4-0":
        entry_cena_40 = Entry(root, textvariable=cena_40, justify=CENTER, width=14)
        entry_cena_40.insert(0, "7.50")
        entry_cena_40.grid(row=30, column=6)
    elif nazwa_40.get() == "Nitinol Guide Pin 1.1":
        entry_cena_40 = Entry(root, textvariable=cena_40, justify=CENTER, width=14)
        entry_cena_40.insert(0, "145.80")
        entry_cena_40.grid(row=30, column=6)
    elif nazwa_40.get() == "Osłona na przewody":
        entry_cena_40 = Entry(root, textvariable=cena_40, justify=CENTER, width=14)
        entry_cena_40.insert(0, "2.50")
        entry_cena_40.grid(row=30, column=6)
    elif nazwa_40.get() == "Ostrze Arthrex 90(86)x19x1,27":
        entry_cena_40 = Entry(root, textvariable=cena_40, justify=CENTER, width=14)
        entry_cena_40.insert(0, "216")
        entry_cena_40.grid(row=30, column=6)
    elif nazwa_40.get() == "Ostrze piły":
        entry_cena_40 = Entry(root, textvariable=cena_40, justify=CENTER, width=14)
        entry_cena_40.insert(0, "108")
        entry_cena_40.grid(row=30, column=6)
    elif nazwa_40.get() == "Pielęgniarka anest.":
        entry_cena_40 = Entry(root, textvariable=cena_40, justify=CENTER, width=14)
        entry_cena_40.insert(0, "50")
        entry_cena_40.grid(row=30, column=6)
    elif nazwa_40.get() == "Pielęgniarka instr.":
        entry_cena_40 = Entry(root, textvariable=cena_40, justify=CENTER, width=14)
        entry_cena_40.insert(0, "50")
        entry_cena_40.grid(row=30, column=6)
    elif nazwa_40.get() == "Pielęgniarka 'Noviline'":
        entry_cena_40 = Entry(root, textvariable=cena_40, justify=CENTER, width=14)
        entry_cena_40.insert(0, "30")
        entry_cena_40.grid(row=30, column=6)
    elif nazwa_40.get() == "Płytka PeekPower do osteotomii klinowej":
        entry_cena_40 = Entry(root, textvariable=cena_40, justify=CENTER, width=14)
        entry_cena_40.insert(0, "2160")
        entry_cena_40.grid(row=30, column=6)
    elif nazwa_40.get() == "Rękawice jałowe 6,5":
        entry_cena_40 = Entry(root, textvariable=cena_40, justify=CENTER, width=14)
        entry_cena_40.insert(0, "1.20")
        entry_cena_40.grid(row=30, column=6)
    elif nazwa_40.get() == "Rękawice jałowe 7,0":
        entry_cena_40 = Entry(root, textvariable=cena_40, justify=CENTER, width=14)
        entry_cena_40.insert(0, "1.20")
        entry_cena_40.grid(row=30, column=6)
    elif nazwa_40.get() == "Rękawice jałowe 7,5":
        entry_cena_40 = Entry(root, textvariable=cena_40, justify=CENTER, width=14)
        entry_cena_40.insert(0, "1.20")
        entry_cena_40.grid(row=30, column=6)
    elif nazwa_40.get() == "Rękawice jałowe 8,00":
        entry_cena_40 = Entry(root, textvariable=cena_40, justify=CENTER, width=14)
        entry_cena_40.insert(0, "1.20")
        entry_cena_40.grid(row=30, column=6)
    elif nazwa_40.get() == "Rękojeść Interpulse wysokoprzepływowa":
        entry_cena_40 = Entry(root, textvariable=cena_40, justify=CENTER, width=14)
        entry_cena_40.insert(0, "216")
        entry_cena_40.grid(row=30, column=6)
    elif nazwa_40.get() == "Serweta":
        entry_cena_40 = Entry(root, textvariable=cena_40, justify=CENTER, width=14)
        entry_cena_40.insert(0, "6")
        entry_cena_40.grid(row=30, column=6)
    elif nazwa_40.get() == "Simplex Hv z Gentamycyna 10x40g":
        entry_cena_40 = Entry(root, textvariable=cena_40, justify=CENTER, width=14)
        entry_cena_40.insert(0, "162")
        entry_cena_40.grid(row=30, column=6)
    elif nazwa_40.get() == "Skalpel 11":
        entry_cena_40 = Entry(root, textvariable=cena_40, justify=CENTER, width=14)
        entry_cena_40.insert(0, "0.38")
        entry_cena_40.grid(row=30, column=6)
    elif nazwa_40.get() == "Skalpel 13":
        entry_cena_40 = Entry(root, textvariable=cena_40, justify=CENTER, width=14)
        entry_cena_40.insert(0, "1")
        entry_cena_40.grid(row=30, column=6)
    elif nazwa_40.get() == "Skalpel 22":
        entry_cena_40 = Entry(root, textvariable=cena_40, justify=CENTER, width=14)
        entry_cena_40.insert(0, "1")
        entry_cena_40.grid(row=30, column=6)
    elif nazwa_40.get() == "Śruba blokująca PeekPower do osteotomii":
        entry_cena_40 = Entry(root, textvariable=cena_40, justify=CENTER, width=14)
        entry_cena_40.insert(0, "194")
        entry_cena_40.grid(row=30, column=6)
    elif nazwa_40.get() == "System do mieszania próżniowego":
        entry_cena_40 = Entry(root, textvariable=cena_40, justify=CENTER, width=14)
        entry_cena_40.insert(0, "216")
        entry_cena_40.grid(row=30, column=6)
    elif nazwa_40.get() == "System wprowadzania implantów ACL TightRope":
        entry_cena_40 = Entry(root, textvariable=cena_40, justify=CENTER, width=14)
        entry_cena_40.insert(0, "702")
        entry_cena_40.grid(row=30, column=6)
    elif nazwa_40.get() == "Szew FiberWire 2":
        entry_cena_40 = Entry(root, textvariable=cena_40, justify=CENTER, width=14)
        entry_cena_40.insert(0, "86.40")
        entry_cena_40.grid(row=30, column=6)
    elif nazwa_40.get() == "Taśma przylepna 10x50":
        entry_cena_40 = Entry(root, textvariable=cena_40, justify=CENTER, width=14)
        entry_cena_40.insert(0, "1.04")
        entry_cena_40.grid(row=30, column=6)
    elif nazwa_40.get() == "Triathlon elem. udowy lewy":
        entry_cena_40 = Entry(root, textvariable=cena_40, justify=CENTER, width=14)
        entry_cena_40.insert(0, "3132")
        entry_cena_40.grid(row=30, column=6)
    elif nazwa_40.get() == "Triathlon PS wkładka x3-9mm #4":
        entry_cena_40 = Entry(root, textvariable=cena_40, justify=CENTER, width=14)
        entry_cena_40.insert(0, "756")
        entry_cena_40.grid(row=30, column=6)
    elif nazwa_40.get() == "Triathlon taca piszczelowa":
        entry_cena_40 = Entry(root, textvariable=cena_40, justify=CENTER, width=14)
        entry_cena_40.insert(0, "1296")
        entry_cena_40.grid(row=30, column=6)
    elif nazwa_40.get() == "Wkłady 3L z żelem":
        entry_cena_40 = Entry(root, textvariable=cena_40, justify=CENTER, width=14)
        entry_cena_40.insert(0, "10.26")
        entry_cena_40.grid(row=30, column=6)
    elif nazwa_40.get() == "Zestaw do artroskopii":
        entry_cena_40 = Entry(root, textvariable=cena_40, justify=CENTER, width=14)
        entry_cena_40.insert(0, "67")
        entry_cena_40.grid(row=30, column=6)
    elif nazwa_40.get() == "Zestaw do artroskopii barku":
        entry_cena_40 = Entry(root, textvariable=cena_40, justify=CENTER, width=14)
        entry_cena_40.insert(0, "108")
        entry_cena_40.grid(row=30, column=6)
    elif nazwa_40.get() == "Zestaw do drenażu":
        entry_cena_40 = Entry(root, textvariable=cena_40, justify=CENTER, width=14)
        entry_cena_40.insert(0, "14.23")
        entry_cena_40.grid(row=30, column=6)
    elif nazwa_40.get() == "Zestaw ortopedyczny":
        entry_cena_40 = Entry(root, textvariable=cena_40, justify=CENTER, width=14)
        entry_cena_40.insert(0, "28.08")
        entry_cena_40.grid(row=30, column=6)
    elif nazwa_40.get() == "Gaziki 20 x 10cm":
        entry_cena_40 = Entry(root, textvariable=cena_40, justify=CENTER, width=14)
        entry_cena_40.insert(0, "0.46")
        entry_cena_40.grid(row=30, column=6)
    else:
        entry_cena_40 = Entry(root, textvariable=cena_40, justify=CENTER, width=14, bg="#ffff00")
        entry_cena_40.insert(0, "0")
        entry_cena_40.grid(row=30, column=6)

    # Przelicznik uruchamia się po zakończeniu
    buttonik = Button(root, command=sprawdz_ceny, image=spr, borderwidth=0, highlightthickness=0)
    buttonik.place(relx=0.6, rely=0.05)
    return

def przelicz():
    lista_nazw = []
    lista_ilosci = []
    lista_cen = []
    lista_sum = []
    if not var_cena_zabieg.get():
        alarmik = Label(root, image=img_err, borderwidth=0, highlightthickness=0)
        alarmik.place(relx=0.29, rely=0.18)
    elif not var_lekarz.get():
        alarmik1 = Label(root, image=img_err, borderwidth=0, highlightthickness=0)
        alarmik1.place(relx=0.29, rely=0.14)
    elif not var_zabieg.get():
        alarmik2 = Label(root, image=img_err, borderwidth=0, highlightthickness=0)
        alarmik2.place(relx=0.29, rely=0.1)
    elif not var_data.get():
        alarmik3 = Label(root, image=img_err, borderwidth=0, highlightthickness=0)
        alarmik3.place(relx=0.29, rely=0.06)
    elif not var_pacjent.get():
        alarmik4 = Label(root, image=img_err, borderwidth=0, highlightthickness=0)
        alarmik4.place(relx=0.29, rely=0.021)
    else:
        pozycja = 0
        dane_lekarza = var_lekarz.get()
        text_lekarz = "Lekarz wykonujacy zabieg : " + dane_lekarza
        dane_pacjenta = var_pacjent.get()
        text_pacjent = "Dane pacjenta : " + dane_pacjenta
        data_zabiegu = var_data.get()
        text_data = "Data zabiegu : " + data_zabiegu
        nazwa_zabiegu = var_zabieg.get()
        text_zabieg = "Nazwa zabiegu : " + nazwa_zabiegu
        nazwa_pliku = "wyniki" + "\\" + dane_lekarza + "_" + dane_pacjenta + "_" + data_zabiegu + ".xlsx"

        # Przedmiotnr01
        if nazwa_01.get() != "--puste--":
            przedmiot_nazwa_01 = nazwa_01.get()
            lista_nazw.append(przedmiot_nazwa_01)
            ilosc01 = float(ilosc_01.get())
            lista_ilosci.append(ilosc01)
            cena01 = float(cena_01.get())
            lista_cen.append(cena01)
            wynik_01 = ilosc01 * cena01
            lista_sum.append(wynik_01)
            if wynik_01 > 0:
                wynik_r_01 = round(wynik_01, 2)
                wynikowy01 = Label(root, text=wynik_r_01, relief=RAISED, width=14)
                wynikowy01.grid(row=11, column=3)
                pozycja += 1
        else:
            wynik_01 = 0

        # Przedmiotnr02
        if nazwa_02.get() != "--puste--":
            przedmiot_nazwa_02 = nazwa_02.get()
            lista_nazw.append(przedmiot_nazwa_02)
            ilosc02 = float(ilosc_02.get())
            lista_ilosci.append(ilosc02)
            cena02 = float(cena_02.get())
            lista_cen.append(cena02)
            wynik_02 = ilosc02 * cena02
            lista_sum.append(wynik_02)
            if wynik_02 > 0:
                wynik_r_02 = round(wynik_02, 2)
                wynikowy02 = Label(root, text=wynik_r_02, relief=RAISED, width=14)
                wynikowy02.grid(row=12, column=3)
                pozycja += 1
        else:
            wynik_02 = 0

        # Przedmiotnr03
        if nazwa_03.get() != "--puste--":
            przedmiot_nazwa_03 = nazwa_03.get()
            lista_nazw.append(przedmiot_nazwa_03)
            ilosc03 = float(ilosc_03.get())
            lista_ilosci.append(ilosc03)
            cena03 = float(cena_03.get())
            lista_cen.append(cena03)
            wynik_03 = ilosc03 * cena03
            lista_sum.append(wynik_03)
            if wynik_03 > 0:
                wynik_r_03 = round(wynik_03, 2)
                wynikowy03 = Label(root, text=wynik_r_03, relief=RAISED, width=14)
                wynikowy03.grid(row=13, column=3)
                pozycja += 1
        else:
            wynik_03 = 0

        # Przedmiotnr04
        if nazwa_04.get() != "--puste--":
            przedmiot_nazwa_04 = nazwa_04.get()
            lista_nazw.append(przedmiot_nazwa_04)
            ilosc04 = float(ilosc_04.get())
            lista_ilosci.append(ilosc04)
            cena04 = float(cena_04.get())
            lista_cen.append(cena04)
            wynik_04 = ilosc04 * cena04
            lista_sum.append(wynik_04)
            if wynik_04 > 0:
                wynik_r_04 = round(wynik_04, 2)
                wynikowy04 = Label(root, text=wynik_r_04, relief=RAISED, width=14)
                wynikowy04.grid(row=14, column=3)
                pozycja += 1
        else:
            wynik_04 = 0

        # Przedmiotnr05
        if nazwa_05.get() != "--puste--":
            przedmiot_nazwa_05 = nazwa_05.get()
            lista_nazw.append(przedmiot_nazwa_05)
            ilosc05 = float(ilosc_05.get())
            lista_ilosci.append(ilosc05)
            cena05 = float(cena_05.get())
            lista_cen.append(cena05)
            wynik_05 = ilosc05 * cena05
            lista_sum.append(wynik_05)
            if wynik_05 > 0:
                wynik_r_05 = round(wynik_05, 2)
                wynikowy05 = Label(root, text=wynik_r_05, relief=RAISED, width=14)
                wynikowy05.grid(row=15, column=3)
                pozycja += 1
        else:
            wynik_05 = 0

        # Przedmiotnr06
        if nazwa_06.get() != "--puste--":
            przedmiot_nazwa_06 = nazwa_06.get()
            ilosc06 = float(ilosc_06.get())
            cena06 = float(cena_06.get())
            wynik_06 = ilosc06 * cena06
            lista_nazw.append(przedmiot_nazwa_06)
            lista_ilosci.append(ilosc06)
            lista_cen.append(cena06)
            lista_sum.append(wynik_06)
            if wynik_06 > 0:
                wynik_r_06 = round(wynik_06, 2)
                wynikowy06 = Label(root, text=wynik_r_06, relief=RAISED, width=14)
                wynikowy06.grid(row=16, column=3)
                pozycja += 1
        else:
            wynik_06 = 0

        # Przedmiotnr07
        if nazwa_07.get() != "--puste--":
            przedmiot_nazwa_07 = nazwa_07.get()
            ilosc07 = float(ilosc_07.get())
            cena07 = float(cena_07.get())
            wynik_07 = ilosc07 * cena07
            lista_nazw.append(przedmiot_nazwa_07)
            lista_ilosci.append(ilosc07)
            lista_cen.append(cena07)
            lista_sum.append(wynik_07)
            if wynik_07 > 0:
                wynik_r_07 = round(wynik_07, 2)
                wynikowy07 = Label(root, text=wynik_r_07, relief=RAISED, width=14)
                wynikowy07.grid(row=17, column=3)
                pozycja += 1
        else:
            wynik_07 = 0

        # Przedmiotnr08
        if nazwa_08.get() != "--puste--":
            przedmiot_nazwa_08 = nazwa_08.get()
            ilosc08 = float(ilosc_08.get())
            cena08 = float(cena_08.get())
            wynik_08 = ilosc08 * cena08
            lista_nazw.append(przedmiot_nazwa_08)
            lista_ilosci.append(ilosc08)
            lista_cen.append(cena08)
            lista_sum.append(wynik_08)
            if wynik_08 > 0:
                wynik_r_08 = round(wynik_08, 2)
                wynikowy08 = Label(root, text=wynik_r_08, relief=RAISED, width=14)
                wynikowy08.grid(row=18, column=3)
                pozycja += 1
        else:
            wynik_08 = 0

        # Przedmiotnr09
        if nazwa_09.get() != "--puste--":
            przedmiot_nazwa_09 = nazwa_09.get()
            ilosc09 = float(ilosc_09.get())
            cena09 = float(cena_09.get())
            wynik_09 = ilosc09 * cena09
            lista_nazw.append(przedmiot_nazwa_09)
            lista_ilosci.append(ilosc09)
            lista_cen.append(cena09)
            lista_sum.append(wynik_09)
            if wynik_09 > 0:
                wynik_r_09 = round(wynik_09, 2)
                wynikowy09 = Label(root, text=wynik_r_09, relief=RAISED, width=14)
                wynikowy09.grid(row=19, column=3)
                pozycja += 1
        else:
            wynik_09 = 0

        # Przedmiotnr10
        if nazwa_10.get() != "--puste--":
            przedmiot_nazwa_10 = nazwa_10.get()
            ilosc10 = float(ilosc_10.get())
            cena10 = float(cena_10.get())
            wynik_10 = ilosc10 * cena10
            lista_nazw.append(przedmiot_nazwa_10)
            lista_ilosci.append(ilosc10)
            lista_cen.append(cena10)
            lista_sum.append(wynik_10)
            if wynik_10 > 0:
                wynik_r_10 = round(wynik_10, 2)
                wynikowy10 = Label(root, text=wynik_r_10, relief=RAISED, width=14)
                wynikowy10.grid(row=20, column=3)
                pozycja += 1
        else:
            wynik_10 = 0

        # Przedmiotnr11
        if nazwa_11.get() != "--puste--":
            przedmiot_nazwa_11 = nazwa_11.get()
            ilosc11 = float(ilosc_11.get())
            cena11 = float(cena_11.get())
            wynik_11 = ilosc11 * cena11
            lista_nazw.append(przedmiot_nazwa_11)
            lista_ilosci.append(ilosc11)
            lista_cen.append(cena11)
            lista_sum.append(wynik_11)
            if wynik_11 > 0:
                wynik_r_11 = round(wynik_11, 2)
                wynikowy11 = Label(root, text=wynik_r_11, relief=RAISED, width=14)
                wynikowy11.grid(row=21, column=3)
                pozycja += 1
        else:
            wynik_11 = 0

        # Przedmiotnr12
        if nazwa_12.get() != "--puste--":
            przedmiot_nazwa_12 = nazwa_12.get()
            ilosc12 = float(ilosc_12.get())
            cena12 = float(cena_12.get())
            wynik_12 = ilosc12 * cena12
            lista_nazw.append(przedmiot_nazwa_12)
            lista_ilosci.append(ilosc12)
            lista_cen.append(cena12)
            lista_sum.append(wynik_12)
            if wynik_12 > 0:
                wynik_r_12 = round(wynik_12, 2)
                wynikowy12 = Label(root, text=wynik_r_12, relief=RAISED, width=14)
                wynikowy12.grid(row=22, column=3)
                pozycja += 1
        else:
            wynik_12 = 0

        # Przedmiotnr13
        if nazwa_13.get() != "--puste--":
            przedmiot_nazwa_13 = nazwa_13.get()
            ilosc13 = float(ilosc_13.get())
            cena13 = float(cena_13.get())
            wynik_13 = ilosc13 * cena13
            lista_nazw.append(przedmiot_nazwa_13)
            lista_ilosci.append(ilosc13)
            lista_cen.append(cena13)
            lista_sum.append(wynik_13)
            if wynik_13 > 0:
                wynik_r_13 = round(wynik_13, 2)
                wynikowy13 = Label(root, text=wynik_r_13, relief=RAISED, width=14)
                wynikowy13.grid(row=23, column=3)
                pozycja += 1
        else:
            wynik_13 = 0

        # Przedmiotnr14
        if nazwa_14.get() != "--puste--":
            przedmiot_nazwa_14 = nazwa_14.get()
            ilosc14 = float(ilosc_14.get())
            cena14 = float(cena_14.get())
            wynik_14 = ilosc14 * cena14
            lista_nazw.append(przedmiot_nazwa_14)
            lista_ilosci.append(ilosc14)
            lista_cen.append(cena14)
            lista_sum.append(wynik_14)
            if wynik_14 > 0:
                wynik_r_14 = round(wynik_14, 2)
                wynikowy14 = Label(root, text=wynik_r_14, relief=RAISED, width=14)
                wynikowy14.grid(row=24, column=3)
                pozycja += 1
        else:
            wynik_14 = 0

        # Przedmiotnr15
        if nazwa_15.get() != "--puste--":
            przedmiot_nazwa_15 = nazwa_15.get()
            ilosc15 = float(ilosc_15.get())
            cena15 = float(cena_15.get())
            wynik_15 = ilosc15 * cena15
            lista_nazw.append(przedmiot_nazwa_15)
            lista_ilosci.append(ilosc15)
            lista_cen.append(cena15)
            lista_sum.append(wynik_15)
            if wynik_15 > 0:
                wynik_r_15 = round(wynik_15, 2)
                wynikowy15 = Label(root, text=wynik_r_15, relief=RAISED, width=14)
                wynikowy15.grid(row=25, column=3)
                pozycja += 1
        else:
            wynik_15 = 0

        # Przedmiotnr16
        if nazwa_16.get() != "--puste--":
            przedmiot_nazwa_16 = nazwa_16.get()
            ilosc16 = float(ilosc_16.get())
            cena16 = float(cena_16.get())
            wynik_16 = ilosc16 * cena16
            lista_nazw.append(przedmiot_nazwa_16)
            lista_ilosci.append(ilosc16)
            lista_cen.append(cena16)
            lista_sum.append(wynik_16)
            if wynik_16 > 0:
                wynik_r_16 = round(wynik_16, 2)
                wynikowy16 = Label(root, text=wynik_r_16, relief=RAISED, width=14)
                wynikowy16.grid(row=26, column=3)
                pozycja += 1
        else:
            wynik_16 = 0

        # Przedmiotnr17
        if nazwa_17.get() != "--puste--":
            przedmiot_nazwa_17 = nazwa_17.get()
            ilosc17 = float(ilosc_17.get())
            cena17 = float(cena_17.get())
            wynik_17 = ilosc17 * cena17
            lista_nazw.append(przedmiot_nazwa_17)
            lista_ilosci.append(ilosc17)
            lista_cen.append(cena17)
            lista_sum.append(wynik_17)
            if wynik_17 > 0:
                wynik_r_17 = round(wynik_17, 2)
                wynikowy17 = Label(root, text=wynik_r_17, relief=RAISED, width=14)
                wynikowy17.grid(row=27, column=3)
                pozycja += 1
        else:
            wynik_17 = 0

        # Przedmiotnr18
        if nazwa_18.get() != "--puste--":
            przedmiot_nazwa_18 = nazwa_18.get()
            ilosc18 = float(ilosc_18.get())
            cena18 = float(cena_18.get())
            wynik_18 = ilosc18 * cena18
            lista_nazw.append(przedmiot_nazwa_18)
            lista_ilosci.append(ilosc18)
            lista_cen.append(cena18)
            lista_sum.append(wynik_18)
            if wynik_18 > 0:
                wynik_r_18 = round(wynik_18, 2)
                wynikowy18 = Label(root, text=wynik_r_18, relief=RAISED, width=14)
                wynikowy18.grid(row=28, column=3)
                pozycja += 1
        else:
            wynik_18 = 0

        # Przedmiotnr19
        if nazwa_19.get() != "--puste--":
            przedmiot_nazwa_19 = nazwa_19.get()
            ilosc19 = float(ilosc_19.get())
            cena19 = float(cena_19.get())
            wynik_19 = ilosc19 * cena19
            lista_nazw.append(przedmiot_nazwa_19)
            lista_ilosci.append(ilosc19)
            lista_cen.append(cena19)
            lista_sum.append(wynik_19)
            if wynik_19 > 0:
                wynik_r_19 = round(wynik_19, 2)
                wynikowy19 = Label(root, text=wynik_r_19, relief=RAISED, width=14)
                wynikowy19.grid(row=29, column=3)
                pozycja += 1
        else:
            wynik_19 = 0

        # Przedmiotnr20
        if nazwa_20.get() != "--puste--":
            przedmiot_nazwa_20 = nazwa_20.get()
            ilosc20 = float(ilosc_20.get())
            cena20 = float(cena_20.get())
            wynik_20 = ilosc20 * cena20
            lista_nazw.append(przedmiot_nazwa_20)
            lista_ilosci.append(ilosc20)
            lista_cen.append(cena20)
            lista_sum.append(wynik_20)
            if wynik_20 > 0:
                wynik_r_20 = round(wynik_20, 2)
                wynikowy20 = Label(root, text=wynik_r_20, relief=RAISED, width=14)
                wynikowy20.grid(row=30, column=3)
                pozycja += 1
        else:
            wynik_20 = 0

        # Przedmiotnr_21
        if nazwa_21.get() != "--puste--":
            przedmiot_nazwa_21 = nazwa_21.get()
            ilosc21 = float(ilosc_21.get())
            cena21 = float(cena_21.get())
            wynik_21 = ilosc21 * cena21
            lista_nazw.append(przedmiot_nazwa_21)
            lista_ilosci.append(ilosc21)
            lista_cen.append(cena21)
            lista_sum.append(wynik_21)
            if wynik_21 > 0:
                wynik_r_21 = round(wynik_21, 2)
                wynikowy_21 = Label(root, text=wynik_r_21, relief=RAISED, width=14)
                wynikowy_21.grid(row=11, column=7)
                pozycja += 1
        else:
            wynik_21 = 0

        # Przedmiotnr_22
        if nazwa_22.get() != "--puste--":
            przedmiot_nazwa_22 = nazwa_22.get()
            ilosc22 = float(ilosc_22.get())
            cena22 = float(cena_22.get())
            wynik_22 = ilosc22 * cena22
            lista_nazw.append(przedmiot_nazwa_22)
            lista_ilosci.append(ilosc22)
            lista_cen.append(cena22)
            lista_sum.append(wynik_22)
            if wynik_22 > 0:
                wynik_r_22 = round(wynik_22, 2)
                wynikowy_22 = Label(root, text=wynik_r_22, relief=RAISED, width=14)
                wynikowy_22.grid(row=12, column=7)
                pozycja += 1
        else:
            wynik_22 = 0

        # Przedmiotnr_23
        if nazwa_23.get() != "--puste--":
            przedmiot_nazwa_23 = nazwa_23.get()
            ilosc23 = float(ilosc_23.get())
            cena23 = float(cena_23.get())
            wynik_23 = ilosc23 * cena23
            lista_nazw.append(przedmiot_nazwa_23)
            lista_ilosci.append(ilosc23)
            lista_cen.append(cena23)
            lista_sum.append(wynik_23)
            if wynik_23 > 0:
                wynik_r_23 = round(wynik_23, 2)
                wynikowy_23 = Label(root, text=wynik_r_23, relief=RAISED, width=14)
                wynikowy_23.grid(row=13, column=7)
                pozycja += 1
        else:
            wynik_23 = 0

        # Przedmiotnr_24
        if nazwa_24.get() != "--puste--":
            przedmiot_nazwa_24 = nazwa_24.get()
            ilosc24 = float(ilosc_24.get())
            cena24 = float(cena_24.get())
            wynik_24 = ilosc24 * cena24
            lista_nazw.append(przedmiot_nazwa_24)
            lista_ilosci.append(ilosc24)
            lista_cen.append(cena24)
            lista_sum.append(wynik_24)
            if wynik_24 > 0:
                wynik_r_24 = round(wynik_24, 2)
                wynikowy_24 = Label(root, text=wynik_r_24, relief=RAISED, width=14)
                wynikowy_24.grid(row=14, column=7)
                pozycja += 1
        else:
            wynik_24 = 0

        # Przedmiotnr_25
        if nazwa_25.get() != "--puste--":
            przedmiot_nazwa_25 = nazwa_25.get()
            ilosc25 = float(ilosc_25.get())
            cena25 = float(cena_25.get())
            wynik_25 = ilosc25 * cena25
            lista_nazw.append(przedmiot_nazwa_25)
            lista_ilosci.append(ilosc25)
            lista_cen.append(cena25)
            lista_sum.append(wynik_25)
            if wynik_25 > 0:
                wynik_r_25 = round(wynik_25, 2)
                wynikowy_25 = Label(root, text=wynik_r_25, relief=RAISED, width=14)
                wynikowy_25.grid(row=15, column=7)
                pozycja += 1
        else:
            wynik_25 = 0

        # Przedmiotnr_26
        if nazwa_26.get() != "--puste--":
            przedmiot_nazwa_26 = nazwa_26.get()
            ilosc26 = float(ilosc_26.get())
            cena26 = float(cena_26.get())
            wynik_26 = ilosc26 * cena26
            lista_nazw.append(przedmiot_nazwa_26)
            lista_ilosci.append(ilosc26)
            lista_cen.append(cena26)
            lista_sum.append(wynik_26)
            if wynik_26 > 0:
                wynik_r_26 = round(wynik_26, 2)
                wynikowy_26 = Label(root, text=wynik_r_26, relief=RAISED, width=14)
                wynikowy_26.grid(row=16, column=7)
                pozycja += 1
        else:
            wynik_26 = 0

        # Przedmiotnr_27
        if nazwa_27.get() != "--puste--":
            przedmiot_nazwa_27 = nazwa_27.get()
            ilosc27 = float(ilosc_27.get())
            cena27 = float(cena_27.get())
            wynik_27 = ilosc27 * cena27
            lista_nazw.append(przedmiot_nazwa_27)
            lista_ilosci.append(ilosc27)
            lista_cen.append(cena27)
            lista_sum.append(wynik_27)
            if wynik_27 > 0:
                wynik_r_27 = round(wynik_27, 2)
                wynikowy_27 = Label(root, text=wynik_r_27, relief=RAISED, width=14)
                wynikowy_27.grid(row=17, column=7)
                pozycja += 1
        else:
            wynik_27 = 0

        # Przedmiotnr_28
        if nazwa_28.get() != "--puste--":
            przedmiot_nazwa_28 = nazwa_28.get()
            ilosc28 = float(ilosc_28.get())
            cena28 = float(cena_28.get())
            wynik_28 = ilosc28 * cena28
            lista_nazw.append(przedmiot_nazwa_28)
            lista_ilosci.append(ilosc28)
            lista_cen.append(cena28)
            lista_sum.append(wynik_28)
            if wynik_28 > 0:
                wynik_r_28 = round(wynik_28, 2)
                wynikowy_28 = Label(root, text=wynik_r_28, relief=RAISED, width=14)
                wynikowy_28.grid(row=18, column=7)
                pozycja += 1
        else:
            wynik_28 = 0

        # Przedmiotnr_29
        if nazwa_29.get() != "--puste--":
            przedmiot_nazwa_29 = nazwa_29.get()
            ilosc29 = float(ilosc_29.get())
            cena29 = float(cena_29.get())
            wynik_29 = ilosc29 * cena29
            lista_nazw.append(przedmiot_nazwa_29)
            lista_ilosci.append(ilosc29)
            lista_cen.append(cena29)
            lista_sum.append(wynik_29)
            if wynik_29 > 0:
                wynik_r_29 = round(wynik_29, 2)
                wynikowy_29 = Label(root, text=wynik_r_29, relief=RAISED, width=14)
                wynikowy_29.grid(row=19, column=7)
                pozycja += 1
        else:
            wynik_29 = 0

        # Przedmiotnr_30
        if nazwa_30.get() != "--puste--":
            przedmiot_nazwa_30 = nazwa_30.get()
            ilosc30 = float(ilosc_30.get())
            cena30 = float(cena_30.get())
            wynik_30 = ilosc30 * cena30
            lista_nazw.append(przedmiot_nazwa_30)
            lista_ilosci.append(ilosc30)
            lista_cen.append(cena30)
            lista_sum.append(wynik_30)
            if wynik_30 > 0:
                wynik_r_30 = round(wynik_30, 2)
                wynikowy_30 = Label(root, text=wynik_r_30, relief=RAISED, width=14)
                wynikowy_30.grid(row=20, column=7)
                pozycja += 1
        else:
            wynik_30 = 0

        # Przedmiotnr_31
        if nazwa_31.get() != "--puste--":
            przedmiot_nazwa_31 = nazwa_31.get()
            ilosc31 = float(ilosc_31.get())
            cena31 = float(cena_31.get())
            wynik_31 = ilosc31 * cena31
            lista_nazw.append(przedmiot_nazwa_31)
            lista_ilosci.append(ilosc31)
            lista_cen.append(cena31)
            lista_sum.append(wynik_31)
            if wynik_31 > 0:
                wynik_r_31 = round(wynik_31, 2)
                wynikowy_31 = Label(root, text=wynik_r_31, relief=RAISED, width=14)
                wynikowy_31.grid(row=21, column=7)
                pozycja += 1
        else:
            wynik_31 = 0

        # Przedmiotnr_32
        if nazwa_32.get() != "--puste--":
            przedmiot_nazwa_32 = nazwa_32.get()
            ilosc32 = float(ilosc_32.get())
            cena32 = float(cena_32.get())
            wynik_32 = ilosc32 * cena32
            lista_nazw.append(przedmiot_nazwa_32)
            lista_ilosci.append(ilosc32)
            lista_cen.append(cena32)
            lista_sum.append(wynik_32)
            if wynik_32 > 0:
                wynik_r_32 = round(wynik_32, 2)
                wynikowy_32 = Label(root, text=wynik_r_32, relief=RAISED, width=14)
                wynikowy_32.grid(row=22, column=7)
                pozycja += 1
        else:
            wynik_32 = 0

        # Przedmiotnr_33
        if nazwa_33.get() != "--puste--":
            przedmiot_nazwa_33 = nazwa_33.get()
            ilosc33 = float(ilosc_33.get())
            cena33 = float(cena_33.get())
            wynik_33 = ilosc33 * cena33
            lista_nazw.append(przedmiot_nazwa_33)
            lista_ilosci.append(ilosc33)
            lista_cen.append(cena33)
            lista_sum.append(wynik_33)
            if wynik_33 > 0:
                wynik_r_33 = round(wynik_33, 2)
                wynikowy_33 = Label(root, text=wynik_r_33, relief=RAISED, width=14)
                wynikowy_33.grid(row=23, column=7)
                pozycja += 1
        else:
            wynik_33 = 0

        # Przedmiotnr_34
        if nazwa_34.get() != "--puste--":
            przedmiot_nazwa_34 = nazwa_34.get()
            ilosc34 = float(ilosc_34.get())
            cena34 = float(cena_34.get())
            wynik_34 = ilosc34 * cena34
            lista_nazw.append(przedmiot_nazwa_34)
            lista_ilosci.append(ilosc34)
            lista_cen.append(cena34)
            lista_sum.append(wynik_34)
            if wynik_34 > 0:
                wynik_r_34 = round(wynik_34, 2)
                wynikowy_34 = Label(root, text=wynik_r_34, relief=RAISED, width=14)
                wynikowy_34.grid(row=24, column=7)
                pozycja += 1
        else:
            wynik_34 = 0

        # Przedmiotnr_35
        if nazwa_35.get() != "--puste--":
            przedmiot_nazwa_35 = nazwa_35.get()
            ilosc35 = float(ilosc_35.get())
            cena35 = float(cena_35.get())
            wynik_35 = ilosc35 * cena35
            lista_nazw.append(przedmiot_nazwa_35)
            lista_ilosci.append(ilosc35)
            lista_cen.append(cena35)
            lista_sum.append(wynik_35)
            if wynik_35 > 0:
                wynik_r_35 = round(wynik_35, 2)
                wynikowy_35 = Label(root, text=wynik_r_35, relief=RAISED, width=14)
                wynikowy_35.grid(row=25, column=7)
                pozycja += 1
        else:
            wynik_35 = 0

        # Przedmiotnr_36
        if nazwa_36.get() != "--puste--":
            przedmiot_nazwa_36 = nazwa_36.get()
            ilosc36 = float(ilosc_36.get())
            cena36 = float(cena_36.get())
            wynik_36 = ilosc36 * cena36
            lista_nazw.append(przedmiot_nazwa_36)
            lista_ilosci.append(ilosc36)
            lista_cen.append(cena36)
            lista_sum.append(wynik_36)
            if wynik_36 > 0:
                wynik_r_36 = round(wynik_36, 2)
                wynikowy_36 = Label(root, text=wynik_r_36, relief=RAISED, width=14)
                wynikowy_36.grid(row=26, column=7)
                pozycja += 1
        else:
            wynik_36 = 0

        # Przedmiotnr_37
        if nazwa_37.get() != "--puste--":
            przedmiot_nazwa_37 = nazwa_37.get()
            ilosc37 = float(ilosc_37.get())
            cena37 = float(cena_37.get())
            wynik_37 = ilosc37 * cena37
            lista_nazw.append(przedmiot_nazwa_37)
            lista_ilosci.append(ilosc37)
            lista_cen.append(cena37)
            lista_sum.append(wynik_37)
            if wynik_37 > 0:
                wynik_r_37 = round(wynik_37, 2)
                wynikowy_37 = Label(root, text=wynik_r_37, relief=RAISED, width=14)
                wynikowy_37.grid(row=27, column=7)
                pozycja += 1
        else:
            wynik_37 = 0

        # Przedmiotnr_38
        if nazwa_38.get() != "--puste--":
            przedmiot_nazwa_38 = nazwa_38.get()
            ilosc38 = float(ilosc_38.get())
            cena38 = float(cena_38.get())
            wynik_38 = ilosc38 * cena38
            lista_nazw.append(przedmiot_nazwa_38)
            lista_ilosci.append(ilosc38)
            lista_cen.append(cena38)
            lista_sum.append(wynik_38)
            if wynik_38 > 0:
                wynik_r_38 = round(wynik_38, 2)
                wynikowy_38 = Label(root, text=wynik_r_38, relief=RAISED, width=14)
                wynikowy_38.grid(row=28, column=7)
                pozycja += 1
        else:
            wynik_38 = 0

        # Przedmiotnr_39
        if nazwa_39.get() != "--puste--":
            przedmiot_nazwa_39 = nazwa_39.get()
            ilosc39 = float(ilosc_39.get())
            cena39 = float(cena_39.get())
            wynik_39 = ilosc39 * cena39
            lista_nazw.append(przedmiot_nazwa_39)
            lista_ilosci.append(ilosc39)
            lista_cen.append(cena39)
            lista_sum.append(wynik_39)
            if wynik_39 > 0:
                wynik_r_39 = round(wynik_39, 2)
                wynikowy_39 = Label(root, text=wynik_r_39, relief=RAISED, width=14)
                wynikowy_39.grid(row=29, column=7)
                pozycja += 1
        else:
            wynik_39 = 0

        # Przedmiotnr_40
        if nazwa_40.get() != "--puste--":
            przedmiot_nazwa_40 = nazwa_40.get()
            ilosc40 = float(ilosc_40.get())
            cena40 = float(cena_40.get())
            wynik_40 = ilosc40 * cena40
            lista_nazw.append(przedmiot_nazwa_40)
            lista_ilosci.append(ilosc40)
            lista_cen.append(cena40)
            lista_sum.append(wynik_40)
            if wynik_40 > 0:
                wynik_r_40 = round(wynik_40, 2)
                wynikowy_40 = Label(root, text=wynik_r_40, relief=RAISED, width=14)
                wynikowy_40.grid(row=30, column=7)
                pozycja += 1
        else:
            wynik_40 = 0

        # Zliczanie różnicy z ceny i sumy zabiegu

        suma_cz1 = wynik_01 + wynik_02 + wynik_03 + wynik_04 + wynik_05 + wynik_06 + wynik_07 + wynik_08 + wynik_09 + wynik_10
        suma_cz2 = wynik_11 + wynik_12 + wynik_13 + wynik_14 + wynik_15 + wynik_16 + wynik_17 + wynik_18 + wynik_19 + wynik_20
        suma_cz3 = wynik_21 + wynik_22 + wynik_23 + wynik_24 + wynik_25 + wynik_26 + wynik_27 + wynik_28 + wynik_29 + wynik_30
        suma_cz4 = wynik_31 + wynik_32 + wynik_33 + wynik_34 + wynik_35 + wynik_36 + wynik_37 + wynik_38 + wynik_39 + wynik_40
        suma_glowna = suma_cz1 + suma_cz2 + suma_cz3 + suma_cz4
        suma = round(suma_glowna, 2)
        suma_label = Label(root, text=(suma, "zł"), relief=GROOVE, bg="#ff3300", width=15)
        suma_label.place(relx=0.866, rely=0.053)
        wszystkich_pozycji = "Liczba pozycji w kosztorysie : [" + str(pozycja) + "]"

        try:
            cena_zabieg = float(var_cena_zabieg.get())
            wynik1a = cena_zabieg - suma
            wynik1 = round(wynik1a, 2)
            text_cena_zabiegu = "Cena zabiegu : " + str(cena_zabieg) + " zł"
            text_suma = "Koszty : " + str(suma) + " zł"
            text_wynik = "Wynik : " + str(wynik1) + " zł"
            if wynik1 >= 0:
                wynik = round(wynik1, 2)
                wynik_label = Label(root, text=(wynik, " zł"), relief=GROOVE, bg="#00cc00", width=15)
                wynik_label.place(relx=0.866, rely=0.085)
            else:
                wynik = round(wynik1, 2)
                wynik_label = Label(root, text=(wynik, " zł"), relief=GROOVE, bg="#e62e00", width=15)
                wynik_label.place(relx=0.866, rely=0.085)
        except ValueError:
            alarmik = Label(root, text="Podaj cenę zabiegu")
            alarmik.place(relx=0.6, rely=0.09)

        # Tworzenie tabeli Excel (.xlsx)
        cars = {'Nazwa': lista_nazw,
                'Ilość': lista_ilosci,
                'Cena': lista_cen,
                'Suma': lista_sum}
        try:
            dane_xl = pd.DataFrame([[text_pacjent], [text_data], [text_zabieg], [text_lekarz], [wszystkich_pozycji], [text_cena_zabiegu], [text_suma], [text_wynik]], columns=["Dane dotyczace zabiegu"])
            nazwa_xl = pd.DataFrame(cars, columns=["Nazwa", "Ilość", "Cena", "Suma"]) # <----- Dopisywać?

            with pd.ExcelWriter(nazwa_pliku, engine="openpyxl") as writer:
                dane_xl.to_excel(writer, sheet_name="Dane", index=False)
                nazwa_xl.to_excel(writer, sheet_name="Kosztorys", index=False)
                writer.save()
        except PermissionError:
            info_excel = Label(root, text="Przed ponownym zapisaniem, usuń plik z odpowiedzią!", bg="#cccc00", relief=GROOVE)
            info_excel.place(relx=0.6, rely=0.01)

        buttonik_koniec = Label(root, image=img_ok, borderwidth=0, highlightthickness=0)
        buttonik_koniec.place(relx=0.45, rely=0.14)
    return


root = Tk()
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
# root.geometry("1080x600")
root.configure(bg="#bfbfbf")
root.title("Dżodżoskowy kalkulejszyn")

var_pacjent = StringVar()
var_data = StringVar()
var_zabieg = StringVar()
var_lekarz = StringVar()
var_cena_zabieg = StringVar()

lekarze = ["dr Andrzej Purwin",
           "dr Marcin Rutka",
           "dr Paweł Szeparowicz"]

label_enabel = Label(root, bg="#bfbfbf", height=16).grid(row=0, column=0)

img_pacjent = PhotoImage(file="dane.png")
label_pacjent = Label(root, image=img_pacjent, borderwidth = 0, highlightthickness = 0)
label_pacjent.place(relx=0.01, rely=0.021)
entry_pacjent = Entry(root, textvariable=var_pacjent, justify=CENTER, width=22, font=15)
entry_pacjent.place(relx=0.15, rely=0.021)

img_data = PhotoImage(file="data.png")
label_data = Label(root, image=img_data, borderwidth = 0, highlightthickness = 0)
label_data.place(relx=0.01, rely=0.060)
entry_data = Entry(root, textvariable=var_data, justify=CENTER, width=22, font=15)
entry_data.place(relx=0.15, rely=0.060)

img_nazwa = PhotoImage(file="nazwa.png")
label_zabieg = Label(root, image=img_nazwa, borderwidth = 0, highlightthickness = 0)
label_zabieg.place(relx=0.01, rely=0.1)
entry_zabieg = Entry(root, textvariable=var_zabieg, justify=CENTER, width=22, font=15)
entry_zabieg.place(relx=0.15, rely=0.1)

img_lekarz = PhotoImage(file="lekarz.png")
label_lekarz = Label(root, image=img_lekarz, borderwidth = 0, highlightthickness = 0)
label_lekarz.place(relx=0.01, rely=0.14)
entry_lekarz = ttk.Combobox(root, textvariable=var_lekarz, justify=CENTER, width=25, value=lekarze)
entry_lekarz.current(0)
entry_lekarz.bind("<<ComboboxSelected>>")
entry_lekarz.place(relx=0.15, rely=0.14)

img_kwota = PhotoImage(file="cena.png")
label_kwota = Label(root, image=img_kwota, borderwidth = 0, highlightthickness = 0)
label_kwota.place(relx=0.01, rely=0.18)
entry_kwota = Entry(root, textvariable=var_cena_zabieg, justify=CENTER, width=22, font=15)
entry_kwota.place(relx=0.15, rely=0.18)

img_naglowek = PhotoImage(file="przedmiot.png")
label_naglowek = Label(root, image=img_naglowek, borderwidth = 0, highlightthickness = 0).grid(row=10, column=0)
img_ilosc = PhotoImage(file="ilosc.png")
label_ilosc = Label(root, image=img_ilosc, borderwidth = 0, highlightthickness = 0).grid(row=10, column=1)
img_cenka = PhotoImage(file="cenka.png")
label_cena = Label(root, image=img_cenka, borderwidth = 0, highlightthickness = 0).grid(row=10, column=2)
img_sumka = PhotoImage(file="sumka.png")
label_suma = Label(root, image=img_sumka, borderwidth = 0, highlightthickness = 0).grid(row=10, column=3)

label_naglowek2 = Label(root, image=img_naglowek, borderwidth = 0, highlightthickness = 0).grid(row=10, column=4)
label_ilosc2 = Label(root, image=img_ilosc, borderwidth = 0, highlightthickness = 0).grid(row=10, column=5)
label_cena2 = Label(root, image=img_cenka, borderwidth = 0, highlightthickness = 0).grid(row=10, column=6)
label_suma2 = Label(root, image=img_sumka, borderwidth = 0, highlightthickness = 0).grid(row=10, column=7)

# Tabelka wynikowa
img_cenapo = PhotoImage(file="cenapo.png")
label_cena_zabiegu = Label(root, image=img_cenapo, borderwidth = 0, highlightthickness = 0)
label_cena_zabiegu.place(relx=0.76, rely=0.02)
entry_cena_zabiegu = Label(root, textvariable=var_cena_zabieg, justify=CENTER, width=15)
entry_cena_zabiegu.place(relx=0.865, rely=0.02)

img_kosztypo = PhotoImage(file="kosztypo.png")
koszty_zabiegu = Label(root, image=img_kosztypo, borderwidth = 0, highlightthickness = 0)
koszty_zabiegu.place(relx=0.76, rely=0.053)

img_wynikpo = PhotoImage(file="wynikpo.png")
kwota_po_zabiegu = Label(root, image=img_wynikpo, borderwidth = 0, highlightthickness = 0)
kwota_po_zabiegu.place(relx=0.76, rely=0.085)

# TEST

opcje = ["--puste--",
         "Ablator",
         "Anestezjolog",
         "Butelka 400ml do długotrwałego odsysania ran j.u. sterylna",
         "Doba",
         "Dren łączący do ssaka Grena",
         "Dren Redona Ch 16 dł. 800mm z trokarem",
         "Dren do pompy Artrex",
         "Drut wiercący 2,4 x 311",
         "Fartuch jałowy L",
         "Fartuch jałowy M",
         "Fartuch jałowy XL",
         "FasatThread BioComposite Interference Screw 8x30",
         "Folia operacyjna, jałowa 45cm x 55cm",
         "Gaziki 10 x 10cm",
         "Gaziki 20 x 10cm", # 0.46
         "Igła 0,6 x 60",
         "Igła 0,7 x 40",
         "Igła 0,8 x 40",
         "Igła 1,1 x 70",
         "Kaniulowana śruba int. biokompozytowa z osłonką jednoraz.",
         "Kaniulowana śruba int. biokompozytowa z pełnym gwintem",
         "Końcówka do Shavera",
         "Kotwica biokompozytowa SwiveLock",
         "Kotwica Corkscrew",
         "Kotwica FASTak",
         "Kotwica PEEK SwiveLock",
         "NaCl 3000ml",
         "NaCl 5000ml",
         "Nici Dafilon 2-0",
         "Nici Novosyn 2",
         "Nici Novosyn 2-0",
         "Nici Novosyn 3-0",
         "Nici Nylon 2-0",
         "Nici Nylon 3-0",
         "Nici PGLA",
         "Nici PremiCron 3",
         "Nici Vicryl 4-0",
         "Nitinol Guide Pin 1.1",
         "Osłona na przewody",
         "Ostrze Arthrex 90(86)x19x1,27",
         "Ostrze piły",
         "Pielęgniarka anest.",
         "Pielęgniarka instr.",
         "Pielęgniarka 'Noviline'",
         "Płytka PeekPower do osteotomii klinowej",
         "Rękawice jałowe 6,5",
         "Rękawice jałowe 7,0",
         "Rękawice jałowe 7,5",
         "Rękawice jałowe 8,00",
         "Rękojeść Interpulse wysokoprzepływowa",
         "Serweta",
         "Simplex Hv z Gentamycyna 10x40g",
         "Skalpel 11",
         "Skalpel 13",
         "Skalpel 22",
         "Śruba blokująca PeekPower do osteotomii",
         "System do mieszania próżniowego",
         "System wprowadzania implantów ACL TightRope",
         "Szew FiberWire 2",
         "Taśma przylepna 10x50",
         "Triathlon elem. udowy lewy",
         "Triathlon PS wkładka x3-9mm #4",
         "Triathlon taca piszczelowa",
         "Wkłady 3L z żelem",
         "Zestaw do artroskopii",
         "Zestaw do artroskopii barku",
         "Zestaw do drenażu",
         "Zestaw ortopedyczny"]


# Przemiotnr_01
ilosc_01 = StringVar()
cena_01 = StringVar()
nazwa_01 = StringVar()
combo_01 = ttk.Combobox(root, value=opcje, width=40, textvariable=nazwa_01, font=7)
combo_01.current(0)
combo_01.bind("<<ComboboxSelected>>")
combo_01.grid(row=11, column=0)
entry_ilosc_01 = Spinbox(root, from_=0, to=100, width=4, justify=CENTER, textvariable=ilosc_01, font=7)
entry_ilosc_01.grid(row=11, column=1)

# Przemiotnr_02
ilosc_02 = StringVar()
cena_02 = StringVar()
nazwa_02 = StringVar()
combo_02 = ttk.Combobox(root, value=opcje, width=40, textvariable=nazwa_02, font=7)
combo_02.current(0)
combo_02.bind("<<ComboboxSelected>>")
combo_02.grid(row=12, column=0)
entry_ilosc_02 = Spinbox(root, from_=0, to=100, width=4, justify=CENTER, textvariable=ilosc_02, font=7)
entry_ilosc_02.grid(row=12, column=1)

# Przemiotnr_03
ilosc_03 = StringVar()
cena_03 = StringVar()
nazwa_03 = StringVar()
combo_03 = ttk.Combobox(root, value=opcje, width=40, textvariable=nazwa_03, font=7)
combo_03.current(0)
combo_03.bind("<<ComboboxSelected>>")
combo_03.grid(row=13, column=0)
entry_ilosc_03 = Spinbox(root, from_=0, to=100, width=4, justify=CENTER, textvariable=ilosc_03, font=7)
entry_ilosc_03.grid(row=13, column=1)

# Przemiotnr_04
ilosc_04 = StringVar()
cena_04 = StringVar()
nazwa_04 = StringVar()
combo_04 = ttk.Combobox(root, value=opcje, width=40, textvariable=nazwa_04, font=7)
combo_04.current(0)
combo_04.bind("<<ComboboxSelected>>")
combo_04.grid(row=14, column=0)
entry_ilosc_04 = Spinbox(root, from_=0, to=100, width=4, justify=CENTER, textvariable=ilosc_04, font=7)
entry_ilosc_04.grid(row=14, column=1)

# Przemiotnr_05
ilosc_05 = StringVar()
cena_05 = StringVar()
nazwa_05 = StringVar()
combo_05 = ttk.Combobox(root, value=opcje, width=40, textvariable=nazwa_05, font=7)
combo_05.current(0)
combo_05.bind("<<ComboboxSelected>>")
combo_05.grid(row=15, column=0)
entry_ilosc_05 = Spinbox(root, from_=0, to=100, width=4, justify=CENTER, textvariable=ilosc_05, font=7)
entry_ilosc_05.grid(row=15, column=1)

# Przemiotnr_06
ilosc_06 = StringVar()
cena_06 = StringVar()
nazwa_06 = StringVar()
combo_06 = ttk.Combobox(root, value=opcje, width=40, textvariable=nazwa_06, font=7)
combo_06.current(0)
combo_06.bind("<<ComboboxSelected>>")
combo_06.grid(row=16, column=0)
entry_ilosc_06 = Spinbox(root, from_=0, to=100, width=4, justify=CENTER, textvariable=ilosc_06, font=7)
entry_ilosc_06.grid(row=16, column=1)

# Przemiotnr_07
ilosc_07 = StringVar()
cena_07 = StringVar()
nazwa_07 = StringVar()
combo_07 = ttk.Combobox(root, value=opcje, width=40, textvariable=nazwa_07, font=7)
combo_07.current(0)
combo_07.bind("<<ComboboxSelected>>")
combo_07.grid(row=17, column=0)
entry_ilosc_07 = Spinbox(root, from_=0, to=100, width=4, justify=CENTER, textvariable=ilosc_07, font=7)
entry_ilosc_07.grid(row=17, column=1)

# Przemiotnr_08
ilosc_08 = StringVar()
cena_08 = StringVar()
nazwa_08 = StringVar()
combo_08 = ttk.Combobox(root, value=opcje, width=40, textvariable=nazwa_08, font=7)
combo_08.current(0)
combo_08.bind("<<ComboboxSelected>>")
combo_08.grid(row=18, column=0)
entry_ilosc_08 = Spinbox(root, from_=0, to=100, width=4, justify=CENTER, textvariable=ilosc_08, font=7)
entry_ilosc_08.grid(row=18, column=1)

# Przemiotnr_09
ilosc_09 = StringVar()
cena_09 = StringVar()
nazwa_09 = StringVar()
combo_09 = ttk.Combobox(root, value=opcje, width=40, textvariable=nazwa_09, font=7)
combo_09.current(0)
combo_09.bind("<<ComboboxSelected>>")
combo_09.grid(row=19, column=0)
entry_ilosc_09 = Spinbox(root, from_=0, to=100, width=4, justify=CENTER, textvariable=ilosc_09, font=7)
entry_ilosc_09.grid(row=19, column=1)

# Przemiotnr_10
ilosc_10 = StringVar()
cena_10 = StringVar()
nazwa_10 = StringVar()
combo_10 = ttk.Combobox(root, value=opcje, width=40, textvariable=nazwa_10, font=7)
combo_10.current(0)
combo_10.bind("<<ComboboxSelected>>")
combo_10.grid(row=20, column=0)
entry_ilosc_10 = Spinbox(root, from_=0, to=100, width=4, justify=CENTER, textvariable=ilosc_10, font=7)
entry_ilosc_10.grid(row=20, column=1)

# Przemiotnr_11
ilosc_11 = StringVar()
cena_11 = StringVar()
nazwa_11 = StringVar()
combo_11 = ttk.Combobox(root, value=opcje, width=40, textvariable=nazwa_11, font=7)
combo_11.current(0)
combo_11.bind("<<ComboboxSelected>>")
combo_11.grid(row=21, column=0)
entry_ilosc_11 = Spinbox(root, from_=0, to=100, width=4, justify=CENTER, textvariable=ilosc_11, font=7)
entry_ilosc_11.grid(row=21, column=1)

# Przemiotnr_12
ilosc_12 = StringVar()
cena_12 = StringVar()
nazwa_12 = StringVar()
combo_12 = ttk.Combobox(root, value=opcje, width=40, textvariable=nazwa_12, font=7)
combo_12.current(0)
combo_12.bind("<<ComboboxSelected>>")
combo_12.grid(row=22, column=0)
entry_ilosc_12 = Spinbox(root, from_=0, to=100, width=4, justify=CENTER, textvariable=ilosc_12, font=7)
entry_ilosc_12.grid(row=22, column=1)

# Przemiotnr_13
ilosc_13 = StringVar()
cena_13 = StringVar()
nazwa_13 = StringVar()
combo_13 = ttk.Combobox(root, value=opcje, width=40, textvariable=nazwa_13, font=7)
combo_13.current(0)
combo_13.bind("<<ComboboxSelected>>")
combo_13.grid(row=23, column=0)
entry_ilosc_13 = Spinbox(root, from_=0, to=100, width=4, justify=CENTER, textvariable=ilosc_13, font=7)
entry_ilosc_13.grid(row=23, column=1)

# Przemiotnr_14
ilosc_14 = StringVar()
cena_14 = StringVar()
nazwa_14 = StringVar()
combo_14 = ttk.Combobox(root, value=opcje, width=40, textvariable=nazwa_14, font=7)
combo_14.current(0)
combo_14.bind("<<ComboboxSelected>>")
combo_14.grid(row=24, column=0)
entry_ilosc_14 = Spinbox(root, from_=0, to=100, width=4, justify=CENTER, textvariable=ilosc_14, font=7)
entry_ilosc_14.grid(row=24, column=1)

# Przemiotnr_15
ilosc_15 = StringVar()
cena_15 = StringVar()
nazwa_15 = StringVar()
combo_15 = ttk.Combobox(root, value=opcje, width=40, textvariable=nazwa_15, font=7)
combo_15.current(0)
combo_15.bind("<<ComboboxSelected>>")
combo_15.grid(row=25, column=0)
entry_ilosc_15 = Spinbox(root, from_=0, to=100, width=4, justify=CENTER, textvariable=ilosc_15, font=7)
entry_ilosc_15.grid(row=25, column=1)

# Przemiotnr_16
ilosc_16 = StringVar()
cena_16 = StringVar()
nazwa_16 = StringVar()
combo_16 = ttk.Combobox(root, value=opcje, width=40, textvariable=nazwa_16, font=7)
combo_16.current(0)
combo_16.bind("<<ComboboxSelected>>")
combo_16.grid(row=26, column=0)
entry_ilosc_16 = Spinbox(root, from_=0, to=100, width=4, justify=CENTER, textvariable=ilosc_16, font=7)
entry_ilosc_16.grid(row=26, column=1)

# Przemiotnr_17
ilosc_17 = StringVar()
cena_17 = StringVar()
nazwa_17 = StringVar()
combo_17 = ttk.Combobox(root, value=opcje, width=40, textvariable=nazwa_17, font=7)
combo_17.current(0)
combo_17.bind("<<ComboboxSelected>>")
combo_17.grid(row=27, column=0)
entry_ilosc_17 = Spinbox(root, from_=0, to=100, width=4, justify=CENTER, textvariable=ilosc_17, font=7)
entry_ilosc_17.grid(row=27, column=1)

# Przemiotnr_18
ilosc_18 = StringVar()
cena_18 = StringVar()
nazwa_18 = StringVar()
combo_18 = ttk.Combobox(root, value=opcje, width=40, textvariable=nazwa_18, font=7)
combo_18.current(0)
combo_18.bind("<<ComboboxSelected>>")
combo_18.grid(row=28, column=0)
entry_ilosc_18 = Spinbox(root, from_=0, to=100, width=4, justify=CENTER, textvariable=ilosc_18, font=7)
entry_ilosc_18.grid(row=28, column=1)

# Przemiotnr_19
ilosc_19 = StringVar()
cena_19 = StringVar()
nazwa_19 = StringVar()
combo_19 = ttk.Combobox(root, value=opcje, width=40, textvariable=nazwa_19, font=7)
combo_19.current(0)
combo_19.bind("<<ComboboxSelected>>")
combo_19.grid(row=29, column=0)
entry_ilosc_19 = Spinbox(root, from_=0, to=100, width=4, justify=CENTER, textvariable=ilosc_19, font=7)
entry_ilosc_19.grid(row=29, column=1)

# Przemiotnr_20
ilosc_20 = StringVar()
cena_20 = StringVar()
nazwa_20 = StringVar()
combo_20 = ttk.Combobox(root, value=opcje, width=40, textvariable=nazwa_20, font=7)
combo_20.current(0)
combo_20.bind("<<ComboboxSelected>>")
combo_20.grid(row=30, column=0)
entry_ilosc_20 = Spinbox(root, from_=0, to=100, width=4, justify=CENTER, textvariable=ilosc_20, font=7)
entry_ilosc_20.grid(row=30, column=1)

# Przemiotnr_21
ilosc_21 = StringVar()
cena_21 = StringVar()
nazwa_21 = StringVar()
combo_21 = ttk.Combobox(root, value=opcje, width=40, textvariable=nazwa_21, font=7)
combo_21.current(0)
combo_21.bind("<<ComboboxSelected>>")
combo_21.grid(row=11, column=4)
entry_ilosc_21 = Spinbox(root, from_=0, to=100, width=4, justify=CENTER, textvariable=ilosc_21, font=7)
entry_ilosc_21.grid(row=11, column=5)

# Przemiotnr_22
ilosc_22 = StringVar()
cena_22 = StringVar()
nazwa_22 = StringVar()
combo_22 = ttk.Combobox(root, value=opcje, width=40, textvariable=nazwa_22, font=7)
combo_22.current(0)
combo_22.bind("<<ComboboxSelected>>")
combo_22.grid(row=12, column=4)
entry_ilosc_22 = Spinbox(root, from_=0, to=100, width=4, justify=CENTER, textvariable=ilosc_22, font=7)
entry_ilosc_22.grid(row=12, column=5)

# Przemiotnr_23
ilosc_23 = StringVar()
cena_23 = StringVar()
nazwa_23 = StringVar()
combo_23 = ttk.Combobox(root, value=opcje, width=40, textvariable=nazwa_23, font=7)
combo_23.current(0)
combo_23.bind("<<ComboboxSelected>>")
combo_23.grid(row=13, column=4)
entry_ilosc_23 = Spinbox(root, from_=0, to=100, width=4, justify=CENTER, textvariable=ilosc_23, font=7)
entry_ilosc_23.grid(row=13, column=5)

# Przemiotnr_24
ilosc_24 = StringVar()
cena_24 = StringVar()
nazwa_24 = StringVar()
combo_24 = ttk.Combobox(root, value=opcje, width=40, textvariable=nazwa_24, font=7)
combo_24.current(0)
combo_24.bind("<<ComboboxSelected>>")
combo_24.grid(row=14, column=4)
entry_ilosc_24 = Spinbox(root, from_=0, to=100, width=4, justify=CENTER, textvariable=ilosc_24, font=7)
entry_ilosc_24.grid(row=14, column=5)

# Przemiotnr_25
ilosc_25 = StringVar()
cena_25 = StringVar()
nazwa_25 = StringVar()
combo_25 = ttk.Combobox(root, value=opcje, width=40, textvariable=nazwa_25, font=7)
combo_25.current(0)
combo_25.bind("<<ComboboxSelected>>")
combo_25.grid(row=15, column=4)
entry_ilosc_25 = Spinbox(root, from_=0, to=100, width=4, justify=CENTER, textvariable=ilosc_25, font=7)
entry_ilosc_25.grid(row=15, column=5)

# Przemiotnr_26
ilosc_26 = StringVar()
cena_26 = StringVar()
nazwa_26 = StringVar()
combo_26 = ttk.Combobox(root, value=opcje, width=40, textvariable=nazwa_26, font=7)
combo_26.current(0)
combo_26.bind("<<ComboboxSelected>>")
combo_26.grid(row=16, column=4)
entry_ilosc_26 = Spinbox(root, from_=0, to=100, width=4, justify=CENTER, textvariable=ilosc_26, font=7)
entry_ilosc_26.grid(row=16, column=5)

# Przemiotnr_27
ilosc_27 = StringVar()
cena_27 = StringVar()
nazwa_27 = StringVar()
combo_27 = ttk.Combobox(root, value=opcje, width=40, textvariable=nazwa_27, font=7)
combo_27.current(0)
combo_27.bind("<<ComboboxSelected>>")
combo_27.grid(row=17, column=4)
entry_ilosc_27 = Spinbox(root, from_=0, to=100, width=4, justify=CENTER, textvariable=ilosc_27, font=7)
entry_ilosc_27.grid(row=17, column=5)

# Przemiotnr_28
ilosc_28 = StringVar()
cena_28 = StringVar()
nazwa_28 = StringVar()
combo_28 = ttk.Combobox(root, value=opcje, width=40, textvariable=nazwa_28, font=7)
combo_28.current(0)
combo_28.bind("<<ComboboxSelected>>")
combo_28.grid(row=18, column=4)
entry_ilosc_28 = Spinbox(root, from_=0, to=100, width=4, justify=CENTER, textvariable=ilosc_28, font=7)
entry_ilosc_28.grid(row=18, column=5)

# Przemiotnr_29
ilosc_29 = StringVar()
cena_29 = StringVar()
nazwa_29 = StringVar()
combo_29 = ttk.Combobox(root, value=opcje, width=40, textvariable=nazwa_29, font=7)
combo_29.current(0)
combo_29.bind("<<ComboboxSelected>>")
combo_29.grid(row=19, column=4)
entry_ilosc_29 = Spinbox(root, from_=0, to=100, width=4, justify=CENTER, textvariable=ilosc_29, font=7)
entry_ilosc_29.grid(row=19, column=5)

# Przemiotnr_30
ilosc_30 = StringVar()
cena_30 = StringVar()
nazwa_30 = StringVar()
combo_30 = ttk.Combobox(root, value=opcje, width=40, textvariable=nazwa_30, font=7)
combo_30.current(0)
combo_30.bind("<<ComboboxSelected>>")
combo_30.grid(row=20, column=4)
entry_ilosc_30 = Spinbox(root, from_=0, to=100, width=4, justify=CENTER, textvariable=ilosc_30, font=7)
entry_ilosc_30.grid(row=20, column=5)

# Przemiotnr_31
ilosc_31 = StringVar()
cena_31 = StringVar()
nazwa_31 = StringVar()
combo_31 = ttk.Combobox(root, value=opcje, width=40, textvariable=nazwa_31, font=7)
combo_31.current(0)
combo_31.bind("<<ComboboxSelected>>")
combo_31.grid(row=21, column=4)
entry_ilosc_31 = Spinbox(root, from_=0, to=100, width=4, justify=CENTER, textvariable=ilosc_31, font=7)
entry_ilosc_31.grid(row=21, column=5)

# Przemiotnr_32
ilosc_32 = StringVar()
cena_32 = StringVar()
nazwa_32 = StringVar()
combo_32 = ttk.Combobox(root, value=opcje, width=40, textvariable=nazwa_32, font=7)
combo_32.current(0)
combo_32.bind("<<ComboboxSelected>>")
combo_32.grid(row=22, column=4)
entry_ilosc_32 = Spinbox(root, from_=0, to=100, width=4, justify=CENTER, textvariable=ilosc_32, font=7)
entry_ilosc_32.grid(row=22, column=5)

# Przemiotnr_33
ilosc_33 = StringVar()
cena_33 = StringVar()
nazwa_33 = StringVar()
combo_33 = ttk.Combobox(root, value=opcje, width=40, textvariable=nazwa_33, font=7)
combo_33.current(0)
combo_33.bind("<<ComboboxSelected>>")
combo_33.grid(row=23, column=4)
entry_ilosc_33 = Spinbox(root, from_=0, to=100, width=4, justify=CENTER, textvariable=ilosc_33, font=7)
entry_ilosc_33.grid(row=23, column=5)

# Przemiotnr_34
ilosc_34 = StringVar()
cena_34 = StringVar()
nazwa_34 = StringVar()
combo_34 = ttk.Combobox(root, value=opcje, width=40, textvariable=nazwa_34, font=7)
combo_34.current(0)
combo_34.bind("<<ComboboxSelected>>")
combo_34.grid(row=24, column=4)
entry_ilosc_34 = Spinbox(root, from_=0, to=100, width=4, justify=CENTER, textvariable=ilosc_34, font=7)
entry_ilosc_34.grid(row=24, column=5)

# Przemiotnr_35
ilosc_35 = StringVar()
cena_35 = StringVar()
nazwa_35 = StringVar()
combo_35 = ttk.Combobox(root, value=opcje, width=40, textvariable=nazwa_35, font=7)
combo_35.current(0)
combo_35.bind("<<ComboboxSelected>>")
combo_35.grid(row=25, column=4)
entry_ilosc_35 = Spinbox(root, from_=0, to=100, width=4, justify=CENTER, textvariable=ilosc_35, font=7)
entry_ilosc_35.grid(row=25, column=5)

# Przemiotnr_36
ilosc_36 = StringVar()
cena_36 = StringVar()
nazwa_36 = StringVar()
combo_36 = ttk.Combobox(root, value=opcje, width=40, textvariable=nazwa_36, font=7)
combo_36.current(0)
combo_36.bind("<<ComboboxSelected>>")
combo_36.grid(row=26, column=4)
entry_ilosc_36 = Spinbox(root, from_=0, to=100, width=4, justify=CENTER, textvariable=ilosc_36, font=7)
entry_ilosc_36.grid(row=26, column=5)

# Przemiotnr_37
ilosc_37 = StringVar()
cena_37 = StringVar()
nazwa_37 = StringVar()
combo_37 = ttk.Combobox(root, value=opcje, width=40, textvariable=nazwa_37, font=7)
combo_37.current(0)
combo_37.bind("<<ComboboxSelected>>")
combo_37.grid(row=27, column=4)
entry_ilosc_37 = Spinbox(root, from_=0, to=100, width=4, justify=CENTER, textvariable=ilosc_37, font=7)
entry_ilosc_37.grid(row=27, column=5)

# Przemiotnr_38
ilosc_38 = StringVar()
cena_38 = StringVar()
nazwa_38 = StringVar()
combo_38 = ttk.Combobox(root, value=opcje, width=40, textvariable=nazwa_38, font=7)
combo_38.current(0)
combo_38.bind("<<ComboboxSelected>>")
combo_38.grid(row=28, column=4)
entry_ilosc_38 = Spinbox(root, from_=0, to=100, width=4, justify=CENTER, textvariable=ilosc_38, font=7)
entry_ilosc_38.grid(row=28, column=5)

# Przemiotnr_39
ilosc_39 = StringVar()
cena_39 = StringVar()
nazwa_39 = StringVar()
combo_39 = ttk.Combobox(root, value=opcje, width=40, textvariable=nazwa_39, font=7)
combo_39.current(0)
combo_39.bind("<<ComboboxSelected>>")
combo_39.grid(row=29, column=4)
entry_ilosc_39 = Spinbox(root, from_=0, to=100, width=4, justify=CENTER, textvariable=ilosc_39, font=7)
entry_ilosc_39.grid(row=29, column=5)

# Przemiotnr_40
ilosc_40 = StringVar()
cena_40 = StringVar()
nazwa_40 = StringVar()
combo_40 = ttk.Combobox(root, value=opcje, width=40, textvariable=nazwa_40, font=7)
combo_40.current(0)
combo_40.bind("<<ComboboxSelected>>")
combo_40.grid(row=30, column=4)
entry_ilosc_40 = Spinbox(root, from_=0, to=100, width=4, justify=CENTER, textvariable=ilosc_40, font=7)
entry_ilosc_40.grid(row=30, column=5)

# Przycisk dopisywania cen
img_dopisz = PhotoImage(file="dopisz2.png")
buttonik_dopisz = Button(root, command=dopisz, image=img_dopisz, borderwidth=0, highlightthickness=0)
buttonik_dopisz.place(relx=0.6, rely=0.015)

# Czas
img_czas = PhotoImage(file="czas.png")
buttonik_czas = Button(root,  image=img_czas, borderwidth=0, highlightthickness=0)
buttonik_czas.place(relx=0.33, rely=0.015)

spr = PhotoImage(file="spr.png")
img_zliczanie = PhotoImage(file="zapisz.png")
img_info1 = PhotoImage(file="info1.png")
img_info2 = PhotoImage(file="info2.png")
img_info3 = PhotoImage(file="info3.png")
img_info4 = PhotoImage(file="info4.png")
img_err = PhotoImage(file="err.png")
img_ok = PhotoImage(file="zapisano.png")

# Informacja
root.mainloop()
