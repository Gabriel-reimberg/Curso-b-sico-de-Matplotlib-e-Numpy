#Importando as bibliotecas
from matplotlib import pyplot as plt
import numpy as np

#estilo do grafico
plt.style.use("ggplot")

#gerando o vetor x (Tempo)
x = np.linspace(0,2*np.pi, 300)
y =  np.cos(2*x)

fig, axe = plt.subplots(figsize=(7, 4))
axe.plot(x, y, color="green", lw="1.0")

axe.set_title("Grafico do Cosseno",)
axe.set_xlabel("Eixo X")
axe.set_ylabel("Eixo Y")

plt.xticks(np.arange(0, 2*np.pi+0.5, 0.5))
plt.yticks(np.arange(-1, 1.2, 0.2))

plt.show()