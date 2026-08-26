MLE Project Sprint 2 — MLflow Tracking
📌 О проекте
Этот проект демонстрирует настройку и использование MLflow Tracking для управления экспериментами машинного обучения. В рамках работы реализовано локальное и удалённое логирование экспериментов с использованием различных бэкендов для хранения артефактов и метаданных.

🛠️ Используемые технологии
Python 3.10

MLflow 2.7.1

Git + GitHub

SQLite (локальное хранение метаданных)

PostgreSQL (опционально, для удалённого хранения)

Yandex Cloud S3 (хранение артефактов)

📂 Структура проекта
text
mle-project-sprint-2-v001/
├── mle-mlflow/
│   ├── mlflow_experiments_store/        # артефакты локальных экспериментов
│   ├── mlflow_experiments_store_sqlite/ # артефакты с SQLite
│   ├── venv_mle_mlflow/                 # виртуальное окружение
│   ├── .env                             # переменные окружения (не в Git!)
│   ├── .env_template                    # шаблон .env
│   ├── .gitignore                       # игнорируемые файлы и папки
│   ├── README.md                        
│   ├── requirements.txt                 # зависимости проекта
│   ├── run_mlflow_server_locally.sh     # запуск MLflow с локальным хранилищем
│   ├── run_mlflow_server_sqlite.sh      # запуск MLflow с SQLite
│   ├── test_locally.py                  # тестовый скрипт с локальным хранилищем
│   ├── test_sqlite.py                   # тестовый скрипт с SQLite
│   ├── test_localTreckingServer.py      # тестовый скрипт с S3
│   ├── test_artifact.txt                # тестовый артефакт
│   └── test.ipynb                       # Jupyter Notebook с экспериментами
├── mydb.sqlite                          # база данных SQLite (не в Git)
└── requirements.txt                     # глобальный список зависимостей