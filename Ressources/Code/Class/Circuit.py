from Ressources.Code.Fonctions.LineMaker import LineMaker
from Ressources.Code.Class.Widget import Widget


class Circuit(Widget):
    """
    Class finale de circuit
    """

    def __init__(self, fen, x, y):
        Widget.__init__(self, x, y,fen)
        self.operation = "No Operation"
        self.image = "No Image"
        self.output = 0

        self.graphical_input_a = [self.x - 20, self.y]
        self.graphical_input_b = [self.x + 20, self.y]

        self.graphical_output = [self.x, self.y]

    class Circuit_Entry_Checker:
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
            # print("uhliuhouihmo!" + op)
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
            # entrées
            # print("test")
            # print(a)

            a = int(a)
            if a != 1 and a != 0:
                raise self.EntryError(a)

    class Circuit_Logic_operateur:
        """class de logic de circuit"""

        def AND(self, a, b):  # android
            if a + b == 2:
                return True
            else:
                return False

        def OR(self, a, b):  # ordroid
            if a + b >= 1:
                return True
            else:
                return False

        def XOR(self, a, b):  # xordroid
            if a + b == 1:
                return True
            else:
                return False

        def NOR(self, a, b):  # nordroid
            return not (self.OR(a, b))

        def NAND(self, a, b):  # nandroid
            return not (self.AND(a, b))

        def XNOR(self, a, b):  # xnordroid
            return not (self.XOR(a, b))

    def logic(self, a, b):
        """s'ocupe d'effectuer le calcule"""
        # on regarde si les entrées sont bonnes
        opera = self.operation

        mod_entry_check = self.Circuit_Entry_Checker()  # je suis main()
        mod_entry_check.operation(opera)
        mod_entry_check.entry(a)
        mod_entry_check.entry(b)

        module_logic = self.Circuit_Logic_operateur()

        # quelle est l'operation ? la faire et la metre dans outpu
        outpu = 0
        if opera == "and":
            outpu = module_logic.AND(a, b)
        elif opera == "or":
            outpu = module_logic.OR(a, b)
        elif opera == "xor":
            outpu = module_logic.XOR(a, b)
        elif opera == "nand":
            outpu = module_logic.NAND(a, b)
        elif opera == "nor":
            outpu = module_logic.NOR(a, b)
        elif opera == "xnor":
            outpu = module_logic.XNOR(a, b)

        if outpu:
            outpu = 1
        else:
            outpu = 0

        # on rend outpu
        self.output = outpu

    def deplacer(self, x, y):
        """change les coordonées"""
        self.x = int(x)
        self.y = int(y)
        self.placer()

    def changer_operation(self, ope):
        """change l'operation par entré"""
        self.operation = ope
        self.changer_image()

    def changer_image(self):
        """Change l'image en raport avec l'operation"""
        # todo change image operation
        if self.operation == "or":
            self.image = pygame.image.load(img_circuit_OR).convert_alpha()
        if self.operation == "nor":
            self.image = pygame.image.load(img_circuit_NOR).convert_alpha()
        if self.operation == "and":
            self.image = pygame.image.load(img_circuit_AND).convert_alpha()
        if self.operation == "nand":
            self.image = pygame.image.load(img_circuit_NAND).convert_alpha()
        if self.operation == "xor":
            self.image = pygame.image.load(img_circuit_XOR).convert_alpha()
        if self.operation == "xnor":
            self.image = pygame.image.load(img_circuit_XNOR).convert_alpha()

        self.Get_image_size()


    def placer(self):
        """Placer sur la surface"""
        xy_coord = (self.x, self.y)
        self.fen.blit(self.image, xy_coord)

    def update(self):
        """actualisation"""
        self.placer()

    def line_tracer(self, destination_location):
        if self.output == 0:
            colo = couleur_off
        else:
            colo = couleur_on
        LineMaker(self.fen, self.graphical_output[0], self.graphical_output[1], destination_location[0],
                  destination_location[
            1], colo, 2)