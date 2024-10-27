phrase = input("Please enter phrase to convert: ")
phrase = phrase.lower()
length = int(len(phrase))
translated = ""

for i in range(length):
    ctr = phrase[i]
    num = ord(ctr)                       
    if (num >= 97) and (num <= 122):     
        num = num + 5
        if (num > 122):
            diff = num - 122
            num = 97 + diff - 1
    ctr = chr(num)
    translated += ctr
    
print("With a right shift of 5, the encoded phrase is: ", translated)


