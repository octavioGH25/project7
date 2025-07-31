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
