import json
import networkx as nx
import distance


# find all paths between starting and ending point; append them to an array
def findAllPaths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if start not in graph.keys():
        return []
    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = findAllPaths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths

# find the depth of each path
def pathLengths(totalPaths):
	lengthOfPaths = []
	for path in totalPaths:
		lengthOfPaths.append(len(path))
	return lengthOfPaths

# find minimum depth
def minPath(totalPaths):
	length = pathLengths(totalPaths)
	return totalPaths[length.index(min(length))]
# find maximum depth
def maxPath(totalPaths):
	length = pathLengths(totalPaths)
	return totalPaths[length.index(max(length))]

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

def stringToAscii(word):

	return	[ord(letter) for letter in word]

def asciiToString(word):
	return ''.join(chr(letter) for letter in word)

# def populateGraph(starting, ending, dictionary):
# 	if  not len(startingState) == len(endingState):

def getSuccessors(wordDictionary, word,target, startingIndex, endingIndex, chain, frontier):
	chain[word] =[]
	wordAscii = stringToAscii(word)
	# child = []
	# for letter in range(0, len(wordAscii)):
	# 	# print wordAscii[letter]
	# 	# temp = wordAscii
	# 	temp = []
	tempString = word
	# print chain

	for key in wordDictionary[startingIndex:startingIndex+endingIndex]:
	# for change in range(65,91):
		# tempIter = letter
		# tempAscii = list(wordAscii)
		# tempAscii[letter] = change
		# # print asciiToString(temp)
		# tempString = asciiToString(tempAscii)
		if distance.hamming(tempString,key) == 1:
			# print "woooo"
		# if tempString in wordDictionary[startingIndex:startingIndex+endingIndex]:
			if not key in chain.keys():
				# print "vat"
				frontier.append(key)
				chain[word].append(key)
				if tempString == target:
					print "Woah"
					return
			# if tempIter == 90:
			# 	tempIter = 65
			# print "word",wordAscii
		# temp = wordAscii
	if len(chain[word]) == 0:
		chain.pop(word, None)
	# chain[word]=child

def findChain(wordDictionary, word,target, startingIndex, endingIndex, chain, frontier):
	# print word
	# if word == target:
	# 	return
	

	# getSuccessors(wordDictionary,word,target, startingIndex, endingIndex, chain,frontier)
	# print chain
	# print frontier
	# findChain(wordDictionary, word,target, startingIndex, endingIndex, chain, frontier)
	while frontier:
		word = frontier.pop()
		# print word

		if(word==target):
			return
		getSuccessors(wordDictionary,word,target, startingIndex, endingIndex, chain,frontier)


	# for item in chain[word]:
	# 	childWord = frontier.pop()
	# 	if childWord == target:
	# 		print "found it"
	# 	getSuccessors(wordDictionary,childWord,target, startingIndex, endingIndex, chain,frontier)


		
# parse json file and return the keys of the json object
def parseJson(fileName):
	f=open(fileName)
	jsonDictionary = json.loads(f.read())
	return jsonDictionary.keys()

def bfs(graph, start, end):
    # maintain a queue of paths
    queue = []
    # push the first path into the queue
    queue.append([start])
    while queue:
        # get the first path from the queue
        path = queue.pop(0)
        # get the last node from the path
        node = path[-1]
        # path found
        if node == end:
            return path
        # enumerate all adjacent nodes, construct a new path and push it into the queue
        for adjacent in graph.get(node, []):
            new_path = list(path)
            new_path.append(adjacent)
            queue.append(new_path)

graph = {'Apple': ['abple', 'bhdfs'],
    'B': ['C', 'D'],
    'C': ['D'],
    'D': ['C'],
    'E': ['F'],
    'F': ['C']}


# url = 'https://raw.githubusercontent.com/adambom/dictionary/master/dictionary.json'

# jsonDictionary = urllib2.urlopen(url).read()


dictionary = parseJson('dictionary.json')
dictionary.sort() 
dictionary.sort(lambda x,y: cmp(len(x), len(y)))
# dictionary.sort() # sorts normally by alphabetical order
# dictionary.sort(key=len, reverse=True)
# print dictionary
iterator = 0

wordLength = calculateWordsLength(dictionary)
# print wordLength
starting  = "CUTE"
ending ="LOOT"
endIndex = wordLength[len(starting)]

# iterator = 0
# # startIndex = wordLength[len(starting)-1]

index = startingIndex(wordLength,starting)
print index
print endIndex

wordChain = {}
frontier =[]
frontier.append(starting)
findChain(dictionary, starting,ending, index, endIndex, wordChain, frontier)



# for key in dictionary[wordLength[1]+wordLength[2]:wordLength[3]+wordLength[1]+wordLength[2]]:
# 	print key
# print findAllPaths(wordChain,starting,ending)
# for key in wordChain.keys():
# 	print wordChain[key]
# wordGraph = nx.DiGraph()

# for key in wordChain.keys():
# 	for item in wordChain[key]:
# 		wordGraph.add_edge(key,item)
print bfs(wordChain, starting,ending)
# print (nx.algorithms.bfs_tree(wordGraph, starting).edges())


# print  [0].extend(nx.algorithms.bfs_successors(wordGraph, starting).values())

# pathsToTarget = []

# for path in nx.all_simple_paths(wordGraph, source=starting, target=ending):  
# 	len(path)
#     pathsToTarget.append(path)
# print minPath(pathsToTarget)
# print nx.shortest_path(wordGraph,source=starting,target=ending)
# print minPath(findAllPaths(wordChain,starting,ending))

# for key in dictionary[index:index+endIndex]:
# 	print key
# 	iterator+=1
# print "total",iterator


# print getSuccessors(dictionary,starting, index, endIndex)
	
		



# dictionary[index:index+endIndex]

# print(maxPath(findAllPaths(graph,'A','D')))





print distance.hamming(starting,ending)