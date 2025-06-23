# =============================================================================
# REGRESIÓN LOGÍSTICA PARA PREDICCIÓN DE RIESGO DE CRÉDITO
# =============================================================================

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report,
    roc_auc_score,
    roc_curve
)
from sklearn.preprocessing import StandardScaler
import statsmodels.api as sm
import joblib
import matplotlib.pyplot as plt

# Cargar datos
df = pd.read_excel("datos_clientes.xlsx", sheet_name="Hoja1")

# Variables
variable_objetivo = 'riesgo_credito'

variables_predictoras = [
    'ingreso_mensual',
    'antiguedad_empleo',
    'numero_creditos',
    'edad',
    'gastos_mensuales',
    'relacion_ingreso_deuda',
    'nivel_escolaridad',
    'tipo_empleo',
    'zona_geografica'
]

# Validar columnas
def validar_columnas(datos, columnas_requeridas):
    faltantes = [col for col in columnas_requeridas if col not in datos.columns]
    if faltantes:
        raise ValueError(f"Columnas faltantes: {faltantes}")
validar_columnas(df, variables_predictoras + [variable_objetivo])

# Codificación de variables categóricas
variables_categoricas = ['nivel_escolaridad', 'tipo_empleo', 'zona_geografica']
df = pd.get_dummies(df, columns=variables_categoricas, drop_first=True)

# Separar X e y
X = df.drop(columns=[variable_objetivo])
y = df[variable_objetivo]

# Escalado de variables numéricas
variables_numericas = [
    'ingreso_mensual',
    'antiguedad_empleo',
    'numero_creditos',
    'edad',
    'gastos_mensuales',
    'relacion_ingreso_deuda'
]
scaler = StandardScaler()
X[variables_numericas] = scaler.fit_transform(X[variables_numericas])

# Separación en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Modelo
modelo = LogisticRegression(max_iter=1000)
modelo.fit(X_train, y_train)

# Predicciones
y_pred = modelo.predict(X_test)
y_proba = modelo.predict_proba(X_test)[:, 1]

# Evaluación
print("\nEvaluación del modelo de regresión logística:")
print(f"Accuracy: {accuracy_score(y_test, y_pred):.4f}")
print("Matriz de Confusión:")
print(confusion_matrix(y_test, y_pred))
print("\nReporte de Clasificación:")
print(classification_report(y_test, y_pred))
print(f"AUC-ROC: {roc_auc_score(y_test, y_proba):.4f}")

# Curva ROC
fpr, tpr, _ = roc_curve(y_test, y_proba)
plt.plot(fpr, tpr, label='ROC Curve (AUC = {:.2f})'.format(roc_auc_score(y_test, y_proba)))
plt.plot([0, 1], [0, 1], 'k--')
plt.xlabel('Tasa de Falsos Positivos')
plt.ylabel('Tasa de Verdaderos Positivos')
plt.title('Curva ROC')
plt.legend()
plt.show()

# Análisis estadístico con statsmodels (opcional, para interpretación de coeficientes)
X_train_sm = sm.add_constant(X_train)
modelo_sm = sm.Logit(y_train, X_train_sm).fit()
print("\nResumen estadístico (statsmodels):")
print(modelo_sm.summary())

# Guardar modelo y escalador
joblib.dump(modelo, 'modelo_logistico_credito.pkl')
joblib.dump(scaler, 'escalador_credito.pkl')