phrase = input("Please enter phrase to convert: ")
phrase = phrase.lower()
translated = ""

for char in phrase:
    num = ord(char)
    if (num >= 97) and (num <= 122):
        num = num + 5
        if (num > 122):
            diff = num - 122
            num = 97 + diff - 1
    new_char = chr(num)
    translated += new_char
    
print("With a right shift of 5, the encoded phrase is: ", translated)


