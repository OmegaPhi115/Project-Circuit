"""---------------------------------------------------------------------------
 V 0.7.1
 Description: Objet des circuit logiques a l'ecran
---------------------------------------------------------------------------
plan:

circuit ()
|
|-> Logic()
|   toute les operations logiques
|
|-> entry_check()
|   Regarde si les entrées sont valide sinon erreur: OperationError
|   |
|   |-> OperationError()
| 	 |		Erreur D'entrée d'operation logique

----------------------------------------------------------------------------
"""

import Logic as Logic
import Entry_check as entry_check

class main():
	"""class du circuit a l'écran"""



def test():
	test = circuit()
	print(test.logic(input("a"), input("b"), input("")))