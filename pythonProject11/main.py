from tkinter import *
from tkinter.messagebox import *
font=('serif',22,'bold')

#important functions
def clear():
    ex=textfield.get()
    ex=ex[0:len(ex)-1]
    textfield.delete(0,END)
    textfield.insert(0,ex)

def all_clear():
    textfield.delete(0,END)

def click_button(event):
    print("button clicked")
    b=event.widget
    text=b['text']
    print(text)

    if text=='x':
        textfield.insert(END,"*")
        return

    if text=='=':
        try:
            ex=textfield.get()
            answer=eval(ex)
            textfield.delete(0,END)
            textfield.insert(0,answer)
        except Exception as e:
            print("error...",e)
            showerror("Error",e)
        return
    textfield.insert(END,text)

window=Tk()
window.title("my calculator")
window.geometry('500x450')
'''headingLabel=Label(window,text="my calculator")
#heading label
headingLabel.pack(side=TOP)'''
heading=Label(window,text="my calculator",font=font)
heading.pack(side=TOP)
#text field
textfield=Entry(window,font=font,justify=CENTER)
textfield.pack(side=TOP,pady=15,fill=X,padx=20)
#buttons
buttonframe=Frame(window)
buttonframe.pack(side=TOP,padx=10)
#adding buttons
'''button1=Button(buttonframe,text="1",font=font)
button1.grid(row=0,column=0)
button2=Button(buttonframe,text="2",font=font)
button2.grid(row=0,column=1)'''
temp=1
for i in range(0,3):
    for j in range(0,3):
        button=Button(buttonframe,text=str(temp),font=font,width=5,relief="ridge",activebackground="orange",activeforeground="white")
        button.grid(row=i,column=j,padx=3,pady=3)
        temp+=1
        button.bind("<Button-1>",click_button)
Zerobutton=Button(buttonframe,text="0",font=font,width=5,relief="ridge",activebackground="orange",activeforeground="white")
Zerobutton.grid(row=3,column=0,padx=3,pady=3)

dotbutton=Button(buttonframe,text=".",font=font,width=5,relief="ridge",activebackground="orange",activeforeground="white")
dotbutton.grid(row=3,column=1,padx=3,pady=3)

equalbutton=Button(buttonframe,text="=",font=font,width=5,relief="ridge",activebackground="orange",activeforeground="white")
equalbutton.grid(row=3,column=2,padx=3,pady=3)

plusbutton=Button(buttonframe,text="+",font=font,width=5,relief="ridge",activebackground="orange",activeforeground="white")
plusbutton.grid(row=0,column=3,padx=3,pady=3)

minusbutton=Button(buttonframe,text="-",font=font,width=5,relief="ridge",activebackground="orange",activeforeground="white")
minusbutton.grid(row=1,column=3,padx=3,pady=3)

multbutton=Button(buttonframe,text="x",font=font,width=5,relief="ridge",activebackground="orange",activeforeground="white")
multbutton.grid(row=2,column=3,padx=3,pady=3)

devidebutton=Button(buttonframe,text="/",font=font,width=5,relief="ridge",activebackground="orange",activeforeground="white")
devidebutton.grid(row=3,column=3,padx=3,pady=3)

clearbutton=Button(buttonframe,text="C",font=font,width=11,relief="ridge",activebackground="orange",activeforeground="white",command=clear)
clearbutton.grid(row=4,column=0,padx=3,pady=3,columnspan=2)

allclearbutton=Button(buttonframe,text="AC",font=font,width=11,relief="ridge",activebackground="orange",activeforeground="white",command=all_clear)
allclearbutton.grid(row=4,column=2,padx=3,pady=3,columnspan=2)


#binding all buttons
plusbutton.bind("<Button-1>",click_button)
minusbutton.bind("<Button-1>",click_button)
multbutton.bind("<Button-1>",click_button)
devidebutton.bind("<Button-1>",click_button)
Zerobutton.bind("<Button-1>",click_button)
dotbutton.bind("<Button-1>",click_button)
equalbutton.bind("<Button-1>",click_button)

window.mainloop()