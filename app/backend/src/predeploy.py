# app/backend/src/predeploy.py
import subprocess, sys

def run(cmd: list[str]):
    print(">>", " ".join(cmd), flush=True)
    subprocess.check_call(cmd)

if __name__ == "__main__":
    # 1) Миграции Alembic
    run(["alembic", "-c", "alembic.ini", "upgrade", "head"])
    # 2) Seed-данные (создание админа и компании)
    run([sys.executable, "src/seed.py"])
