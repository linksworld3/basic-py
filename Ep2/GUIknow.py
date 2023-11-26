from tkinter import *
from tkinter import ttk #theme of tk
from tkinter import messagebox


GUI = Tk()
GUI.title('โปรแกรมบันทึกข้อมูล') #ชื่อโปรแกรม
GUI.geometry('500x400') #ขนาดหน้าต่าง

L1=Label(GUI,text='โปรแกรมบันทึกกว่ารู้',font=('Angsana New',30),fg='green')
L1.place(x=30,y=20)
#Button ใช้ในการสร้างปุ่ม  ttk.เป็นtheme สวยงาม
#B1 = ttk.Button(GUI,text='เงินมีอยู่กี่บาท') 
#B1.pack(ipadx=20,ipady=20) #pack ทำให้ปุ่ม B1 อยู่ตรงกลางโปรแกรม
                            #ipadx y ขนาดปุ่ม
#############################################
def Button2():
    text = 'ตอนนี้มีเงินในบัญชี 500 บาท'
    messagebox.showinfo('เงินในบัญชี',text)


FB1= Frame(GUI) #คล้ายกระดาน
FB1.place(x=100,y=100)
B2 = ttk.Button(FB1,text='เงินมีอยู่กี่บาท',command=Button2)  
B2.pack(ipadx=20,ipady=20)
#B2.place(x=50,y=200) #place ใช้วางปุ่มไว้ในพื้นที่ ที่ต้องการ

def Button3():
    text = 'ยุ่ง ไม่บอกหรอก'
    messagebox.showinfo('ตอนนี้กำลัง',text)


FB2= Frame(GUI) #คล้ายกระดาน
FB2.place(x=200,y=100)
B3 = ttk.Button(FB1,text='ตอนนี้ทำอะไร',command=Button3)  
B3.pack(ipadx=20,ipady=20)

#############################################
GUI.mainloop()
