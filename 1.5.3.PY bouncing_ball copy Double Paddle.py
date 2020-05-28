#####
# bouncing_ball.py
# 
# Creates a Scale and a Canvas. Animates a circle based on the Scale
# (c) 2013 PLTW
# version 11/1/2013
####

import tkinter #often people import Tkinter as *
import math
import random
import time
#####
# Create root window 
####
root = tkinter.Tk()
root.wm_title('Pong')
#global direction
#####
# Create Model
######
speed_intvar = tkinter.IntVar()
speed_intvar.set(2) # Initialize y coordinate
# radius and x-coordinate of circle

paddle_speed_intvar = tkinter.IntVar()
paddle_speed_intvar.set(3)
paddle_speed_intvar2 = tkinter.IntVar()
paddle_speed_intvar2.set(3)

r = 10
x = 350
y = 150
direction = 0.5 # radians of angle in standard position, ccw from positive x axis
paddle_speed = 5
end_paddle_speed = 15
paddle_speed2 = 5
end_paddle_speed2 = 15
ball_speed = 1
end_ball_speed = 2
AI= -1
score = 0
score2 = 0

def paddle_speed_changed(new_intval):
    global paddle_speed
    global end_paddle_speed
    global paddle_speed2
    global end_paddle_speed2
    d = paddle_speed_slider.get()
    end_paddle_speed = paddle_speed*d
    f = paddle_speed_slider2.get()
    end_paddle_speed2 = paddle_speed2*f

def ball_speed_changed(new_intval):
    global ball_speed
    global end_ball_speed
    x = speed_slider.get()
    end_ball_speed = ball_speed*x


    
def paddle_move(event):
    global end_paddle_speed
    global AI
    
    if event.keysym == 'a':
        if 0 <=canvas.coords(paddle)[1] <=20:
           canvas.coords(paddle, 25, 0, 35, 80)
        else:
            canvas.move (paddle, 0, -end_paddle_speed)
    if event.keysym == 's':
        if 580 <=canvas.coords(paddle)[3] <=600:
           canvas.coords(paddle, 25,520, 35, 600)
        else:
            canvas.move (paddle, 0, end_paddle_speed)

    if AI != 1:
        if event.keysym == 'k':
            if 0 <=canvas.coords(paddle2)[1] <=20:
               canvas.coords(paddle2, 565, 0, 575, 80)
            else:
                canvas.move (paddle2, 0, -end_paddle_speed2)
            
        if event.keysym == 'l':
            if 580 <=canvas.coords(paddle2)[3] <=600:
               canvas.coords(paddle2, 565,520, 575, 600)
            else:
                canvas.move (paddle2, 0, end_paddle_speed)



def Computer():
    global AI
    AI = (-1)*AI 

    if AI == 1:
        canvas.coords(paddle2, 565, 0, 575, 600)
        c.config(text="Click here to play Duo")

    else:
        canvas.coords(paddle2, 565, 260, 575, 340)
        c.config(text="Click here to play Solo")

        
def reset_game():
    global x
    global y
    global direction
    global paddle_speed
    global end_paddle_speed
    global paddle_speed2
    global end_paddle_speed2
    global ball_speed
    global end_ball_speed
    global score
    global score2
    global AI

    speed_intvar.set(2) 
    paddle_speed_intvar.set(3)
    paddle_speed_intvar.set(3)
    r = 10
    x = 350
    y = 150
    AI = -1
    direction = 0.5 # radians of angle in standard position, ccw from positive x axis
    paddle_speed = 5
    end_paddle_speed = 15
    ball_speed = 1
    end_ball_speed = 2
    score = 0
    score2 = 0
    canvas.coords(circle_item, x-r, y-r, x+r, y+r)
    canvas.coords(paddle, 25, 260, 35, 340)
    canvas.coords(paddle2, 565, 260, 575, 340)
    canvas.coords(streak1, x-8, y-10, x-20, y-13)
    canvas.coords(streak2, x-10, y+5, x-20, y+8)
    editor.delete(1.0,tkinter.END)
    editor.insert(tkinter.END, score)
    editor.insert(tkinter.END, ' : ')
    editor.insert(tkinter.END, score2)
    c.config(text="Click here to play Solo")



def start_over():
    reset_game()

    
    
######
# Create Controller
#######
# Instantiate and place slider
text = tkinter.Label(root, text='Drag slider \nto adjust\nspeed.',width = 15)
text.grid(row=0, column =0)

speed_slider = tkinter.Scale(root, from_=1, to=10, variable=speed_intvar, orient=tkinter.HORIZONTAL,  command=ball_speed_changed, 
                              label='Ball speed')
speed_slider.grid(row=1, column=0, sticky=tkinter.W)

