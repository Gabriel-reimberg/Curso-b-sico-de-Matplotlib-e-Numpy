import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 5, 0.1)
y1 = x**1
y2 = x**2
y3 = x**3
y4 = x**4

#subplots para plotar varios graficos na mesma figura

fig, axes = plt.subplots(nrows = 2,
                         ncols=2, figsize=(8,4))#os parametros sao respectivamente:quantidades de linha, colunas e tamanho da figura
plt.suptitle("Gráficos com Subplots")

#Ajusta a distancia de cada grafico
plt.subplots_adjust(
    left=0.12,
    right=0.9,
    top=0.86,
    bottom=0.02,
    wspace=0.385,
    hspace=0.56
)

#plotando os diferentes graficos
axes[0, 0].plot(x, y1)
axes[0, 0].set_title("Função de Primeiro grau X¹")
axes[0, 0].set_xlabel("Eixo de tempo")
axes[0, 0].set_ylabel("Eixo de amplitude")
axes[0, 0].grid()

axes[0, 1].plot(x, y2)
axes[0, 1].set_title("Função do Segundo grau X²")
axes[0, 1].set_xlabel("Eixo de tempo")
axes[0, 1].set_ylabel("Eixo de amplitude")
axes[0, 1].grid()

axes[1, 0].plot(x, y3)
axes[1, 0].set_title("Função de Terceiro grau X³")
axes[1, 0].set_xlabel("Eixo de tempo")
axes[1, 0].set_ylabel("Eixo de amplitude")
axes[1, 0].grid()

axes[1, 1].plot(x, y4)
axes[1, 1].set_title("Função do Quarto grau X⁴")
axes[1, 1].set_xlabel("Eixo de tempo")
axes[1, 1].set_ylabel("Eixo de amplitude")
axes[1, 1].grid()

plt.show()