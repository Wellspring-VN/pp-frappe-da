import sys

sys.path.append("../../ppda")

from db_service import DBService
import config


def main():
    conn = DBService()
    conn.login("administrator", "wellspring@2024")

    print(f"Logged in host {config.BASE_URL}")


if __name__ == "__main__":
    main()
