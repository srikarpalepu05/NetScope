from db.connection import get_connection

def find_failed_logins(threshold=5):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT user, COUNT(*) as failures
        FROM auth_logs
        WHERE status = 'FAIL'
        GROUP BY user
        HAVING failures >= ?
    """, (threshold,))

    results = cursor.fetchall()
    conn.close()
    return results
