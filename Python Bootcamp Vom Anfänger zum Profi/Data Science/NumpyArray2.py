#Mehrdimensionale Arrays
import numpy as np

a = np.array([1, 2, 3, 4, 5, 6, 7, 8])

reshaped = a.reshape((2,4))
#Ändert das eindimensionale Array in ein mehrdimensionales Array
#Hierbei gibt die 2 die Dimensionen an und 4 die Zahlen in einer Dimension
#bei 2,4 müssen es dann auch in Summe 8 Zahlen sein, die sich im Array befinden

print(reshaped[0])
#Ausgabe: [1 2 3 4]
print(reshaped[0][1])
#Ausgabe: 2

reshaped = a.reshape((4,2))
print(reshaped)
#Ausgabe: [[1 2] [3 4] [5 6] [7 8]]

print(reshaped.reshape(-1))
#mit der -1 berechnet Python dann automatisch was das beste ist, in diesem Fall schreibt alles in eine Dimension

print(reshaped.shape)
#Ausgabe: (4, 2), gibt zurück welche Dimensionen das Array hat