import requests
import httplib
import re
import data_breach
i=1
def patch_send():
    old_send= httplib.HTTPConnection.send
    print(i)
    def new_send( self, data ):
        global i
        if i==1:
            
            
            print(data)
            t = data.find('GET')
            t=t+4
            s = data[t:].find('HTTP')
            xx = data[t:t+s-1]
            evaluate.pred(xx)
        i+=1
        
        return old_send(self, data) #return is not necessary, but never hurts, in case the library is changed
    httplib.HTTPConnection.send= new_send

from Tkinter import *

def OnClick():
    url = entry.get()
    print(url)
    
    #url = raw_input("enter url")
    data_breach.aaaa(url)
	
root = Tk()
root.geometry('500x130+100+100')
root.attributes('-topmost', True)
label = Label(root,text='Enter text here')
label.pack(fill=BOTH,pady=5)
entry = Entry(root,width=50)
entry.pack(pady=10)
button = Button(root, text="Submit", command=OnClick)
button.pack(pady=10)
root.mainloop()
