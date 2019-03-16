class Main():
	"""class de logic de circuit"""
	def AND(self, a, b):#              android
		if a + b == 2:
			return True
		else:
			return False

	def OR(self,a,b):#               ordroid
		if a + b >= 1:
			return True
		else:
			return False

	def XOR(self,a,b):#           	  xordroid
	  if a + b == 1:
	    return True
	  else:
	    return False

	def NOR(self,a,b):#              nordroid
	  return not(self.OR(a,b))

	def NAND(self,a,b):#						  nandroid
	  return not(self.AND(a,b))

	def XNOR(self,a,b):#             xnordroid
	  return not(self.XOR(a,b))
