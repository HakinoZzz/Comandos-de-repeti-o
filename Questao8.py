import random

secret_number = random.randint(1, 100)
attempts = 0
guessed = False

print("Tente adivinhar o número secreto entre 1 e 100.\n")

while not guessed:
    try:
        user_guess = int(input("Digite seu palpite: "))
        
        if user_guess < 1 or user_guess > 100:
            print("Digite um número entre 1 e 100.\n")
            continue
        
        attempts += 1
        
        if user_guess == secret_number:
            guessed = True
            print(f"\nParabéns! Você acertou o número {secret_number}!")
            print(f"Total de tentativas: {attempts}")
            
            # Performance message
            if attempts <= 5:
                print("Desempenho: Excelente!")
            elif attempts <= 10:
                print("Desempenho: Bom!")
            else:
                print("Desempenho: Tente melhorar!")
        
        elif user_guess < secret_number:
            print(f"O número secreto é MAIOR que {user_guess}.\n")
        
        else:
            print(f"O número secreto é MENOR que {user_guess}.\n")
    
    except ValueError:
        print("Entrada inválida! Digite um número inteiro.\n")

input("Pressione Enter para sair...")
