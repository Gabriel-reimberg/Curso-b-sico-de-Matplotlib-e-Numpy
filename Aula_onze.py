#importando as bibliotecas
import matplotlib.pyplot as plt
import numpy as np

plt.style.use("ggplot")

x = np.linspace(1, 5, 500)
y = np.log10(x)

fig, axe = plt.subplots(figsize=(7, 4))
axe.plot(x, y, lw=1.2)

#escrita dentro do grafico
axe.text(2.6, 0.39, "p(2,5; 0,4)")
#Gerar texto com cor de fundo
axe.text(3.4, 0.39, "Logaritimo $y = log_{10}x$",
         fontsize=10, bbox=dict(facecolor="red",
         alpha=0.5)) #usar equação dentro do matplotlib $equação$
#Gerar texto com seta
axe.annotate("p(2,5; 0,4)", xy=(2.5, 0.4),
             fontsize=10, xytext=(1.5, 0.5),
             arrowprops=dict(facecolor="blue"),
             color="orange")

#colocando as linhas paralelas
axe.plot([0, 2.5], [0.4, 0.4],
         color="pink", linestyle="--", lw=0.8)
axe.plot([2.5, 2.5], [0, 0.4],
         color="pink", linestyle="--", lw=0.8)

#colocando o ponto no grafico
axe.plot([2.5], [0.4], marker="o", color="green")
axe.set_xticks(np.arange(0, 5.5, 0.5))

#colocando as indicaçoes no grafico
axe.set_title("Grafico logaritimico")
axe.set_xlabel("Eixo X")
axe.set_ylabel("Eixo Y")

plt.show()
