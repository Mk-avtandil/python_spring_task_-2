from tkinter import *
from random import *
from PIL import ImageTk,Image

window = Tk()
window.geometry('600x400')
window.resizable(False, False)

window.configure(background='#B0C4DE')

button = Button(window, text='Бросить кости', width=15)
button.place(x=480,y=340)

button2 = Button(window, text='Закрыть', width=15)
button2.place(x=480,y=370)

def close_window(event):
    window.destroy()

class myGame:
    def count_bones(self, n):
        
        
    def draw_bones(self, event):
        i, counter = 0,20
        
        while i < 6:
            random_bone = randint(1, 6)
            if random_bone == 1:
                bone = Canvas(window, height=40, width=40, bg="aqua")
                dot = bone.create_oval(19,19,24,24,fill="white",outline="white")
                bone.place(x=counter,y=0)
                counter += 50
                one += 1
                if one < 3:
                    sum += 100
                elif one == 3:
                    sum += 800
                elif one > 3:
                    sum += 1000
            elif random_bone == 2:
                bone = Canvas(window, height=40, width=40, bg="aqua")
                dot = bone.create_oval(32,5,37,10,fill="white",outline="white")
                dot = bone.create_oval(5,34,10,39,fill="white",outline="white")
                bone.place(x=counter, y=50)
                counter += 50
                two += 1
                if two >= 3:
                    sum += 200
            elif random_bone == 3:
                bone = Canvas(window, height=40, width=40, bg="aqua")
                dot = bone.create_oval(32,5,37,10,fill="white",outline="white")
                dot = bone.create_oval(19,20,24,25,fill="white",outline="white")
                dot = bone.create_oval(5,35,10,40,fill="white",outline="white")
                bone.place(x=counter,y=100)
                counter += 50
                three += 1
                if three >= 3:
                    sum += 300
            elif random_bone == 4:
                bone = Canvas(window, height=40, width=40, bg="aqua")
                dot = bone.create_oval(12,10,17,15,fill="white",outline="white")
                dot = bone.create_oval(27,10,32,15,fill="white",outline="white")
                dot = bone.create_oval(12,26,17,31,fill="white",outline="white")
                dot = bone.create_oval(27,26,32,31,fill="white",outline="white")
                bone.place(x=counter,y=150)
                counter += 50
                four += 1
                if four >= 3:
                    sum += 400
            elif random_bone == 5:
                bone = Canvas(window, height=40, width=40, bg="aqua")
                dot = bone.create_oval(11,9,16,14,fill="white",outline="white")
                dot = bone.create_oval(27,9,32,14,fill="white",outline="white")
                dot = bone.create_oval(19,18,24,23,fill="white",outline="white")
                dot = bone.create_oval(11,26,16,31,fill="white",outline="white")
                dot = bone.create_oval(27,27,32,32,fill="white",outline="white")
                bone.place(x=counter,y=200)
                counter += 50
                five += 1
                if five < 3:
                    sum += 50
                elif five == 3:
                    sum += 400
                elif five > 3:
                    sum += 500
            elif random_bone == 6:
                bone = Canvas(window, height=40, width=40, bg="aqua")
                dot = bone.create_oval(12,8,17,13,fill="white",outline="white")
                dot = bone.create_oval(27,8,32,13,fill="white",outline="white")
                dot = bone.create_oval(12,18,17,23,fill="white",outline="white")
                dot = bone.create_oval(27,18,32,23,fill="white",outline="white")
                dot = bone.create_oval(12,28,17,33,fill="white",outline="white")
                dot = bone.create_oval(27,28,32,33,fill="white",outline="white")
                bone.place(x=counter,y=250)
                counter += 50
                six += 1
                if six >= 3:
                    sum += 600
            if one == 1 and two == 1 and three == 1 and four == 1 and five == 1 and six == 1:
                sum = 1500
            if two == 2 and four == 2 and six == 2:
                sum = 750
            i += 1
            window.after(1300, bone.destroy)
        label1 = Label(text="Result is " + str(sum))
        label1.place(x=480,y=300)



p = myGame()


        
button.bind('<Button-1>', p.draw_bones)
button2.bind('<Button-1>', close_window)

window.mainloop()
