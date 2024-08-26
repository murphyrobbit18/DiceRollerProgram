#imports needed to make code function
# import explorerhat
from guizero import App, PushButton, Text, Window
from random import randint
from time import sleep

#defintions to select random number in range and to open and close  window
def open_window():
    random = randint(1,4)
    text2.value= random
    window.show()

def close_window():
    window.hide()

def open_window2():
    random = randint(1,6)
    text2.value= random
    window.show()

def open_window3():
    random = randint(1,8)
    text2.value= random
    window.show()

def open_window4():
    random = randint(1,10)
    text2.value= random
    window.show()

def open_window5():
    random = randint(1,12)
    text2.value= random
    window.show()

def open_window6():
    random = randint(1,20)
    text2.value= random
    window.show()

'''#if roll is a 20, three LED flashes for two seconds
    if random==20:
        explorerhat.output.two.on()
        explorerhat.output.three.on()
        explorerhat.output.four.on()
        sleep(2)
        explorerhat.output.two.off()
        explorerhat.output.three.off()
        explorerhat.output.four.off()

    #if roll is a 1, a buzzer turns on for two seconds
    if random==1:
        explorerhat.output.one.on()
        sleep(2)
        explorerhat.output.one.off()'''

def open_window7():
    random = randint(1,100)
    text2.value= random
    window.show()

#where the dice roll buttons are displayed
app=App(title='Dice Roll Generator', height = '450', width = '450', bg='#A7C0F0')

#buttons user clicks to get roll
DiceRoll= PushButton(app, command=open_window, text= "Roll a d4")
DiceRoll2= PushButton(app, command=open_window2, text= "Roll a d6")
DiceRoll3= PushButton(app, command=open_window3, text= "Roll a d8")
DiceRoll4= PushButton(app, command=open_window4, text= "Roll a d10")
DiceRoll5= PushButton(app, command=open_window5, text= "Roll a d12")
DiceRoll6 = PushButton(app, command=open_window6, text= "Roll a d20")
DiceRoll7= PushButton(app, command=open_window7, text= "Roll a d100")

#definition for random
random=randint

#window where random roll is shown
window=Window(app, title="Random Roll", height = '375', width = '375', bg='#A7C0F0')

text=Text(window, text="Your random roll is", font= "Times New Roman")
text2=Text(window, text="", font= "Times New Roman")

#window is hidden until user clicks button
window.hide()

app.display()