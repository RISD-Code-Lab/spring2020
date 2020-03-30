from drawBot import *

# Let's add some more "constants" up tom
# (ie, inputs to our drawing program that won't change during the run.)
W=1000 # Width of the GIF
H=1000 # Height of the GIF
SPF=0.25 # Seconds per frame.


# This coordinates defines a sequence of steps for our simple "animation engine"
# To follow. Each step contains a center, given as a percetange of the
# width and height of the image, a pair of side lengths, given as a percentage of the
# width and height of the image, and a border, given in pixels.
#
# We call these relative coordinates, since they are relative to the
# size of our canvas.
#
coordinates = [
	#   center        sides       border
	(   (.050, .500), (.10, .10), 0), # first keypoint
	(   (.500, .150), (.30, .30), 0), # second keypoint
	(   (.875, .500), (.25, .25), 0), # third keypoint
	(   (.500, .975), (.05, .05), 0),  # fourth keypoint
	# Try adding some more coordinates here.
]



# ------------------------------------------------------------------------------
# Library Of Functions
# ------------------------------------------------------------------------------
#
# Our draw box function draws a single box given center, sides and border,
# and an optional fill color. All of the numbers are given in our
# relative coordinate system, so this function has to convert them
# to drawbot's absolute coordinate system by doing some multiplications
# with the width and height constants we defined at the top of the document.
#
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

# new frame is a simple wrapper that creates a new frame with
# a given duration in seconds, and draws a black background
# to render content on.
#
def new_frame(duration):
	newPage(W, H)
	frameDuration(duration)
	fill(0,0,0)
	rect(0,0, W, H)

# Finally, our make animation function needs to take
# in a list of coordinates, loop over them, and call
# draw_frame, and draw_box with each coordinate pair.
#
# - What happens if you move where new_frame is called?
# - What happens if you call draw_box multiple times per frame with
# different parameters?
def make_animation(coordinates, output="simple-04.gif"):

	for object in coordinates:
		new_frame(SPF)
		center, sides, border = object
		draw_box(center, sides, border)

	saveImage(output)

# Draw the animation and save it.
make_animation(coordinates)
# makeAnimation(message, output="test.pdf") # uncomment if you want to look at a PDF. useful for debugging.
