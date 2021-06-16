import os


def cipher(line, shift):
    new_str = ""
    for i in line:
        if i.lower() in alphabet:
            count = alphabet.index(i.lower())
            if (count + 1) + shift > len(alphabet):
                count = (len(alphabet) - (count + 2))
            new_str += alphabet[count + shift]

    return new_str.title()


alphabet = "abcdefghijklmnopqrstuvwxyz"
k = 1
input_file = open(os.path.abspath("text.txt"), "r", encoding="UTF-8")

if os.path.exists("cipher_text.txt"):
    output_file = open(os.path.abspath("cipher_text.txt"), "w", encoding="Utf-8")
    output_file.write("")
    output_file.close()

output_file = open(os.path.abspath("cipher_text.txt"), "a", encoding="Utf-8")
for i_line in input_file:
    output_file.write(cipher(i_line, k) + "\n")
    k += 1
input_file.close()
output_file.close()

# зачёт! 🚀
