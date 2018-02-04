#!/usr/bin/env python
# -*- coding: utf-8 -*-

x = int(input("Please enter a integer: "))

if x < 0:
    x = 0
    print("Negative changed to zero.")
elif x == 0:
    print("Zero")
elif x == 1:
    print("Single")
else:
    print("More")

champion = 'Stipe Miočić'

if champion == "Stipe Miočić":
    print("UFC Heavyweight Champion: " + champion)