## Import All Global Libs Here ##
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtPrintSupport import *
import sys,sqlite3,time
## Local Libs ##
from config import DB_FILE
from Helpers import randomChatId






class ManageDB(QMainWindow):
    try:
        def __init__(self, *args, **kwargs):
            super(ManageDB, self).__init__(*args, **kwargs)
            
            # Creating The Data Base
            self.conn = sqlite3.connect(DB_FILE)
            self.c = self.conn.cursor()
            self.c.execute("""
            CREATE TABLE IF NOT EXISTS userinfo (
                id INTEGER NOT NULL PRIMARY KEY,
                full_name VARCHAR(60) NOT NULL,
                age INTEGER NOT NULL,
                phone_number INTEGER NOT NULL UNIQUE, 
                chat_id VARCHAR(255) NOT NULL UNIQUE,
                identity_id INTEGER NOT NULL UNIQUE,
                username VARCHAR(255) NOT NULL UNIQUE,
                password VARCHAR(255) NOT NULL UNIQUE,
                read_user BOOLEAN DEFAULT False
            );""")
            self.c.close()
            
            
            ## main Window: The database Table That user Sees ##
            file_menu = self.menuBar().addMenu("&File")
            self.setWindowTitle("User Manager")
            self.setMinimumSize(800, 600)

            self.tableWidget = QTableWidget()
            self.setCentralWidget(self.tableWidget)
            self.tableWidget.setAlternatingRowColors(True)
            self.tableWidget.setColumnCount(8)
            self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
            self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
            self.tableWidget.horizontalHeader().setStretchLastSection(True)
            self.tableWidget.verticalHeader().setVisible(False)
            self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
            self.tableWidget.verticalHeader().setStretchLastSection(False)
            self.tableWidget.setHorizontalHeaderLabels(("Roll No.", "Full Name", "Age", "Phone Number", "Chat ID","Identity ID", "User name", "Password"))
            
            
            toolbar = QToolBar()
            toolbar.setMovable(False)
            self.addToolBar(toolbar)

            statusbar = QStatusBar()
            self.setStatusBar(statusbar)
            btn_ac_adduser = QAction(QIcon("pics/add.png"), "Add User", self)
            btn_ac_adduser.triggered.connect(self.insert)
            btn_ac_adduser.setStatusTip("Add Student")
            toolbar.addAction(btn_ac_adduser)

            btn_ac_refresh = QAction(QIcon("pics/refresh.png"),"Refresh",self)
            btn_ac_refresh.triggered.connect(self.loaddata)
            btn_ac_refresh.setStatusTip("Refresh Table")
            toolbar.addAction(btn_ac_refresh)

            btn_ac_search = QAction(QIcon("pics/search.png"), "Search", self)
            btn_ac_search.triggered.connect(self.search)
            btn_ac_search.setStatusTip("Search User")
            toolbar.addAction(btn_ac_search)

            btn_ac_delete = QAction(QIcon("pics/trash.png"), "Delete", self)
            btn_ac_delete.triggered.connect(self.delete)
            btn_ac_delete.setStatusTip("Delete User")
            toolbar.addAction(btn_ac_delete)

            adduser_action = QAction(QIcon("pics/add.png"),"Insert User", self)
            adduser_action.triggered.connect(self.insert)
            file_menu.addAction(adduser_action)

            searchuser_action = QAction(QIcon("pics/search.png"), "Search User", self)
            searchuser_action.triggered.connect(self.search)
            file_menu.addAction(searchuser_action)

            deluser_action = QAction(QIcon("pics/trash.png"), "Delete", self)
            deluser_action.triggered.connect(self.delete)
            file_menu.addAction(deluser_action)

        def loaddata(self):
            self.connection = sqlite3.connect(DB_FILE)
            query = "SELECT * FROM userinfo;"
            result = self.connection.execute(query)
            self.tableWidget.setRowCount(0)
            for row_number, row_data in enumerate(result):
                self.tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, column_number,QTableWidgetItem(str(data)))
            self.connection.close()

        def handlePaintRequest(self, printer):
            document = QTextDocument()
            cursor = QTextCursor(document)
            model = self.table.model()
            table = cursor.insertTable(model.rowCount(), model.columnCount())
            for row in range(table.rows()):
                for column in range(table.columns()):
                    cursor.insertText(model.item(row, column).text())
                    cursor.movePosition(QTextCursor.NextCell)
            document.print_(printer)

        def insert(self):
            dlg = InsertDialog()
            dlg.exec_()

        def delete(self):
            dlg = DeleteDialog()
            dlg.exec_()

        def search(self):
            dlg = SearchDialog()
            dlg.exec_()
                   
    except ValueError:
        QMessageBox.warning(QMessageBox(), "Error!", "There Is A Value Error Solve It")      
    

class InsertDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super(InsertDialog, self).__init__(*args, **kwargs)

        self.QBtn = QPushButton()
        self.QBtn.setText("Register")

        self.setWindowTitle("Add User")
        self.setFixedWidth(500)
        self.setFixedHeight(400)

        self.QBtn.clicked.connect(self.adduser)

        layout = QVBoxLayout()

        self.nameinput = QLineEdit()
        self.nameinput.setPlaceholderText("Full Name")
        layout.addWidget(self.nameinput)

        self.age = QLineEdit()
        self.age.setPlaceholderText("Age")
        onlyInt = QIntValidator()
        onlyInt.setRange(0,100)
        self.age.setValidator(onlyInt)
        layout.addWidget(self.age)

        self.phonenumber = QLineEdit()
        self.phonenumber.setPlaceholderText("Phone Number")
        self.phonenumber.setInputMask("9999 999 9999")
        layout.addWidget(self.phonenumber)
        
        self.chatid = QLineEdit(randomChatId())
        onlyInt = QIntValidator()
        self.chatid.setValidator(onlyInt)
        self.chatid.setReadOnly(True)
        layout.addWidget(self.chatid)
        
        self.identityid = QLineEdit()
        self.identityid.setPlaceholderText("Your Identity ID")
        onlyInt = QIntValidator()
        onlyInt.setRange(0,1000000000)
        self.identityid.setValidator(onlyInt)
        layout.addWidget(self.identityid)
        

        self.usernm = QLineEdit()
        self.usernm.setPlaceholderText("User Name:")
        layout.addWidget(self.usernm)
        
        self.passw = QLineEdit()
        self.passw.setPlaceholderText("Choose Your Password Wisely:")
        layout.addWidget(self.passw)
        

        layout.addWidget(self.QBtn)
        self.setLayout(layout)

    def adduser(self):

        full_name = ""
        age = -1
        phone_number = -1
        chat_id = -1
        identity_id = -1
        username = ""
        password = ""


        full_name = self.nameinput.text()
        age = self.age.text()
        phone_number = self.phonenumber.text()
        chat_id = self.chatid.text()
        identity_id = self.identityid.text()
        username = self.usernm.text()
        password = self.passw.text()
        

        while True:
            if self.nameinput.text() == "":
                self.conn = sqlite3.connect(DB_FILE)
                self.c = self.conn.cursor()
                QMessageBox.warning(QMessageBox(), 'Warning', 'Name Field Can Not Be Empty!')
                self.c.close()
                self.conn.close()
                break
            
            elif self.age.text() == "":
                self.conn = sqlite3.connect(DB_FILE)
                self.c = self.conn.cursor()
                QMessageBox.warning(QMessageBox(), 'Warning', 'Age Field Can Not Be Empty!')
                self.c.close()
                self.conn.close()
                break
            
            elif self.phonenumber.text() == "":
                self.conn = sqlite3.connect(DB_FILE)
                self.c = self.conn.cursor()
                QMessageBox.warning(QMessageBox(), 'Warning', 'Phone Number Field Can Not Be Empty!')
                self.c.close()
                self.conn.close()
                break
            
            elif self.identityid.text() == "":
                self.conn = sqlite3.connect(DB_FILE)
                self.c = self.conn.cursor()
                QMessageBox.warning(QMessageBox(), 'Warning', 'Identity ID Field Can Not Be Empty!')
                self.c.close()
                self.conn.close()
                break
            
            elif self.usernm.text() == "":
                self.conn = sqlite3.connect(DB_FILE)
                self.c = self.conn.cursor()
                QMessageBox.warning(QMessageBox(), 'Warning', 'User Name Field Can Not Be Empty!')
                self.c.close()
                self.conn.close()
                break
            
            elif self.passw.text() == "":
                self.conn = sqlite3.connect(DB_FILE)
                self.c = self.conn.cursor()
                QMessageBox.warning(QMessageBox(), 'Warning', 'Password Field Can Not Be Empty!')
                self.c.close()
                self.conn.close()
                break
            
            else:
                try:
                    self.conn = sqlite3.connect(DB_FILE)
                    self.c = self.conn.cursor()
                    self.c.execute("""INSERT INTO userinfo(full_name, age, phone_number, chat_id, identity_id, username, password) VALUES (?,?,?,?,?,?,?)""",(full_name, age, phone_number, chat_id, identity_id, username, password))
                    self.conn.commit()
                    self.c.close()
                    self.conn.close()
                    QMessageBox.information(QMessageBox(),'Successful','User Was added to the database successfully.')
                    self.close()
                    break
                except Exception:
                    QMessageBox.warning(QMessageBox(), 'Error', 'Could not add USer to the database.')
                    break


class SearchDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super(SearchDialog, self).__init__(*args, **kwargs)

        self.QBtn = QPushButton()
        self.QBtn.setText("Search")

        self.setWindowTitle("Search user")
        self.setFixedWidth(300)
        self.setFixedHeight(100)
        self.QBtn.clicked.connect(self.searchUser)
        layout = QVBoxLayout()

        self.searchinput = QLineEdit()
        onlyInt = QIntValidator()
        self.searchinput.setValidator(onlyInt)
        self.searchinput.setInputMask("9999999999999")
        self.searchinput.setPlaceholderText("Chat Id:")
        layout.addWidget(self.searchinput)
        layout.addWidget(self.QBtn)
        self.setLayout(layout)

    def searchUser(self):
        app_id = ""
        app_id = self.searchinput.text()
        try:
            self.conn = sqlite3.connect(DB_FILE)
            self.c = self.conn.cursor()
            result = self.c.execute("""SELECT * FROM userinfo WHERE chat_id="""+str(app_id))
            row = result.fetchone()
                
            result = "| Roll No: "+str(row[0])+'\n'+"| Full Name: "+str(row[1])+'\n'+"| Age: "+str(row[2])+'\n'+"| Phone Number: "+str(row[3])+'\n'+"| Chat ID: "+str(row[4])+'\n'+"| Identity ID: "+str(row[5])+'\n'+"| User Name: "+str(row[6])+'\n'+"| Password: "+str(row[7])+'\n'
            QMessageBox.information(QMessageBox(), "User:"+str(row[6]), result)
            self.close()
            
        except Exception:
            QMessageBox.warning(QMessageBox(), 'Error', 'Could not Find User from the database.')

class DeleteDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super(DeleteDialog, self).__init__(*args, **kwargs)

        self.QBtn = QPushButton()
        self.QBtn.setText("Delete")

        self.setWindowTitle("Delete User")
        self.setFixedWidth(300)
        self.setFixedHeight(100)
        self.QBtn.clicked.connect(self.deleteUser)
        layout = QVBoxLayout()

        self.deleteinput = QLineEdit()
        onlyint = QIntValidator()
        self.deleteinput.setValidator(onlyint)
        self.deleteinput.setInputMask("9999999999999")
        self.deleteinput.setPlaceholderText("Chat ID:")
        layout.addWidget(self.deleteinput)
        layout.addWidget(self.QBtn)
        self.setLayout(layout)

    def deleteUser(self):
        delrol = ""
        delrol = self.deleteinput.text()
        try:
            self.conn = sqlite3.connect(DB_FILE)
            self.c = self.conn.cursor()
            self.c.execute("""DELETE FROM userinfo WHERE chat_id ="""+str(delrol))
            self.conn.commit()
            self.c.close()
            self.conn.close()
            QMessageBox.information(QMessageBox(),'Successful',' User Deleted From The Table.')
            self.close()
        except ValueError:
            QMessageBox.warning(QMessageBox(), 'Error', 'Could not Delete Uder from the database Or User Does NOT Exist.')
    
# app = QApplication(sys.argv)
# if __name__ == "__main__":
#     window = ManageDB()
#     window.show()
#     window.loaddata()
# sys.exit(app.exec_())