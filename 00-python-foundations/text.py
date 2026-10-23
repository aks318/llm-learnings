from pydantic import BaseModel, ValidationError, Field
import json

class User(BaseModel):
    name: str
    age: int

class Config(BaseModel):
    users: list[User]


def main():
    try:
        with open('txt.json', 'r') as file:
            data = json.load(file)

        config = Config.model_validate(data)
        print("JSON structure is valid!")
        for user in config.users:
            print(user.name)
    except FileNotFoundError:
        print("Error: config.json not found")

    except json.JSONDecodeError as error:
        print("Invalid JSON syntax:", error)

    except ValidationError as error:
        print("JSON structure validation failed:")
        print(error)


if __name__ == "__main__":
    main()