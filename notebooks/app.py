import pandas as pd
import plotly.express as px
import streamlit as st
     
car_data = pd.read_csv(r'vehicles_us.csv') # leer los datos

# Configuración de la página de Streamlit
st.set_page_config(
    page_title="Análisis de Anuncios de Venta de Coches",
    layout="wide", # Usa un diseño ancho para mejor visualización de gráficos
    initial_sidebar_state="expanded"
)

# Título principal de la aplicación
st.title('Análisis de Datos de Anuncios de Venta de Coches 🚗')

# Subtítulo introductorio
st.subheader('Explora la distribución y relaciones de las características de los vehículos.')
# Preparación de datos
# En un proyecto real, se haría un preprocesamiento más exhaustivo.
# Aquí se rellena 'model_year' con la mediana y 'cylinders' con la moda
# para asegurar que los gráficos funcionen sin errores de valores nulos si esas columnas se usan.
car_data['model_year'].fillna(car_data['model_year'].median(), inplace=True)
car_data['cylinders'].fillna(car_data['cylinders'].mode()[0], inplace=True)
car_data['odometer'].fillna(car_data['odometer'].median(), inplace=True)
car_data['price'].fillna(car_data['price'].median(), inplace=True)


#Secciones de la aplicación con controles interactivos

# Sección para Histograma
st.header('Histogramas Interactivos')
st.write('Selecciona una característica para visualizar su distribución en el conjunto de datos.')

# Checkbox para mostrar el histograma
build_histogram = st.checkbox('Mostrar histograma de datos de anuncios de venta de coches')

if build_histogram:
    # Mensaje cuando el histograma está activo
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches:')

    # Selector para elegir la columna del histograma
    # Excluye columnas no numéricas o irrelevantes para histogramas
    numeric_cols = car_data.select_dtypes(include=['number']).columns.tolist()
    column_to_plot_hist = st.selectbox(
        'Selecciona la columna para el histograma:',
        numeric_cols,
        index=numeric_cols.index('price') if 'price' in numeric_cols else 0 # Establece 'price' como valor predeterminado
    )

    # Crear el histograma
    fig_hist = px.histogram(car_data, x=column_to_plot_hist, title=f'Distribución de {column_to_plot_hist.replace("_", " ").title()}')

    # Mostrar el gráfico Plotly interactivo
    st.plotly_chart(fig_hist, use_container_width=True)
    st.info(f"Este histograma muestra cómo se distribuyen los valores de la columna '{column_to_plot_hist.replace('_', ' ').title()}' en el dataset.")


# Separador para mejor organización visual
st.markdown('---')


# Sección para Gráfico de Dispersión
st.header('Gráficos de Dispersión Interactivos')
st.write('Explora la relación entre dos características diferentes de los vehículos.')

# Checkbox para mostrar el gráfico de dispersión
build_scatter = st.checkbox('Mostrar gráfico de dispersión de datos de anuncios de venta de coches')

if build_scatter:
    # Mensaje cuando el gráfico de dispersión está activo
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches:')

    # Selectores para elegir las columnas del eje X y Y para el gráfico de dispersión
    # Solo usamos columnas numéricas que tienen sentido para un scatter plot
    scatter_cols = ['price', 'odometer', 'model_year', 'cylinders', 'condition']
    
    col_x_scatter = st.selectbox(
        'Selecciona la columna para el eje X:',
        scatter_cols,
        index=scatter_cols.index('odometer') # Establece 'odometer' como predeterminado para X
    )

    col_y_scatter = st.selectbox(
        'Selecciona la columna para el eje Y:',
        scatter_cols,
        index=scatter_cols.index('price') # Establece 'price' como predeterminado para Y
    )

    # Crear el gráfico de dispersión
    fig_scatter = px.scatter(
        car_data,
        x=col_x_scatter,
        y=col_y_scatter,
        title=f'Relación entre {col_x_scatter.replace("_", " ").title()} y {col_y_scatter.replace("_", " ").title()}',
        hover_data=['model', 'type', 'condition', 'fuel'] # Datos adicionales para mostrar al pasar el mouse
    )

    # Mostrar el gráfico Plotly interactivo
    st.plotly_chart(fig_scatter, use_container_width=True)
    st.info(f"Este gráfico de dispersión visualiza la correlación entre '{col_x_scatter.replace('_', ' ').title()}' y '{col_y_scatter.replace('_', ' ').title()}'.")


# Mensaje de pie de página
st.markdown('---')
st.caption('Desarrollado como parte del proyecto del Sprint 7 de TripleTen.')