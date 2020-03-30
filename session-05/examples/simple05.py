from drawBot import *

# Let's add some more "constants" up top
# (ie, inputs to our drawing program that won't change during the run.)
W=1000
H=1000
SPF=(1/30)


# This recipe defines a sequence of steps for our simple "animation engine"
# To follow. We're going to use the same set of basic keypoints as last time,
# but this time we're going to give them a new meaning by creating an
# interpolation routine.
#
keypoint_coordinates = [
	#   center        sides       border
	(   (.050, .500), (.10, .10), 0), # first keypoint
	(   (.500, .150), (.30, .30), 0), # second keypoint
	(   (.875, .500), (.25, .25), 0), # third keypoint
	(   (.500, .975), (.05, .05), 0),  # fourth keypoint
	(   (.050, .500), (.10, .10), 0) # first keypoint
]

# The interpolation routine is a rotuine that operates on recipes
# Given a recipe, and a number of steps, it interpolates linearly between
# each step in the recipe, `steps` number of times. So, an animation
# generated with the above list of 5 keypoints, and a steps parameter
# of 5 ==> interpolate_recipe(keypoint_coordinates, 5),
# would create a new recipe with 21 steps in it. Why?
#
# – What happens if you change the number of steps?
# – What happens if you change the interpolation formula below?
# – What happens if you call this routine on a recipe with border parameters
# - What about negative border parameters?
#
def interpolate_recipe(recipe, steps):
	new_recipe = []
	for index in range(len(recipe) - 1):
		starting_keypoint = recipe[index]
		ending_keypoint = recipe[index + 1]

		start_x = starting_keypoint[0][0]
		start_y = starting_keypoint[0][1]
		end_x   = ending_keypoint[0][0]
		end_y   = ending_keypoint[0][1]

		start_w = starting_keypoint[1][0]
		start_h = starting_keypoint[1][1]
		end_w   = ending_keypoint[1][0]
		end_h   = ending_keypoint[1][1]

		start_b = starting_keypoint[2]
		end_b   = ending_keypoint[2]

		new_recipe.append(starting_keypoint)

		for i in range(1, steps):
			t = i/steps # get a number between 0 and 1 for interpolation
			new_keypoint = (
				(t*(end_x-start_x)+start_x, t*(end_y-start_y)+start_y),
				(t*(end_w-start_w)+start_w, t*(end_h-start_h)+start_h),
				t*(end_b-start_b)+start_b
			)
			new_recipe.append(new_keypoint)

	return new_recipe

# Generate frames!
frames = interpolate_recipe(keypoint_coordinates, 10)

# – What happens if you call interpolate recipe multiple times?
# uncomment below to find out:
# frames = interpolate_recipe(frames, 10)


# ------------------------------------------------------------------------------
# Library Of Animation Functions
# ------------------------------------------------------------------------------

# No change with this one.
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

# No change with this one.
def new_frame():
	newPage(W, H)
	frameDuration(SPF)
	fill(0,0,0)
	rect(0,0, W, H)

# No change to this one
# – Now what happens if you move draw_frame outside the loop?
def make_animation(frames, output="simple-05.gif"):

	for object in frames:
		new_frame()
		center, sides, border = object
		draw_box(center, sides, border)

	saveImage(output)

# ------------------------------------------------------------------------------
# Run the Animation
# ------------------------------------------------------------------------------
# Draw the animation and save it.
make_animation(recipe)
# makeAnimation(message, output="test.pdf") # uncomment if you want to look at a PDF. useful for debugging.
