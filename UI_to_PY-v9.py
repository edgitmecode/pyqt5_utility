# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:/Python/Scripts/UI_to_PY-v5.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
# Code purpose : A GUI version of utility to convert PyQT5 designer .ui code to 
#                python .py code.   

from PyQt5 import QtCore, QtGui, QtWidgets 
from PyQt5.QtWidgets import QMessageBox, QWidget
import subprocess, sys, os


class Ui_Main_window(QWidget):
    """ Created by: PyQt5 UI code generator 5.11.3
generated from reading ui file 'D:/Python/Scripts/UI_to_PY-v5.ui
    
    """
    
    fileName = " "
    

    def setupUi(self, Main_window):
        Main_window.setObjectName("Main_window")
        Main_window.resize(711, 353)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setKerning(True)
        Main_window.setFont(font)
        Main_window.setAutoFillBackground(False)

        self.buttonBox = QtWidgets.QDialogButtonBox(Main_window)
        self.buttonBox.setGeometry(QtCore.QRect(500, 290, 156, 23))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")

        self.layoutWidget = QtWidgets.QWidget(Main_window)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 290, 96, 15))
        self.layoutWidget.setObjectName("layoutWidget")

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.label_version = QtWidgets.QLabel(self.layoutWidget)
        self.label_version.setObjectName("label_version")
        self.horizontalLayout_2.addWidget(self.label_version)

        self.label_version_number = QtWidgets.QLabel(self.layoutWidget)
        self.label_version_number.setObjectName("label_version_number")
        self.horizontalLayout_2.addWidget(self.label_version_number)

        self.layoutWidget1 = QtWidgets.QWidget(Main_window)
        self.layoutWidget1.setGeometry(QtCore.QRect(20, 10, 639, 22))
        self.layoutWidget1.setObjectName("layoutWidget1")

        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")

        self.radioOut_to_File = QtWidgets.QRadioButton(self.layoutWidget1)
        self.radioOut_to_File.setObjectName("radioOut_to_File")
        self.horizontalLayout_3.addWidget(self.radioOut_to_File)

        self.radioOut_to_Screen = QtWidgets.QRadioButton(self.layoutWidget1)
        self.radioOut_to_Screen.setObjectName("radioOut_to_Screen")
        self.horizontalLayout_3.addWidget(self.radioOut_to_Screen)

        self.checkBox_Exe_option = QtWidgets.QCheckBox(self.layoutWidget1)
        self.checkBox_Exe_option.setObjectName("checkBox_Exe_option")
        self.horizontalLayout_3.addWidget(self.checkBox_Exe_option)

        self.Debug_checkbox = QtWidgets.QCheckBox(self.layoutWidget1)
        self.Debug_checkbox.setObjectName("Debug_checkbox")
        self.horizontalLayout_3.addWidget(self.Debug_checkbox)

        self.label_indent = QtWidgets.QLabel(self.layoutWidget1)
        self.label_indent.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_indent.setObjectName("label_indent")
        self.horizontalLayout_3.addWidget(self.label_indent)

        self.spinBox_indent = QtWidgets.QSpinBox(self.layoutWidget1)
        self.spinBox_indent.setObjectName("spinBox_indent")
        self.horizontalLayout_3.addWidget(self.spinBox_indent)
        
        self.checkBox_Help = QtWidgets.QPushButton(self.layoutWidget1)
        self.checkBox_Help.setObjectName("checkBox_Help")
        self.horizontalLayout_3.addWidget(self.checkBox_Help)
  
        self.layoutWidget2 = QtWidgets.QWidget(Main_window)
        self.layoutWidget2.setGeometry(QtCore.QRect(0, 48, 661, 231))
        self.layoutWidget2.setObjectName("layoutWidget2")

        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget2)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")

        self.lineEdit_Ui_file_selection = QtWidgets.QLineEdit(self.layoutWidget2)
        self.lineEdit_Ui_file_selection.setObjectName("lineEdit_Ui_file_selection")
        self.gridLayout.addWidget(self.lineEdit_Ui_file_selection, 0, 1, 1, 1)
        
        self.pushButton_UI_select = QtWidgets.QPushButton(self.layoutWidget2)
        self.pushButton_UI_select.setObjectName("pushButton_UI_select")
        self.gridLayout.addWidget(self.pushButton_UI_select, 0, 0, 1, 1)

        self.label_py_filename = QtWidgets.QLabel(self.layoutWidget2)
        self.label_py_filename.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_py_filename.setAlignment(QtCore.Qt.AlignCenter)
        self.label_py_filename.setObjectName("label_py_filename")
        self.gridLayout.addWidget(self.label_py_filename, 1, 0, 1, 1)

        self.lineEdit_Py_file_name = QtWidgets.QLineEdit(self.layoutWidget2)
        self.lineEdit_Py_file_name.setObjectName("lineEdit_Py_file_name")
        self.gridLayout.addWidget(self.lineEdit_Py_file_name, 1, 1, 1, 1)

        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.layoutWidget2)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.gridLayout.addWidget(self.plainTextEdit, 3, 1, 1, 1)

        self.pushButton_create = QtWidgets.QPushButton(self.layoutWidget2)
        self.pushButton_create.setObjectName("pushButton_create")
        self.gridLayout.addWidget(self.pushButton_create, 3, 0, 1, 1)

        self.pushButton_gui_preview = QtWidgets.QPushButton(self.layoutWidget2)
        self.pushButton_gui_preview.setObjectName("pushButton_gui_preview")
        self.gridLayout.addWidget(self.pushButton_gui_preview, 2, 0, 1, 1)

        self.pushButton = QtWidgets.QPushButton(Main_window)
        self.pushButton.setGeometry(QtCore.QRect(290, 290, 75, 21))
        self.pushButton.setObjectName("pushButton")
        
        self.retranslateUi(Main_window)

        self.buttonBox.accepted.connect(Main_window.accept)
        self.buttonBox.rejected.connect(Main_window.reject)

        QtCore.QMetaObject.connectSlotsByName(Main_window)
        
        # clicked button action -------------------------------

        self.pushButton_UI_select.clicked.connect(self.file_select)
        self.pushButton_create.clicked.connect(self.convert)
        self.pushButton_gui_preview.clicked.connect(self.gui_preview)
        self.checkBox_Help.clicked.connect(self.help_display)
        self.pushButton.clicked.connect(self.clear_txt)
        
        # Display version number ----------------------------------
       
        output2 = subprocess.getoutput('pyuic5 --version')
        version = output2[30:-22]
        self.label_version_number.setText(version)
        
        # set radio button default to screen ---------------------
        self.radioOut_to_Screen.setChecked(True)
        
        # set slider default to 4 --------------------------------
        self.spinBox_indent.setMinimum(1)
        self.spinBox_indent.setMaximum(20)
        self.spinBox_indent.setProperty("value", 4)
        
        # Function Definitions -----------------------------------
        
    def clear_txt(self):
        self.plainTextEdit.clear()
              
              
    def gui_preview(self):
        """ Displays GUI version of .ui file """ 

        if self.Debug_checkbox.isChecked() == True :
           cmdString = 'pyuic5 -p -d ' + self.fileName
        else:
           cmdString = 'pyuic5 -p ' + self.fileName
        
        output = subprocess.getoutput(cmdString)
        self.plainTextEdit.insertPlainText( output )
         
    def file_select(self):
        """Displays a file select window of .ui files. Changes .ui extenion to
        .py for destination file. """
        # select ui file and change file extension to .py
        self.lineEdit_Ui_file_selection.clear()
        self.lineEdit_Py_file_name.clear()
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        self.fileName, _ = QtWidgets.QFileDialog.getOpenFileName(
                        None,
                        "QFileDialog.getOpenFileName()",
                        "",
                        "UI Files (*.ui);;All Files (*)",
                        options=options)
        py_Filename = self.fileName[:-2]
        py_Filename = py_Filename + "py"
        self.lineEdit_Ui_file_selection.insert( self.fileName )
        if self.fileName:
            self.lineEdit_Py_file_name.insert( py_Filename )
        

    def help_display(self):
        """Displays help in text window """
        cmdString = 'pyuic5 -h' 
        # execute command and return stdout string
        output2 = subprocess.getoutput(cmdString) 
        # show stdout 
        self.plainTextEdit.insertPlainText( output2 )
         
         
    def convert(self):
        """Executes pyuic5 command to convert ui to py file.
        Checks debug, exe, indentation options and screen vs file output """
        status = self.Debug_checkbox.isChecked() 
        status2 = self.checkBox_Exe_option.isChecked()
        status3 = self.radioOut_to_File.isChecked()
        combine = bin(status3) + bin(status2) + bin(status) 
        spin_value = self.spinBox_indent.value()
        str_spinvalue = str(spin_value)
        line_edit_txt = self.lineEdit_Py_file_name.text()
        overwrite_y_n = QMessageBox.No
        exists = os.path.isfile(line_edit_txt) #returns true if line_edit_txt is present

        cmdStr = {'0b00b00b0' : 'pyuic5 ' + self.fileName + ' -i ' + str_spinvalue,
                  '0b00b00b1' : 'pyuic5 -d -i ' + str_spinvalue +' ' + self.fileName,
                  '0b00b10b0' : 'pyuic5 -x -i ' + str_spinvalue +' ' + self.fileName,
                  '0b00b10b1' : 'pyuic5 -x -d -i ' + str_spinvalue +' ' + self.fileName,
                  '0b10b00b0' : 'pyuic5 -i ' + str_spinvalue +' ' + self.fileName + ' -o ' + line_edit_txt,
                  '0b10b00b1' : 'pyuic5 -d -i ' + str_spinvalue +' ' + self.fileName + ' -o ' + line_edit_txt,
                  '0b10b10b0' : 'pyuic5 -x -i ' + str_spinvalue +' ' + self.fileName+ ' -o ' + line_edit_txt,
                  '0b10b10b1' : 'pyuic5 -d -x -i ' + str_spinvalue +' ' + self.fileName+ ' -o ' + line_edit_txt,
                  }
        cmdStr2 = cmdStr[combine] # get dictionary command string defined by user selection
        # If out to file selected --------------------
        if self.radioOut_to_File.isChecked() == True: # is write out to file selected
        # else if file is present -----------------
           if exists == False : # is file present? If true ask permission to overwrite
                 output2 = subprocess.getoutput(cmdStr2) # write command string - write file 
                 self.plainTextEdit.insertPlainText( "\n" + "Created file : " + line_edit_txt )
           else :  
                 overwrite_y_n = QMessageBox.question(self,'File Overwrite', "File exist Overwrite ? ", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                 if overwrite_y_n == QMessageBox.Yes :
                    output2 = subprocess.getoutput(cmdStr2) # write command string - write file 
                    self.plainTextEdit.insertPlainText( output2 +"\n" + "File updated  " )
                 else:
                   self.plainTextEdit.insertPlainText( "\n" + "pyuic5 command not executed NO File updated " )

        else:
           output2 = subprocess.getoutput(cmdStr2) # write command string - write file 
           self.plainTextEdit.insertPlainText( output2 + "output to screen \n" ) # show return message
        
                  
             
            
        
    def retranslateUi(self, Main_window):
        _translate = QtCore.QCoreApplication.translate
        Main_window.setWindowTitle(_translate("Main_window", "PYQT5"))
        self.label_version.setText(_translate("Main_window", "Version"))
        self.label_version_number.setText(_translate("Main_window", "Number"))
        self.radioOut_to_File.setText(_translate("Main_window", "Output to file"))
        self.radioOut_to_Screen.setText(_translate("Main_window", "Output to screen"))
        self.checkBox_Exe_option.setText(_translate("Main_window", "-x Exe option"))
        self.Debug_checkbox.setText(_translate("Main_window", "Debug"))
        self.label_indent.setText(_translate("Main_window", "Indent"))
        self.checkBox_Help.setText(_translate("Main_window", "Help"))
        self.pushButton_UI_select.setText(_translate("Main_window", ".UI Source"))
        self.label_py_filename.setText(_translate("Main_window", ".PY Destination"))
        self.pushButton_create.setText(_translate("Main_window", "Convert Ui to PY"))
        self.pushButton_gui_preview.setText(_translate("Main_window", "GUI Preview"))
        self.pushButton.setText(_translate("Main_window", "Clear"))
       
        # ----------------------------------------------------


if __name__ == "__main__":

    print(Ui_Main_window.__doc__)
    #print(QtWidgets.QDialog.__doc__)
    app = QtWidgets.QApplication(sys.argv)
    Main_window = QtWidgets.QDialog()
    ui = Ui_Main_window()
    ui.setupUi(Main_window)
    Main_window.show()
    sys.exit(app.exec_())
    
