from drawBot import *

# Let's add some more "constants" up top
# (ie, inputs to our drawing program that won't change during the run.)
W=1000
H=1000
SPF=0.1


# Take the list of borders and reverse it
# so that the animation bounces in and out.
borders = [ 10, 20, 40, 80, 160, 320 ]
borders = borders + [*reversed(borders)]

# Linearly ramp the border value out
# from a starting value to an ending value.
def linear_borders(start, end, steps):
	borders = []
	for i in range(steps):
		t = i / steps
		borders.append( t*(end-start) + start )

	return borders

borders = linear_borders(10, 500, 100)
# ------------------------------------------------------------------------------
# Library Of Functions
# ------------------------------------------------------------------------------
# No change with this one:
def draw_frame(border):
	newPage(W, H)
	frameDuration(SPF)
	fill(0,0,0)
	rect(0,0, W, H)
	fill(1,1,1)
	rect( border, border, W-2*border, H-2*border )


# Redefine make animation to take our recipe, which contains
# A list of borders.
def make_animation(recipe, output="simple-03.gif"):

	for border in recipe: draw_frame(border)

	saveImage(output)

# Draw the animation and save it.
make_animation(borders)
# makeAnimation(message, output="test.pdf") # uncomment if you want to look at a PDF. useful for debugging.


# Now, we've been able to change thinking about drawings in terms
# Of DrawBot Opetaions, into thinking about drawings in terms
# of lists of numbers. We've turned operations on drawings
# into operations on recipes.
#
# But what if we want more expressive power?
