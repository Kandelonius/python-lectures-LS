
byte_word_list = {}
def byte_word_creator(word = '', num = 0, target = 0):
    # small = 'a\\ b'
    ### create a program that will calculate the character combinations using byte
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz !"#$%&\'()*+,-./0123456789:;<=>?@[\\]^_`{}|~'
    for i in alphabet:
        if ord(i) + num == target:
            word.__add__(str(i))
            byte_word_list.append(word)
            return
        elif ord(i) + num < target:
            word += (str(i))
            if word.encode('utf-8') + 32 > target:
                return
            else:
                byte_word_creator(word, word.encode(), target)
        # print(ord(i))

# byte_word_creator('', 0, 197)
large = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz !"#$%&\'()*+,-./0123456789:;<=>?@[\\]^_`{}|~'
# small = 'a\\ b'
# print(small)
print(large)
for i in large:
    print(f"{i} is {ord(i)}")