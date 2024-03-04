# Write a function that takes a sentence as input and returns a new sentence 
# with the words reversed, while keeping the order of the words in the sentence.

def ReverseWords(sentence) :
    reversed_sentence = ""
    for word in sentence :
        reversed_word = word[::-1]
        reversed_sentence += reversed_word + ' '
    return reversed_sentence

sentence=input("Enter a sentence :").split()
if not sentence :
    print("Sentence is empty")
else :
    print("Reversed Sentence is ->",ReverseWords(sentence))



