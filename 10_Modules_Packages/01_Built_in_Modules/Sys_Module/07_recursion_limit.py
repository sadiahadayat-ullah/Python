import sys
print("Current recursion limit:", sys.getrecursionlimit())
sys.setrecursionlimit(2000)
print("New recursion limit:", sys.getrecursionlimit())