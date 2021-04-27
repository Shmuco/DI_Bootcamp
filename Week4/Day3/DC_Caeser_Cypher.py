text = input("Enter the message: ")
option = int(input("Press 1 to Encrypt or 2 to Decrypt: "))
cypher_text=""
if option==1:
    for letter in text:
        if letter.isdigit()==True or letter.isalpha()==False:
            cypher_text=cypher_text+letter 
        elif ord(letter)>=121:
            cypher_text =cypher_text + chr(ord(letter)-23)
        else:
            cypher_text =cypher_text + chr(ord(letter)+ 3)
    cypher_text=cypher_text.replace("#", " ")

elif option==2:
    for letter in text:
        if letter.isdigit()==True or letter.isalpha()==False:
            cypher_text=cypher_text+letter 
        elif ord(letter)<=67:
            cypher_text =cypher_text + chr(ord(letter)+23)
        else:
            cypher_text =cypher_text + chr(ord(letter)- 3)
    cypher_text=cypher_text.replace("7", " ")
    
print(cypher_text)
