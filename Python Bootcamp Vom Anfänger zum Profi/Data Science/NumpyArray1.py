#Numpy Arrays
import numpy as np

a = np.array([1,2,3,4])
print(a)
#Ausgabe: [1 2 3 4]

b = np.array([False,True, True, False])
print(b)
#Ausgabe: [False True True False]

print(b[1])
#Ausgabe: True an der Stelle 1

print(a[b])
#Ausgabe: Array mit den Zahlen [2 3], also die Werte an der Stelle, bei der bei "b" ein True steht

c= a >= 3
#damit weiße ich "c" ein Array zu mit allen Zahlen aus dem Array "a" die größer gleich 3 sind
print(c)
#Ausgabe: [False False  True  True]
print(a[c])
#Ausgabe: [3 4]
print(a[a >= 3])
#kürzere Schreibeweise

