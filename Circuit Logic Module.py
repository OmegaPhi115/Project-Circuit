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

def test(a,b):
  print("OR = " + str(OR(a,b)))
  print("AND = " + str(AND(a,b)))
  print("XOR = " + str(XOR(a,b)))
  print("NOR = " + str(NOR(a,b)))
  print("NAND = " + str(NAND(a,b)))
  print("XNOR = " + str(XNOR(a,b)))

def test():
	while 1:
		print("a = 0, b = 0")
		a = 0
		b = 0
		test(a,b)
		a = input("")
		print("a = 1, b = 0")
		a = 1
		b = 0
		test(a,b)
		a = input("")
		print("a = 0, b = 1")
		a = 0
		b = 1
		test(a,b)
		a = input("")
		print("a = 1, b = 1")
		a = 1
		b = 1
		test(a,b)
		a = input("")
