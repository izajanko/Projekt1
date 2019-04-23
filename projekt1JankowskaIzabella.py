from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QApplication, QGridLayout, QLabel,QLineEdit, QColorDialog
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import sys
import matplotlib.pyplot as plt
from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np

class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        # stworzenie przycisku z napisem test
        self.button = QPushButton('Oblicz i zapisz', self)
        self.xlabel=QLabel("współrzędna XA", self)
        self.xEdit=QLineEdit()
        self.ylabel=QLabel("współrzędna YA", self)
        self.yEdit=QLineEdit()
        self.x_2label=QLabel("współrzędna XB", self)
        self.x_2Edit=QLineEdit()
        self.y_2label=QLabel("współrzędna YB", self)
        self.y_2Edit=QLineEdit()
        self.x_3label=QLabel("współrzędna XC", self)
        self.x_3Edit=QLineEdit()
        self.y_3label=QLabel("współrzędna YC", self)
        self.y_3Edit=QLineEdit()
        self.x_4label=QLabel("współrzędna XD", self)
        self.x_4Edit=QLineEdit()
        self.y_4label=QLabel("współrzędna YD", self)
        self.y_4Edit=QLineEdit()
        self.y_5label=QLabel("Informacja dla użytkownika", self)
        self.y_5Edit=QLineEdit()
        
        self.clrChoose=QPushButton("Wybierz kolor", self)
        # połączenie przycisku (signal) z akcją (slot)
        self.button.clicked.connect(self.handleButton)
        self.clrChoose.clicked.connect(self.clrChooseF)
        
        self.figure=plt.figure()
        self.canvas=FigureCanvas(self.figure)
        # ladne ustawienie i wyrodkowanie
        layout = QGridLayout(self)
        layout.addWidget(self.button, 10, 1)
        layout.addWidget(self.xlabel, 1, 1)
        layout.addWidget(self.xEdit, 1, 2)
        layout.addWidget(self.ylabel, 2, 1)
        layout.addWidget(self.yEdit, 2, 2)
        layout.addWidget(self.x_2label, 3, 1)
        layout.addWidget(self.x_2Edit, 3, 2)
        layout.addWidget(self.y_2label, 4, 1)
        layout.addWidget(self.y_2Edit, 4, 2)
        layout.addWidget(self.x_3label, 5, 1)
        layout.addWidget(self.x_3Edit, 5, 2)
        layout.addWidget(self.y_3label, 6, 1)
        layout.addWidget(self.y_3Edit, 6, 2)
        layout.addWidget(self.x_4label, 7, 1)
        layout.addWidget(self.x_4Edit, 7, 2)
        layout.addWidget(self.y_4label, 8, 1)
        layout.addWidget(self.y_4Edit, 8, 2)
        
        layout.addWidget(self.y_5label, 9, 1)
        layout.addWidget(self.y_5Edit, 9, 2)
        
        layout.addWidget(self.canvas, 11, 1, 1, -1)
        layout.addWidget(self.clrChoose, 12, 1, 1, -1)

#    def Check Values(self,lineE):
#        if lineE.text().lstrip('-').replace('.','').isdigit():
#            return float (LineE.text())
#    def checkValues(self, lineE):
#        if lineE.text().lstrip('-').replace('.','').isdigit():
#            return float(lineE.text())
#        else:
#            return None    
    def handleButton(self, clr='r'):
        X1=(self.xEdit.text())
        Y1=(self.yEdit.text())
        X2=(self.x_2Edit.text())
        Y2=(self.y_2Edit.text())
        X3=(self.x_3Edit.text())
        Y3=(self.y_3Edit.text())
        X4=(self.x_4Edit.text())
        Y4=(self.y_4Edit.text())
        
        lista=[X1,Y1,
               X2,Y2,
               X3,Y3,
               X4,Y4]
        
        for i in range(len(lista)):
            if lista[i].replace('.','',1).isdigit() == True:
                print("wspolrzedne ok")
                
            else:
                sys.exit("zle wspolrzedne, wprowadz jeszcze raz")
                
        S=np.array(lista).astype(np.float)        
        self.figure.clear()
        ax=self.figure.add_subplot(111)
        ax.plot(S[0],S[1],'ro', color=clr)
        ax.plot(S[2],S[3],'ro', color=clr)
        ax.plot(S[4],S[5],'ro', color=clr)
        ax.plot(S[6],S[7],'ro', color=clr)
        x1=[S[0],S[2]]
        y1=[S[1],S[3]]
        ax.plot(x1,y1, color=clr)
        x2=[S[4],S[6]]
        y2=[S[5],S[7]]
        ax.plot(x2,y2, color=clr)
        M=((S[2]-S[0])*(S[7]-S[5])-(S[3]-S[1])*(S[6]-S[4]))

        if M!=0:
            t1=((S[4]-S[0])*(S[7]-S[5])-(S[5]-S[1])*(S[6]-S[4]))/((S[2]-S[0])*(S[7]-S[5])-(S[3]-S[1])*(S[6]-S[4]))
            t2=((S[4]-S[0])*(S[3]-S[1])-(S[5]-S[1])*(S[2]-S[0]))/((S[2]-S[0])*(S[7]-S[5])-(S[3]-S[1])*(S[6]-S[4]))
        else:
                sys.exit("dzielenie przez 0")
        XP=S[0]+t1*(S[2]-S[0])
        YP=S[1]+t1*(S[3]-S[1])
        ax.plot(XP,YP,'ro',color="black")
        if t1<=1 and t1>=0 and t2<=1 and t2>=0:
           # (self.y_5Edit.text(nn))
            self.y_5Edit.setText("Punkt należy do odcinków")
        elif t1<=1 and t1>=0 or t2<=1 and t2>=0:
            self.y_5Edit.setText("Punkt leży na przedłużeniu jednego z odcinków")
        else:
            self.y_5Edit.setText("Punkt leży na przedłużeniu obu odcinków")
        
        
        x3=[S[0],S[2],XP]
        y3=[S[1],S[3],YP]
        ax.plot(x3,y3, color=clr)
        x4=[S[4],S[6],XP]
        y4=[S[5],S[7],YP]
        ax.plot(x4,y4, color=clr)
        self.canvas.draw()
#    def zapis(self)
        plik=open('wynikiproj1.txt',"a") 
        plik.write("\n|  {:^17} |  {:^16} |\n".format('XP[m]', 'YP[m]'))
#        XP=XP                         
#        YP=YP      
        o1="{:.3f}".format(XP)
        p1="{:.3f}".format(YP)
        plik.write('|{:^20}|{:^20}|'.format(o1,p1)+'\n')     
        if t1<=1 and t1>=0 and t2<=1 and t2>=0:
           # (self.y_5Edit.text(nn))
            plik.write("Punkt należy do odcinków")
        elif t1<=1 and t1>=0 or t2<=1 and t2>=0:
            plik.write("Punkt leży na przedłużeniu jednego z odcinków")
        else:
            plik.write("Punkt leży na przedłużeniu obu odcinków")
        plik.close()
    def clrChooseF(self):
         color=QColorDialog.getColor()
         if color.isValid():
             self.handleButton(color.name())
        
    

if __name__ == '__main__':
    if not QApplication.instance():
        app=QApplication(sys.argv)
    else:
        app=QApplication.instance()
    
    window = Window()
    window.show()
    sys.exit(app.exec_())
    