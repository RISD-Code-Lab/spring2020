from drawBot import *

# Let's add some "constants" up top
# (ie, inputs to our drawing program that won't change during the run.)
W=1000
H=1000
SPF=0.875

# 1. Setup
# Create a new drawing with a single page.
# A drawing is a container of one or multiple pages
newDrawing()

# 1. Instance 1
newPage(W, H)
frameDuration(SPF) # Set a duration for this "page". Only matters for gifs or animations, where "pages" are frames.
fill(0,0,0) # set the fill state for the application R=0, G=0, B=0, or black.
rect(0,0, W, H) # draw a rectangle covering the background.
fill(1,1,1) # set the fill state for the application to R=1, G=1, B=1 or white.
rect(25, 25, W-50, H-50)

# Repeat
newPage(W, H)
frameDuration(SPF)
fill(0,0,0)
rect(0,0, W, H)
fill(1,1,1)
rect(125, 125, W-250, H-250)

# Repeat
newPage(W, H)
frameDuration(SPF)
fill(0,0,0)
rect(0,0, W, H)
fill(1,1,1)
rect(400, 400, W-800, H-800)

# Repeat
newPage(W, H)
frameDuration(SPF)
fill(0,0,0)
rect(0,0, W, H)
fill(1,1,1)

# Output the sketch as both a .gif and .pdf
saveImage('simple-01.gif')
# saveImage('test.pdf') # Uncomment to generate a PDF


# The Question:
# There are a lot of sequential patterns here. What can we
# do to abstract over these patterns?
