"""Daniel Licht
Simple Autocorrect Project"""

##Program cannot yet handle punctuation or symbols.
##Input must be a .txt file.
#Find referenceable dictionary to check if word is in dict.
import enchant

#Create graph of qwerty keyboard
QWERTY = {
    'q': ['w', 'a', 's', '', ' '],
    'Q': ['W', 'A', 'S', '', ' '],
    'w': ['q', 'a', 's', 'd', 'e', '', ' '],
    'W': ['Q', 'A', 'S', 'D', 'E', '', ' '],
    'e': ['w', 's', 'd', 'f', 'r', '', ' '],
    'E': ['W', 'S', 'D', 'F', 'R', '', ' '],
    'r': ['e', 'd', 'f', 'g', 't', '', ' '],
    'R': ['E', 'D', 'F', 'G', 'T', '', ' '],
    't': ['r', 'f', 'g', 'h', 'y', '', ' '],
    'T': ['R', 'F', 'G', 'H', 'Y', '', ' '],
    'y': ['t', 'g', 'h', 'j', 'u', '', ' '],
    'Y': ['T', 'G', 'H', 'J', 'U', '', ' '],
    'u': ['y', 'h', 'j', 'k', 'i', '', ' '],
    'U': ['Y', 'H', 'J', 'K', 'I', '', ' '],
    'i': ['u', 'j', 'k', 'l', 'o', '', ' '],
    'I': ['U', 'J', 'K', 'L', 'O', '', ' '],
    'o': ['i', 'k', 'l', 'p', '', ' '],
    'O': ['I', 'K', 'L', 'P', '', ' '],
    'p': ['o', 'l', '', ' '],
    'P': ['O', 'L', '', ' '],
    'a': ['q', 'w', 's', 'z', '', ' '],
    'A': ['Q', 'W', 'S', 'Z', '', ' '],
    's': ['q', 'w', 'e', 'd', 'x', 'z', 'a', '', ' '],
    'S': ['Q', 'W', 'E', 'D', 'X', 'Z', 'A', '', ' '],
    'd': ['w', 'e', 'r', 'f', 'c', 'x', 's', '', ' '],
    'D': ['W', 'E', 'R', 'F', 'C', 'X', 'S', '', ' '],
    'f': ['e', 'r', 't', 'g', 'v', 'c', 'd', '', ' '],
    'F': ['E', 'R', 'T', 'G', 'V', 'C', 'D', '', ' '],
    'g': ['r', 't', 'y', 'h', 'b', 'v', 'f', '', ' '],
    'G': ['R', 'T', 'Y', 'H', 'B', 'V', 'F', '', ' '],
    'h': ['t', 'y', 'u', 'j', 'n', 'b', 'g', '', ' '],
    'H': ['T', 'Y', 'U', 'J', 'N', 'B', 'G', '', ' '],
    'j': ['y', 'u', 'i', 'k', 'm', 'n', 'h', '', ' '],
    'J': ['Y', 'U', 'I', 'K', 'M', 'N', 'H', '', ' '],
    'k': ['u', 'i', 'o', 'l', 'm', 'j', '', ' '],
    'K': ['U', 'I', 'O', 'L', 'M', 'J', '', ' '],
    'l': ['i', 'o', 'p', 'k', '', ' '],
    'L': ['I', 'O', 'P', 'K', '', ' '],
    'z': ['a', 's', 'x', '', ' '],
    'Z': ['A', 'S', 'X', '', ' '],
    'x': ['z', 's', 'd', 'c', '', ' '],
    'X': ['Z', 'S', 'D', 'C', '', ' '],
    'c': ['x', 'd', 'f', 'v', '', ' '],
    'C': ['X', 'D', 'F', 'V', '', ' '],
    'v': ['c', 'f', 'g', 'b', '', ' '],
    'V': ['C', 'F', 'G', 'B', '', ' '],
    'b': ['v', 'g', 'h', 'n', '', ' '],
    'B': ['V', 'G', 'H', 'N', '', ' '],
    'n': ['b', 'h', 'j', 'm', '', ' '],
    'N': ['B', 'H', 'J', 'M', '', ' '],
    'm': ['n', 'j', 'k', '', ' '],
    'M': ['N', 'J', 'K', '', ' ']
    
}

#If word is not in dict. check if combinations using nearby keys are words
def check(word):
    """ Check if input is a word in English lang.
        Args:
            word (str): potential word
        Returns:
            bool: True if input is a word. False if otherwise
    """                   
    dictionary = enchant.Dict('en_US')
    """if "'" in word:
        count = 0
        for i in word:
            if i != "'":
                count += 1
        if dictionary.check(word[:count]) and word[count:]"""
    if dictionary.check(word):
        return True
    return False

def dissect(word):
    """ Divide input string by letter into an array
        Args:
            word (str): word
        Returns:
            listWord (list): Array in which the values are the letters of
            the input word
    """
    listWord = []
    for i in range(len(word)):
        listWord += word[i]
    return listWord

def assemble(L):
    """ Combine input array by letter into concatenated string
        Args:
            L (list): Array of letters in a word as strings
        Returns:
            strWord (str): String of word
    """
    strWord = ''
    for i in L:
        strWord += i
    return strWord


def suggestions(listWord):
    """ Create an array with all possible fixes for typo based on adjacent
        letters on QWERTY keyboard
        Args:
            listWord (list): Array in which the values are the letters of
            the input word 
        Returns:
            pos_suggestions (list): Array of all string combinations, altering
            original input string, changing one letter at a time
    """
    tempWord = listWord[:]
    pos_suggestions = []
    for i in range(len(tempWord)):
       #if listWord[0] in '.,\'";:?!()[]{}': #problematic
            #listWord = listWord[1:]
       #if listWord[i] in '.,\'";:?!()[]{}':
            #listWord = listWord[:i] + listWord[i + 1:]
        for j in QWERTY[listWord[i]]:
            tempWord[i] = j
            pos_suggestions += [assemble(tempWord)]
        tempWord = listWord[:]
    return pos_suggestions


def main(doc):
    """ Read a doc, identify misspelled words, and suggest fixes for typos
        Args:
            doc (string): .txt file being checked
        Returns:
            doc (.txt): Same file with typos signified by "**" on both sides
            of word and suggestions listed at bottom of doc.
    """
    sugg = {}               #initialize suggestions dict.
    output = ''        #initialize output doc
    f = open(doc, 'r')
    text = f.read()                 
    f.close                        
    wordList = text.split() #read doc and create wordlist
    for i in range(len(wordList)):
        if check(wordList[i]):
            output += wordList[i] + ' '
        else:
            pos_suggestions = []
            sugg[wordList[i]] = []
            output += '**' + wordList[i] + '** '
            pos_suggestions += suggestions(dissect(wordList[i]))
            for j in pos_suggestions:
                if check(j):
                    sugg[wordList[i]] += [j]
    print(sugg)
    for k in sugg:
        output += '\n' + 'suggestions for typo "' + str(k) + '": ' + str(sugg[k])
    g = open(doc, 'w')
    g.write(output)
    g.close()
    return
        
           
        
        
    

 
