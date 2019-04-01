
from tkinter import *
from backendOP import Book
#selectedTuple self.selectedTuple
class FrontView:
	
	def viewAll(self):
		self.list1.delete(0,END)
		for row in bookdb.view():
			self.list1.insert(END,row)
	def searchDb(self):
		self.list1.delete(0,END)
		for row in bookdb.search(self._title.get(),self._author.get(),self._year.get(),self._imdb.get()):
			self.list1.insert(END,row)
	def addEn(self):
		bookdb.insert(self._title.get(),self._author.get(),self._year.get(),self._imdb.get())	
		self.list1.delete(0,END)
		self.list1.insert(END,(self._title.get(),self._author.get(),self._year.get(),self._imdb.get()))	
	def getSel(self,event):
		global selectedTuple
		index=self.list1.curselection()[0]
		selectedTuple=self.list1.get(index)
		self.e0.delete(0,END)
		self.e0.insert(END,selectedTuple[1])
		self.e1.delete(0,END)
		self.e1.insert(END,selectedTuple[2])
		self.e2.delete(0,END)
		self.e2.insert(END,selectedTuple[3])
		self.e3.delete(0,END)
		self.e3.insert(END,selectedTuple[4])
			
	def delFun(self):
		bookdb.delete(selectedTuple[0])
		
	def updFun(self):
		bookdb.update(selectedTuple[0],self._title.get(),self._author.get(),self_year.get(),self._imdb.get())
	
	
	def __init__(self,window):	
		
		mystr=StringVar()
		self.window=window
		self.window.wm_title("Booook")
		self.b1=Button(self.window,text="ViewA",command=self.viewAll)
		self.b1.grid(row=0,column=6,rowspan=1)
		
		self._title=StringVar()
		self._author=StringVar()
		self._year=StringVar()
		self._imdb=StringVar()
		self.b2=Button(self.window,text="SearC",command=self.searchDb)
		self.b2.grid(row=1,column=6,rowspan=1)
		
		self.b3=Button(self.window,text="AddEn",command=self.addEn)
		self.b3.grid(row=2,column=6,rowspan=1)
		
		self.b4=Button(self.window,text="Delet",command=self.delFun)
		self.b4.grid(row=3,column=6,rowspan=1)
		
		
		self.b5=Button(self.window,text="Updat",command=self.updFun)
		self.b5.grid(row=4,column=6,rowspan=1)
		
		self.b6=Button(self.window,text="quirt",command=window.destroy)
		self.b6.grid(row=5,column=6,rowspan=1)
		
		
		self.e0=Entry(self.window,text="Ex",textvariable=self._title)
		self.e0.grid(row=0,column=0,rowspan=1)
		
		
		self.e1=Entry(self.window,text="Ex",textvariable=self._author)
		self.e1.grid(row=1,column=0,rowspan=1)
		
		self.e2=Entry(self.window,text="Ex",textvariable=self._year)
		self.e2.grid(row=2,column=0,rowspan=1)
		
		
		self.e3=Entry(self.window,text="Ex",textvariable=self._imdb)
		self.e3.grid(row=3,column=0,rowspan=1)
		
		
		self.list1=Listbox(self.window,height=6,width=35)
		self.list1.grid(row=4,column=0,rowspan=4,columnspan=4)
		
		self.sb1=Scrollbar(self.window)
		
		self.sb1.grid(row=4,column=4,rowspan=4)
		self.list1.configure(yscrollcommand=self.sb1.set)
		self.sb1.configure(command=self.list1.yview)
		self.list1.bind('<<ListboxSelect>>',self.getSel)
		
	
window=Tk()
view=FrontView(window)
bookdb=Book("book.db")
window.mainloop()