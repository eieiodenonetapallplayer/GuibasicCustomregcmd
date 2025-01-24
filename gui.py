class u(object):
    def s(self, aa):
        aa.setObjectName("O")
        aa.setWindowTitle("TeTeTeTeTe#7420")
        aa.resize(263, 82)
        self.cw = QWidget(aa)
        self.cw.setObjectName("cw")
        self.ed = QLineEdit(self.cw)
        self.ed.setGeometry(QRect(20, 30, 113, 30))
        self.ed.setText("")
        self.ed.setObjectName("ed")
        self.btn = QPushButton(self.cw)
        self.btn.setGeometry(QRect(160, 30, 75, 30))
        self.btn.setObjectName("btn")
        self.btn.setText("USE")
        self.btn.clicked.connect(self.__)
        aa.setCentralWidget(self.cw)

    def __(self):
        e = self.ed.text()
        if e in["REG","reg","Reg"]:
                                # ใส่ค่า reg
            os.system('msg * "สำเร็จ ( REG )"')
        elif e in["NET","net","Net"]:
                                # ใส่ค่า Netsh
            os.system('msg * "สำเร็จ ( NET )"')
        elif e in["CMD","cmd","Cmd"]:
                                # ใส่ค่า Cmd
            os.system('msg * "สำเร็จ ( CMD )"')
        else:
            os.system('msg * "REG,NET,CMD"')

if __name__=="__main__":from PyQt5.QtCore import *;from PyQt5.QtWidgets import *;import sys,os;a=QApplication(sys.argv);aa=QMainWindow();e=u();e.s(aa);aa.show();a.exec_()
