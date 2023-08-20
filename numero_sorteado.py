import random

def main():
    n1 = random.randint(1, 100)
    tentativas = 0

    while True:
        text = int(input('Digite um número: '))

        if text == n1:
            tentativas += 1
            print('Parabéns, você acertou em, {} tentativas.'.format(tentativas))
            break
        elif text > n1:
            print('Seu numero esta MENOR que o numero Sorteado')
        else:
            print('Seu numero esta MAIOR que o numero Sorteado')
            tentativas += 1

if __name__ == "__main__":
    main()
