userInput= input("Write a sentence")
userInput2 = input("Write a second sentence please")
userInput3 = userInput + userInput2
userInput3 = userInput3.split()

def main():
    print("This is the occurrence of each word you have used")
    dic = {}
    for w in userInput3:
        if w not in dic:
            dic[w] = 1
        else:
            dic[w] += 1
    print(dic)
    
def sentences():
    print("I have concatenated the two sentences for you")
    print(userInput + userInput2)
    print("These are the lists of words you have used in each sentence")
    words = userInput.split()
    print(words)
    words2 = userInput2.split()
    print(words2)
    print("These are the lists sorted alphabetically")
    print(sorted(words))
    print(sorted(words2))
    print("I have counted the words for each sentence you wrote and below are the results")
    print(len(userInput.split()))
    print(len(userInput2.split()))
    main()

sentences()
    

            
