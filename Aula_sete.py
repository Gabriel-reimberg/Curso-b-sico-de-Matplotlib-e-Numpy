#impotando as biblotecas
from matplotlib import pyplot as plt
import numpy as np

x = np.linspace(0, 2*np.pi, 50)
y = np.cos(4*x)

plt.figure(figsize=(8, 4))
plt.plot(x, y, color="purple", lw=1.0,
         marker="o", linestyle="dashed" )

plt.grid()
plt.title("Grafico do Cosseno")
plt.xlabel("Eixo Tempo")
plt.ylabel("Eixo da Amplitude")
plt.show()