# 📊 Project 7: Interactive Car Sale Ads Analysis (Streamlit App)

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://project7-r80d.onrender.com/)

---

### 🚀 **Overview and Application Purpose**

This Streamlit application has been designed to offer an **interactive and visual exploration** of the car sale ads dataset (`vehicles_us.csv`). Its primary purpose is to allow users (analysts, car enthusiasts, or anyone interested in the automotive market) to easily analyze variable distributions and relationships between them through **customizable histograms and scatter plots**.

By providing interactive tools like column selectors and checkboxes, the application aims to **simplify the insight extraction process** and facilitate a deep understanding of the data without the need for coding, thus supporting evidence-based decision-making in the automotive sector.

---

### 🛠️ **Technologies and Libraries Used**

This project was developed using the following key tools:

* **Python:** Main programming language.
* **Streamlit:** Framework for building interactive web applications for data science.
* **Pandas:** For data manipulation and analysis.
* **Plotly Express:** For creating interactive and dynamic visualizations.

---

### ✨ **Key Application Features**

The application offers the following interactive functionalities:

* **Histogram Visualization:** Allows selecting any numerical column from the dataset to generate and explore its distribution.
* **Scatter Plots:** Facilitates visualizing the relationship between two selected variables (e.g., `price` vs. `odometer`).
* **Basic On-Load Preprocessing:** Performs initial handling of null values to ensure correct data visualization.
* **`hover_data` Interactivity:** When hovering over points in scatter plots, additional information from the dataset is displayed.
* **Responsive Design:** Adjusts to the container width for a better user experience on different screens.

---

### 💻 **Code Structure and Functionality**

The application's code follows a clear and modular structure:

1.  **Imports:** Loading of necessary libraries (`pandas`, `plotly.express`, `streamlit`).
2.  **Page Configuration:** `st.set_page_config` to optimize the application's visual layout.
3.  **Data Loading and Preprocessing:** Reading the `vehicles_us.csv` file and basic preprocessing to handle null values (`fillna` with median/mode in `model_year`, `cylinders`, `odometer`, `price`) before visualization.
4.  **Interactive Components (Streamlit):**
    * **`st.checkbox`:** Allows the user to toggle the display of histograms and scatter plots.
    * **`st.selectbox`:** Offers dropdown selectors for the user to choose which data columns to visualize in each chart type.
5.  **Chart Generation (Plotly Express):** Uses `px.histogram()` and `px.scatter()` to create interactive charts, including `hover_data` functionality for detailed insights.
6.  **Streamlit Visualization:** `st.plotly_chart()` is used to display interactive charts within the application, with `use_container_width=True` for responsiveness.
7.  **UI Elements and Messages:** Inclusion of titles (`st.title`, `st.subheader`), informational messages (`st.write`, `st.info`), and a footer to enhance user experience.

---

### 🚀 **Explore the Application!**

Click the badge to access and experiment with the application directly in your browser:

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://project7-r80d.onrender.com/)

---

### 📝 **Implementation Notes**

* Null value preprocessing is basic for demonstration purposes of the application. In a complete data analysis, a more in-depth and sophisticated study of missing value treatment would be performed.
* Column selection for scatter plots has been limited to those that typically offer the most interesting correlations in this type of dataset.

---

### 🤝 **Let's Connect**

I am always open to new opportunities and collaborations. Feel free to reach out!

