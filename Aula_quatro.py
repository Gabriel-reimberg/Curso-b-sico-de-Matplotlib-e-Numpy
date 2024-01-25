import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2*np.pi, 500) #sendo 0 a 2pi o intervalo de tempo e 500 o numero de amostras
c = np.cos(x)
s = np.sin(x)

plt.figure("Gráficos consenoidais", figsize=(8, 4))
plt.subplots_adjust(
    left=0.11,
    right=0.9,
    top=0.9,
    bottom=0.14,
    wspace=0.438,
    hspace=0.5
)

ax1 = plt.subplot(1, 2, 1)#os argumentos sao respectivamente, quantidade de linhas e de colunas e posição do axes
plt.plot(x, c)
ax1.set_title("Grafico do cosseno")
ax1.set_xlabel("Eixo de tempo")
ax1.set_ylabel("Eixo de amplitude")
ax1.grid()


ax2 = plt.subplot(1, 2, 2)#subplot vai ter na coluna obs: outro grafico
plt.plot(x, s)
ax2.set_title("Grafico do seno")
ax2.set_xlabel("Eixo de tempo")
ax2.set_ylabel("Eixo de amplitude")
ax2.grid()

plt.show()
