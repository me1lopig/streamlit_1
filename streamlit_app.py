
import streamlit as st
import math

st.title('Calculadora de Ecuaciones de Segundo Grado')

# Entradas para los coeficientes
a = st.number_input('Coeficiente a:', value=1.0)
b = st.number_input('Coeficiente b:', value=0.0)
c = st.number_input('Coeficiente c:', value=0.0)

# Botón para calcular
if st.button('Calcular'):
    # Calcular el discriminante
    discriminante = b**2 - 4*a*c

    # Calcular las soluciones
    if discriminante > 0:
        x1 = (-b + math.sqrt(discriminante)) / (2*a)
        x2 = (-b - math.sqrt(discriminante)) / (2*a)
        st.write(f'Soluciones: x1 = {x1}, x2 = {x2}')
    elif discriminante == 0:
        x = -b / (2*a)
        st.write(f'Solución única: x = {x}')
    else:
        st.write('La ecuación no tiene soluciones reales.')

    # Mostrar la ecuación introducida
    st.write(f'Ecuación: {a}x² + {b}x + {c} = 0')