paddle_speed_slider = tkinter.Scale(root, from_=1, to=10, variable=paddle_speed_intvar, orient=tkinter.HORIZONTAL,  command=paddle_speed_changed,  
                              label='Paddle speed')
paddle_speed_slider.grid(row=2, column=0, sticky=tkinter.W)

paddle_speed_slider2 = tkinter.Scale(root, from_=1, to=10, variable=paddle_speed_intvar2, orient=tkinter.HORIZONTAL,  command=paddle_speed_changed,  
                              label='Paddle2 speed')
paddle_speed_slider2.grid(row=3, column=0, sticky=tkinter.W)
# Create and place directions for the user

text2 = tkinter.Label(root, text='Person 1 Score: Person 2 Score ', width=30)
text2.grid(row=0, column=2)

editor = tkinter.Text(root, width=30)
editor.grid(row = 1, column=2)
editor.insert(tkinter.END, score)
editor.insert(tkinter.END, ' : ')
editor.insert(tkinter.END, score2)
editor.config(font=("Courier", 20))

c = tkinter.Button(root, text="Click here to play Solo", command = Computer)
c.grid(row = 3,column = 3)

######
# Create View
#######
# Create and place a canvas
canvas = tkinter.Canvas(root, width=600, height=600, background='#000000')
canvas.grid(row=0, rowspan=3, column=1)

for i in range(0,600,60):
    net = canvas.create_rectangle(297.5, i, 302.5, i+50, fill='white') 

# Create a circle on the canvas to match the initial model
circle_item = canvas.create_oval(x-r, y-r, x+r, y+r, 
                                 outline='#000000', fill='#08d31c')

streak1 = canvas.create_rectangle(x-8, y-10, x-20, y-13, fill='white')
streak2 = canvas.create_rectangle(x-10, y+5, x-20, y+8, fill='white')

red_line = canvas.create_rectangle(0, 0, 20, 600, fill='red')

paddle = canvas.create_rectangle(25, 260, 35, 340, fill='blue')

red_line2 = canvas.create_rectangle(580 ,0, 600, 600, fill='red')

paddle2 = canvas.create_rectangle(565, 260, 575, 340, fill='green')

reset = tkinter.Button(root, text="Reset Game", command= reset_game)
reset.grid(row = 4, column=2,sticky=tkinter.E)
 


    

