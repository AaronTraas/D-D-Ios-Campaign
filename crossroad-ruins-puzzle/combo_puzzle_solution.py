import enchant

options_1 = ["AB", "FR", "XI", "VI", "PO", "EK", "QA", "RU"]
options_2 = ["TI", "DR", "A", "CA", "I", "RE", "NE", "O"]
options_3 = ["US", "TON", "RY", "NLE", "RLE", "ZA", "PIN", "ON"]

coin = ["O", "K", "M"]

# create list of words containing all combinations of letters
words = []
for o1 in options_1:
    for o2 in options_2:
        for o3 in options_3:
            words.append(o1 + o2 + o3)
            words.append(o1 + coin[0] + o2 + coin[1] + o3 + coin[2])
            words.append(coin[0] + o1 + coin[1] + o2 + coin[2] + o3)
            words.append(o3 + o2 + o1)
            words.append(o3 + coin[0] + o2 + coin[1] + o1 + coin[2])
            words.append(coin[0] + o3 + coin[1] + o2 + coin[2] + o1)

# add reverses of words
for word in words[:]:
    words.append(word[::-1])

# dictionary lookup
dictionary = enchant.DictWithPWL("en_US", "custom_pwl.txt")
print("Looking up {} words in dictionary".format(len(words)))
for word in sorted(words):
    if (dictionary.check(word)):
        print("{} -> {}".format(word, dictionary.check(word)))
