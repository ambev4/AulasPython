import importlib
# (Singleton)
import aula156_m # Se tentar importar lib de novo com import, o python irá ignorar. É só um no código.

print(aula156_m.variavel)

for i in range(10):
    importlib.reload(aula156_m) # Reload no import do módulo, mais útil dentro do console do python
    print(i)

print('Fim')