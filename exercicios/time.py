#Pacote Time
import time
'''
print("Começei agora...")
time.sleep(3)
print("Terminei")

agora =time.localtime()
print(agora)
print(type(agora))
'''
agora=time.localtime()

print(time.strftime("%d/%m/%y , %H:%M>%S",agora))

