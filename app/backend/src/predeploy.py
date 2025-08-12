# app/backend/src/predeploy.py
import subprocess, sys

def run(cmd):
    print(">>", " ".join(cmd), flush=True)
    subprocess.check_call(cmd)

if __name__ == "__main__":
    try:
        # Пытаемся применить миграции нормально
        run(["alembic", "-c", "alembic.ini", "upgrade", "head"])
    except subprocess.CalledProcessError:
        # Если уже создано руками/частично — помечаем текущую схему как актуальную
        print("!! upgrade failed — stamping to head and continuing", flush=True)
        run(["alembic", "-c", "alembic.ini", "stamp", "head"])
    # После этого сид-данные
    run([sys.executable, "src/seed.py"])
