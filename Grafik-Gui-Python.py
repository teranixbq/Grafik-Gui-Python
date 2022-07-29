# Author Kodeteks.com
from tkinter import *
import matplotlib.pyplot as plt


bulan = ['JUL 16','AGS 16','SEPT 16','OKT 16','NOV 16','DES 16','JAN 17','FEB 17','MAR 17','APR 17','MEI 17','JUNI 17']
persen = [0,3,4,10,11,3,7,7,7,5,5,1]
perbulan = [97,690,879,2202,2538,678,1509,1545,1561,1133,1121,122]
rata = [4,27,34,85,98,26,58,59,60,44,43,5]



class Menu:
    def __init__(self,master):
        self.master=master
        self.master.title("Tugas Pertemuan 9 IMK")
        self.master.minsize(200,100)

        self.grafik = Label(self.master, text = "Grafik Pengunjung Perpustakaan Sukma", height=2)
        self.grafik.grid(row=0,column=1)

        self.spersen = Button(self.master, text = "Persentase Pengunjung",command=self.persen1)
        self.spersen.grid(row=3,column=0,ipadx=15)
        self.sperbulan = Button(self.master, text = "Jumlah Pengunjung",command=self.perbulan1)
        self.sperbulan.grid(row=3,column=1,ipadx=15)
        self.srata = Button(self.master, text = "Rata-Rata Pengunjung",command=self.rata1)
        self.srata.grid(row=3,column=2,ipadx=15)
        

    def persen1(self):
        plt.figure(num='Tugas IMK Pertemuan 9', figsize=(9,5))
        plt.bar(bulan,persen)
        plt.xlabel("Bulan")
        plt.ylabel("Persentase Pengunjung Perbulan (%)")
        plt.title("Grafik Pengunjung Perpustakaan Sukma")
        plt.show()

    def perbulan1(self):
        plt.figure(num='Tugas IMK Pertemuan 9', figsize=(9,5))
        plt.bar(bulan,perbulan)
        plt.xlabel("Bulan")
        plt.ylabel("Jumlah Pengunjung / Bulan")
        plt.title("Grafik Pengunjung Perpustakaan Sukma")
        plt.show()

    def rata1(self):
        plt.figure(num='Tugas IMK Pertemuan 9', figsize=(9,5))
        plt.bar(bulan,rata)
        plt.xlabel("Bulan")
        plt.ylabel("Rata - Rata Pengunjung Per Bulan")
        plt.title("Grafik Pengunjung Perpustakaan Sukma")
        plt.show()

        
def main():
    root_Menu = Tk()
    root_Menu.resizable(False, False)
    root= Menu(root_Menu)
    root_Menu.mainloop()
    

if __name__ == '__main__':
    main()