class Main():
	"""Regarde si les entrées sont valides sinon erreur: OperationError"""
	class OperationError(Exception):
		"""Erreur D'entrée d'operation logique"""
		def __init__(self, wrong_operation):
			print("Erreur D'entrée d'operation logique")
			print("")
			if wrong_operation != "Operation Variable not set":
				print(str(wrong_operation) + " n'est pas une entrée correcte")
			else:
				print("La variable d'operation n'est pas initialisée")

	def operation(self, op):
		#print("uhliuhouihmo!" + op)
		if op != "or" and op != "and" and op != "xor" and op != "nor" and op != "nand" and op != "xnor":
			if op == "init":
				op = "Operation Variable Not Set"
			raise self.OperationError(op)
	
	class EntryError(Exception):
		"""Erreur D'entrée d'operation logique"""
		def __init__(self, wrong_operation):
			print("Erreur D'entrée d'operation logique")
			print("")
			print(str(wrong_operation) + " n'est pas une entrée correcte, doit etre 1 ou 0")

	def entry(self, a):
		#entrées
		#print("test")
		#print(a)
	
		a = int(a)
		if a != 1 and a != 0:
			raise self.EntryError(a)
