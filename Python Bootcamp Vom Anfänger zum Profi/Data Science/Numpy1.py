
import matplotlib.pyplot as plt
import numpy as np

#erstellt ein Array mit Zahlen von 0 bis 9
# "np.arane(10) + 3" würde bei jeder Zahl 3 addieren
xs = np.arange(10)
ys = xs **2

#gibt den Durchschnitt aus von dem Array "xs"
print(xs.mean())

#gibt die kleinste und größte Zahl aus von dem Array "xs"
print(xs.min())
print(xs.max())

plt.plot(xs,ys)
plt.show()
