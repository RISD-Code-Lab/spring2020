from drawBot import *

# Let's add some more "constants" up tom
# (ie, inputs to our drawing program that won't change during the run.)
W=1000
H=1000
SPF=.25


# Define a general method for drawing one of our frames
# with centered text of our choosing, a scale relative
# to a basic size (24points by default), and a choice
# of typeface.
def drawFrame(border):
	newPage(W, H)
	frameDuration(SPF)
	fill(0,0,0)
	rect(0,0, W, H)
	fill(1,1,1)
	rect( border, border, W-2*border, H-2*border )

# Define a routine that combines our drawFrame primitives in
# Into an anmation, and saves the result
def makeAnimation(output="simple-02.gif"):

	drawFrame(10)
	drawFrame(20)
	drawFrame(40)
	drawFrame(80)
	drawFrame(160)
	drawFrame(320)
	drawFrame(640)
	drawFrame(1280)

	saveImage(output)


# Draw the animation and save it.
makeAnimation()
# makeAnimation(message, output="test.pdf") # uncomment if you want to look at a PDF. useful for debugging.
