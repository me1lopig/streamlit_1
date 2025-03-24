import streamlit as st
import numpy as np
import pandas as pd



def calcular_tensiones_principales(tensor):
    """Calcula las tensiones principales y los vectores principales de un tensor de tensiones simétrico."""
    eigenvalores, eigenvectores = np.linalg.eig(tensor)

    # Ordenar las tensiones principales (eigenvalores) de mayor a menor
    indices_ordenados = np.argsort(eigenvalores)[::-1]
    tensiones_principales_ordenadas = eigenvalores[indices_ordenados]
    direcciones_principales_ordenadas = eigenvectores[:, indices_ordenados]

    return tensiones_principales_ordenadas, direcciones_principales_ordenadas

def main():
    st.title("Cálculo de valores y direcciones principales")

    st.write("Introduce los valores del tensor ")

    # Inicializar el tensor con valores por defecto
    tensor = np.zeros((3, 3))

    # Entradas para los valores únicos del tensor (debido a la simetría)
    tensor[0, 0] = st.number_input("σxx:", value=1.0)
    tensor[1, 1] = st.number_input("σyy:", value=1.0)
    tensor[2, 2] = st.number_input("σzz:", value=1.0)
    tensor[0, 1] = tensor[1, 0] = st.number_input("σxy = σyx:", value=0.0)
    tensor[0, 2] = tensor[2, 0] = st.number_input("σxz = σzx:", value=0.0)
    tensor[1, 2] = tensor[2, 1] = st.number_input("σyz = σzy:", value=0.0)

    st.subheader("Tensor de Tensiones Introducido:")
    st.write(pd.DataFrame(tensor))  # Mostrar el tensor como un DataFrame

    if st.button("Calcular Tensiones Principales"):
        tensiones_principales, direcciones_principales = calcular_tensiones_principales(tensor)

        st.subheader("Tensiones Principales (Ordenadas):")
        st.write(tensiones_principales)

        st.subheader("Direcciones Principales Correspondientes:")
        # Crear un DataFrame para mostrar las direcciones principales
        df_direcciones = pd.DataFrame(direcciones_principales,columns=[f"Dirección Principal {i+1}" for i in range(3)])
        st.write(df_direcciones)

        # Etiquetar las tensiones principales con sus direcciones correspondientes
        st.subheader("Relación Tensiones Principales - Direcciones Principales:")
        for i in range(3):
            st.write(f"Tensión Principal {i+1}: {tensiones_principales[i]:.4f}")
            st.write(f"Dirección Principal {i+1}: {direcciones_principales[:, i]}")
            st.write("---")

if __name__ == "__main__":
    main()