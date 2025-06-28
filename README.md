ZentroAppGym - Sistema de Gestión para Gimnasios
ZentroAppGym es una aplicación integral de gestión para gimnasios, diseñada para facilitar la administración de clientes, clases, planes de pago y servicios. Cuenta con un backend robusto en FastAPI y un frontend moderno en JavaScript.
📁 Estructura del Proyecto

ZentroAppGym-main/
├── Zentro_Backend/
│   ├── Backend/
│   │   ├── app/
│   │   │   ├── api/v1/             # Rutas principales (ej. usuarios)
│   │   │   ├── core/               # Configuración y seguridad
│   │   │   ├── dao/                # Acceso a datos (DAOs)
│   │   │   ├── db/                 # Conexión y utilidades de base de datos
│   │   │   ├── models/             # Modelos SQLAlchemy
│   │   │   ├── schemas/            # Esquemas Pydantic
│   │   │   └── services/           # Lógica de negocio
│   └── requirements.txt
├── zentro_Frontend/
│   └── Frontend/                   # Interfaz de usuario (JS/React/Vue)
│       ├── Dockerfile
│       └── package.json

🚀 Tecnologías Utilizadas
Backend (Zentro_Backend):
- FastAPI – Framework rápido para APIs en Python
- SQLAlchemy – ORM para manejo de base de datos
- Pydantic – Validación de datos
- Python-dotenv – Carga de variables de entorno
- MySQL / SQLite – Motor de base de datos (configurable)
Frontend (zentro_Frontend):
- Framework JS moderno (React o Vue.js)
- Gestión de dependencias con npm
- Contenedor Docker opcional para despliegue
⚙️ Instalación
1. Clonar el repositorio:

git clone https://github.com/Reinosojp96/ZentroAppGym.git
cd ZentroAppGym/Zentro_Backend/Backend
2. Crear entorno virtual e instalar dependencias:

python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
pip install -r requirements.txt
3. Ejecutar el backend:

uvicorn app.main:app --reload

Accede a la documentación interactiva en: http://localhost:8000/docs
📦 Frontend (Opcional)
cd ../../zentro_Frontend/Frontend
npm install
npm run dev
📌 Funcionalidades Clave
- Gestión de clientes
- Gestión de planes y pagos
- Control de clases y entrenadores
- Seguridad con autenticación JWT
- Arquitectura modular y escalable
🛠 Pendientes / Roadmap
- [ ] Autenticación con OAuth o Google
- [ ] Subida de imágenes de perfil
- [ ] Soporte para múltiples gimnasios
- [ ] Panel de administración completo
- [ ] Chatbot con IA para clientes
🤝 Contribuciones
Pull requests bienvenidos. Si deseas colaborar, por favor abre una issue primero para discutir cambios importantes.
📄 Licencia
Este proyecto está licenciado bajo la MIT License.
👨‍💻 Autor
Julian Reinoso
GitHub: https://github.com/Reinosojp96
