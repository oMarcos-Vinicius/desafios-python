#Calcular o Seno, Cosseno e Tangente
'''
Seno (sen): É a razão entre o comprimento do cateto oposto ao ângulo e o comprimento da hipotenusa. 
A fórmula é: sen(a) = cateto oposto / hipotenusa

Cosseno (cos): É a razão entre o comprimento do cateto adjacente ao ângulo e o comprimento da 
hipotenusa. A fórmula é: cos(a) = cateto adjacente / hipotenusa

Tangente (tan): É a razão entre o comprimento do cateto oposto e o comprimento do cateto adjacente. 
A fórmula é: tan(a) = cateto oposto / cateto adjacente
'''
from math import sin, cos, tan, radians

angulo = float(input("Digite o angula que você deseja: "))

angulo = radians(angulo)

print(f"O angulo de {angulo:.2f} tem o SENO de {sin(angulo):.2f}")
print(f"O angulo de {angulo:.2f} tem o COSSENO de {cos(angulo):.2f}")
print(f"O angulo de {angulo:.2f} tem o TANGENTE de {tan(angulo):.2f}")
