import sys

from PyQt5.QtWidgets import QApplication,QLabel,QLineEdit,QPushButton,QVBoxLayout,QHBoxLayout,QWidget,QListWidget

from database import Core

class Main(QWidget):
    def __init__(self) -> None:
        super().__init__()
        
        self.setStyleSheet("background-color: #5E6561")
        self.setFixedSize(600,800)
        
        self.new_create_btn=Button("New Create User")
        self.all_users_btn=Button("All Users")
        self.update_username_user_btn=Button("Update Username")
        self.update_password_user_btn=Button("Update Password")
        self.delete_user_btn=Button("Delete User")
        self.exit_btn=Button("Exit")
        
        self.pustoy_joy=QLabel()
        self.pustoy_joy.setStyleSheet("background-color: #BF1C42;border-radius:20px;")
        
        self.h_box=QHBoxLayout()
        self.v_box=QVBoxLayout()
        self.v_box.addWidget(self.new_create_btn)
        self.v_box.addWidget(self.all_users_btn)
        self.v_box.addWidget(self.update_username_user_btn)
        self.v_box.addWidget(self.update_password_user_btn)
        self.v_box.addWidget(self.delete_user_btn)
        self.v_box.addWidget(self.exit_btn)
        
        self.h_box.addLayout(self.v_box)
        self.h_box.addWidget(self.pustoy_joy)
        
        self.setLayout(self.h_box)
        
        self.new_create_btn.clicked.connect(self.toNewCreateUser)
        self.all_users_btn.clicked.connect(self.toAllUsers)
        self.update_username_user_btn.clicked.connect(self.toUpdateUsername)
        self.update_password_user_btn.clicked.connect(self.toUpdatePassword)
        self.delete_user_btn.clicked.connect(self.toDeleteUser)
        self.exit_btn.clicked.connect(self.chiqish)
        
        self.show()
        
    def chiqish(self):
        self.close()
    
    def toNewCreateUser(self):
        self.close()
        self.new=NewCreateUser()
    
    def toAllUsers(self):
        self.close()
        self.new=AllUsers()
    
    def toUpdateUsername(self):
        self.close()
        self.win=UpdateUsername()
    
    def toUpdatePassword(self):
        self.close()
        self.new=UpdatePassword()
    
    def toDeleteUser(self):
        self.close()
        self.new=DeleteUser()
        
class NewCreateUser(QWidget):
    def __init__(self) -> None:
        super().__init__()
        
        self.setStyleSheet("background-color: #5E6561")
        self.setFixedSize(600,800)
        self.User=Core()
        
        self.all_users_btn=Button("All Users")
        self.update_username_user_btn=Button("Update Username")
        self.update_password_user_btn=Button("Update Password")
        self.delete_user_btn=Button("Delete User")
        self.exit_btn=Button("Exit")
        
        self.username_edit=QLineEdit()
        self.password_edit=QLineEdit()
        self.username_edit.setPlaceholderText("Enter Username....")
        self.password_edit.setPlaceholderText("Enter Password....")
        self.username_edit.setStyleSheet("""background-color: #181818; 
            border: 1px solid black;
            color: pink;
            font-size:15px;
            font-weight:bold;
            border-radius:20px;""")
        self.password_edit.setStyleSheet("""background-color: #181818; 
            border: 1px solid black;
            color: pink;
            font-size:15px;
            font-weight:bold;
            border-radius:20px;""")
        self.username_edit.setFixedSize(250,100)
        self.password_edit.setFixedSize(250,100)
        
        self.save_btn=Button("Save")
        self.line=QLineEdit()
        self.line.setStyleSheet("""background-color: #181818; 
            border: 1px solid black;
            color: pink;
            font-size:15px;
            font-weight:bold;
            border-radius:20px;""")
        self.line.setFixedSize(250,40)
        
        self.h_box=QHBoxLayout()
        self.v_box=QVBoxLayout()
        self.v_box.addWidget(self.all_users_btn)
        self.v_box.addWidget(self.update_username_user_btn)
        self.v_box.addWidget(self.update_password_user_btn)
        self.v_box.addWidget(self.delete_user_btn)
        self.v_box.addWidget(self.exit_btn)
        
        self.v_box1=QVBoxLayout()
        self.v_box1.addWidget(self.username_edit)
        self.v_box1.addWidget(self.password_edit)
        self.v_box1.addWidget(self.save_btn)
        self.v_box1.addWidget(self.line)
        self.h_box.addLayout(self.v_box)
        self.h_box.addLayout(self.v_box1)
        
        self.setLayout(self.h_box)
        
        self.update_username_user_btn.clicked.connect(self.toUpdateUsername)    
        self.update_password_user_btn.clicked.connect(self.toUpdatePassword)    
        self.all_users_btn.clicked.connect(self.toAllUsers)
        self.delete_user_btn.clicked.connect(self.toDeleteUser)
        self.save_btn.clicked.connect(self.save)
        self.exit_btn.clicked.connect(self.chiqish)
        
        self.show()
        
    def save(self):
        username=self.username_edit.text()
        password=self.password_edit.text()
        
        if username =="":
            self.username_edit.setPlaceholderText("Invalid Username !!!")
            self.line.setText("Invalid")
        elif password=="":
            self.password_edit.setPlaceholderText("Invalid Password !!!")
            self.line.setText("Invalid")

        else:
            self.User.createUser(username,password)
            self.username_edit.clear()
            self.password_edit.clear()
            self.username_edit.setPlaceholderText("Enter username....")
            self.password_edit.setPlaceholderText("Enter password....")
            self.line.setText("User Accepted")
        
    def chiqish(self):
        self.close()
    
    def toAllUsers(self):
        self.close()
        self.new=AllUsers()
    
    def toUpdateUsername(self):
        self.close()
        self.new=UpdateUsername()
    
    def toUpdatePassword(self):
        self.close()
        self.new=UpdatePassword()
    
    def toDeleteUser(self):
        self.close()
        self.new=DeleteUser()
        