* [![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/octavio-landa-verde/)
* [![Hotmail](https://img.shields.io/badge/email-Hotmail-blue.svg)](mailto:octaviolanda@hotmail.com)

---
---

# 📊 Proyecto 7: Análisis Interactivo de Anuncios de Venta de Coches (Streamlit App)

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://project7-r80d.onrender.com/)

---

### 🚀 **Visión General y Propósito de la Aplicación**

Esta aplicación de Streamlit ha sido diseñada para ofrecer una **exploración interactiva y visual** del conjunto de datos de anuncios de venta de coches (`vehicles_us.csv`). Su propósito principal es permitir a usuarios (analistas, entusiastas de coches, o cualquier interesado en el mercado automotriz) analizar fácilmente las distribuciones de variables y las relaciones entre ellas a través de **histogramas y gráficos de dispersión personalizables**.

Al proporcionar herramientas interactivas como selectores de columnas y casillas de verificación, la aplicación busca **simplificar el proceso de extracción de insights** y facilitar una comprensión profunda de los datos sin necesidad de escribir código, apoyando así la toma de decisiones basada en la evidencia en el sector automotriz.

---

### 🛠️ **Tecnologías y Librerías Utilizadas**

Este proyecto ha sido desarrollado utilizando las siguientes herramientas clave:

* **Python:** Lenguaje de programación principal.
* **Streamlit:** Framework para la construcción de aplicaciones web interactivas de ciencia de datos.
* **Pandas:** Para la manipulación y el análisis de datos.
* **Plotly Express:** Para la creación de visualizaciones interactivas y dinámicas.

---

### ✨ **Características Principales de la Aplicación**

La aplicación ofrece las siguientes funcionalidades interactivas:

* **Visualización de Histogramas:** Permite seleccionar cualquier columna numérica del dataset para generar y explorar su distribución.
* **Gráficos de Dispersión:** Facilita la visualización de la relación entre dos variables seleccionadas (ej. `price` vs. `odometer`).
* **Preprocesamiento Básico en Carga:** Realiza un tratamiento inicial de valores nulos para asegurar la correcta visualización de los datos.
* **Interactividad con `hover_data`:** Al pasar el ratón sobre los puntos en los gráficos de dispersión, se muestra información adicional del dataset.
* **Diseño Responsivo:** Se ajusta al ancho del contenedor para una mejor experiencia de usuario en diferentes pantallas.

---

### 💻 **Estructura y Funcionamiento del Código**

El código de la aplicación sigue una estructura clara y modular:

1.  **Importaciones:** Carga de las librerías necesarias (`pandas`, `plotly.express`, `streamlit`).
2.  **Configuración de la Página:** `st.set_page_config` para optimizar el diseño visual de la aplicación.
3.  **Carga y Preprocesamiento de Datos:** Lectura del archivo `vehicles_us.csv` y un preprocesamiento básico para manejar valores nulos (`fillna` con mediana/moda en `model_year`, `cylinders`, `odometer`, `price`) antes de la visualización.
4.  **Componentes Interactivos (Streamlit):**
    * **`st.checkbox`:** Permite al usuario activar o desactivar la visualización de histogramas y gráficos de dispersión.
    * **`st.selectbox`:** Ofrece selectores desplegables para que el usuario elija las columnas de datos a visualizar en cada tipo de gráfico.
5.  **Generación de Gráficos (Plotly Express):** Utiliza `px.histogram()` y `px.scatter()` para crear los gráficos interactivos, incluyendo la funcionalidad `hover_data` para insights detallados.
6.  **Visualización en Streamlit:** `st.plotly_chart()` se emplea para mostrar los gráficos interactivos dentro de la aplicación, con `use_container_width=True` para responsividad.
7.  **Elementos de UI y Mensajes:** Inclusión de títulos (`st.title`, `st.subheader`), mensajes informativos (`st.write`, `st.info`) y un pie de página para mejorar la experiencia del usuario.

---

### 🚀 **¡Explora la Aplicación!**

Haz clic en el badge para acceder y experimentar con la aplicación directamente en tu navegador:

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://project7-r80d.onrender.com/)

---

### 📝 **Notas de Implementación**

* El preprocesamiento de nulos es básico para fines de demostración de la aplicación. En un análisis de datos completo, se realizaría un estudio más profundo y sofisticado del tratamiento de los valores ausentes.
* La selección de columnas para los gráficos de dispersión se ha limitado a aquellas que suelen ofrecer las correlaciones más interesantes en este tipo de dataset.

---

### 🤝 **Conectemos**

Estoy siempre abierto a nuevas oportunidades y colaboraciones. ¡No dudes en contactarme!

* [![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/octavio-landa-verde/)
* [![Hotmail](https://img.shields.io/badge/email-Hotmail-blue.svg)](mailto:octaviolanda@hotmail.com)
