import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 5, 0.1)
y1 = x**1
y2 = x**2
y3 = x**3
y4 = x**4

#subplots

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(nrows = 2,ncols=2, figsize=(8,4))#os parametros sao respectivamente:quantidades de linha, colunas e tamanho da figura
plt.suptitle("Gráficos com Subplots")
plt.subplots_adjust(
    left=0.12,
    right=0.9,
    top=0.86,
    bottom=0.02,
    wspace=0.385,
    hspace=0.56
)

ax1.plot(x, y1)
ax1.set_title("Função de Primeiro grau X¹")
ax1.set_xlabel("Eixo de tempo")
ax1.set_ylabel("Eixo de amplitude")
ax1.grid()

ax2.plot(x, y2)
ax2.set_title("Função do Segundo grau X²")
ax2.set_xlabel("Eixo de tempo")
ax2.set_ylabel("Eixo de amplitude")
ax2.grid()

ax3.plot(x, y3)
ax3.set_title("Função de Terceiro grau X³")
ax3.set_xlabel("Eixo de tempo")
ax3.set_ylabel("Eixo de amplitude")
ax3.grid()

ax4.plot(x, y4)
ax4.set_title("Função do Quarto grau X⁴")
ax4.set_xlabel("Eixo de tempo")
ax4.set_ylabel("Eixo de amplitude")
ax4.grid()

plt.show()