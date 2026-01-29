import csv
from db.connection import get_connection

def ingest_auth_logs(file_path):
    conn = get_connection()
    cursor = conn.cursor()

    with open(file_path, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            cursor.execute(
                "INSERT INTO auth_logs (timestamp, user, ip_address, status) VALUES (?, ?, ?, ?)",
                (row["timestamp"], row["user"], row["ip"], row["status"])
            )

    conn.commit()
    conn.close()
