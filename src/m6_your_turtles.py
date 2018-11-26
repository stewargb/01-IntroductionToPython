"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Aaron Wilkin, their colleagues, and Grant Stewart.
"""
########################################################################
# Done: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# Done again: 2.
#   You should have RUN the  m5e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
#
########################################################################
import rosegraphics as rg
window = rg.TurtleWindow()

top_turtle = rg.SimpleTurtle('classic')
top_turtle.pen = rg.Pen('red', 3)
top_turtle.speed = 20

size = 100
for k in range(10):
    top_turtle.draw_regular_polygon(8,size)

    top_turtle.pen_up()
    top_turtle.left(45)
    top_turtle.forward(10)
    top_turtle.right(45)

    top_turtle.pen_down()

    size = size - 10

bot_turtle = rg.SimpleTurtle('classic')
bot_turtle.pen = rg.Pen('blue', 3)
bot_turtle.speed = 20

size = 100
#bot_turtle.pen_up()
#bot_turtle.right(90)
#bot_turtle.forward(150)
#bot_turtle.left(90)

for k in range (100):


    bot_turtle.pen_down()
    bot_turtle.forward(size)
    bot_turtle.right(45)
    size = size - 1


window.close_on_mouse_click()
