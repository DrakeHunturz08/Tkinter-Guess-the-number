from random import randint
import time
import tkinter as tk

i = 1

def essai(event=None):
    global enter_proposition, random_number, attemps, attempsvar, inforvar, i

    proposition = enter_proposition.get()

    if proposition.isdigit():
        nombre_proposition = int(proposition)

        if random_number > nombre_proposition:
            infovar.set("It's higher")
        elif random_number < nombre_proposition:
            infovar.set("It's less")
        else:
            infovar.set("The mystery number was " + str(random_number) + "\nYou won")
            enter_proposition.destroy()
            button.destroy()
            close.pack()

        attemps -= 1

        if attemps > 1:
            attempsvar.set(f"{attemps - 1} attemps left")
        elif attemps == 1:
            attempsvar.set(f"{attemps - 1} attemps left")
        else:
            attempsvar.set("Out of attempts")
            infovar.set("The mystery number was "+ str(random_number))
            enter_proposition.destroy()
            button.destroy()
            close.pack()
    else:
        infovar.set("Error : This is not a number")

def timer(t=15):
    global i

    start_button.destroy()
    title.destroy()
    instructions.destroy()
    enter_proposition.focus()
    enter_proposition.pack()
    button.pack()
    info.pack()
    number_attempts.place(x=800, y=20)

    if i == 1:
        time.config(text=(str(t) + " seconds left"))
        if t <= 1:
            time.config(text=(str(t) + " seconds left"))

        if t > 0:
            root.after(1000,timer, t-1)
        elif t == 0:
            time.config(text="Time's up !")
            enter_proposition.destroy()
            button.destroy()
            infovar.set("The mystery number was "+ str(random_number))
            close.pack()
    else:
        infovar.set("Vous êtes idiot")

random_number = randint(1, 100)

attemps = 10

temps = time.time()

# Creer la fenetre
root = tk.Tk()

# Personnaliser la fenetre
root.title("Guess the number")
root.geometry("1100x400")
root.minsize(480, 360)
root.resizable(width=False, height=False)
root.config(bg='#202020')

# Creer une frame
frame = tk.Frame(root, bg='#202020')
frame.pack(expand=True)

# Afficher les consignes

titlevar = tk.StringVar()
titlevar.set("Welcome in the game 'Guess the number'")
title = tk.Label(frame, textvariable=titlevar, font=("Courrier", 35), bg='#202020', fg='white')
title.pack()

instructionsvar = tk.StringVar()
instructionsvar.set("The goal is simple : guess the mystery number between 1 and 100\nBut careful you have only 15 seconds and 10 attemps")
instructions = tk.Label(frame, textvariable=instructionsvar, font=("Courrier", 20), bg='#202020', fg='white')
instructions.pack()

# Lancer le jeu

start_button = tk.Button(frame, text="Start",font=("Courrier", 30), command=timer)
start_button.pack()

# Entrer un nombre
enter_proposition = tk.Entry(frame, font=("Courrier", 30))
enter_proposition.bind('<Return>', essai)

# Ajouter un bouton de validation
button = tk.Button(frame, text="Check", font=("Courrier", 25), command=essai)

# Ajouter un texte
infovar = tk.StringVar()
infovar.set("Good luck !")
info = tk.Label(frame, textvariable=infovar, font=("Courrier", 30), bg='#202020', fg='white')

# Ajouter une variable qui stock le nombre de tentatives
attempsvar = tk.StringVar()
attempsvar.set("10 attemps left")

# Afficher le nombre de tentatives
number_attempts = tk.Label(root, textvariable=attempsvar, bg='#202020', fg='white', font=("Courrier", 20))

# Afficher le temps restant

time = tk.Label(root, text="", font=("Courrier", 20), fg='white', bg='#202020')
time.place(x=40, y=20)

# Ajouter un bouton close
close = tk.Button(frame, text="Close", font=("Courrier", 25), command=root.destroy)

# Afficher la fenetre
root.mainloop()
