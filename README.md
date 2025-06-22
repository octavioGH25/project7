# project7
## Proyecto Final del Sprint 7
### Para que sirve ésta app de Streamlit
#### Esta aplicación de Streamlit ha sido diseñada para ofrecer una exploración interactiva y visual del conjunto de datos de anuncios de venta de coches (vehicles_us.csv). El propósito principal es permitir a los usuarios analizar fácilmente las distribuciones de variables y las relaciones entre ellas a través de histogramas y gráficos de dispersión personalizables. Al proporcionar herramientas interactivas como selectores de columnas y casillas de verificación, la aplicación busca simplificar el proceso de extracción de insights y facilitar una comprensión profunda de los datos sin necesidad de escribir código, apoyando así la toma de decisiones basada en la evidencia.

### 1.- Importaciones:
#### Se importan pandas para el manejo de datos, plotly.express para gráficos interactivos y streamlit para construir la aplicación web. 
### 2.- Configuración de la Página (st.set_page_config):
#### Establece el título de la pestaña del navegador y el diseño de la página (wide es útil para gráficos grandes). 
### 3.- Carga de Datos:
#### Lee el archivo vehicles_us.csv
### 4.- Preprocesamiento Básico:
#### Añadí unas líneas simples para rellenar valores nulos en algunas columnas numéricas comunes (model_year, cylinders, odometer, price) con su mediana o moda. Esto es crucial para que plotly.express no tenga problemas al intentar graficar columnas con NaNs. En un proyecto real, haría un análisis y tratamiento de nulos más sofisticado. 
### 5.- Títulos y Subtítulos:
#### st.title() y st.subheader() se usan para dar una estructura clara a la aplicación.
### 6.- Checkboxes (st.checkbox):
#### Son la clave para la interactividad. Permiten al usuario decidir si quiere ver un histograma o un gráfico de dispersión. El código dentro de un if st.checkbox(...) solo se ejecuta si la casilla está marcada. 
### 7.- Selectboxes (st.selectbox):
#### Dentro de cada sección de gráfico, estos selectores permiten al usuario elegir qué columnas del dataset quiere analizar. 
#### •	Para el histograma, se listan todas las columnas numéricas.
#### •	Para el gráfico de dispersión, seleccioné un subconjunto de columnas que suelen ser interesantes para correlaciones en este tipo de dataset.
### 8.- Creación de Gráficos Plotly: 
#### •	px.histogram() crea el histograma.
#### •	px.scatter() crea el gráfico de dispersión. hover_data es una característica útil de Plotly que muestra información adicional de las columnas especificadas cuando el usuario pasa el mouse sobre un punto del gráfico.
### 9.- Mostrar Gráficos (st.plotly_chart):
#### st.plotly_chart(fig, use_container_width=True) muestra el gráfico interactivo. use_container_width=True es importante para que el gráfico se ajuste al ancho de la columna donde está alojado en Streamlit, haciéndolo responsivo. 
### 10.- Mensajes Informativos (st.write, st.info):
#### Estos añaden contexto a los gráficos, explicando qué está mostrando cada uno. 
### 11.- Mensaje de Pie de Página:
#### Un pequeño detalle para el final de la aplicación.
