import classes
import os
import sys

print("main.py")

poop = classes.resource_management()


with open(poop.error_log, "a") as target:
    target.write("write the god dam error")
