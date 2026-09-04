import os
from datetime import datetime

import mlflow
import pandas as pd


# Каждый запуск получит новое имя эксперимента
EXPERIMENT_NAME = f"churn_uliana_v13"
RUN_NAME = "data_check"


# 1. Загружаем данные
df = pd.read_csv("users_churn.csv")


# 2. Создаём файл со списком столбцов
with open("columns.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(df.columns.tolist()))


# 3. Создаём новый эксперимент
experiment_id = mlflow.create_experiment(EXPERIMENT_NAME)


# 4. Логируем артефакты и метрики
with mlflow.start_run(run_name=RUN_NAME, experiment_id=experiment_id) as run:
    run_id = run.info.run_id
    
    # логируем метрики эксперимента
    # предполагается, что переменная stats содержит словарь с метриками,
    # объявлять переменную stats не надо,
    # где ключи — это названия метрик, а значения — числовые значения метрик
    # mlflow.log_metrics(stats)

    mlflow.log_artifact("users_churn.csv", artifact_path="dataframe")
    mlflow.log_artifact("columns.txt", artifact_path="dataframe")
    
experiment = mlflow.get_experiment_by_name(EXPERIMENT_NAME)
# получаем данные о запуске эксперимента по его уникальному идентификатору
run = mlflow.get_run(run_id)

# проверяем, что статус запуска эксперимента изменён на 'FINISHED'
# это утверждение (assert) можно использовать для автоматической проверки того, 
# что эксперимент был завершён успешно
assert run.info.status == "FINISHED"

# удаляем файлы 'columns.txt' и 'users_churn.csv' из файловой системы,
# чтобы очистить рабочую среду после логирования артефактов
os.remove("columns.txt")
os.remove("users_churn.csv")

