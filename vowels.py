def countVowels(myWord):
    myWord = list(myWord)
    vowels = ['a', 'e', 'i', 'o', 'u']
    wordWithNoDups = set(myWord)
    listOfVowelsInMyWord = []

    for letter in wordWithNoDups:
        if letter in vowels:
            listOfVowelsInMyWord.append(letter)
    
    dupVowels = [element for element  in wordWithNoDups if len([letter for  letter in myWord if letter == element]) > 1 ]
    result = (''.join(listOfVowelsInMyWord), len(dupVowels) )
     
    return result


print(countVowels("allocations"))
