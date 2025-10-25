
class User:
    def __init__(self,username,email,password):
        self.username = username
        self._email = email
        self.password = password

    def send_greet_to (self, user):
        print(f"Greeting to {user.username}. Hi {user.username} this is {self.username}. How are you?")
    
    def get_email(self):
        return self._email
    
    def set_email(self, new_email):
        self._email = new_email


user1 = User("Jeff", "jeff@gmail.com", "abc123")
user2 = User("Tom", "tom@gmail.com", "123abc")

user2.send_greet_to(user1)

print(f"Email of {user1.username} : {user1.get_email()}")

print(f"Email of {user2.username} : {user2.get_email()}")

user1.set_email("hello@234.com")

print(f"Email of {user1.username} : {user1.get_email()}")





