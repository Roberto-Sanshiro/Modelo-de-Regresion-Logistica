## :bulb: Modelo de Regresión Logística para Credit Scoring

Este proyecto implementa un modelo de **Regresión Logística** para estimar el **Riesgo Crediticio**, utilizando variables tanto **numéricas** como **categóricas**. El objetivo es realizar una **clasificación binaria** a partir de datos estructurados, con el fin de predecir si un cliente representa un riesgo de incumplimiento.

### 📐 Fundamento Matemático

La regresión logística modela la probabilidad de un evento binario (por ejemplo: que un cliente incumpla o no) como:

$$
P(y=1 \mid \mathbf{x}) = \frac{1}{1 + e^{-(\beta_0 + \beta_1 x_1 + \cdots + \beta_n x_n)}}
$$

Esta función toma una combinación lineal de las variables de entrada $\mathbf{x} = (x_1, \ldots, x_n)$ y sus coeficientes $\beta_i$, y la transforma en un valor entre 0 y 1, que representa una probabilidad.

Aquí, las variables de entrada son las características o datos que conocemos del cliente, como su edad, ingreso, historial crediticio, etc. Los coeficientes $\beta_0, \beta_1, \ldots, \beta_n$ indican la importancia que cada característica tiene para predecir el riesgo.

### 🛠️ Construcción del Modelo

Para construir el modelo de regresión logística seguimos estos pasos:

1. **Selección de Variables:**  
   Se eligen las características relevantes del cliente (edad, ingresos, historial crediticio, etc.) que podrían influir en el riesgo de incumplimiento.

2. **Estimación de Coeficientes:**  
   Se ajustan los coeficientes $\beta_0, \beta_1, \ldots, \beta_n$ utilizando el método de máxima verosimilitud, que busca los valores que mejor explican los datos observados.

3. **Función de Verosimilitud:**  
   El modelo maximiza la probabilidad de observar los datos bajo las probabilidades predichas por la función sigmoide.

4. **Evaluación del Modelo:**  
   Se evalúa el desempeño usando métricas como la matriz de confusión, AUC-ROC, precisión y recall para asegurar que el modelo predice bien el riesgo.

5. **Umbral de Clasificación:**  
   Se define un umbral (usualmente 0.5) para decidir si un cliente es considerado de riesgo o no, basado en la probabilidad estimada.
