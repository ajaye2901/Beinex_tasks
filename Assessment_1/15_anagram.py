def anagram(s1,s2):

    l1=sorted(list(s1))
    print(l1)

    l2=sorted(list(s2))
    print(l2)

    if l1==l2:
        print("Anagram")

string1=input("Enter the first string : ")
string2=input("Enter the second string : ")

anagram(string1,string2)
