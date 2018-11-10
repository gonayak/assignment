class Emplyee(object):

	def __init__(self,firstname,lastname,payrate,vcation):
		self.fisrt_name=firstname
		self.last_name=lastname
		self.payrate=payrate
		self.vacation=vcation

	def get_name(self):
		print self.fisrt_name,self.last_name

	def get_pay_rate (self):
		print self.payrate

	def get_yearly_vacation(self):
		print self.vacation

class Contractor(object):
	def __init__(self,firstname,lastname,payrate,AgencyName,vcation=0 ):
		self.fisrt_name=firstname
		self.last_name=lastname
		self.pay_rate=payrate
		self.vacation=vcation
		self.agency_name=AgencyName

	def get_name(self):
		print self.fisrt_name,self.last_name +  "[ C ]"
	def get_pay_rate(self):
		print self.pay_rate
	def get_yearly_vacation(self):
		print self.vacation
	def get_agency(self):
		print self.agency_name



class Temporary(object):
	def __init__(self,firstname,lastname,payrate,AgencyName,vcation=0 ):
		self.fisrt_name=firstname
		self.last_name=lastname
		self.pay_rate=payrate
		self.vacation=vcation
		self.agency_name=AgencyName

	def get_name(self):
		print self.fisrt_name,self.last_name+  "[ T ]"
	def get_pay_rate (self):
		print self.pay_rate
	def get_yearly_vacation(self):
		print self.vacation
	def get_agency(self):
		print self.agency_name

emp = Contractor('gowri','nayak','5','20')
emp.get_name()
emp.get_pay_rate()
emp.get_yearly_vacation()