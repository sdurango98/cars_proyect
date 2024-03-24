import pandas as pd
import plotly.express as px
import streamlit as st
        
car_data = pd.read_csv("C:\\Users\\SANTIAGO DURANGO\\anaconda3\\envs\\myenv\\cars_proyect\\vehicles_us.csv") # leer los datos
hist_button = st.button('Construir histograma') # crear un botón
        
if hist_button: # al hacer clic en el botón
            # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
            
            # crear un histograma
    fig = px.histogram(car_data, x="odometer")
        
            # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)


# crear una casilla de verificación
build_dispersion = st.checkbox('Construir un diagrama de dispercion')

if build_dispersion: # si la casilla de verificación está seleccionada
    st.write('Construir un digrama de dispercion para la columna odómetro')

     # crear un diagrama de dispersion 
    fig = px.scatter(car_data, x="odometer", y= "price")
        
            # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)