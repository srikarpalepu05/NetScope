from db.schema import create_tables
from ingest.auth_ingest import ingest_auth_logs
from audit.failed_logins import find_failed_logins

def main():
    create_tables()
    ingest_auth_logs("data/raw/auth_logs.csv")

    flagged = find_failed_logins()
    for user, count in flagged:
        print(f"User {user} has {count} failed login attempts")

if __name__ == "__main__":
    main()
