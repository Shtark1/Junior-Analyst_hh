from functional.requests_db import Database
from functional.computing import average_time

db = Database('test.db')


def main():
    all_info = db.get()
    answer = average_time(all_info)

    for key, value in answer.items():
        print(f'В группе {key}, задачи находятся в статусе "Open": {value}')


if __name__ == '__main__':
    main()
