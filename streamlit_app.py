import streamlit as st
import numpy as np
import numpy.linalg as la
import matplotlib.pyplot as plt

st.title('Cálculo de Valores y Direcciones Principales con Círculos de Mohr')

# Selección del tipo de tensor
tensor_type = st.radio('Tipo de Tensor', ('Tensiones', 'Deformaciones'))

# Entrada de la matriz del tensor
st.write(f'Introduce los valores de la parte triangular superior de la matriz del tensor de {tensor_type.lower()}:')

# Crear campos de entrada para la parte triangular superior de la matriz 3x3
matrix_input = np.zeros((3, 3))
for i in range(3):
    for j in range(i, 3):
        value = st.number_input(f'Elemento ({i+1}, {j+1})', key=f'{i}{j}')
        matrix_input[i, j] = value
        if i != j:
            matrix_input[j, i] = value  # Rellenar la parte simétrica

# Mostrar la matriz completa en pantalla
st.subheader('Matriz del Tensor:')
st.write(matrix_input)

# Botón para calcular
if st.button('Calcular'):
    if matrix_input.shape == (3, 3):
        # Calcular valores y vectores propios
        eigenvalues, eigenvectors = la.eig(matrix_input)

        # Mostrar resultados
        st.subheader('Valores Principales:')
        st.write(eigenvalues)

        st.subheader('Direcciones Principales (Vectores Propios):')
        st.write(eigenvectors)

        # Calcular parámetros para los Círculos de Mohr
        sigma_1, sigma_2, sigma_3 = eigenvalues
        R1 = (sigma_1 - sigma_2) / 2
        C1 = (sigma_1 + sigma_2) / 2
        R2 = (sigma_1 - sigma_3) / 2
        C2 = (sigma_1 + sigma_3) / 2
        R3 = (sigma_2 - sigma_3) / 2
        C3 = (sigma_2 + sigma_3) / 2

        # Dibujar los Círculos de Mohr
        fig, ax = plt.subplots()

        # Círculo para sigma_1 y sigma_2
        circle1 = plt.Circle((C1, 0), R1, color='b', fill=False, linewidth=2, label=f'σ1-σ2')
        ax.add_artist(circle1)

        # Círculo para sigma_1 y sigma_3
        circle2 = plt.Circle((C2, 0), R2, color='g', fill=False, linewidth=2, label=f'σ1-σ3')
        ax.add_artist(circle2)

        # Círculo para sigma_2 y sigma_3
        circle3 = plt.Circle((C3, 0), R3, color='r', fill=False, linewidth=2, label=f'σ2-σ3')
        ax.add_artist(circle3)

        # Configuración del gráfico
        ax.set_xlabel('Tensión Normal (σ)')
        ax.set_ylabel('Tensión Cortante (τ)')
        ax.set_title('Círculos de Mohr')
        ax.legend()
        ax.grid(True)
        ax.set_aspect('equal', 'box')

        # Mostrar el gráfico en Streamlit
        st.pyplot(fig)
    else:
        st.write('La matriz debe ser 3x3')

