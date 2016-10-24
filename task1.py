import json

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
def calculateWordsLength(dictionary):
	wordLength = {}
	for keys in dictionary:
		if not len(keys) in wordLength.keys():
			wordLength[len(keys)] = 1
		else:
			wordLength[len(keys)]+=1
	return wordLength

# claculate the starting index based on length of starting point
def startingIndex(wordLength, startingIndex):
	index = 0
	for key in wordLength.keys():
		if key < len(starting):
			index+= wordLength[key]
	return index

# parse json file and return the keys of the json object
def parseJson(fileName):
	f=open(fileName)
	jsonDictionary = json.loads(f.read())
	return jsonDictionary.keys()

graph = {'Apple': ['abple', 'bhdfs'],
    'B': ['C', 'D'],
    'C': ['D'],
    'D': ['C'],
    'E': ['F'],
    'F': ['C']}


# url = 'https://raw.githubusercontent.com/adambom/dictionary/master/dictionary.json'

# jsonDictionary = urllib2.urlopen(url).read()


dictionary = parseJson('dictionary.json')
dictionary.sort(lambda x,y: cmp(len(x), len(y)))
# print dictionary
# iterator = 0

# for keys in dictionary:
# 	if(iterator==1000):
# 		break
# 	print keys
# 	iterator+=1


wordLength = calculateWordsLength(dictionary)
print wordLength
starting  = "food"

iterator = 0
# startIndex = wordLength[len(starting)-1]
endIndex = wordLength[len(starting)]

index = startingIndex(wordLength,endIndex)
print index
print endIndex

for key in dictionary[index:index+endIndex]:
	# print key
	iterator+=1
print "total",iterator
# print(maxPath(findAllPaths(graph,'A','D')))


