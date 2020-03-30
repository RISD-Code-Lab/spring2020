from drawBot import *

# Let's add some more "constants" up tom
# (ie, inputs to our drawing program that won't change during the run.)
W=1000
H=1000
SPF=.25


# Define a general method of drawing a frame given
# a specific value for the border.
#
def draw_frame(border):
	newPage(W, H)
	frameDuration(SPF)
	fill(0,0,0)
	rect(0,0, W, H)
	fill(1,1,1)
	rect( border, border, W-2*border, H-2*border )

# Define a routine that combines our draw_frame primitives in
# Into an anmation, and saves the result
#
def make_animation(output="simple-02.gif"):

	draw_frame(10)
	draw_frame(20)
	draw_frame(40)
	draw_frame(80)
	draw_frame(160)
	draw_frame(320)
	draw_frame(640)
	draw_frame(1280)

	saveImage(output)


# Draw the animation and save it.
make_animation()
# make_animation(message, output="test.pdf") # uncomment if you want to look at a PDF. useful for debugging.
