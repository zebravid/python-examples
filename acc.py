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
	"""Example of inheritance
	and class variable and doc string"""
	type="checking"
	def __init__(self,filepath,fee):
		Acco.__init__(self,filepath)
		self.fee=fee
	
	def transfer(self,amount):
		self.balance=self.balance-amount- self.fee
		self.commit()
		
		
chec=Checking("bal.txt",1)

print(chec.balance)
chec.withdrow(100)
chec.transfer(15)
print(chec.balance)