#------------------------------------------------------
# V 0.6.1
# Description: Objet des circuit logiques a l'ecran
#------------------------------------------------------
#plan:
#
#circuit ()
#|
#|-> Logic()
#|   toute les operations logiques
#|
#|-> entry_check()
#|   Regarde si les entrées sont valide sinon erreur: OperationError
#|   |
#|   |-> OperationError()
#| 	 |		Erreur D'entrée d'operation logique
#
#-------------------------------------------------------

class circuit():
	"""class du circuit a lecran"""

		#debut entry_check
		class entry_check():
			"""Regarde si les entrées sont valide sinon erreur: OperationError"""
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


	def __init__(self):
		#declaration variable
		self.operation = "init"
		self.entry_a = "init"
		self.entry_b = "init"
		self.output = "init"
		self.logic_mod = logic()
	
	def value_refresh(self, a, b:
		self.entry_a = a
		self.entry_b = b
		self.output = o
	
	def configure(self, operation = "null"):
		if operation != "null":
			self.operation = operation
