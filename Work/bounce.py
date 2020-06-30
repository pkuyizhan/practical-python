# bounce.py
#
# Exercise 1.5

height = 100.0
nth = 0

while nth < 10:
    nth += 1
    height *= 0.6
    print(nth, round(height, 4))

