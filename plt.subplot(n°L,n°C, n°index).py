# Exemplo de visualização de dados simplificado em gráficos com matplotlib e seaborn

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# importação de dados e tratamento
arvore = pd.read_csv(
    "C:/Users/Valdir Oliveira/Documents/FormacaoCD/13.Pratica em Python/dados/trees.csv")
print(arvore)
x = arvore.Girth
y = arvore.Volume

# plotagem de dados com matplotlib e seaborn
plt.figure(1)
plt.subplot(2, 2, 1)
plt.scatter(x, y, color="gray")
plt.title("Árvore")
plt.xlabel("Circunferência")
plt.ylabel("Volume")
plt.subplot(2, 2, 2)
plt.plot(x, y, color="gray")
plt.title("Gráfico de evolução da árvore")
plt.xlabel("Circunferência")
plt.ylabel("Volume")
plt.subplot(2, 2, 3)
sns.histplot(y, bins=10, color="gray", kde=False)
plt.title("Gráfico de Histograma da árvore")
plt.xlabel("Frequência")
plt.ylabel("Volume")
plt.tight_layout()
plt.show()
