# ngrams.py
# A program that tallies n-gram counts in given text files
# Eric Alexander
# CS 111

def getOneGrams(filename):
    ''' Function takes in a given text filename and counts one-grams in the file '''

    oneGramCounts = {}

    with open(filename, 'r') as f:
        for line in f:
            # Clean out punctuation
            for ch in '!@#$%^&*()_+-=;:",./<>?\\':
                line = line.replace(ch, ' ')

            # Reduce to all lowercase
            line = line.lower()

            # Split into words
            words = line.split()

            # Add to oneGramCounts for each word (checking to see if it is already present)
            for word in words:
                if word in oneGramCounts:
                    oneGramCounts[word] += 1
                else:
                    oneGramCounts[word] = 1

    return oneGramCounts

def getTwoGrams(filename):
    ''' Function takes in a given text filename and counts two-grams in the file '''
    pass

def getNGrams(filename, n):
    ''' Function takes in a given text filename and an integer n and counts n-grams in the file '''
    pass

def printTopN(countDict, n):
    ''' Function takes a dictionary mapping n-grams to counts and prints top n n-grams by count. '''

    dictItems = list(countDict.items())
    dictItems.sort()
    dictItems.sort(key=lambda pair: pair[1], reverse=True)

    for i in range(n):
        word, count = dictItems[i]
        print('{} {}'.format(word, count))

def main():
    filename = 'Shakespeare/Hamlet.txt'
    oneGramDict = getOneGrams(filename)
    printTopN(oneGramDict, 50)

if __name__ == '__main__':
    main()