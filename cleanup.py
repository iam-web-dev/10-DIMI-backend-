import os
import shutil

files_to_delete = [
    'db.sqlite3',
    'api/migrations/0001_initial.py',
]
dirs_to_delete = [
    'api/migrations/__pycache__',
]

for f in files_to_delete:
    if os.path.exists(f):
        try:
            os.remove(f)
            print(f"Deleted {f}")
        except Exception as e:
            print(f"Error deleting {f}: {e}")

for d in dirs_to_delete:
    if os.path.exists(d):
        try:
            shutil.rmtree(d)
            print(f"Deleted {d}")
        except Exception as e:
            print(f"Error deleting {d}: {e}")
