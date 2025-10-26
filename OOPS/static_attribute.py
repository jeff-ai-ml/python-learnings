
class User:

    user_count = 0

    def __init__(self, username, email):
        self.username = username
        self.email = email

        User.user_count += 1

    def display_user(self):
        print(f"The user {self.username} email is {self.email}")
    

user1 = User("Dan", "dan1@gmail.com")
user2 = User("Clark", "clark1@gmail.com")

user1.display_user()
user2.display_user()

print(f"The object or user count is {User.user_count}")
