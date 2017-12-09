from Tkinter import *
import cap
def OnClick():
	url = entry.get()
	cap.aaaa(url)
	print(url)
	
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
