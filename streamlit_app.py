import streamlit as st
import numpy as np
import numpy.linalg as la
import matplotlib.pyplot as plt

st.title('Cálculo de Valores y Direcciones Principales con Círculo de Mohr')

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

        # Calcular parámetros para el Círculo de Mohr
        sigma_1, sigma_2, sigma_3 = eigenvalues
        R = (sigma_1 - sigma_3) / 2
        C = (sigma_1 + sigma_3) / 2

        # Dibujar el Círculo de Mohr
        fig, ax = plt.subplots()
        circle = plt.Circle((C, 0), R, color='b', fill=False, linewidth=2)
        ax.add_artist(circle)

        # Líneas de referencia
        ax.plot([C, C], [-R, R], color='r', linestyle='--')
        ax.plot([sigma_1, sigma_1], [-R, R], color='g', linestyle='--')
        ax.plot([sigma_3, sigma_3], [-R, R], color='g', linestyle='--')

        # Configuración del gráfico
        ax.set_xlabel('Tensión Normal (σ)')
        ax.set_ylabel('Tensión Cortante (τ)')
        ax.set_title('Círculo de Mohr')
        ax.grid(True)
        ax.set_aspect('equal', 'box')

        # Mostrar el gráfico en Streamlit
        st.pyplot(fig)
    else:
        st.write('La matriz debe ser 3x3')
