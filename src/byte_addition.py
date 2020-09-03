
byte_word_list = []
partial_word_list = {}
def byte_word_creator(word = '', num = 0, target = 0):
    index = 0
    # small = 'a\\ b'
    ### create a program that will calculate the character combinations using byte
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!"#$%&\'()*+,-./0123456789:;<=>?@[\\]^_`{}|~'
    for i in alphabet:
        if ord(i) + num == target:
            word += (str(i))
            byte_word_list.append(word)
            print(f"this value is {ord(i)} value is {num} target is {target} word is {word} word value is {get_bytes(word)}")
            index += 1
            word = ''
            continue
        elif ord(i) + num < target:
            word += (str(i))
            if get_bytes(word) + 33 > target:
                word = ''
                continue
            else:
                print(f"word is {word} value is {get_bytes(word)} target is {target}")
                byte_word_creator(word, get_bytes(word), target)
        word = ''
    return word
        # print(ord(i))

def get_bytes(w):
    b = w.encode()
    total = 0
    for i in b:
        total += i
    return total

byte_word_creator('', 0, 374)
large = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz !"#$%&\'()*+,-./0123456789:;<=>?@[\\]^_`{}|~'
# small = 'a\\ b'
# print(small)
# print(large)
# for i in large:
#     print(f"{i} is {ord(i)}")
# print(byte_word_list)