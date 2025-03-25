import streamlit as st

def main():
    st.title("Cálculo de valores y direcciones principales")
    st.write("Introduce los valores del tensor ")

    
    value = st.number_input(f'Elemento ({1}, {1})', key=f'{1}{1}')
    st.write("Valor ",value)



if __name__ == "__main__":
    main()