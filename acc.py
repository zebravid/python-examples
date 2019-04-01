class Acco:
	def __init__(self,filename):
		self.filepath=filename
		with open(filename,"r") as file:
			self.balance=int(file.read())
	
	def withdrow(self,amount):
		self.balance=self.balance-amount
		self.commit()
	def deposit(self,amount):
		self.balance=self.balance+amount
		self.commit()
	def commit(self):
		with open(self.filepath,'w') as file:
			file.write(str(self.balance))
class Checking(Acco):
	def __init__(self,filepath):
		Acco.__init__(self,filepath)
		
		
chec=Checking("bal.txt")

print(chec.balance)
chec.withdrow(100)
print(chec.balance)
