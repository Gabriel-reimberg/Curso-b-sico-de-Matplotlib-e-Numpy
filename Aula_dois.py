import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(0, 2*np.pi, 1000)
y = np.cos(4*t)
y1 = np.sin(4*t)
print(y)
print(y1)

plt.figure("COSSENO", figsize=(5,4))
plt.plot(t, y,)
plt.title("GRÁFICO DO COSSENO")
plt.xlabel("Tempo (s)")
plt.ylabel("Amplitude")


plt.figure("SENO", figsize=(7, 5))
plt.plot(t, y1,)
plt.title("GRÁFICO DO SENO")
plt.xlabel("Tempo (s)")
plt.ylabel("Amplitude")
plt.show()

plt.show()
