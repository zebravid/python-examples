class Acco:
	def __init__(self,filename):
		with open(filename,"r") as file:
			self.balance=int(file.read())
	
	def withdrow(self,amount):
		self.balance=self.balance-amount
	def deposit(self,amount):
		self.balance=self.balance+amount
account=Acco("bal.txt")

print(account.balance)
account.withdrow(100)
print(account.balance)
