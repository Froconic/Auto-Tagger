import string
import os
# TODO Function that renames files in a directory
# TODO function that parses dates from the title and adds them at the top of the file
# TODO Function to move files to a new directory

def stripPunctuation(word):
    for char in string.punctuation:
        word = word.replace(char, "")
    return word

input = "input/"
output = "output/"
object = os.scandir(input)

wordCount = {}

# with open(input, 'r') as f:
#     for line in f:
#       for word in line.split():
#             word = stripPunctuation(word)
#             word = word.lower()
#             text = text + word + " "
#             if word not in wordCount:
#                 wordCount[word] = 1
#             else:
#                 wordCount[word] += 1
#     print("Full Text: " + text)

# Create a data frame of the most common words
def frequencySort(dictionary):
  sortedList = []
  for key in dictionary:
      sortedList.append((dictionary[key], key))
      sortedList = sorted(sortedList, reverse=True)
  return sortedList


def filterWordCheck(dictionary):
  filteredList = {}
  filterWords = ['the', 'and', 'of', 'a', 'to', 'in', 'is', 'it', 'you', 'that', 'he', 'was', 'for', 'on', 'are', 'with', 'as', 'i', 'his', 'they', 'be', 'at', 'one', 'have', 'this', 'from', 'or', 'had', 'by', 'but', 'not', 'what', 'all', 'were', 'we', 'when', 'your', 'can', 'there', 'use', 'an', 'each', 'which', 'she', 'do', 'how', 'their', 'if', 'will', 'up', 'other', 'about', 'out', 'many', 'then', 'them', 'these', 'so', 'some', 'her', 'would', 'make', 'like', 'him', 'into', 'time', 'has', 'look', 'two', 'more', 'go', 'see', 'number', 'no', 'way', 'could', 'people', 'my', 'than', 'first', 'water', 'been', 'call', 'who', 'oil', 'its', 'now', 'find', 'long', 'down', 'day', 'did', 'get', 'come', 'made', 'may', 'part', 'am', 'seems', 'something', 'kind', 'im', 'just', 'dont', 'theres', 'where', 'very', 'certain', 'addendum', 'too', 'thats', 'stuff', 'because', 'also', 'us', 'things', 'put', 'might', 'let', 'cuz', 'whos', 'werent', 'those', 'thing', 'theyre', 'themselves', 'sure', 's', 'most', 'maybe', 'gets', 'except', 'any', 'already', 'actually', 'yours', 'youre', 'wont', 'whatever', 'wasnt', 'was', 'unless','typically', 'totally', 'stays', 'seem', 'same', 'quite', 'mostly', 'likely', 'jumps', 'hes', 'having', 'gotten', 'getting', 'coming', 'both', 'blah', 'anything', 'really', 'me', '', 'after', 'while', 'turn', 'while', 'instead', 'during', 'yadi', 'without', '']

  for key in dictionary:
    if key not in filterWords:
      filteredList[key] = dictionary[key]

  return filteredList

def AutoTag(object):
  text = ""
  for n in object:
    if n.is_file():
      print("File found: " + n.name)
      with open(n.path, 'r') as i:
        print("Sifting through file...")
        for line in i:
          for word in line.split():
            word = stripPunctuation(word)
            word = word.lower()
            text = text + word + " "
            if word not in wordCount:
                wordCount[word] = 1
            else:
                wordCount[word] += 1
                
        print('Text sifted thru and word count found' + '\n')
        print("Full Text: " + text + "\n")
        print("Filtering for unecessary words..." + "\n")
        filtered = filterWordCheck(wordCount)
        print("Now sorting..." + "\n")
        sorted = frequencySort(filtered)
        print("Now adding list of words tags and backlinks..." + "\n")
        print("Please Wait..." + "\n")
        with open(n.path, 'w') as o:
          o.write(text + "\n")
          o.write("\n" + '# Most Common Words: ' + "\n")
          for frequency in sorted:
            count, word = frequency
            o.write('### ' + str(wordCount[word]) + '\n')
            o.write('#' + word + '\n')
            o.write('[[' + word + ']]\n')
          print("File written")

# print(text)
# filtered = filterWordCheck(wordCount)
# sorted = frequencySort(filtered)
# print("Sorted Results: ",sorted)
# print("Full list:")
# for frequency in sorted:
#     count, word = frequency
#     print(word, ": ", wordCount[word])

# with open(output, 'w') as r:
#     for frequency in sorted:
#         count, word = frequency
#         r.write('# ' + str(wordCount[word]) + '\n')
#         r.write('#'+ word +  '\n')
#         r.write('[[' + word + ']]\n')

# with open(input, 'w') as f:
#   f.write(text + '\n')
#   f.write('\n' + "# List of common words: " + '\n')
#   for frequency in sorted:
#     count, word = frequency
#     f.write('# ' + str(wordCount[word]) + '\n')
#     f.write('#' + word + '\n')
#     f.write('[[' + word + ']]\n')

AutoTag(object)