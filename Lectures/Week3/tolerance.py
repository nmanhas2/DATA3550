from math import sqrt

ESPILON = 1E-14 #tolerance for comparing floating point numbers
r = sqrt(2.0)

if(abs(r*r - 2.0) < ESPILON):
    print("sqrt(2.0) squared is approximately 2.0")
