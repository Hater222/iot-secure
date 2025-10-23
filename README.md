

---

```markdown
# 🔐 IoT Secure App

Aplicación educativa desarrollada con **Streamlit** para simular **seguridad en sistemas IoT**, incluyendo comunicación UART, MQTT, firmware seguro y blockchain simulada para trazabilidad.

Este laboratorio es **local-only** (sin conexión a red) y sirve para prácticas de **Ciberseguridad IoT** o asignaturas de **Seguridad en Sistemas Embebidos**.

---

## 🚀 Estructura del Proyecto

```

iot-secure-app/
├── app.py                         # Página principal Streamlit
├── core/
│   ├── uart_sim.py                # Simulación UART (modo seguro/inseguro)
│   ├── mqtt_sim.py                # Simulación de broker MQTT local
│   ├── fw_sim.py                  # Gestión de firmware y contraseñas
│   ├── chain_sim_py.py            # Ledger simulado en Python (Blockchain)
├── pages/
│   ├── 1_Amenazas_IoT.py          # Interfaz UART y MQTT
│   ├── 2_Firmware_y_Contraseñas.py# Gestión de firmware seguro
│   ├── 3_Blockchain_Seguridad.py  # Registro en cadena simulada
│   ├── 4_Auditoria_Entrega.py     # Exportación y auditoría
├── tests/
│   ├── test_uart.py
│   ├── test_mqtt.py
│   ├── test_fw.py
│   ├── test_chain_py.py
├── self_check.py                  # Script de autoevaluación
├── pack_for_students.py           # Empaquetado del proyecto
├── make_zip.sh                    # Script shell para crear el ZIP
├── setup_local_lab.sh             # Instalación local del entorno
├── requirements.txt               # Dependencias mínimas
├── ENTREGA.md                     # Guía de entrega del laboratorio
└── teacher_notes.md               # Notas y guía para el profesor

````

---

## ⚙️ Instalación local

### 1. Crear entorno virtual y activar
```bash
bash setup_local_lab.sh
````

### 2. Ejecutar la aplicación Streamlit

```bash
streamlit run app.py
```

> 💡 Si usas Windows, activa el entorno con:
>
> ```
> .venv\Scripts\activate
> ```

---

## 🧩 Componentes Principales

### 🔌 UART Simulation

* Simula comandos de consola (`HELP`, `STATUS`, `DUMP SECRETS`, etc.).
* Soporta modo seguro/inseguro y bloqueo tras intentos fallidos.

### 📡 MQTT Simulation

* Broker en memoria (sin sockets).
* Funciones `publish`, `sniff`, `spoof` y `mitm_publish`.

### 🧰 Firmware Simulation

* Simula credenciales por defecto, primer arranque, y actualizaciones OTA.
* Firma y verificación RSA con `cryptography`.

### 🔗 Blockchain Simulation

* Ledger en memoria (hash + JSON).
* Control de acceso y actuadores simulados.

---

## 🧪 Ejecución de Tests

```bash
pytest -v
```

Verifica que todos los módulos (`core/`) funcionan correctamente sin acceso a red.

---

## 🔍 Autoevaluación Rápida

Puedes usar el script `self_check.py` para verificar tu instalación y módulos:

```bash
python self_check.py
```

Muestra ✔ o ✖ en cada test básico del sistema.

---

## 📤 Entrega de Práctica

Consulta el archivo `ENTREGA.md` para conocer:

* Qué capturas realizar.
* Qué ficheros subir.
* Rúbrica de evaluación (10 puntos).

---

## 🧑‍🏫 Créditos

**Autor base:** Laboratorio educativo para simulación de ciberseguridad IoT
**Framework:** Streamlit + Python 3.11 + Cryptography
**Licencia:** Uso académico (no comercial)

```

---


```
