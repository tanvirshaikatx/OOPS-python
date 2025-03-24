class chatbook:


    def __init__(self):
        
        self.username=""
        self.password=""
        self.login=False
        self.menu()

    def menu(self):
        print("1. Signup")
        print("2. Login")
        print("3. write a post")
        print("4. to meessg e friend")
        print("5. press any things else for exit")
        user_input=input("Enter your choice: ")
        if user_input=="1":
            self.signup()
        elif user_input=="2":
            self.signin()
        elif user_input=="3":
            self.write_post()
        elif user_input=="4":
            self.message_friend()
        else:
            exit()

    def signup(self):
        self.username=input("Enter your username: ")
        self.password=input("Enter your password: ")
        print("Signup successful")
        self.menu()

    def signin(self):
        if self.username=='' and self.password=='':
            print("Please signup first by pressing 1 in the main menu")
        else:
            username=input("Enter your username: ")
            password=input("Enter your password: ")
            if self.username==username and self.password==password:
             self.login=True
             print("Login successful")
            else:
             print("Login failed")
        self.menu()

    def write_post(self):
        if self.login:
            post=input("Enter your post: ")
            print("Post successful")
        else:
            print("Login first")
        self.menu()

    def message_friend(self):
        if self.login==True:
            friend=input("Enter your friend: ")
            message=input("Enter your message: ")
            print("Message sent")
        else:
            print("Login first")
        self.menu()

chat=chatbook()
        
    