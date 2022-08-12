# palindromo

word = "kayak"
is_equal = True

word = word.replace(" ", "")

for i in range(len(word)):
    j = len(word)-i-1

    if word[i] != word[j]:
        is_equal = False

print(is_equal)