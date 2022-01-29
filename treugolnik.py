# найти площадь и периметр
import math
AB = float (input("длина первого катета:"))
AC = float (input("длина второго катета:"))
BC = math.sqrt(AB**2*AC**2)
s = (AB*AC)/2
p = AB + AC + BC
print (s)
print (p)