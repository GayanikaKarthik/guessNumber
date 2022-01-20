def countWordsFromFile():
    fileName = input("Enter the file name: ")

    numberOfWords=0

    file=open(fileName, 'r')
    for line in file:
        words=line.split()
        numberOfWords=numberOfWords+len(words)

    guess = input("Guess the amount of words: ")

while chances < 5:
    if guess == numberOfWords:
        print("Congratulations! You won!")
        break
    if not chances < 5:
        print("You lose! The number is:", number)