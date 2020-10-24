#!/usr/bin/env python3


from random import randrange
import unidecode


def menu():
    while True:
        print('-----------------------------')
        print('j - Jogar\ns - Sair\n')
        option = input("Selecione uma opção: ")

        if option == 's':
            break
        elif option == 'j':
            play()
        else:
            continue


def get_secret_word():
    wordlist = []

    with open('resources/wordlist.txt', 'r') as wordsfile:
        for word in wordsfile:
            myword = unidecode.unidecode(word.strip())
            wordlist.append(myword)

    word_index = randrange(1, len(wordlist))
    return wordlist[word_index].upper()


def initialize_hited_letters(secret_word):
    return [ "_" for letter in secret_word ]


def get_hint():
    hint = input("Digite uma letra: ")
    return hint.strip().upper()


def check_hint(secret_word, hint, hited_letters):
    index = 0
    for letter in secret_word:
        if(hint == letter):
            hited_letters[index] = letter
        index += 1


def message_loser(secret_word):
    print("Você foi enforcado!")
    print("A palavra era {}".format(secret_word))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")



def message_winner():
	print("Parabéns, você ganhou!")
	print("       ___________      ")
	print("      '._==_==_=_.'     ")
	print("      .-\\:      /-.    ")
	print("     | (|:.     |) |    ")
	print("      '-|:.     |-'     ")
	print("        \\::.    /      ")
	print("         '::. .'        ")
	print("           ) (          ")
	print("         _.' '._        ")
	print("        '-------'       ")


def draw_gallows(errors):
    print("  _______     ")
    print(" |/      |    ")

    if(errors == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(errors == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(errors == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(errors == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(errors == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(errors == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (errors == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


def play():
    secret_word = get_secret_word()
    hited_letters = initialize_hited_letters(secret_word)

    hanged = False
    hited = False
    errors = 0

    while(not hanged and not hited):
        hint = get_hint()

        if hint.isalpha() and len(hint) == 1:
            if(hint in secret_word):
                check_hint(secret_word, hint, hited_letters)
            else:
                errors += 1
                draw_gallows(errors)
        else:
            continue

        hanged = errors == 7
        hited = "_" not in hited_letters
        print(hited_letters, '\n')

    if(hited):
        message_winner()
    else:
        message_loser(secret_word)


if __name__ == '__main__':
    menu()

