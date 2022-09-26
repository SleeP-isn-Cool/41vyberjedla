import tkinter

canvas = tkinter.Canvas(width=399, height=200,bg = "white")

canvas.pack()

#Premenna
premenna1 = 0
premenna2 = 0
premenna3 = 0
premenna4 = 0
#premenna

#vymazanie suboru pri vstupe
subor = open("vyber_jedla.txt", "w")
subor.truncate(0)
subor.close()
#vymazanie suboru pri vstupe

#otvorenie
vysledok = open("vyber_jedla.txt", "a+")
#otvorenie

#def
def vyber(event):
#def
    global premenna1
    global premenna2
    global premenna3
    global premenna4

    #suradnice-klikanie
    x = event.x
    y = event.y
    #suradnice-klikanie

    #cislo ziaka
    ziak = int(entry1.get())
    #cislo ziaka

    #kliknute suradnice
    if x>0 and y>100 and x<99 and y<199:
        #pripocitava pocet kolkokrat je to jedlo zakliknute
        premenna1 = premenna1 + 1

        #zapisovanie do suboru
        vysledok.write(str(ziak) + " Z , počet dokopy =  " + str(premenna1) + (".\n"))
        vysledok.write(" ")

        #zapisovanie do shellu pre kontrolu
        print(str(ziak) ," Z, pocet = ",premenna1)
        
    if x>100 and y>100 and x<199 and y<199:
        #pripocitava pocet kolkokrat je to jedlo zakliknute
        premenna2 = premenna2 + 1

        #zapisovanie do suboru
        vysledok.write(str(ziak) + " Č , počet dokopy =  " + str(premenna2) + (".\n"))
        vysledok.write(" ")

        #zapisovanie do shellu pre kontrolu
        print(str(ziak) ,"Č , počet =  ",premenna2)

    if x>200 and y>100 and x<299 and y<199:
        #pripocitava pocet kolkokrat je to jedlo zakliknute
        premenna3 = premenna3 + 1

        #zapisovanie do suboru
        vysledok.write(str(ziak) + " M , pocet dokopy =  " + str(premenna3) + (".\n"))
        vysledok.write(" ")

        #zapisovanie do shellu pre kontrolu
        print(str(ziak) ,"M,  pocet =  ",premenna3)
    
    if x>300 and y>100 and x<399 and y<199:
        #pripocitava pocet kolkokrat je to jedlo zakliknute
        premenna4 = premenna4 + 1

        #zapisovanie do suboru
        vysledok.write(str(ziak) + " O , pocet dokopy = " + str(premenna4) + (".\n"))
        vysledok.write(" ")

        #zapisovanie do shellu pre kontrolu
        print(str(ziak) ,"O , pocet =  ",premenna4)

     #kliknute suradnice

#def pre ukoncenie a zapisanie do suboru, v ulohe to neni zobrazene ale bez toho mi to neslo
def koniec():
    vysledok.close()
#def pre ukoncenie a zapisanie do suboru, v ulohe to neni zobrazene ale bez toho mi to neslo
       
#stvorce
canvas.create_rectangle(0, 100, 99, 199, fill="green")
canvas.create_rectangle(100, 100, 199, 199, fill="red")
canvas.create_rectangle(200, 100, 299, 199, fill="blue")
canvas.create_rectangle(300, 100, 399, 199, fill="orange")
#stvorce

#text
canvas.create_text(200, 50, text="VÝBER JEDLA", font="Arial 40", fill="red")
#text

#entry na zadanie cisla ziaka        
entry1 = tkinter.Entry()
entry1.pack()
#entry na zadanie cisla ziaka

#button ktory ukonci zapisovanie
button1 = tkinter.Button(text='uložiť', command=koniec)
button1.pack()
#button ktory ukonci zapisovanie

#bind na vyber stvorcov
canvas.bind("<Button-1>", vyber)
#bind na vyber stvorcov

