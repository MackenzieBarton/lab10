##########################################
#                                        #
#             Draw a house!              #
#                                        #
##########################################

# Use create_line(), create_rectangle() and create_oval() to make a 
# drawing of a house using the tKinter Canvas widget.

# 70pt: House outline (roof and the house)
# 80pt: Square windows and a door
# 90pt: A door handle plus a chimney!
# 100pt: Green grass on the ground and a red house!

# Minus 5pts if your code has no comments
# Minus 10pts if you only commit once to github

from Tkinter import *
root = Tk()

# Create the canvas widget
drawpad = Canvas(root, width=800,height=600, background='white')
drawpad.grid(row=0, column=1)

# Insert your code here to draw the house!
#This is The House shape
rectangle2 = drawpad.create_rectangle(250,180,520,440,fill = 'red')

#windows
rectangle3 = drawpad.create_rectangle(280,230,350,300,fill = 'white')
rectangle4 = drawpad.create_rectangle(420,230,490,300,fill = 'white')

#door
rectangle5 = drawpad.create_rectangle(360,360,410,440,fill = 'brown')

#roof
line1 = drawpad.create_line(250,180,390,60,fill = 'dark red')
line1 = drawpad.create_line(520,180,390,60,fill = 'dark red')
line1 = drawpad.create_line(250,180,390,60,fill = 'dark red')

#door knob
oval1 = drawpad.create_oval(400,400,410,410,fill = 'yellow')

#grass
rectangle6 = drawpad.create_rectangle(150,440,630,470,fill = 'dark green')

#chimney
line1 = drawpad.create_line(300,90,300,140,fill = 'dark red')
line1 = drawpad.create_line(300,90,250,90,fill = 'dark red')
line1 = drawpad.create_line(250,90,250,90,fill = 'dark red')

root.mainloop()
