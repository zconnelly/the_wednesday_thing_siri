#!/usr/bin/env python
import time

name = "Zac"

query = str(raw_input("How can I help you? "))


def anticipation():
    time.sleep(1)
    print "."
    time.sleep(1)
    print "."
    time.sleep(1)
    print "."

if query == "What is the weather?":
    anticipation()
    print "50 degrees F and Cloudy"
elif query == "Can you convert degrees for me?":
    print "Sure!"
    f = int(raw_input("How many degrees Fathneuh is it? "))
    c = (f - 32) / 1.8
    anticipation()
    print str(c) + " Degrees Celcius"
elif query == "What is the time?":
    print time.strftime("%H:%M:%S")
else:
    print "I didn't understand that..."
