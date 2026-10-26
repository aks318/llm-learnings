from fastapi import Depends


class Database:
    def open(self):
        return "connection open"

    def close(self):
        print("connection closed")


def get_database():
    db = Database()
    try:
        yield db
    finally:
        db.close()


def get_user(db: Database = Depends(get_database)):
    return {
        "message": "Users fetched successfully",
        "connection": db.open()
    }


# Call manually, without a decorator
db_generator = get_database()
db = next(db_generator)

try:
    result = get_user(db)
    print(result)
finally:
    db_generator.close()