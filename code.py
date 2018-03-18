class user():
   def __init__(self,first_name,last_name,username):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username.title()
        self.no_login = 0
   def describe_user(self):
       print("First Name: " + self.first_name)
       print("Last Name: " + self.last_name)
       print("User Name: " + self.username)
       
   def greet_user(self):
       print("Hi," + self.username)
   def set_number_login(self):
       self.no_login +=1
       print("Number of Attempts: " + str(self.no_login))
   def reset_loginattempts(self):
       self.no_login = 0
vansh = user('vansh','gupta','algo')
vansh.describe_user()
vansh.set_number_login()
vansh.set_number_login()
vansh.set_number_login()   