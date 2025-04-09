text = input()
text = text.lower()
textset = set(text)
dict_litter = {char: text.count(char) for char in textset if char.isalpha()}
sorted_dict = dict(sorted(dict_litter.items(), key=lambda item: item[1], reverse=True))
print(sorted_dict)
