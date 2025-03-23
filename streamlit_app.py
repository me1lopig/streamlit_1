import streamlit as st
import numpy as np
import numpy.linalg as la

st.title('Cálculo de Valores y Direcciones Principales')

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
    else:
        st.write('La matriz debe ser 3x3')


