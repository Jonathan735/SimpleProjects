import random
import string

letras = string.ascii_letters
numeros = string.digits
pontuações = string.punctuation
combinação = letras + numeros + pontuações

def random_senha(tamanho):
    senha = ""
    senha += random.choice(string.ascii_lowercase)
    senha += random.choice(string.ascii_uppercase)
    senha += random.choice(string.digits)
    senha += random.choice(string.punctuation)

    for i in range(tamanho-4):
        senha += random.choice(combinação)
    return senha


senha_len = int(input('quantos digitos quer que tenha a senha?\n'))
print ("primeira senha:", random_senha(senha_len))
print ("segunda senha:", random_senha(senha_len))
print ("terceira senha:", random_senha(senha_len))

