# Ready, Set, Loop with Python & DrawBot

⚠️ **Code Lab has moved online!** Please join us at [this Zoom link](https://risd.zoom.us/j/299845160) to participate. Sign in with your RISD email.

🎥 **We recorded a walkthrough of this README on April 1, 2020.** Find that video in this folder [here](https://drive.google.com/drive/u/1/folders/16JYAiNXY3YaXdd2UtqKkQx2xqiFoW9LQ). Click on the `session-05` file.

Let's explore the concepts we learned in our basic programming lecture in the context of python and DrawBot. For this session, you'll need a few things, hopefully all of which are within your grasp to get set up.

## Requirements

- Access to your Terminal and your favorite Text Editor. I use Atom most of the time, but you're welcome to use anything you're comfortable with.

- This repository, either cloned or downloaded onto your computer and in an accessible place.

- A working **Python 3** installation. To see if you have one, try the following:
    1. Run `python -V` at the command line. It should print out a version number. If the version starts with `3`, then you have Python 3. If it starts with `2`, or if it says something like "Command Not Found", you don't have the command installed.
    2. Run `python3 -V` at the command link. It should print out a version number. If it says something like "Command Not Found", you don't have the command installed.
    3. If neither of the above work, follow [these instructions](https://docs.python-guide.org/starting/install3/osx/) to get the command set up.


## Getting Set Up

To start, let's set up a virtual environment, so we can easily install libraries for this particular project. This is how we'll install drawBot. Specifically, we'll be using drawBot as a python module, rather than in the standalone GUI program.

```sh
# Set up a python3 virtual environment to store the libraries we need.
$ python3 -m venv .env
$ source .env/bin/activate
```

We can install `drawBot` it from the git repository directly. Run:

```sh
# Install drawBot
$ pip install git+https://github.com/typemytype/drawbot
```

This will download drawbot and build all of its dependencies.

## Introduction

In the previous lab session, we touched on the basics of jQuery, using the special API (a conceptual framework embodied by a set of functions and methods that expose functionality to a programmer) that jQuery makes available to us to manipulate the DOM and parse an external JSON file. We saw that having the right language available to us (like jQuery `$('.selector')` notation) makes it much easier for us to get more done with less thought and energy.

In many ways, all programming is a mixture of two activities:

- Using a provided language or API (like jQuery) to design and sequence a computer's behavior.

- Designing new languages and APIs to expand the methods, means, and conceptual frameworks available to us.

In the previous lab, we focused on the first point, learning how to use jQuery to get things done. In this lab, we'll focus on the second point; designing a new language that changes what's easy for us to do.

## Iteration One: The Environment

[Drawbot](https://www.drawbot.com/) is a Python library that provides fairly easy to use functions that allow us to sequentially create drawings. Many Drawbot programs use loops and functions to control blocks of code that look a little something like recipes:

```python
# 1. Instance 1
newPage(W, H)
frameDuration(.875) # Set a duration for this "page". Only matters for gifs or animations, where "pages" are frames.
fill(0,0,0) # set the fill state for the application R=0, G=0, B=0, or black.
rect(0,0, W, H) # draw a rectangle covering the background.
fill(1,1,1) # set the fill state for the application to R=1, G=1, B=1 or white.
rect(25, 25, W-50, H-50)
```

*This code is taken from the file `simple/simple01.py`. Follow along there for the full program.*

These are all built in Drawbot functions (documented [here](https://www.drawbot.com/content/shapes.html) for shapes) for colors. The docs are organized reasonably well, so try and navigate them yourself for future confusions about syntax or functions. You can always google if you get lost, too). You can read this code as a recipe:

1. `newPage`: Set up a new page with a given width `W` and height `H`. In drawbot, a "page" means different things, depending on what kind of document you're creating. If you're creating a PDF, for example, it means a new page in that PDF. If you're creating a GIF, like we are, it means a new frame in that gif. All subsequent operations are made onto that new page. [Here is more documentation on `newPage`](https://www.drawbot.com/content/canvas/pages.html).
2. `frameDuration`: This function is specific to drawing GIFs. It specifies how long, in seconds, to draw the frame for in the GIF. That number is passed as a parameter to the call to `frameDuration`. [Here is more documentation on `frameDuration`](https://www.drawbot.com/content/canvas/pages.html#drawBot.frameDuration).
3. `fill`: this is a super basic operation in Drawbot. It sets the fill color for the next operation (and for all of subsequent operations until you call `fill` again). There's a corresponding operation called `stroke` which you can use to set the stroke color. Notice that fill takes an RGB value, in the range `0` to `1`, rather that `0` - `255`. If you prefer thinking in terms of `0` – `255`, you can just divide everything by `255` before passing them to this function: `fill( 127/255, 127/255, 127/255)`. [Here is more documentation on `fill`](https://www.drawbot.com/content/color/fill.html).
4. `rect`: This draws a rectangle on the screen at the specified coordinates. The first parameter is the `x` coordinate of the rectangle, then the `y` coordinate, then the `width`, and then the `height`. [Here is more documentation on `rect`](https://www.drawbot.com/content/shapes/primitives.html#drawBot.rect).

For this session, these are the only Drawbot functions we're going to use. However, there are LOTS more. They all work in roughly the same way – set up some fill colors, draw something to the page, and then output the result.

Take a look at the file named `simple01.py` in the `examples` folder. Read it through, and run it with:

```bash
$ python examples/simple01.py
```

It should generate a file named `simple-01.gif` in the folder you're in. The gif should look something like this:

![Output of simple01.py](images/simple-01.gif)

Try playing with the file a little bit. Change some of the numbers in there and see how the output changes. When you're ready, move on to the next section


## Iteration Two: Basic Parameter Abstraction

You probably noticed that there was *a lot* of repetition in the `simple01.py`. We basically did the same exact thing three times, and just varied the function arguments a bit to change the size and position of the rectangle together (changing the width/height changed the size, and changing the x/y kept it centered).

What we have here is a **recipe** that we want to repeat with different inputs to achieve different effects. We can turn that recipe into a procedure in our language by making a new definition. Making new definitions is how we extend our conceptual vocabulary.

```python
def draw_frame(border):
	newPage(W, H)
	frameDuration(SPF)
	fill(0,0,0)
	rect(0,0, W, H)
	fill(1,1,1)
	rect( border, border, W-2*border, H-2*border )
```

This new definition lets us draw a frame. It makes a new page, sets the duration, draws a black background, and then draws a white rectangle with the parameter `border`, which we give it. `border` is a number that specifies how far from the edge of the screen we want our white rectangle offset in. Notice how at the end, we need to substract `2*border` from the width, because we want a border on all sides of the rectangle. Try changing this, and see what happens to the resulting GIF.

While we're at it, we might as well create a new recipe for making an animation, too.

```python
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
```

Now rather than describing *how* to draw a frame each time we want to draw one, we can just say `draw_frame(x)`, where I'm using `x` to represent whatever border value we want. Any time we want to change how a frame is drawn, all we need to do is change the definition of `draw_frame`, rather than changing each place we ever drew a frame in the program.

Take a look at `examples/simple02.py`, and run it. You should get a GIF that looks something like this:

![Output of simple02.py](images/simple-02.gif)

Try adding another parameter to draw frame, like one that lets you change the color of the rectangle. Or, try adding an [oval](https://www.drawbot.com/content/shapes/primitives.html#drawBot.oval) that sits inside the rectangle to the frame.

When you're ready, move on to the next section.


## Iteration Three: Recipes can be Data, Too

Okay, there was still a lot of repetition in the last example. We added a recipe for drawing frames, but we still needed to call `draw_frame` a bunch of times in the program, once for each frame we wanted to draw. In our program last time, what was changing each time wasn't anything about `draw_frame`, it was the parameter that we were passing to `draw_frame`, the border we wanted for each frame.

Rather than expressing our GIF, as a sequence of `draw_frames`:

```python
draw_frame(border_1)
draw_frame(border_2)
draw_frame(border_3)
```

a more succinct way way would be to just specify the GIF as a list of the border values in the sequence that we want to display them.

```python
borders = [border_1, border_2, border_3]
```

Then, we could pass that list, `borders`, off to a modified version of our `make_animation` function that knows how to handle a list of borders:

```python
def make_animation(recipe, output='simple-03.gif'):

    # Here, we loop across the border,
    # and draw a frame for each one.
    for border_value in recipe:
        draw_frame(border_value)

    saveImage(output)

make_animation(borders)
```

One of the advantages of this, is that now we're no longer constrained to writing down a **explicit list** of borders that we want. We can calculate the list from a function, or read it from a file, or generate it some other way. What was previously a program – us writing down an explicit list of function calls `draw_frame(border)` or a list of border values `[border_1, border_2]`, has become data we can manipulate.

For example, we could consider drawing the animation with an easing function, like linear easing:

```python
def linear_borders(start, end, steps):
    # put border values in here.
	borders = []

    # The range function gives us a list from 0 to steps.
	for i in range(steps):
        # divide the current step by the total to get
        # a number between 0 and 1
		t = i / steps

        # interpolate the start and end values linearly.
		borders.append( t*(end-start) + start )

    # Once we get here, we're done!
	return borders
```

Have changed our programs into data, we can start to think about new programs which compute that data.

Go ahead and run `examples/simple03.py` now. You should get a GIF like the one below:

![The default output of simple03.py](images/simple-03-reversed.gif)

Modify the code to use the `linear_borders` function provided in the file. Pick your own `start`, `end`, and `steps` values. You should get something like the GIF below (although the output will vary depending on your choice of parameters).

![The modified output of simple03.py](images/simple-03-linear.gif)

What else can you modify? Can you write a new easing function, like `linear_borders`, that produces a new list of borders given a `start`, `stop`, and `steps` value? What other parameters can you abstract out of the frame? Can you parameterize `fill`? `frameDuration`?

Can you keep climbing the ladder of abstraction? Try writing a function that produces `start`, `stop`, and `steps` values to pass to `linear_borders` based on some other data.

## To Be Continued

If you're tight on time, now's a good place to take a pause. You've learned some very basic drawbot commands, as well as the imperative, commands-oriented programming style drawbot uses, you've created some functions to play with those commands, and you've created some functions that play with those functions that play with those commands.

We've provided two slightly more advanced examples for you to take a look at whenever you like. These deal with building recipes that change the position of the rectangle and vary other parameters as well. To get started, read through the comments in `simple04.py` and `simple05.py`.
