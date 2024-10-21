import numpy as np
import math
from datetime import datetime

def method1(entries):
    #Wurzel berechnen mit Python (for Schleife)
    out = []
    for entry in entries:
        out.append(math.sqrt(entry))

def method2(entries):
    #Wurzel berechnen mit Python (List - Comprehension)
    out = [math.sqrt(entry) for entry in entries]

def method3(entries_np):
    #Wurzel berechnen mit Numpy
    #schnellste Variante von allen 3 
    out = np.sqrt(entries_np)

N = 10000000
entries_np = np.random.random(N)
entries = list(entries_np)

start = datetime.now()
method1(entries)
end = datetime.now()
print("Method1 = " + str(end - start))

start = datetime.now()
method2(entries)
end = datetime.now()
print("Method2 = " + str(end - start))

start = datetime.now()
method3(entries)
end = datetime.now()
print("Method3 = " + str(end - start))