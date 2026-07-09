# a = input("entre your name: ")
# b = input("entre the date: ")

# print("dear", a)
# print("You are selected!")
# print(b)

letter = '''
Dear <|Name|>,
You are selected!
<|Date|>
'''
print(letter.replace("<|Name|>","Ayush").replace("<|Date|>","22 jan 2027"))