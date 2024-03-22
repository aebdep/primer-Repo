import string
def minion_game(string):
    vowels ="AEIOU"
    lon = len(string)
    stuart_score = 0
    kevin_score = 0
    stuart_substr=[]
    kevin_substr=[]
    for i in range(lon):
        if string[i] in vowels:
            kevin_score += lon-i
            kevin_substr.append(string[i:])
        else:
            stuart_score += lon-i
            stuart_substr.append(string[i:])
    if stuart_score > kevin_score:
        print("Stuart =",stuart_score)
        print("Stuart Sub String:",stuart_substr)
        print("Kevin Sub String:", kevin_substr)
    elif kevin_score > stuart_score:
        print("Kevin =",kevin_score)
        print("Kevin Sub String:", kevin_substr)
        print("Stuart Sub String:", stuart_substr)
    else:
        print("Draw")
input_string = input("enter a string =")
minion_game(input_string)

