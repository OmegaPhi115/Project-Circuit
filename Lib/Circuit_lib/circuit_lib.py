#------------------------------------------------------
# V 0.7.1
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

import Logic as Logic
import Entry_check as entry_check

class circuit():
	"""class du circuit a l'écran"""

	def __init__(self):
		#declaration variable
		self.operation = "Operation Variable not set"

	def logic(self, a, b, opera = "null"):
		#on regarde si les entreées sont bonnes
		if opera == "null" or "":
			opera = self.operation
		else:
			self.operation = opera

		mod_entry_check = entry_check.Main()## je suis main()
		mod_entry_check.operation(opera)
		mod_entry_check.entry(a)
		mod_entry_check.entry(b)

		module_logic = Logic.Main()
		#quelle est l'operation ? la faire et la metre dans outpu
		if opera == "and":
			outpu = module_logic.AND(a,b)
		elif opera == "or":
			outpu = module_logic.OR(a,b)
		elif opera == "xor":
			outpu = module_logic.XOR(a,b)
		elif opera == "nand":
			outpu = module_logic.NAND(a,b)
		elif opera == "nor":
			outpu = module_logic.NOR(a,b)
		elif opera == "xnor":
			outpu = module_logic.XNOR(a,b)
		else:
			outpu = "impossible"

		#on rend outpu
		self.output = outpu
		return outpu

def test():
	test = circuit()
	print(test.logic(input("a"), input("b"), input("")))
