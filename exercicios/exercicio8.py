def multiplicacao(*args):
  total = 1
  for val in args:
    total *= val

  return total  

mult = multiplicacao(1, 2, 8, 8)    
print(mult)
print(1*2*8*8)

def impar_ou_par(num):
  if(num % 2 == 0):
    return print("Par")
  
  return print("Impar") 

um = impar_ou_par(1)
dois = impar_ou_par(2)

