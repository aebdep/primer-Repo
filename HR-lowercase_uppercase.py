import string
def swap_case(s):
    new_case=""
    for i in s:
        if i.islower():
            new_case += i.upper()
        elif i.isupper():
            new_case += i.lower()
        else:
            new_case += i
    return new_case
if __name__ == "__main__":
    s=input()
    print(s)
    result = swap_case(s)
    print(result)







