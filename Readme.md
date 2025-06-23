## :bulb: Modelo de Regresión Logística para Credit Scoring

Este proyecto implementa un modelo de **Regresión Logística** para predecir el **Riesgo Crediticio**, utilizando un conjunto de variables numéricas y categóricas. El modelo está diseñado para realizar clasificación binaria a partir de datos estructurados.

## 📌 Funciones principales

### ✅ Preprocesamiento automatizado
- Validación de columnas requeridas
- Codificación de variables categóricas mediante One-Hot Encoding
- Escalado de variables numéricas con `StandardScaler`

### ✅ Entrenamiento del modelo
- Entrenamiento de un modelo de regresión logística (`LogisticRegression`)
- Separación automática en conjuntos de entrenamiento y prueba

### ✅ Evaluación del desempeño
- Cálculo de métricas de clasificación:
  - Accuracy
  - Matriz de confusión
  - AUC-ROC
  - Precision, Recall, F1-Score
- Visualización de la curva ROC

### ✅ Interpretación estadística (opcional)
- Estimación de coeficientes y significancia estadística con `statsmodels`

### ✅ Persistencia del modelo
- Guardado del modelo entrenado (`modelo_logistico_credito.pkl`)
- Guardado del escalador (`escalador_credito.pkl`)

## 📁 Estructura esperada de los datos

El archivo de entrada debe ser un archivo Excel llamado `datos_clientes.xlsx`, con una hoja de nombre `"Hoja1"`. Debe contener la siguiente información:

### Variable objetivo
- `riesgo_credito` (0 = bajo riesgo, 1 = alto riesgo)

### Variables predictoras

#### Numéricas:
- `ingreso_mensual`
- `antiguedad_empleo`
- `numero_creditos`
- `edad`
- `gastos_mensuales`
- `relacion_ingreso_deuda`

#### Categóricas:
- `nivel_escolaridad`
- `tipo_empleo`
- `zona_geografica`

## 📦 Requisitos

Las bibliotecas utilizadas son:

```bash
pandas
numpy
scikit-learn
statsmodels
matplotlib
joblib
openpyxl
