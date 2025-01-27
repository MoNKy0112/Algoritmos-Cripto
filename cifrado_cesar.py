
def cifrar(texto_plano, key, alphabet):
    final_word = ""
    for letter in texto_plano:
        try:
            new_index = (alphabet.index(letter) + key) % len(alphabet)

            final_word += alphabet[new_index]
            # print(alphabet[new_index])
        except Exception as e:
            print("Error")
            print(e)
    return final_word


def descifrar(texto_cifrado, key, alphabet):
    final_word = ""
    for letter in texto_cifrado:
        try:
            new_index = (alphabet.index(letter) - key) % len(alphabet)

            final_word += alphabet[new_index]
            # print(alphabet[new_index])
        except Exception as e:
            print("Error")
            print(e)
    return final_word
