class circuit():
	"""class du circuit a lecran"""

	#class de logic de circuit
	class logic():
		def AND(a,b):#              android
			if a + b == 2:
				return True
			else:
				return False

		def OR(a,b):#               ordroid
  		if a + b >= 1:
  	  	return True
		  else:
  		  return False

		def XOR(a,b):#           	  xordroid
		  if a + b == 1:
		    return True
		  else:
		    return False

		def NOR(a,b):#              nordroid
		  return not(OR(a,b))

		def NAND(a,b):#						  nandroid
		  return not(AND(a,b))

		def XNOR(a,b):#             xnordroid
		  return not(XOR(a,b))
		
		#debut entry_check
		class entry_check():
			"""regarde si ca marche sinon erreur"""
			class OperationError():
				"""Erreur D'entrée d'operation logique"""
				def __init__(self, wrong_operation):
					print("Erreur D'entrée d'operation logique")
					print(str(wrong_operation) + " n'est pas une entrée correcte")

			def operation(op):
				if op != "or", "and", "xor", "nor", "nand", "nxor":
					raise OperationError
			
			def entry(a):
				#entrées
				pass
		#fin entry_check

		def logic(opera, a, b):
			#on regarde si les entreées sont bonne
			mod_entry_check = self.entry_check()
			opera = mod_entry_check.operation(opera)
			a = mod_entry_check.entry(a)
			b = mod_entry_check.entry(b)
		
			#quelle est l'operation ? la faire et la metre dans outpu

			#on rend outpu
			return outpu


	def __init__(self, ope):
		#declaration variable
		self.operation = ope
		self.entry_a = "init"
		self.entry_b = "init"
		self.output = "init"
		self.logic_mod = logic()
	
	def value_refresh(self, a, b, o):
		self.entry_a = a
		self.entry_b = b
		self.output = o
	
	def configure(self, operation = "null"):
		if operation != "null":
			self.operation = operation
