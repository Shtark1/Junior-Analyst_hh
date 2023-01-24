import datetime
from functional.requests_db import Database


db = Database("test.db")

def main():
    all_info = db.get()

    for info in all_info:
        time = datetime.datetime.fromtimestamp(info[2] / 1000)
        print(f"\nКлюч: {info[0]} \nСтатус: {info[1]} \nВремя: {time}\n ")


if __name__ == '__main__':
    main()