linhas =str('===')
print('{:=^18}'.format(linhas))
n1 = int(input('digite o número:'))
aux = 0  
print('=' * 18)  
while(aux <= 10):  
  print('{0} X {1} = {2}'.format(aux, n1, (aux * n1)))  
  aux = aux + 1
