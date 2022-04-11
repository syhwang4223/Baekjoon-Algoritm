from sys import stdin
import math

n, m = stdin.readline().split()

print(m - math.gcd(m, n))