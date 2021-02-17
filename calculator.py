from tkinter import *
def btnclick(number):
    global operator
    operator=operator+str(number)
    text_Input.set(operator)

def btnClearDisplay():
    global operator
    operator=" "
    text_Input.set(" ")

def equal():
    global operator
    s=str(eval(operator))
    text_Input.set(s)
    operator=s

def delete():
    length=len(txtDisplay.get())
    txtDisplay.delete(length-1,'end')
    
cal=Tk()
cal.title("Casio Calculator")
operator=" "
text_Input=StringVar()
txtDisplay=Entry(cal,font=("arial",20,"bold"),textvariable=text_Input,\
                 insertwidth=4,bg="powder blue",justify="right",bd=30)
txtDisplay.grid(columnspan=4)

btn7=Button(cal,padx=16,bd=8,fg="red",font=("arial",20,"bold"),text="7",command=lambda:btnclick(7))
btn7.grid(row=1,column=0)
btn8=Button(cal,padx=16,bd=8,fg="red",font=("arial",20,"bold"),text="8",command=lambda:btnclick(8))
btn8.grid(row=1,column=1)
btn9=Button(cal,padx=16,bd=8,fg="red",font=("arial",20,"bold"),text="9",command=lambda:btnclick(9))
btn9.grid(row=1,column=2)
add=Button(cal,padx=16,bd=8,fg="red",font=("arial",20,"bold"),text="+",command=lambda:btnclick("+"))
add.grid(row=1,column=3)

btn4=Button(cal,padx=16,bd=8,fg="red",font=("arial",20,"bold"),text="4",command=lambda:btnclick(4))
btn4.grid(row=2,column=0)
btn5=Button(cal,padx=16,bd=8,fg="red",font=("arial",20,"bold"),text="5",command=lambda:btnclick(5))
btn5.grid(row=2,column=1)
btn6=Button(cal,padx=16,bd=8,fg="red",font=("arial",20,"bold"),text="6",command=lambda:btnclick(6))
btn6.grid(row=2,column=2)
sub=Button(cal,padx=16,bd=8,fg="red",font=("arial",20,"bold"),text="-",command=lambda:btnclick("-"))
sub.grid(row=2,column=3)

btn1=Button(cal,padx=16,bd=8,fg="red",font=("arial",20,"bold"),text="1",command=lambda:btnclick(1))
btn1.grid(row=3,column=0)
btn2=Button(cal,padx=16,bd=8,fg="red",font=("arial",20,"bold"),text="2",command=lambda:btnclick(2))
btn2.grid(row=3,column=1)
btn3=Button(cal,padx=16,bd=8,fg="red",font=("arial",20,"bold"),text="3",command=lambda:btnclick(3))
btn3.grid(row=3,column=2)
mul=Button(cal,padx=16,bd=8,fg="red",font=("arial",20,"bold"),text="*",command=lambda:btnclick("*"))
mul.grid(row=3,column=3)

clear=Button(cal,padx=16,bd=8,fg="red",font=("arial",20,"bold"),text="C",command=btnClearDisplay)
clear.grid(row=4,column=0)
btn0=Button(cal,padx=16,bd=8,fg="red",font=("arial",20,"bold"),text="0",command=lambda:btnclick(0))
btn0.grid(row=4,column=1)
equal=Button(cal,padx=16,bd=8,fg="red",font=("arial",20,"bold"),text="=",command=equal)
equal.grid(row=4,column=2)
div=Button(cal,padx=16,bd=8,fg="red",font=("arial",20,"bold"),text="/",command=lambda:btnclick("/"))
div.grid(row=4,column=3)

delete=Button(cal,padx=16,bd=8,fg="red",font=("arial",20,"bold"),text="del",command=delete)
delete.grid(row=5,column=0)
point=Button(cal,padx=16,bd=8,fg="red",font=("arial",20,"bold"),text=".",command=lambda:btnclick("."))
point.grid(row=5,column=1)

cal.mainloop()
