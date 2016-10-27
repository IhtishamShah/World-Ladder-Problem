import json

import distance
import csv




# find total number of words of same length in dictionary 
def calculateWordsLength(wordDictionary):
    wordLength = {}
    for keys in wordDictionary:
        if not len(keys) in wordLength.keys():
            wordLength[len(keys)] = 1
        else:
            wordLength[len(keys)]+=1
    return wordLength

# claculate the starting index based on length of starting point
def startingIndex(wordLengthDictionary, word):
    index = 0
    for key in wordLengthDictionary.keys():
        if key < len(word):
            index+= wordLengthDictionary[key]
    return index

def getSuccessors(wordDictionary, word,target, startingIndex, endingIndex, chain, frontier, explored):
    chain[word] =[]
    tempString = word
    successor =[]
    for key in wordDictionary[startingIndex:startingIndex+endingIndex]:
        if distance.hamming(word,key) == 1:
            if not key in explored:
                chain[word].append(key)
                successor.append(key)
                if tempString == target:
                    print "Woah"
                    return successor
    if len(chain[word]) == 0:
      chain.pop(word, None)
    # print "successor", successor
    return successor

def findChain(wordDictionary, word,target, startingIndex, endingIndex, chain):
    if word.upper() not in wordDictionary:
        print word, " is not in the distionary."
        return
    elif target.upper() not in wordDictionary:
        print target, " is not in dictionary."
        return
    if len(word) != len(target):
        print "Word length needs to be the same"
        return
    start = (word,[word])
    frontier = []
    frontier.append(start)
    # print "front",frontier
    explored =[]
    while True:
        if not frontier:
            print "broken"
            break
        pos, path = frontier.pop(0)
        if pos == target:
            # print "woah 2"
            return path

        neighbours = getSuccessors(wordDictionary,pos,target, startingIndex, endingIndex, chain,frontier,explored)
        # print neighbours
        for key in neighbours:
            if (not key in explored) and (key not in frontier):
                frontier.append((key,path+[key]))
                explored.append(key)
    
    return []

# find the chain between all words in the dictionary
def chainBetweenWords(wordArray):
    wordChain = {}

    noChains =[]
    chains = []
    ##################
    for key in dictionary:
        index = startingIndex(wordArray,key)
        endIndex = wordArray[len(key)]
        visited =[]

        for word in dictionary[index:endIndex+index]:
            if (not word == key) and ((key,word) not in visited) and ((word,key) not in visited) :
                visited.append((key,word))
                print "key:",key
                print "word:",word
                # frontier = []

                rows =  findChain(dictionary, key,word, index, endIndex, wordChain)

                if rows:
                    chains.append(rows)
                else:
                    noChains.append(rows)
        
        with open("words" + str(len(key))+ ".csv", "ab") as csv_file:
            writer = csv.writer(csv_file, delimiter=',')
            for row in chains:
                if row:
                    print "Entering data"
                    rowData = [row[0],row[len(row)-1],"->".join(row), len(row)]
                    writer.writerow(rowData)
 
def chainFrequency():
    chainFreq = {}
    chains = []
    for number in range(1,4):
        cr = csv.reader(open("words"+str(number)+".csv","rb")) 
        for row in cr:
            temp = int(row[3])
            temp-=1
            chains.append([row[0],row[1],row[2],temp])

            if temp not in chainFreq.keys():
                chainFreq[temp] = 1
            else:
                chainFreq[temp]+=1
    with open("chainLength.csv", "ab") as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        writer.writerow(["ChainLength","Frequency"])
        for row in chainFreq.keys():
            print "Chain Length: ", row
            print "Frequency:  ", chainFreq[row]
            rowData = [row,chainFreq[row]]
            writer.writerow(rowData)
    longest = []
    for row in chains:
        longest.append(row[3])
    maxChain = max(chainFreq.keys())
    maxChains = [key for key in chains if key[3] == maxChain ]
    
    print "chains with max length i.e. "+str(maxChain)+ ":\n"
    for key in maxChains:
        print "Starting Point: ", key[0]
        print "Destination: ", key[1]
        print "Chain: ", key[2]




# parse json file and return the keys of the json object
def parseJson(fileName):
    f=open(fileName)
    jsonDictionary = json.loads(f.read())
    return jsonDictionary.keys()


# url = 'https://raw.githubusercontent.com/adambom/dictionary/master/dictionary.json'

dictionary = parseJson('dictionary.json')
dictionary.sort() 
dictionary.sort(lambda x,y: cmp(len(x), len(y)))

wordLength = calculateWordsLength(dictionary)
# chainBetweenWords(wordLength)
# chainFrequency(wordLength)

while True:
    choice  = raw_input("Enter choice\n1.Find Chaing between 2 words\n2.Find all chains\n3.Create Frequency Distribution and check longest chain:\n4.Exit\n\n")
    if(int(choice) == 1):
        print "Enter Capital Letters"
        source = raw_input("Enter starting word: ")
        destination = raw_input("Enter destination word: ")
        if len(source) == len(destination):

            index = startingIndex(wordLength,source)
            endIndex = wordLength[len(source)]
            wordChain={}
            print findChain(dictionary, source,destination, index, endIndex, wordChain)
        else:
            break

        
    if(int(choice)==2):
        chainBetweenWords(wordLength)
    if(int(choice)==3):
        chainFrequency()
    if(int(choice)==4):
        break
