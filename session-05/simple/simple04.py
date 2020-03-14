from drawBot import *

# Let's add some more "constants" up tom
# (ie, inputs to our drawing program that won't change during the run.)
W=1000
H=1000
SPF=0.25


# This recipe defines a sequence of steps for our simple "animation engine"
# To follow. Each step will render a frame with the named font, and scale factor.
#
recipe = [
	#   center        sides       border
	(   (.050, .500), (.10, .10), 0), # first keypoint
	(   (.500, .150), (.30, .30), 0), # second keypoint
	(   (.875, .500), (.25, .25), 0), # third keypoint
	(   (.500, .975), (.05, .05), 0),  # fourth keypoint

]



# ------------------------------------------------------------------------------
# Library Of Functions
# ------------------------------------------------------------------------------
# No change with this one:
def draw_box(center, sides, border, fill_color=(1,1,1)):
	center_x, center_y = center
	width, height = sides

	fill(*fill_color)
	rect(
		center_x*W - (width*W/2) + border,
		center_y*H - (height*H/2) + border,
		width*W-2*border,
		height*H-2*border
	)

def new_frame():
	newPage(W, H)
	frameDuration(SPF)
	fill(0,0,0)
	rect(0,0, W, H)

# Redefine make animation to take our recipe, which contains
# A list of Fonts
def make_animation(recipe, output="simple-04.gif"):

	for object in recipe:
		new_frame()
		center, sides, border = object
		draw_box(center, sides, border)

	saveImage(output)

# Draw the animation and save it.
make_animation(recipe)
# makeAnimation(message, output="test.pdf") # uncomment if you want to look at a PDF. useful for debugging.
