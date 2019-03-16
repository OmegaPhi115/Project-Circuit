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

import Circuit_lib.Logic as Logic
import Circuit_lib.Entry_check as entry_check

class circuit():
	"""class du circuit a lecran"""
	#debut entry_check

		#fin entry_check

	def logic(opera, a, b):
		#on regarde si les entreées sont bonnes
		mod_entry_check = entry_check()
		opera = mod_entry_check.operation(opera)
		a = mod_entry_check.entry(a)
		b = mod_entry_check.entry(b)

		#quelle est l'operation ? la faire et la metre dans outpu

		#on rend outpu
		#return outpu


	def __init__(self):
		#declaration variable
		self.operation = "init"
		self.entry_a = "init"
		self.entry_b = "init"
		self.output = "init"
		self.logic_mod = Logic()

	def value_refresh(self, a, b):
		self.entry_a = a
		self.entry_b = b
		#self.output = o

	def configure(self, operation = "null"):
		if operation != "null":
			self.operation = operation

test = circuit()