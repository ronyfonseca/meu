linhas =str('===')
print('{:=^18}'.format(linhas))
n1 = int(input('digite o número:'))
aux = 0  
print('=' * 18)  
while(aux <= 10):  
  print('{0} X {1} = {2}'.format(aux, n1, (aux * n1)))  
  aux = aux + 1

  import os 
from pytube import YouTube
import sys 
from colorama import init
from colorama import Fore, Back, Style
os.system("clear")
banner = """ 

 ░░░░░░░░░░░░░░░░░░░▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄░░
██░░██░░░░░░░░░░░▄█░░░░░░████░░████████▄
██▄▄██░░░░░░░░░░░████░░██████░░█████████
▀████▀░████░█░░█░████░░█░██░█░▄▄░█░░▄▄██   -   Mass Download   - 
░░██░░░█░░█░█▄▄█░████░░█░░░░█░▀▀░█░░▄▄██   -  Created by Ergo  -  
░░██░░░████░████░▀███▄▄█▄▄▄▄█▄▄▄▄█▄▄▄▄█▀
░░░░░░░░░░░░░░░░░░░▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀░░ v 1.0

"""
print(Fore.RED + banner + Fore.RESET)
help = "Usage: downtube.py file.txt"
if(len(sys.argv) > 1):
  arquivo = sys.argv[1]

else: 
  print(help)
  sys.exit()
try:
  with open(arquivo) as file: 
    for line in file: 
      print("Baixando musica " + Fore.RED + line + Fore.RESET + "...")
      YouTube(line).streams.first().download("/output")
  print("Todas as musicas foram salvas no output/")
except: 
  print("File not found ! :(")
  sys.exit()


