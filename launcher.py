from Configuration import Ui_Configuration
from PyQt4 import *
import sys


class Launcher(QtGui.QMainWindow):
    
    def __init__(self):
        super(Launcher, self).__init__()
        self.ui = Ui_Configuration()
        self.ui.setupUi(self)
        #Event handlers
        self.ui.generate_button.clicked.connect(self.parseText)
        self.show()


    def parseText(self):
        print "Parsing text"
        print self.ui.config_file_name.text()
        print self.ui.pol1.currentText()
        filename = self.ui.config_file_name.text()
        
        target = open(filename, 'w')
        target.truncate()
        
        target.write("COMMANDOVERRIDE=OFF")
        target.write("\n")
        target.write("READER="+self.ui.input_mode.currentText())
        target.write("\n")
        target.write("OUTPUT="+self.ui.output_file.text())
        target.write("\n")
        target.write("INPUT="+self.ui.input_file.text())
        target.write("\n")
        
        #config one
        target.write("%")
        target.write("\n")
        target.write("POL="+self.ui.pol1.currentText())
        target.write("\n")
        target.write("TIMEFINDER="+self.ui.time1.currentText())
        target.write("\n")
        target.write("VERTEX="+ self.makeLine(self.ui.vertex1.currentText(), self.ui.coordinate1.currentText()))
        target.write("\n")
        target.write("%")
        target.write("\n")
        
        #config 2
        target.write("%")
        target.write("\n")
        target.write("POL="+self.ui.pol2.currentText())
        target.write("\n")
        target.write("TIMEFINDER="+self.ui.time2.currentText())
        target.write("\n")
        target.write("VERTEX="+self.makeLine(self.ui.vertex2.currentText(), self.ui.coordinate2.currentText()))
        target.write("\n")
        target.write("%")
        target.write("\n")
        #config 3
        target.write("%")
        target.write("\n")
        target.write("POL="+self.ui.pol3.currentText())
        target.write("\n")
        target.write("TIMEFINDER="+self.ui.time3.currentText())
        target.write("\n")
        target.write("VERTEX="+ self.makeLine(self.ui.vertex3.currentText(), self.ui.coordinate3.currentText()))
        target.write("\n")
        target.write("%")
        target.write("\n")
        target.close()

    def makeLine(self, finder, myType="TIMES", val1="0", val2="0", val3="0"):
        
        return str( finder + "[" + myType +"]"+ "("+ val1 + ","+ val2 + "," + val3 + ")" )


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    launch  = Launcher()
    sys.exit(app.exec_())
