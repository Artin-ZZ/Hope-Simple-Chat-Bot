## Import All Global Libs Here ##
import datetime, sqlite3, random, webbrowser
from sqlite3 import Error
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtPrintSupport import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import QPoint
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
## Local Libs ##
from src.App_Ui import Ui_App
from DB_manage import ManageDB
from Helpers import randomChatId
from config import DB_FILE



class Main_Run(QMainWindow):
        try:
            def __init__(self) -> None:
                    ## Setting Up Our Ui:
                    QMainWindow.__init__(self)
                    self.ui = Ui_App()
                    self.ui.setupUi(self)
                    
                    ## Now We have To Set up The Other buttons Of Our Ui File:
                    ##----------- Login Page Index No: 0 ---------------##
                    self.ui.login_btn.clicked.connect(self.logIn)
                    self.ui.reg_btn.clicked.connect(self.regUser)
                    ##----------- Page Home Index No: 1 ---------------##
                    self.ui.btn1.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(1))
                    self.ui.btn2.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(2))
                    self.ui.btn3.clicked.connect(self.abHope)
                    self.ui.btn4.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))
                    self.ui.btn5.clicked.connect(self.dbMng)
                    ##----------- Page Talk & Speach Index No: 2 ---------------##
                    self.ui.btn1_2.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(1))
                    self.ui.btn2_2.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(2))
                    self.ui.btn4_2.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))
                    self.ui.sp_tk.clicked.connect(self.start_ai)
                    self.ui.btn3_2.clicked.connect(self.abHope)
                    self.ui.btn5_2.clicked.connect(self.dbMng)
                    self.ui.submit_btn.clicked.connect(self.submitText)
            
            
            
            ######################
            # Button Functions   #
            ######################
            ### Submit Button ###
            def submitText(self):
                ## Speach Lists:
                GREET = ["Hello",'hello','HELLO','hEllo','heLlo','helLo','hellO','Hi','HI','hi','hI']
                AGE_AND_OTHERS = ['your age','yourage','yourage?','your age?','how old are you?','how old are you','howoldareyou','howoldareyou?']
                INTRO = ['who are you?','whoareyou','whoareyou?','who are you','what are you','what are you?','whatareyou','whatareyou?']
                FEELINGS = ['how are you','how are you?','howareyou?','howareyou','how are you feeling','howareyoufeeling','howareyoufeeling?','how are you feeling?']
                USER_FEEL_G = ['im good','im fantastic','perfect','im feeling amazing','im perfect','im cool','cool','amazing','legendary']
                USER_FEEL_B = ['not bad','im not good','not good','my heart is broken','broken heart','fucked up','im fucked up','im angry','angry','im hopeless','hopeless','i lost hope']
                OFC = ['online search','search','google me','music','online music']
                ##############################
                
                if self.ui.txt_box.text() in GREET:
                    data_txt = "Hello There!"
                    resText = self.ui.result.setText("Hope Says: "+data_txt)
                    self.ui.txt_box.clear()
                    return resText
                
                elif self.ui.txt_box.text() in INTRO:
                    txt = "Im Hope A Chatty Friend For You."
                    resText4 = self.ui.result.setText("Hope Says: "+txt)
                    self.ui.txt_box.clear()
                    return resText4
                
                elif self.ui.txt_box.text() == "":
                    resText1 = self.ui.result.setText("Hope Says: You Said Nothing Say Somthing First!")
                    return resText1
                
                elif self.ui.txt_box.text() in AGE_AND_OTHERS:
                    ### Age Counter And Stuff ###
                    yr_of_birth = 2022
                    m_of_birth = 7
                    d_of_birth = 29
                    cr_yr = datetime.datetime.now().year
                    cr_month = datetime.datetime.now().month
                    cr_day = datetime.datetime.now().day
                    cr_age_yr = abs(cr_yr) - abs(yr_of_birth)
                    cr_age_month = abs(m_of_birth) - abs(cr_month)
                    cr_age_day = abs(cr_day) - abs(d_of_birth)
                    resAge = f"Im {abs(cr_age_yr)} years, {abs(cr_age_month)} Months ,And {abs(cr_age_day)} Days Old."
                    resText3 = self.ui.result.setText("Hope Says: "+resAge)
                    self.ui.txt_box.clear()
                    return resText3
                
                elif self.ui.txt_box.text() in FEELINGS:
                    hsay = "Well Im A Program I have No Emotions But I Feel Good Talking To You :)\n"
                    hsay += "How Are You Doing & Feeling?"
                    resText5 = self.ui.result.setText("Hope Says: "+hsay)
                    self.ui.txt_box.clear()
                    return resText5
                
                elif self.ui.txt_box.text() in USER_FEEL_G:
                    h_say = "Fantasitic Im Realy happy For You Always Be Good And Saty Positive :)"
                    resText6 = self.ui.result.setText("Hope Says: "+h_say)
                    self.ui.txt_box.clear()
                    return resText6
                
        
                elif self.ui.txt_box.text() in USER_FEEL_B:
                    hSay1 = "Hang In There Friend Im Sure Every Thing Will Change For The Better And You Will See Better\nDays And Move Forward on What Ever It Is That You Feel Bad For Right Now\nTrust Yor Strength And Keep Fighting The Good Fight :)"
                    hSay2 = "Life Is Fool Of Wonders & Lessons ,Right Now It Taught You A Lesson Get Up And\nLearn From Your Lesson You Stil Have A Lot To Bring To This World My Good Friend :)"
                    hSay3 = "The secret of life is to fall seven times and to get up eight times. — Paulo Coelho"
                    hSay4 = "It is impossible to live without failing at something unless you live so cautiously\nThat you might as well not have lived at all\nIn which case you have failed by default. ― J.K. Rowling"
                    hSay5 = "When you take risks, you learn that there will be times when you succeed\nAnd there will be times when you fail\nAnd both are equally important. ― Ellen DeGeneres"
                    hSay6 = "Children have a lesson adults should learn, to not be ashamed of failing\nBut to get up and try again. Most of us adults are so afraid, so cautious, so 'safe,' and therefore\nSo shrinking and rigid and afraid that it is why so many humans fail\nMost middle-aged adults have resigned themselves to failure. ― Malcolm X"
                    hSay7 = "We need to accept that we won't always make the right decisions, that we'll\nScrew up royally sometimes – understanding that failure is not the opposite of\nSuccess, it's part of success. ― Arianna Huffington"
                    hSay8 = "Heart break such a hard and self killing lesson that we have to face some times\nJust know that what can not kill you will make you stronger\nMore careful more wise im sure you will get over what ever or whom ever broke your heart\nWith love ― Hope"
                    
                    
                    randList = [hSay1, hSay2, hSay3, hSay4, hSay5, hSay6, hSay7, hSay8]
                    resText7 = self.ui.result.setText("Hope Says: "+random.choice(randList))
                    self.ui.txt_box.clear()
                    return resText7
                
                elif self.ui.txt_box.text() in OFC:
                    res = self.ui.result.setText("Hope Says: Type in something in the new page so i can search for you")
                    self.ui.txt_box.clear()
                    dlg = Goole_Search()
                    dlg.exec_()
                    return res
                
                
                else:
                    data_txt = "Sorry I don't Understand What You Said :("
                    resText2 = self.ui.result.setText("Hope Says: "+data_txt)
                    self.ui.txt_box.clear()
                    return resText2
            
            ### About Hope ###
            def abHope(self):
                QMessageBox.information(QMessageBox(), 'About Hope', '| Im Hope\n| A Chatty Friend For You\n| Im Super Fun To talk & Hangout With :)')
            ##########################
            # Mouse Press Event Func #
            ##########################
            def mousePressEvent(self, evt):
                try:
                    self.oldPos = evt.globalPos()
                except:
                    QMessageBox.warning(QMessageBox(), "Error!", "Oops!, something went wrong try again or contact support.")

            #########################
            # Mouse Move Event Func #
            #########################
            def mouseMoveEvent(self, evt):
                try:
                    delta = QPoint(evt.globalPos() - self.oldPos)
                    self.move(self.x() + delta.x(), self.y() + delta.y())
                    self.oldPos = evt.globalPos()
                except:
                    QMessageBox.warning(QMessageBox(), "Error!", "Oops!, something went wrong try again or contact support.")
                 
            
            ## add User Func:
            def regUser(self):
                dlg = RegUserDialog()
                dlg.exec_()
            
            ## Data Base manager Func:
            def dbMng(self):
                self.window1 = ManageDB()
                if self.window1.isVisible():
                    self.window1.hide()
                else:
                    self.window1.show()
            
            ## Log In Function:
            def logIn(self):
                self.con = sqlite3.connect(DB_FILE)
                self.c = self.con.cursor()
                
                user_txtbox = ""
                password_txtbox = ""
                
                
                
                while True:
                    if self.ui.usernm_txtbox.text() == "":
                        self.conn = sqlite3.connect(DB_FILE)
                        self.c = self.conn.cursor()
                        QMessageBox.warning(QMessageBox(), 'Warning', 'User Name Is Requiered!')
                        self.c.close()
                        self.conn.close()
                        break
                    
                    elif self.ui.passw_txtbox.text() == "":
                        self.conn = sqlite3.connect(DB_FILE)
                        self.c = self.conn.cursor()
                        QMessageBox.warning(QMessageBox(), 'Warning', 'Password Is Requiered!')
                        self.c.close()
                        self.conn.close()
                        break
                    
                    else:
                        try:
                            if self.userNameChek(username=user_txtbox) and self.passwordCheck(password=password_txtbox):
                                self.ui.stackedWidget.setCurrentIndex(1)
                                QMessageBox.information(QMessageBox(), "Welcome!", "LogIn Successful")
                                self.ui.usernm_txtbox.clear()
                                self.ui.passw_txtbox.clear()
                                break
                                
                            else:
                                QMessageBox.warning(QMessageBox(), "Wrong UserName/Password", "Wrong Password Or User Name Or User Does Not Exist!")
                                break
                                
                                
                        except ValueError:
                            QMessageBox.warning(QMessageBox(), 'Error', 'Value Error!')
                        except Exception:
                            QMessageBox.warning(QMessageBox(), 'Error', 'Exception Error! Something is wrong with the database table!')
                            break
                
                ## Query Data Bind:
            def query(self, sql: str, data_bind: list = []):

                # Check required params
                if not sql:
                    # Raise error
                    raise Exception("You must provide the required parameters: ['sql']")

                # Try to query to the database
                try:
                    # Return the query result
                    self.c.execute(sql, data_bind)

                    return self.c

                # Catch error
                except Error as e:
                    # Raise error
                    raise Exception(e)
            
            def userNameChek(self, username):
                self.con = sqlite3.connect(DB_FILE)
                self.c = self.con.cursor()
                sql = """
                    SELECT * FROM userinfo
                    WHERE username = ?;
                """
                data = [username]
                if self.query(sql, data).fetchone():
                    return self.query(sql, data).fetchone()
                else:
                    return False
            
            def passwordCheck(self, password):
                self.con = sqlite3.connect(DB_FILE)
                self.c = self.con.cursor()
                sql = """
                    SELECT * FROM userinfo
                    WHERE password = ?;
                """
                data = [password]
                if self.query(sql, data).fetchone():
                    return self.query(sql, data).fetchone()
                else:
                    return False
                
                
            #############################################################   
            #####################
            # Start Method Func #
            #####################
            def start_ai(self):
                pass
                
 
                
        except ValueError:
            QMessageBox.warning(QMessageBox(), "Error!", "Value Error!!")
        
        except TimeoutError:
            QMessageBox.warning(QMessageBox(), "Network Error!", "Your Connection To Internet Was Lost!, Check Your Network And Try Again.")
        
        except ImportError:
            QMessageBox.warning(QMessageBox(), "File Error!", "There is a misssing important file that the app could not find!\nTry Reinstalling The app or contact support.")

        except TypeError:
            QMessageBox.warning(QMessageBox(), "Error!", "There is a Type Error!")

