import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 854)
        font = QtGui.QFont()
        font.setPointSize(12)
        
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(270, 20, 451, 61)) 
        font = QtGui.QFont()
        font.setFamily("Tempus Sans ITC")
        font.setPointSize(40)
        self.frame.setFont(font)
        self.frame.setStyleSheet("background-color: rgb(255, 170, 0);\n""")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(130, 10, 201, 41))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(14)
        font.setBold(True) #to make it bold
        font.setWeight(75) #increase the font weight
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.text_info = QtWidgets.QTextEdit(self.centralwidget)
        self.text_info.setGeometry(QtCore.QRect(500, 520, 400, 150))
        self.text_info.setObjectName("text_info")
        self.text_info.setFont(font)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(200, 140, 181, 41))
    
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")

        self.label_season = QtWidgets.QLabel(self.centralwidget)
        self.label_season.setGeometry(QtCore.QRect(55, 145, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_season.setFont(font)
        self.label_season.setObjectName("label_season")
        self.label_state = QtWidgets.QLabel(self.centralwidget)
        self.label_state.setGeometry(QtCore.QRect(55, 245, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_state.setFont(font)
        self.label_state.setObjectName("label_state")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(200, 240, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        
        self.label_acres = QtWidgets.QLabel(self.centralwidget)
        self.label_acres.setGeometry(QtCore.QRect(55, 350, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_acres.setFont(font)
        self.label_acres.setObjectName("label_acres")
        self.label_budget = QtWidgets.QLabel(self.centralwidget)
        self.label_budget.setGeometry(QtCore.QRect(55, 452, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_budget.setFont(font)
        self.label_budget.setObjectName("label_budget")
        self.lineEdit_acres = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_acres.setGeometry(QtCore.QRect(200, 350, 181, 41))
        self.lineEdit_acres.setObjectName("lineEdit_acres")
        self.lineEdit_budget = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_budget.setGeometry(QtCore.QRect(200, 450, 181, 41))
        self.lineEdit_budget.setObjectName("lineEdit_budget")
        self.button_submit = QtWidgets.QPushButton(self.centralwidget)
        self.button_submit.setGeometry(QtCore.QRect(200, 550, 181, 41))
        self.button_submit.setStyleSheet("background-color: rgb(0,255,0);\n"
"")
        font = QtGui.QFont()
        font.setPointSize(12)
        self.button_submit.setFont(font)
        self.button_submit.setObjectName("button_submit")
        self.button_submit.clicked.connect(self.submit)  #connect to the function submit

        #To make a vertcal line as a partition
        #self.line = QtWidgets.QFrame(self.centralwidget)
        #self.line.setGeometry(QtCore.QRect(330, 120, 20, 371))
        #self.line.setFrameShape(QtWidgets.QFrame.VLine)
        #self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        #self.line.setObjectName("line")
        self.label_image = QtWidgets.QLabel(self.centralwidget)
        self.label_image.setGeometry(QtCore.QRect(500, 130, 791, 300))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_image.setText("")
        self.label_image.setObjectName("label_image")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1375, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def submit(self):
       #dict "res" has cropname as key and Pesticides as value
        res={'Sugarcane': 'insecticides and fungicides', 'Rice': 'Lambda-cyhalothrin, malathion and zeta-cypermethrin', 'Cotton': 'Pyrethroids and Organophosphates', 'Maize': ' herbicides, atrazine', 'Wheat': 'organochlorines, organophosphates', 'Mustard': 'Plasmodiophora brassicae', 'Banana': 'Chlorpyrifos,Thiabendazole', 'Mango': 'Imidacloprid, Endosulfan', 'Cucumber': 'Carbaryl and Dichlorvos (DDVP)', 'Jute': 'Endosulfan and fenpropathrin', 'Pumpkin': 'Sevin (carbaryl), Furadan', 'Tomato': 'permethrin, bifenthrin'}    
       
        print("Clicked")
        conn = sqlite3.connect('crop_guide1.sqlite')
        cur = conn.cursor()
        ans=cur.execute("SELECT * FROM crop WHERE northern IS NOT NULL")#get all the northern states
        ans=cur.fetchall()#fetch the output
        
        ans=list(ans[0][5:-1]) #remove null values by converting into a list and using slice operator

        se = self.comboBox.currentText() #get text from the user(input) in case of comboBox
        sta =  self.comboBox_2.currentText()
        money = int(self.lineEdit_budget.text()) #get text from the user(input) in case of lineEdit
        acres = int(self.lineEdit_acres.text())
        #print(se)
        #print(sta)
        #print(money)
        #print(acres)
        #print(sta,se)
        ns = sta in ans[0]
        if ns:
            #print("north")
            if money>=50000 and acres>=10:
                #print("North High")
                cur.execute("SELECT nh FROM crop WHERE season=?",[se])
                dd = cur.fetchall()
                dd=str(dd[0])[2:-3]
                print(dd)
                self.label_image.setPixmap(QtGui.QPixmap("D://ML_Projects//Crop_Guide_Application//img//"+dd+".png"))
                result =dd+ "\nPesticides used are "+res[dd]#"+" used to concat
                self.text_info.setText(result)#add text to the line_edit

            else:
                #print("North Low")
                cur.execute("SELECT nl FROM crop WHERE season=?",[se])
                dd = cur.fetchall()
                dd=str(dd[0])[2:-3]
                print(dd)

                self.label_image.setPixmap(QtGui.QPixmap("D://ML_Projects//Crop_Guide_Application//img//"+dd+".png"))
                self.text_info.setText(dd)
                result =dd+ "\nPesticides used are "+res[dd]
                self.text_info.setText(result)

        else:
            print("south")
            if money>=50000 and acres>=10:
                #print("South High")
                cur.execute("SELECT sh FROM crop WHERE season=?",[se])
                dd = cur.fetchall()
                dd=str(dd[0])[2:-3]
                print(dd)

                self.label_image.setPixmap(QtGui.QPixmap("D://ML_Projects//Crop_Guide_Application//img//"+dd+".png"))
                self.text_info.setText(dd)
                result =dd+ "\nPesticides used are "+res[dd]
                self.text_info.setText(result)  

            else:
                print("South Low")
                cur.execute("SELECT sl FROM crop WHERE season=?",[se])
                dd = cur.fetchall()
                dd=str(dd[0])[2:-3]
                print(dd)

                self.label_image.setPixmap(QtGui.QPixmap("D://ML_Projects//Crop_Guide_Application//img//"+dd+".png"))
                self.text_info.setText(dd)
                result =dd+ "\nPesticides used are "+res[dd]
                self.text_info.setText(result)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.label_image.setPixmap(QtGui.QPixmap("D://ML_Projects//Crop_Guide_Application//img//main.png"))#add the image to the label
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "CROP GUIDE"))
        self.label_season.setText(_translate("MainWindow", "Season"))
        self.comboBox.setItemText(0,_translate("MainWindow","Kharif"))
        self.comboBox.setItemText(1,_translate("MainWindow","Zaid"))
        self.comboBox.setItemText(2,_translate("MainWindow","Rabi"))

        self.label_state.setText(_translate("MainWindow", "State"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "Chandigarh"))#add elements to the comboBox_2(State)
        self.comboBox_2.setItemText(1, _translate("MainWindow", "Delhi"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "Haryana"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "Himachal Pradesh"))
        self.comboBox_2.setItemText(4, _translate("MainWindow", "Jammu  Kashmir"))
        self.comboBox_2.setItemText(5, _translate("MainWindow", "Ladakh"))
        self.comboBox_2.setItemText(6, _translate("MainWindow", "Punjab"))
        self.comboBox_2.setItemText(7, _translate("MainWindow", "Rajasthan"))
        self.comboBox_2.setItemText(8, _translate("MainWindow", "Uttarakhand"))
        self.comboBox_2.setItemText(9, _translate("MainWindow", "Uttar Pradesh"))
        self.comboBox_2.setItemText(10, _translate("MainWindow", "Madhya Pradesh"))
        self.comboBox_2.setItemText(11, _translate("MainWindow", "West Bengal"))
        self.comboBox_2.setItemText(12, _translate("MainWindow", "Bihar"))
        self.comboBox_2.setItemText(13, _translate("MainWindow", "Gujarat"))
        self.comboBox_2.setItemText(14, _translate("MainWindow", "Andhra Pradesh"))
        self.comboBox_2.setItemText(15, _translate("MainWindow", "Karnataka"))
        self.comboBox_2.setItemText(16, _translate("MainWindow", "Kerala"))
        self.comboBox_2.setItemText(17, _translate("MainWindow", "Lakshadweep"))
        self.comboBox_2.setItemText(18, _translate("MainWindow", "Puducherry"))
        self.comboBox_2.setItemText(19, _translate("MainWindow", "Tamil Nadu"))
        self.comboBox_2.setItemText(20, _translate("MainWindow", "Telangana"))
        self.comboBox_2.setItemText(21, _translate("MainWindow", "Chennai"))
        self.comboBox_2.setItemText(22, _translate("MainWindow", "Bengaluru"))
        self.comboBox_2.setItemText(23, _translate("MainWindow", "Hyderabad"))
        self.comboBox_2.setItemText(24, _translate("MainWindow", "Kochi"))
        self.comboBox_2.setItemText(25, _translate("MainWindow", "Warangal"))
        self.comboBox_2.setItemText(26, _translate("MainWindow", "Thiruvananthapuram"))
        self.comboBox_2.setItemText(27, _translate("MainWindow", "Coimbatore"))
        self.comboBox_2.setItemText(28, _translate("MainWindow", "Visakhapatanam"))
        self.comboBox_2.setItemText(29, _translate("MainWindow", "Mysuru"))
        self.comboBox_2.setItemText(30, _translate("MainWindow", "Madurai"))
        self.comboBox_2.setItemText(31, _translate("MainWindow", "Vijayawada"))
        self.comboBox_2.setItemText(32, _translate("MainWindow", "Kozhikode"))

        self.label_acres.setText(_translate("MainWindow", "Acres"))
        self.label_budget.setText(_translate("MainWindow", "Budget"))
        self.button_submit.setText(_translate("MainWindow", "Submit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())