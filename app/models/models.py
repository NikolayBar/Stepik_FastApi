from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str


if __name__ == "__main__":
    users = [User(id=1, name="John Doe"), User(id=2, name="Tom Bad")]

    for us in users:
        print(us)
