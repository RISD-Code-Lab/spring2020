# Code Lab Session 02: Let’s Talk Terminal
Wednesday, February 26th, 5:00pm–6:30pm | Design Center Room 212


Our topic: **Three Triplets on the Terminal**! Today, we’ll explore three sets of commands that help you accomplish different things in the macOS Terminal application. We’ll enjoy a tasting menu of varying levels of complexity, starting with an intro to navigating around, then looking at starting and stopping processes in the terminal, and concluding with a snack-level introduction to making `HTTP` requests right from the terminal, without a browser. There will be time for some light Q&A throughout. Good? Good.

*Note: This guide assumes you’re using macOS. Due to our own deficiencies, we are not able to support Windows users at this time. Dear Windows users: we’re sorry. Please find a macOS user near you to look on with; many of the concepts we’re covering are transferrable.*

- **Prelude: `whoami`**. Just what is this terminal thing? Why would we use it instead of a GUI, like Finder? Also, how do I make it look nice with the fonts and colors I want.
    - How to type?
- **Vignette #1: Location and Navigation.** Let’s get comfortable moving back and forth between the computer’s GUI in Finder, and the terminal. We’ll cover commands like:
    - `pwd` – which tells you where your terminal is in the filesystem right now.
    - `ls` – which tells you what’s in a directory (the pre-Finder word for “Folder”).
        - Let’s also talk about `ls -l` and `ls -la` variants that show you even more information.
    - `cd` – which allows you to move your terminal around through the filesystem, just like clicking on folders in Finder.
    - *With a special bonus appearance from:*
        - `open` – a macOS utility program that lets you open files, addresses, and locations in their default programs.
        -  `clear` or `cmd-K` – free up your visual real estate.
    - For those who want another look at the terminal, [this video](https://www.youtube.com/watch?v=V4ShSik25Wo) has more information.
    - If you'd like a more comprehensive reference, [check this website out](https://ss64.com/).
- **Vignette #2: The Lifecycle of a Software Process**. There are two kinds of processes, programs that run for a finite amount of time and then exit, and programs intended to be run forever. For the first kind, we can just fire and forget – they’ll clean up after themselves. The second kind needs management. In this short story, we’ll discuss how to manage long running processes like web servers, web crawlers, and other infinite loops:
    - `ps` – which shows you all the processes your user is currently running.
        - Let’s also talk about `ps gv` which shows you a bit more detail, including memory utilization.
        - Let’s also talk about `ps ax`, which shows you everything thats running on your computer.
    - `chmod` – which allows you to change what your user is allowed to do with a file, including which files are executable.
    - `./` – how to actually run a process.
        - `>` – how to redirect a process’s output to a file.
        - `^C` - how to kill a foreground process.
        - `&` – how to run a process in the background.
    - `kill -9` – which allows you to send control signals to processes from other terminals, and managing background processes.
    - *With a special bonus appearance from:*
        - `nano` – the worst text editor ever, but since we’re in the terminal, i guess…
        - `top` – a better version of `ps`.
- **Vignette #3: Local Area Networking** Your browser is basically a really fancy rendering engine that sends and recieves HTTP traffic. If we strip all of the rendering away, we get something that’s basically equivalent to `curl`, a option-laden utility that sends and receives HTTP traffic through the terminal.
    - `man` – a command that shows you the documentation for another terminal command. Yes, it has an unfortunate name; it’s a shortening of `man`ual. *Warning:* Not all commands have manual pages.
    - `curl` – a general purpose tool for sending and receiving HTTP traffic (and lots of other kinds of network traffic). The full scope of curl is way beyond us, but everything you would ever want to know about it is [here](https://ec.haxx.se/).
        - Sending a post request with `curl -X POST`
        - Sending a post request with a header using `curl -X POST -H "{Key}: {Value}" {url}`
    - *With a special bonus appearance from:*
        - a really dumb game that I made for the occasion.
- **Extra Credit: Not for Completion in Lab.** Try to run the server in `session-02/vignette-03` on your own. This will include downloading and installing `node` and `npm`, installing the dependencies for the server with `npm install`, and running the server with `node index.js`.

## Prelude and Motivation

The terminal is a command line interface to your computer. It lets you navigate around your computer, the way you can with the finder. However, Unlike the Finder, its main purpose is not navigation. Its purpose is to **run programs**:
- **local webservers** for developing your work. It's often easier to develop a site on a webserver, rather than in your fileystem. This allows you to read files (like csv files, or other bits of data), do AJAX requests with javascript.
- **remote servers** for deploying website projects to the web and managing remote servers. There are lots of ways of getting your files onto a remotely hosted server, so that people can access them. Once of the fastest ways is using `ssh`, a command line tool that allows you to log on to remote servers. Most remote servers do not have a GUI layer like Finder does; all interaction is handled through terminal-like interfaces, and fluency in these interfaces will be required for some setups.
- **content management systems** for building updatable websites and websites with backend. This might be something like Wordpress or Jekyll or Kirby, or any of the hundreds of static sites. These static site generators are run through the command line.
- **build processes** Many web development workflows include steps that transform and reorganize your code. For example, a tool like [sass](https://sass-lang.com/) provides an easier way to write CSS. sass files need to be compiled down to CSS before the browser can read them. This translation is done on the command line.
- **general programs and scripts** that you wrote. These might be javascript / node.js programs, or python programs that do anything you want. These are executed on the command line.
- **installing libraries and packages** often, someone else has written a tool that does something you need. These tools are often command line programs, and, further, are often installed via the command line.
- **training machine learning models** in tensorflow or pytorch. Most machine learning development is done in python using deep learning libraries like tensorflow and pytorch. These are exclusively run through the commandline.
- **reading documentation and expanding your knowledge** Once you get past the basis with web development, many resources and tutorials assume you're familiar with the command line. Not having a basic knowledge of the command line will slow you down. When it comes to machine learning, 100% of the resources I've seen (with the exception of RunwayML and ml5.js) assume terminal fluency. If you're interested in trying your own architectures or training custom models on a GPU, this is absolutely essential.
