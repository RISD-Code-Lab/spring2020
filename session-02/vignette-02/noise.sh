#!/bin/bash

# How wide a range?
SIZE=3

# Where to start?
# ( 32 to 37 is a good range, as is 91 - 97 )
OFFSET=91

# Rendering Loop
while true; do printf "\x$(printf "%x" $(( ($RANDOM % $SIZE) + $OFFSET)))"; done;
