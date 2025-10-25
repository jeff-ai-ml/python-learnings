
class User:
    def __init__(self,username,email,password):
        self.username = username
        self._email = email
        self.password = password

    def send_greet_to (self, user):
        print(f"Greeting to {user.username}. Hi {user.username} this is {self.username}. How are you?")
    
    @property
    def email(self):
        print(f"This is the email of {self.username}")
        return self._email
    
    @email.setter
    def email(self, new_email):
        self._email = new_email


user1 = User("Jeff", "jeff@gmail.com", "abc123")
user2 = User("Tom", "tom@gmail.com", "123abc")

user2.send_greet_to(user1)

print(f"Email of {user1.username} : {user1.email}")

print(f"Email of {user2.username} : {user2.email}")

user1.email = "hello@234.com"

print(f"Email of {user1.username} : {user1.email}")