h = 0
l = 0
g = 0
def animate():
    global h
    global l
    global AI
    global g
    if h == 0:
        h+= 1
        if g== 0:
            instructions = tkinter.Tk()
            instructions.wm_title('Welcome to Pong!!!!')
            instructions.configure(background='black')
            editor2 = tkinter.Text(instructions, width = 50,height = 20)
            editor2.grid(row = 0,column=0)
            editor2.insert(tkinter.END, 'WELCOME TO PONG!!!!!')
            editor2.config(background = 'black', fg='yellow')
            editor2.insert(tkinter.END, '\n When in Solo Mode: \n "a" to go up. \n "s" to go down')
            editor2.insert(tkinter.END, '\n \n ')
            editor2.insert(tkinter.END, 'When in Duo Mode \n "k" to go up for second paddle \n "l" to go down for second paddle')
            editor2.config(background = 'black', fg='yellow')
            g = 1

        canvas.after(5000, animate)
    else:
        global direction
        global score
        global score2
        global end_ball_speed
        # Get the slider data and create x- and y-components of velocity
        velocity_x = end_ball_speed * math.cos(direction) # adj = hyp*cos()
        velocity_y = end_ball_speed * math.sin(direction) # opp = hyp*sin()
        # Change the canvas item's coordinates
        canvas.move(circle_item, velocity_x, velocity_y)
        canvas.move(streak1, velocity_x, velocity_y)
        canvas.move(streak2, velocity_x, velocity_y)
        
    
        # Get the new coordinates and act accordingly if ball is at an edge
        x1, y1, x2, y2 = canvas.coords(circle_item)
        x3, y3, x4, y4 = canvas.coords(paddle)
        x5, y5, x6, y6 = canvas.coords(paddle2)
        m = y4 -80
        k = y6 - 80
        j = y2 - 10
    
        if x1 <= 30:
            if m <= y1 <= y4 or m <= j <= y4 :
                # If crossing left or right of canvas
                if x2>=canvas.winfo_width() or x1<= 30: 
                    direction = math.pi - direction # Reverse the x-component of velocity
                    canvas.coords(streak1, x1-3, y1, x1-13, y1+3)
                    canvas.coords(streak2, x1-3, y1+17, x1-13, y1+20)
                    
                # If crossing top or bottom of canvas
                if y2>=canvas.winfo_height() or y1<=0: 
                    direction = -1 * direction # Reverse the y-component of velocity
    
                
                score += 1
                editor.delete(1.0,tkinter.END)
                editor.insert(tkinter.END, score)
                editor.insert(tkinter.END, ' : ')
                editor.insert(tkinter.END, score2)
                    


            else:

                '''while x1 >= 20:
                    canvas.move(circle_item, velocity_x, velocity_y)
                    time.sleep(0.1)'''
                if l == 0:
                    end = tkinter.Tk()
                    end.wm_title('Score Window')
                    end.configure(background='black')
                    editor2 = tkinter.Text(end, width = 50,height = 20)
                    editor2.grid(row = 0,column=0)
                    n = 'GAME OVER! \n Person 2 WON!!!....The score was \n' + str(score) + ' : ' + str(score2)
                    editor2.insert(tkinter.END, n)
                    editor2.config(background = 'black', fg='yellow')
                    l=1
                reset.destroy()
                start_again = tkinter.Button(root, text="Start Over", command= start_over)
                start_again.grid(row = 2, column=2,sticky=tkinter.E)
                h = 0


        if x2 >= 570:
            '''if score%2 == 1:
                t = y1
            elif score%2 == 0:
                t = y2'''

            if AI == 1:
            # If crossing left or right of canvas
                if x2>=canvas.winfo_width() or x2>= 570: 
                    direction = math.pi - direction # Reverse the x-component of velocity
                    canvas.coords(streak1, x2+3, y2-20, x2+13, y2-17)
                    canvas.coords(streak2, x2+3, y2, x2+13, y2+3)
                    
                # If crossing top or bottom of canvas
                if y2>=canvas.winfo_height() or y1<=0: 
                    direction = -1 * direction # Reverse the y-component of velocity
    
                
                score2 += 1
                editor.delete(1.0,tkinter.END)
                editor.insert(tkinter.END, score)
                editor.insert(tkinter.END, ' : ')
                editor.insert(tkinter.END, score2)


            else:
                
                if k <= y2 <= y6 or k<= j <= y6:
                # If crossing left or right of canvas
                    if x2>=canvas.winfo_width() or x2>= 570: 
                        direction = math.pi - direction # Reverse the x-component of velocity
                        canvas.coords(streak1, x2+3, y2-20, x2+13, y2-17)
                        canvas.coords(streak2, x2+3, y2, x2+13, y2+3)
                    
                # If crossing top or bottom of canvas
                    if y2>=canvas.winfo_height() or y1<=0: 
                        direction = -1 * direction # Reverse the y-component of velocity
    
                
                    score2 += 1
                    editor.delete(1.0,tkinter.END)
                    editor.insert(tkinter.END, score)
                    editor.insert(tkinter.END, ' : ')
                    editor.insert(tkinter.END, score2)
                    


                else:

                    '''while x1 >= 20:
                        canvas.move(circle_item, velocity_x, velocity_y)
                        time.sleep(0.1)'''
                    if l == 0:
                        end = tkinter.Tk()
                        end.wm_title('Score Window')
                        end.configure(background='black')
                        editor2 = tkinter.Text(end, width = 50,height = 20)
                        editor2.grid(row = 0,column=0)
                        n = 'GAME OVER! \n Person 1 WON!!!....The score was \n' + str(score) + ' : ' + str(score2)
                        editor2.insert(tkinter.END, n)
                        editor2.config(background = 'black', fg='yellow')
                        l=1
                    reset.destroy()
                    start_again = tkinter.Button(root, text="Start Over", command= start_over)
                    start_again.grid(row = 2, column=2,sticky=tkinter.E)
                    h = 0
            
            
        
        else:
            if x2>=canvas.winfo_width() or x1<= 0: 
                direction = math.pi - direction # Reverse the x-component of velocity
        # If crossing top or bottom of canvas
            if y2>=canvas.winfo_height() or y1<=0: 
                direction = -1 * direction # Reverse the y-component of velocity


    
    # Create an event in 1 msec that will be handled by animate(),
    # causing recursion        
        canvas.after(1, animate)
# Call function directly to start the recursion
animate()


iterate = 0

def animate_background():
    items = ['7','8','9', 'A', 'B', 'C', 'D', 'E', 'F']
    hexadecimal = '#'
    for i in range(0,6):
        hexadecimal = hexadecimal + random.choice(items)

    items = ['0','1','2', '3', '4']
    hexadecimal2 = '#'
    for i in range(0,6):
        hexadecimal2 = hexadecimal2 + random.choice(items)
        
    canvas.itemconfig(circle_item, fill = hexadecimal )
    canvas.configure(background = hexadecimal2)
    # Create an event in 1 msec that will be handled by animate(),
    # causing recursion        
    canvas.after(1000, animate_background)
# Call function directly to start the recursion
animate_background()




        
canvas.bind_all ('<Key>', paddle_move)

#######
# Event Loop
#######
root.configure(background='black')
root.mainloop()
