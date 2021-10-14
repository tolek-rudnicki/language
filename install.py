import os
import sys

def inst():
    print("test")


a = input("This script is only for linux that has github installed! press Y to proceede and N to cancle")
if a == 'N':
    print("cancelling!")
else:
    if a == "Y":
        print("Ok proceeding")
