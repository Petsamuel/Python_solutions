import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    if ( (n%2) != 0):
        print("weird")
    elif (n in range (2, 5, 2)):
        print ("not weird")
    elif (n in range(6,20, 2 )):
        print ("weird")
    elif (n > 20):
        print ("not weird")
    else:
        print (" Not weird")