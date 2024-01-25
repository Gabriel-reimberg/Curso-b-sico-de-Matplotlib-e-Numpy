import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(0, 2*np.pi, 1000)
y = np.cos(4*t)
print(y)

plt.plot(t, y,)
plt.title("GRÁFICO DO COSSENO")
plt.xlabel("Tempo (s)")
plt.ylabel("Amplitude")
plt.show()
