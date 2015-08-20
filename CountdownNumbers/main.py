import math as m
import random as r

def getRandoms(lows, highs):
  numbers = []
  # Low numbers can be from 1-10, inclusive
  for val in range(lows):
    numbers.append(r.randint(1, 10))

  # High numbers can be from 25 - 100, multiples of 25
  for val in range(highs):
    numbers.append(r.randrange(25, 101, 25))

  print numbers

if __name__ == '__main__':
  # TODO: need to check for length of both, can't be over 6
  lows = raw_input('How many low numbers? ')
  highs = raw_input('How many high numbers? ')
  print getRandoms(lows, highs)