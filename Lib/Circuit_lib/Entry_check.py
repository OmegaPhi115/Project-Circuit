class Main():
	"""Regarde si les entrées sont valides sinon erreur: OperationError"""
	class OperationError(Exception):
		"""Erreur D'entrée d'operation logique"""
		def __init__(self, wrong_operation):
			print("Erreur D'entrée d'operation logique")
			print(str(wrong_operation) + " n'est pas une entrée correcte")
	
	class ValueError(Exception):
		"""Erreur D'entrée d'operation logique"""
		def __init__(self, wrong_operation):
			print("Erreur D'entrée d'operation logique")
			print(str(wrong_operation) + " n'est pas une entrée correcte, doit etre True ou False")

	def operation(self, op):
		if op != "or" or "and" or "xor" or "nor" or "nand" or "nxor":
			raise self.OperationError(op)

	def entry(self, a):
		#entrées
		if a != True or False:
			raise self.ValueError(a)