# Ready, Set, Loop with Python & DrawBot

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

Now, let's install all of the libraries that we'll need to run to use drawBot. The list of these is included in `requirements.txt`. Don't freak out, though you don't have to install these all by hand. Just run:

```sh
# Install the list of requirements automatically.
$ pip install -r requirements.txt
```

And python will install all of them for you. If you ever install a new module, it's a good practice to record that new module in the list. Again, don't freak out, you don't have to record this stuff by hand. Just run:

```sh
# Update the list of requirements when something changes.
$ pip freeze > requirements.txt
```

This will dump the complete list of current dependencies into the requirements.txt file, for future `pip install` calls.

## Basics

**Code Will be Posted on Sunday, 3/15**