### Google Search Dialog ###
class Goole_Search(QDialog):
    try:
        def __init__(self, *args, **kwargs):
            super(Goole_Search, self).__init__(*args, **kwargs)
        
            self.Search = QPushButton()
            self.Search.setText("SEARCH")
            
            self.srch_lbl = QLabel()
            self.srch_lbl.setText("Search Somthing Below:")
            font = QFont()
            font.setBold(True)
            font.setPointSize(16)
            self.srch_lbl.setFont(font)
            
            self.srch_field = QLineEdit()
            font2 = QFont()
            font2.setBold(True)
            font2.setPointSize(12)
            self.srch_field.setFont(font2)

            self.setWindowTitle("Online Search")
            self.setFixedWidth(500)
            self.setFixedHeight(250)

            self.Search.clicked.connect(self.gSearch)
            
            layout = QVBoxLayout()
            
            layout.addWidget(self.srch_lbl)
            layout.addWidget(self.srch_field)
            layout.addWidget(self.Search)
            self.setLayout(layout)
        
        def gSearch(self):
            LIB = self.srch_field.text()
            URL_SEARCH = "https://www.google.co.in/search?q="+(str(LIB))+ "&oq="+(str(LIB))+"&gs_l=serp.12..0i71l8.0.0.0.6391.0.0.0.0.0.0.0.0..0.0....0...1c..64.serp..0.0.0.UiQhpfaBsuU"
            webbrowser.open_new(URL_SEARCH)
            self.srch_field.clear()
        
        
    except TimeoutError:
        QMessageBox.warning(QMessageBox(), "Network Error!","Make Sure You Are Connected & Try Again")

    
### Add User/Sign Up Dialog ###
class RegUserDialog(QDialog):
    try:
        def __init__(self, *args, **kwargs):
            super(RegUserDialog, self).__init__(*args, **kwargs)
            
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
    except ValueError:
        QMessageBox.warning(QMessageBox(), "Error!", "Value Error!!")
        
    except TimeoutError:
        QMessageBox.warning(QMessageBox(), "Network Error!", "Your Connection To Internet Was Lost!, Check Your Network And Try Again.")
        
    except ImportError:
        QMessageBox.warning(QMessageBox(), "File Error!", "There is a misssing important file that the app could not find!\nTry Reinstalling The app or contact support.")

    except TypeError:
            QMessageBox.warning(QMessageBox(), "Error!", "There is a Type Error!")


######################
# Runs The Whole App #
######################
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    root = Main_Run()
    root.show()
    sys.exit(app.exec())
