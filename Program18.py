# A Python program to add two number using parser arguments

import argparse

parser=argparse.ArgumentParser()

parser.add_argument('nums',type=float,nargs=2,help=' put two numbers as arguments')

args=parser.parse_args()

result=args.nums[0]+args.nums[1]

print("Sum is :",result)