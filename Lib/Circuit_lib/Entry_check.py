class Main():
	"""Regarde si les entrées sont valides sinon erreur: OperationError"""
	class OperationError():
		"""Erreur D'entrée d'operation logique"""
		def __init__(self, wrong_operation):
			print("Erreur D'entrée d'operation logique")
			print(str(wrong_operation) + " n'est pas une entrée correcte")

	def operation(op):
		if op != "or" or "and" or "xor" or "nor" or "nand" or "nxor":
			raise OperationError

	def entry(a):
		#entrées
		pass