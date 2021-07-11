# A Python program using argument parser to find the square of a given number

import argparse

parser = argparse.ArgumentParser(description='This program display square value of a given number')

parser.add_argument("num", type=int,help='please input integer type number.')

args=parser.parse_args()

result=args.num * args.num

print("square is :",result)