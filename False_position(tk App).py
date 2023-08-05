from tkinter import *
def f2(x):
    return a*x**2+b*x+c
def f3(x):
    return a*x**3+b*x**2+c*x+d
ans=""
index=1
nn=0
a=0
b=0
c=0
d=0
num=0
A=0
B=0
window=Tk()
window.title("False Position")
window.geometry("800x700")

def delete_page1():
    l1.destroy()
    btn1.destroy()
    lmyname.destroy()
    l2.pack()
    e1.pack()
    btn2.pack()
def com1():
    global nn
    n=e1.get()
    if int(n)==2:
        nn=2
        l4.pack()
        a2_.pack()
        a2.pack()
        b2_.pack()
        b2.pack()
        c2_.pack()
        c2.pack()
        btn3.pack()
    if int(n)==3:
        nn=3
        l3.pack()
        a3_.pack()
        a3.pack()
        b3_.pack()
        b3.pack()
        c3_.pack()
        c3.pack()
        d3_.pack()
        d3.pack()
        btn3.pack()
def com2():
    global nn,a,b,c,d
    if nn==2:
        a=int(a2.get())
        b=int(b2.get())
        c=int(c2.get())
        l5.pack()
        e5.pack()
        l6.pack()
        e6.pack()
        btn4.pack()
    if nn==3:
        a=int(a3.get())
        b=int(b3.get())
        c=int(c3.get())
        d=int(d3.get())
        l5.pack()
        e5.pack()
        l6.pack()
        e6.pack()
        btn4.pack()
def com3():
    global A,B
    A=float(e5.get())
    B=float(e6.get())
    e7.pack()
    btn5.pack()
def com4():
    global num
    num=int(e7.get())
    l2.destroy()
    e1.destroy()
    btn2.destroy()
    if nn==3:
        l3.destroy()
        a3_.destroy()
        a3.destroy()
        b3_.destroy()
        b3.destroy()
        c3_.destroy()
        c3.destroy()
        d3_.destroy()
        d3.destroy()
    if nn==2:
        l4.destroy()
        a2_.destroy()
        a2.destroy()
        b2_.destroy()
        b2.destroy()
        c2_.destroy()
        c2.destroy()
    btn3.destroy()
    l5.destroy()
    e5.destroy()
    l6.destroy()
    e6.destroy()
    btn4.destroy()
    e7.destroy()
    btn5.destroy()
    btn6.pack()
def com5():
    global A,B,ans,index
    if nn==2:
        for _ in range(num):    
            C=A-(B-A)*f2(A)/(f2(B)-f2(A))
            ans = ans + '\n' +str("{:>2d} :".format(index)) + str("{:.10f}".format(C))
            index+=1
            if f2(A)*f2(C) < 0:
                B=C
            if f2(C)*f2(B) < 0:
                A=C        
    if nn==3:
        for _ in range(num):    
            C=A-(B-A)*f3(A)/(f3(B)-f3(A))
            ans = ans + '\n' +str("{:>2d} :".format(index)) + str("{:.10f}".format(C))
            index+=1
            if f3(A)*f3(C) < 0:
                B=C
            if f3(C)*f3(B) < 0:
                A=C 
    l7.config(text=ans)
    l7.pack()
    btn7.pack() 
           
#/////////////// page 1  //////////////////////

l1=Label(text="\n Calculating the root based on the displacement method for polynomial functions \nHow the formula works: at each step, we calculate the root \nwith the intersection of the connecting line\n between the start and end points of the interval\n\ny- f(a) = (x-a)[f(a)-f(b)]/(a-b)\n\ny=0 => x_new = a - f(a)(b-a)/[f(b)-f (a)]\n",font=(30),bg="pink")
l1.pack()
btn1=Button(text="  Continue  ",font=(30),bg="purple",fg="white",bd=5,command=delete_page1)
btn1.pack()
lmyname=Label(text="\n\n\n\n\n\n\n\n\n\n\nErfan Golshan\nspring 2023",font=(1))
lmyname.pack()

#//////////////// page 2 //////////////////////

l2=Label(text="Degree of polynomial function\n(choose degree 2 or 3)",font=(30),bg="pink")
e1=Entry()
btn2=Button(text="Set coefficients",font=(30),bg="purple",fg="white",bd=5,command=com1)
l3=Label(text="\na x3 + b x2 + c x +d = 0\n",font=(30))
a3_=Label(text="a :",font=(30))
a3=Entry()
b3_=Label(text="b :",font=(30))
b3=Entry()
c3_=Label(text="c :",font=(30))
c3=Entry()
d3_=Label(text="d :",font=(30))
d3=Entry()
l4=Label(text="\na x2 + b x + c = 0\n",font=(30))
a2_=Label(text="a :",font=(30))
a2=Entry()
b2_=Label(text="b :",font=(30))
b2=Entry()
c2_=Label(text="c :",font=(30))
c2=Entry()
btn3=Button(text="Set interval",command=com2,font=(30),bg="purple",fg="white",bd=5)
l5=Label(text="Start point",font=(30))
e5=Entry()
l6=Label(text="End point",font=(30))
e6=Entry()
btn4=Button(text="Number of iterations",command=com3,font=(30),bg="purple",fg="white",bd=5)
e7=Entry()
btn5=Button(text= "   Calculate  "  ,command=com4,font=(20),bg="red",fg="white",bd=5)

#///////////////// page 3 ///////////////////////

btn6=Button(text="See results",command=com5,bg="purple",fg="white",bd=5,font=(30))
l7=Label(text=ans,font=(30))
btn7=Button(text="Quit",command=window.destroy,font=(30),bg="red",fg="white",bd=5)

################################################
window.mainloop()