class AllUsers(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.User=Core()
        
        self.setStyleSheet("background-color: #5E6561")
        self.setFixedSize(600,800)
        
        self.new_create_btn=Button("New Create User")    
        self.update_username_user_btn=Button("Update Username")
        self.update_password_user_btn=Button("Update Password")
        self.delete_user_btn=Button("Delete User")
        self.exit_btn=Button("Exit")
        
        self.user_name_list=QListWidget()
        self.user_password_list=QListWidget()
        self.user_name_list.setStyleSheet("""background-color: #181818; 
            border: 1px solid black;
            color: pink;
            font-size:15px;
            font-weight:bold;
            border-radius:20px;""")
        
        self.user_password_list.setStyleSheet("""background-color: #181818; 
            border: 1px solid black;
            color: pink;
            font-size:15px;
            font-weight:bold;
            border-radius:20px;""")
        
        data=self.User.getAllUsers()
        
        for username,password in data:
            self.user_name_list.addItem(username)
            self.user_password_list.addItem(password)
        
        self.v_box1=QVBoxLayout()
        self.v_box1.addWidget(self.new_create_btn)
        self.v_box1.addWidget(self.update_username_user_btn)
        self.v_box1.addWidget(self.update_password_user_btn)
        self.v_box1.addWidget(self.delete_user_btn)
        self.v_box1.addWidget(self.exit_btn)
        
        self.h_box2=QHBoxLayout()
        self.h_box2.addWidget(self.user_name_list)
        self.h_box2.addWidget(self.user_password_list)
        
        self.h_box=QHBoxLayout()
        self.h_box.addLayout(self.v_box1)
        self.h_box.addLayout(self.h_box2)
        self.setLayout(self.h_box)

        self.show()
        self.new_create_btn.clicked.connect(self.toNewCreateUser)
        self.update_username_user_btn.clicked.connect(self.toUpdateUsername)    
        self.update_password_user_btn.clicked.connect(self.toUpdatePassword)    
        self.delete_user_btn.clicked.connect(self.toDeleteUser)
        self.exit_btn.clicked.connect(self.chiqish)
    
        self.show()
    
    def toNewCreateUser(self):
        self.close()
        self.new=NewCreateUser()
        
    def chiqish(self):
        self.close()
    
    def toAllUsers(self):
        self.close()
        self.new=AllUsers()
    
    def toUpdateUsername(self):
        self.close()
        self.new=UpdateUsername()
    
    def toUpdatePassword(self):
        self.close()
        self.new=UpdatePassword()
    
    def toDeleteUser(self):
        self.close()
        self.new=DeleteUser()

class UpdateUsername(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.User=Core()
        
        self.setStyleSheet("background-color: #5E6561")
        self.setFixedSize(600,800)
        self.new_create_btn=Button("New Create User")
        self.all_users_btn=Button("All Users")
        self.update_password_btn=Button("Update Password")
        self.delete_user_btn=Button("Delete User")
        self.exit_btn=Button("Exit")
        
        self.username_edit=QLineEdit()
        self.password_edit=QLineEdit()
        self.new_username_edit=QLineEdit()
        self.new_username_edit.setPlaceholderText("Enter New Username")
        self.username_edit.setPlaceholderText("Enter Username....")
        self.password_edit.setPlaceholderText("Enter Password....")
        self.username_edit.setStyleSheet("""background-color: #181818; 
            border: 1px solid black;
            color: pink;
            font-size:15px;
            font-weight:bold;
            border-radius:20px;""")
        self.password_edit.setStyleSheet("""background-color: #181818; 
            border: 1px solid black;
            color: pink;
            font-size:15px;
            font-weight:bold;
            border-radius:20px;""")
        self.new_username_edit.setStyleSheet("""background-color: #181818; 
            border: 1px solid black;
            color: pink;
            font-size:15px;
            font-weight:bold;
            border-radius:20px;""")
        self.username_edit.setFixedSize(250,100)
        self.new_username_edit.setFixedSize(250,100)
        self.password_edit.setFixedSize(250,100)
        
        self.save_btn=Button("Save")
        self.line=QLineEdit()
        self.line.setStyleSheet("""background-color: #181818; 
            border: 1px solid black;
            color: pink;
            font-size:15px;
            font-weight:bold;
            border-radius:20px;""")
        self.line.setFixedSize(250,40)
        
        self.h_box=QHBoxLayout()
        self.v_box=QVBoxLayout()
        self.v_box.addWidget(self.new_create_btn)
        self.v_box.addWidget(self.all_users_btn)
        self.v_box.addWidget(self.update_password_btn)
        self.v_box.addWidget(self.delete_user_btn)
        self.v_box.addWidget(self.exit_btn)
        
        self.v_box1=QVBoxLayout()
        self.v_box1.addWidget(self.username_edit)
        self.v_box1.addWidget(self.password_edit)
        self.v_box1.addWidget(self.new_username_edit)
        
        self.v_box1.addWidget(self.save_btn)
        self.v_box1.addWidget(self.line)
        
        self.h_box.addLayout(self.v_box)
        self.h_box.addLayout(self.v_box1)
        
        self.setLayout(self.h_box)
    
        self.exit_btn.clicked.connect(self.chiqish)
        
        self.new_create_btn.clicked.connect(self.toNewCreateUser)
        self.all_users_btn.clicked.connect(self.toAllUsers)
        self.update_password_btn.clicked.connect(self.toUpdatePassword)
        self.delete_user_btn.clicked.connect(self.toDeleteUser)
        self.save_btn.clicked.connect(self.save)
        self.exit_btn.clicked.connect(self.chiqish)
    
        self.show()
    
    def save(self):
        username=self.username_edit.text()
        password=self.password_edit.text()
        newusername=self.new_username_edit.text()
        
        if username =="":
            self.username_edit.setPlaceholderText("Invalid Username !!!")
            self.line.setText("Invalid")

        elif password=="":
            self.password_edit.setPlaceholderText("Invalid Password !!!")
        elif newusername=="":
            self.new_username_edit.setPlaceholderText("Invalid New Username !!!")
            self.line.setText("Invalid")
        else:
            self.User.updateUser(username,password,newusername)
            self.username_edit.clear()
            self.password_edit.clear()    
            self.new_username_edit.clear()
            self.username_edit.setPlaceholderText("Enter username....")
            self.password_edit.setPlaceholderText("Enter password....")   
            self.line.setText("Update Username") 
    
    def toNewCreateUser(self):
        self.close()
        self.new=NewCreateUser()
        
    def chiqish(self):
        self.close()
    
    def toAllUsers(self):
        self.close()
        self.new=AllUsers()
    
    def toUpdatePassword(self):
        self.close()
        self.new=UpdatePassword()
    
    def toDeleteUser(self):
        self.close()
        self.new=DeleteUser()
        
    def chiqish(self):
        self.close()
    
 
 
class UpdatePassword(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.User=Core()
        
        self.setStyleSheet("background-color: #5E6561")
        self.setFixedSize(600,800)
        
        self.all_users_btn=Button("All Users")
        self.update_username_user_btn=Button("Update Username")
        self.delete_user_btn=Button("Delete User")
        self.exit_btn=Button("Exit")
        
        self.username_edit=QLineEdit()
        self.password_edit=QLineEdit()
        self.new_username_edit=QLineEdit()
        self.new_username_edit.setPlaceholderText("Enter New Password")
        self.username_edit.setPlaceholderText("Enter Username....")
        self.password_edit.setPlaceholderText("Enter Password....")
        self.username_edit.setStyleSheet("""background-color: #181818; 
            border: 1px solid black;
            color: pink;
            font-size:15px;
            font-weight:bold;
            border-radius:20px;""")
        self.password_edit.setStyleSheet("""background-color: #181818; 
            border: 1px solid black;
            color: pink;
            font-size:15px;
            font-weight:bold;
            border-radius:20px;""")
        self.new_username_edit.setStyleSheet("""background-color: #181818; 
            border: 1px solid black;
            color: pink;
            font-size:15px;
            font-weight:bold;
            border-radius:20px;""")
        self.username_edit.setFixedSize(250,100)
        self.new_username_edit.setFixedSize(250,100)
        self.password_edit.setFixedSize(250,100)
        
        self.save_btn=Button("Save")
        self.line=QLineEdit()
        self.line.setStyleSheet("""background-color: #181818; 
            border: 1px solid black;
            color: pink;
            font-size:15px;
            font-weight:bold;
            border-radius:20px;""")
        self.line.setFixedSize(250,40)
        
        self.h_box=QHBoxLayout()
        self.v_box=QVBoxLayout()
        self.new_create_btn=Button("New Create User")
        self.v_box.addWidget(self.new_create_btn)
        self.v_box.addWidget(self.all_users_btn)
        self.v_box.addWidget(self.update_username_user_btn)
        self.v_box.addWidget(self.delete_user_btn)
        self.v_box.addWidget(self.exit_btn)
        
        self.v_box1=QVBoxLayout()
        self.v_box1.addWidget(self.username_edit)
        self.v_box1.addWidget(self.password_edit)
        self.v_box1.addWidget(self.new_username_edit)
        
        self.v_box1.addWidget(self.save_btn)
        self.v_box1.addWidget(self.line)
        self.h_box.addLayout(self.v_box)
        self.h_box.addLayout(self.v_box1)
        
        self.setLayout(self.h_box)
        
        self.exit_btn.clicked.connect(self.chiqish)
    
        self.show()
    
        self.new_create_btn.clicked.connect(self.toNewCreateUser)
        self.update_username_user_btn.clicked.connect(self.toUpdateUsername)    
        self.all_users_btn.clicked.connect(self.toAllUsers)
        self.delete_user_btn.clicked.connect(self.toDeleteUser)
        self.save_btn.clicked.connect(self.save)
        self.exit_btn.clicked.connect(self.chiqish)
    
    def save(self):
        username=self.username_edit.text()
        password=self.password_edit.text()
        newpassword=self.new_username_edit.text()
        
        if username =="":
            self.username_edit.setPlaceholderText("Invalid Username !!!")
            self.line.setText("Invalid")

        elif password=="":
            self.password_edit.setPlaceholderText("Invalid Password !!!")
            self.line.setText("Invalid")
        elif newpassword=="":
            self.new_username_edit.setPlaceholderText("Invalid New Password !!!")
            self.line.setText("Invalid")
        else:
            self.User.updatePassword(username,password,newpassword)
            self.username_edit.clear()
            self.password_edit.clear()    
            self.new_username_edit.clear() 
            self.username_edit.setPlaceholderText("Enter username....")
            self.password_edit.setPlaceholderText("Enter password....")  
            self.new_username_edit.setPlaceholderText("Enter new password....")  
            self.line.setText("Update Password")
    
    def toNewCreateUser(self):
        self.close()
        self.new=NewCreateUser()
        
    def chiqish(self):
        self.close()
    
    def toAllUsers(self):
        self.close()
        self.new=AllUsers()
    
    def toUpdateUsername(self):
        self.close()
        self.new=UpdateUsername()
    
    def toDeleteUser(self):
        self.close()
        self.new=DeleteUser()
        
    def chiqish(self):
        self.close()
    
    
class DeleteUser(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.User=Core()
        
        self.setStyleSheet("background-color: #5E6561")
        self.setFixedSize(600,800)
        
        self.new_create_btn=Button("New Create User")
        self.all_users_btn=Button("All Users")
        self.update_username_user_btn=Button("Update Username")
        self.update_password_user_btn=Button("Update Password")
        self.exit_btn=Button("Exit")
        
        self.username_edit=QLineEdit()
        self.password_edit=QLineEdit()
        self.username_edit.setPlaceholderText("Enter Username....")
        self.password_edit.setPlaceholderText("Enter Password....")
        self.username_edit.setStyleSheet("""background-color: #181818; 
            border: 1px solid black;
            color: pink;
            font-size:15px;
            font-weight:bold;
            border-radius:20px;""")
        self.password_edit.setStyleSheet("""background-color: #181818; 
            border: 1px solid black;
            color: pink;
            font-size:15px;
            font-weight:bold;
            border-radius:20px;""")
        self.username_edit.setFixedSize(250,100)
        self.password_edit.setFixedSize(250,100)
        
        self.save_btn=Button("Delete User")
        self.line=QLineEdit()
        self.line.setStyleSheet("""background-color: #181818; 
            border: 1px solid black;
            color: pink;
            font-size:15px;
            font-weight:bold;
            border-radius:20px;""")
        self.line.setFixedSize(250,40)
        
        self.h_box=QHBoxLayout()
        self.v_box=QVBoxLayout()
        self.v_box.addWidget(self.new_create_btn)
        self.v_box.addWidget(self.all_users_btn)
        self.v_box.addWidget(self.update_username_user_btn)
        self.v_box.addWidget(self.update_password_user_btn)
        self.v_box.addWidget(self.exit_btn)
        
        self.v_box1=QVBoxLayout()
        self.v_box1.addWidget(self.username_edit)
        self.v_box1.addWidget(self.password_edit)
        self.v_box1.addWidget(self.save_btn)
        self.v_box1.addWidget(self.line)
        self.h_box.addLayout(self.v_box)
        self.h_box.addLayout(self.v_box1)
        
        self.setLayout(self.h_box)
        
        self.exit_btn.clicked.connect(self.chiqish)
        
        self.new_create_btn.clicked.connect(self.toNewCreateUser)
        self.update_username_user_btn.clicked.connect(self.toUpdateUsername)    
        self.update_password_user_btn.clicked.connect(self.toUpdatePassword)    
        self.all_users_btn.clicked.connect(self.toAllUsers)
        self.save_btn.clicked.connect(self.save)
        self.exit_btn.clicked.connect(self.chiqish)
    
        self.show()
    
    def save(self):
        username=self.username_edit.text()
        password=self.password_edit.text()
        
        if username =="":
            self.username_edit.setPlaceholderText("Invalid Username !!!")
            self.line.setText("Invalid")

        elif password=="":
            self.password_edit.setPlaceholderText("Invalid Password !!!")
            self.line.setText("Invalid")
        else:
            self.User.deleteUser(username,password)
            self.username_edit.clear()
            self.password_edit.clear()
            self.username_edit.setPlaceholderText("Enter username....")
            self.password_edit.setPlaceholderText("Enter password....")
            self.line.setText("Delete User")
    
    def toNewCreateUser(self):
        self.close()
        self.new=NewCreateUser()
        
    def chiqish(self):
        self.close()
    
    def toAllUsers(self):
        self.close()
        self.new=AllUsers()
    
    def toUpdateUsername(self):
        self.close()
        self.new=UpdateUsername()
    
    def toUpdatePassword(self):
        self.close()
        self.new=UpdatePassword()
    
    def toDeleteUser(self):
        self.close()
        self.new=DeleteUser()
        
    def chiqish(self):
        self.close()
    
        
class Button(QPushButton):
    def __init__(self,text):
        super().__init__(text)
        self.setFixedSize(200,100)
        self.setStyleSheet("""
        QPushButton {
            background-color: #181818; 
            border: 1px solid black;
            color: pink;
            font-size:15px;
            font-weight:bold;
            border-radius:20px;
        }
        QPushButton:hover {
            color: yellow;
        }
    """)   

app=QApplication([])
win=Main()
sys.exit(app.exec_())
