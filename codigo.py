import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Função para gerar uma esfera
def gerar_esfera(raio, resolucao):
    u = np.linspace(0, 2 * np.pi, resolucao)
    v = np.linspace(0, np.pi, resolucao)
    x = raio * np.outer(np.cos(u), np.sin(v))
    y = raio * np.outer(np.sin(u), np.sin(v))
    z = raio * np.outer(np.ones(np.size(u)), np.cos(v))
    return x, y, z

# Função para aplicar uma matriz de transformação
def aplicar_transformacao(matriz, pontos):
    pontos_homogeneos = np.vstack((pontos, np.ones((1, pontos.shape[1]))))
    pontos_transformados = np.dot(matriz, pontos_homogeneos)[:3, :]
    return pontos_transformados

# Parâmetros da esfera
raio = 1
resolucao = 30

# Gera a esfera
x, y, z = gerar_esfera(raio, resolucao)

# Converte os pontos da esfera em uma única matriz de pontos
pontos = np.array([x.flatten(), y.flatten(), z.flatten()])

# Matriz de transformação de exemplo (translação)
matriz_translacao = np.array([
    [1, 0, 0, 2],  # Move 2 unidades no eixo X
    [0, 1, 0, 1],  # Move 1 unidade no eixo Y
    [0, 0, 1, 1],  # Move 1 unidade no eixo Z
    [0, 0, 0, 1]
])

# Aplica a transformação aos pontos da esfera
pontos_transformados = aplicar_transformacao(matriz_translacao, pontos)

# Reshape os pontos transformados para as dimensões originais
x_t = pontos_transformados[0, :].reshape((resolucao, resolucao))
y_t = pontos_transformados[1, :].reshape((resolucao, resolucao))
z_t = pontos_transformados[2, :].reshape((resolucao, resolucao))

# Plotando a esfera transformada
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x_t, y_t, z_t, color='b')

# Configuração do gráfico
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Esfera Movimentada por Matrizes')

plt.show()
