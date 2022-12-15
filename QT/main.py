import sys
import time
import datetime

from PyQt5.QtCore import pyqtSignal, QThread, Qt
from PyQt5 import QtWidgets
from PyQt5.QtGui import QFont

TEXT_FONT = QFont("Verdana", 12)

class WatchThread(QThread):
    update = pyqtSignal()
    
    def run(self):
        while True:
            time.sleep(1)
            
            self.update.emit()

class ElectronicWatch(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.width = 400
        self.height = 400
        
        self.setWindowTitle("Electronic Watch")
        self.setFixedWidth(self.width)
        self.setFixedHeight(self.height)
        
        self.build()

    def build(self):
        self.timeLabel = QtWidgets.QLabel(self)
        self.dateLabel = QtWidgets.QLabel(self)
        self.dayOfWeekLabel = QtWidgets.QLabel(self)
        
        self.timeLabel.move(
            int(self.width / 2) - 50, 
            int(self.height / 2) - 50
        )
        
        self.timeLabel.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.timeLabel.setAlignment(Qt.AlignCenter)
        
        self.timeLabel.setFont(TEXT_FONT)
        
        self.dateLabel.move(
            int(self.width / 2) - 50, 
            int(self.height / 2)
        )
        
        self.dateLabel.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.dateLabel.setAlignment(Qt.AlignCenter)
        
        self.dateLabel.setFont(TEXT_FONT)
        
        self.dayOfWeekLabel.move(
            int(self.width / 2) - 50, 
            int(self.height / 2) + 40
        )
        
        self.dayOfWeekLabel.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.dayOfWeekLabel.setAlignment(Qt.AlignCenter)
        
        self.dayOfWeekLabel.setFont(TEXT_FONT)
        
        self.update_time()
        
        self.updateThread = WatchThread(self)
        self.updateThread.start()
        self.updateThread.update.connect(lambda self=self: self.update_time())
        
    def update_time(self):
        curtime = datetime.datetime.now()
        
        self.timeLabel.setText(curtime.strftime("%T"))
        self.dateLabel.setText(curtime.strftime("%x"))
        self.dayOfWeekLabel.setText(curtime.strftime("%A"))

def main():
    app = QtWidgets.QApplication(sys.argv)
    
    window = ElectronicWatch()
    window.show()
    
    app.exec_()
    
if __name__ == "__main__":
    main()
