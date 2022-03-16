import string
# TODO add a function that will delete common words in a filter list

def stripPunctuation(word):
    for char in string.punctuation:
        word = word.replace(char, "")
    return word

input = "Auto Tagger/input/test.txt"
output = "Auto Tagger/output/list.md"

wordCount = {}

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

top = frequencySort(wordCount)[:10]
print('Top Ten:')
for frequency in top:
    count, word = frequency
    print(word, ": ", wordCount[word])

sort = frequencySort(wordCount)
print("Full list:")
for frequency in sort:
    count, word = frequency
    print(word, ": ", wordCount[word])
    
with open(output, 'w') as r:
  
  
    for frequency in sort:
        count, word = frequency
        r.write('# ' + str(wordCount[word]) + '\n')
        r.write('#'+ word +  '\n')