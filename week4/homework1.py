# 20120818a

import math


def distance(p1, p2):
    a = abs(p1[0] - p2[0])
    b = abs(p1[1] - p2[1])
    return math.sqrt(a ** 2 + b ** 2)


def main():
    p1 = (1, 2)
    p2 = (6, 5)
    print('A ket pont kozti tavolsag:', f"{distance(p1, p2):.2f}")


#############################################################################

if __name__ == "__main__":
    main()
