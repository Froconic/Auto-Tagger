import string
# TODO Function that checks for common words in a file and outputs a list of tags and backlinks that are added to the end of the file under titles

def stripPunctuation(word):
    for char in string.punctuation:
        word = word.replace(char, "")
    return word

input = "input/test.txt"
output = "output/list.md"
linked = "output/links.md"

wordCount = {}
text = ""

with open(input, 'r') as f:
    for line in f:
        for word in line.split():
            word = stripPunctuation(word)
            word = word.lower()
            if word not in wordCount:
                wordCount[word] = 1
            else:
                wordCount[word] += 1

# Create a data frame of the most common words
def frequencySort(dictionary):
  sortedList = []
  for key in dictionary:
      sortedList.append((dictionary[key], key))
      sortedList = sorted(sortedList, reverse=True)
  return sortedList


def filterWordCheck(dictionary):
  filteredList = {}
  filterWords = ['the', 'and', 'of', 'a', 'to', 'in', 'is', 'it', 'you', 'that', 'he', 'was', 'for', 'on', 'are', 'with', 'as', 'i', 'his', 'they', 'be', 'at', 'one', 'have', 'this', 'from', 'or', 'had', 'by', 'but', 'not', 'what', 'all', 'were', 'we', 'when', 'your', 'can', 'there', 'use', 'an', 'each', 'which', 'she', 'do', 'how', 'their', 'if', 'will', 'up', 'other', 'about', 'out', 'many', 'then', 'them', 'these', 'so', 'some', 'her', 'would', 'make', 'like', 'him', 'into', 'time', 'has', 'look', 'two', 'more', 'go', 'see', 'number', 'no', 'way', 'could', 'people', 'my', 'than', 'first', 'water', 'been', 'call', 'who', 'oil', 'its', 'now', 'find', 'long', 'down', 'day', 'did', 'get', 'come', 'made', 'may', 'part', 'am', 'seems', 'something', 'kind', 'im', 'just', 'dont', 'theres', 'where', 'very', 'certain', 'addendum', 'too', 'thats', 'stuff', 'because', 'also', 'us', 'things', 'put', 'might', 'let', 'cuz', 'whos', 'werent', 'those', 'thing', 'theyre', 'themselves', 'sure', 's', 'most', 'maybe', 'gets', 'except', 'any', 'already', 'actually', 'yours', 'youre', 'wont', 'whatever', 'wasnt', 'was', 'unless','typically', 'totally', 'stays', 'seem', 'same', 'quite', 'mostly', 'likely', 'jumps', 'hes', 'having', 'gotten', 'getting', 'coming', 'both', 'blah', 'anything']

  for key in dictionary:
    if key not in filterWords:
      filteredList[key] = dictionary[key]

  return filteredList

print(text)
filtered = filterWordCheck(wordCount)
sorted = frequencySort(filtered)
# print("Sorted Results: ",sorted)
# print("Full list:")
# for frequency in sorted:
#     count, word = frequency
#     print(word, ": ", wordCount[word])

with open(output, 'w') as r:
    for frequency in sorted:
        count, word = frequency
        r.write('# ' + str(wordCount[word]) + '\n')
        r.write('#'+ word +  '\n')
        r.write('[[' + word + ']]\n')

# with open(linked, 'w') as p:
#     with open(input, 'r') as f:
#         for line in f:
#             for word in line.split():
#                 word = stripPunctuation(word)
#                 word = word.lower()
#                 if word in sorted:
#                     word = '[[' + word + ']] '
#                     print('Backlinked word' + word)
#                     text = text + word
#                     print(text)
#                 else:
#                     text = text + ' ' + word
#                     print(text)
#         p.write(text)
