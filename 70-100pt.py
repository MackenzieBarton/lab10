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
rectangle2 = drawpad.create_rectangle(250,180,520,440)

#windows
rectangle3 = drawpad.create_rectangle(280,230,350,300)
rectangle4 = drawpad.create_rectangle(420,230,490,300)

#door
rectangle5 = drawpad.create_rectangle(360,360,410,440)

#roof
line1 = drawpad.create_line(250,180,390,60)
line1 = drawpad.create_line(520,180,390,60)

#door knob
oval1 = drawpad.create_oval(400,400,410,410)


root.mainloop()
