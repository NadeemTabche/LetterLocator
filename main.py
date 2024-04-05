Aanswer = str(input("enter answer: "))
ArandomLetters = ["O", "P", "X", "C", "M", "U", "R", "E", "T", "N"]
def validateAnswer(answer, randomLetters):
    foundLetters = 0
    for i in range(0, len(answer)):
        char = answer[i]
        for j in range(0, len(randomLetters)):
            if char == randomLetters[j]:
                foundLetters += 1
                randomLetters[j] = " "
    if foundLetters == len(answer):
        print(str(foundLetters))
    else:
        print(str(0))
validateAnswer(Aanswer, ArandomLetters)
