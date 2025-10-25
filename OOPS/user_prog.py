
class User:
    def __init__(self,username,email,password):
        self.username = username
        self.email = email
        self.password = password

    def send_greet_to (self, user):
        print(f"Greeting to {user.username}. Hi {user.username} this is {self.username}. How are you?")


user1 = User("Jeff", "jeff@gmail.com", "abc123")
user2 = User("Tom", "tom@gmail.com", "123abc")

user2.send_greet_to(user1)

