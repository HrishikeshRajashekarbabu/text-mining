from urllib.request import urlopen #package to find, open, and read files
import re #package to find characters in html file, in this case, numbers
import collections
import urllib
from collections import Counter

url = "https://www.gutenberg.org/cache/epub/12058/pg12058.txt"

page = urlopen(url)
page
html_bytes = page.read()
html = html_bytes.decode("utf-8")

# page
# html_bytes = page.read()
# html = html_bytes.decode("utf-8")

  # the lib that handles the url stuff

# data = urllib.re(url) # it's a file like object and works just like a file
# for line in data: # files are iterable
#     print (line)

Years = []


NewYears = []

def most_frequent():
    Years = re.findall(r"\d+", html)
    for i in Years:
        if int(i) >= 1000 and int(i) <= 2022:
            NewYears.append(i)
    NewYearsDict = collections.Counter(NewYears)
   
    topfrequency = max(NewYearsDict.values())
    topfreqList = []
   
    #print(topfrequency)
   
    for x in NewYearsDict:
        if topfrequency == NewYearsDict[x]:
            topfreqList.append(x)
   
    lowestYear = 2023
    for x in topfreqList:
        if lowestYear > int(x):
            lowestYear = int(x)
   
        # if not int(x) >= 1000 and int(x) <= 2022:
        #     Years.remove(x)
        # else:
        #     NewYears.insert(1, x)
    #print(topfreqList)
    #print(NewYears)
    #print(NewYearsDict)
   
    return lowestYear
most_frequent()



# print(html)


# substring = "End of the Project Gutenberg"

# if html != None and substring in html:
#     html.rstrip("End of the Project Gutenberg")
# else:
#     print("Not found!")

test_str = html
 
# printing original string
# print("The original string is : " + str(test_str))
 
# initializing sub string
sub_str = "End of the Project Gutenberg"
 
# slicing off after length computation
bookwords = test_str[:test_str.index(sub_str) + len(sub_str)]
 
# printing result
# print("The string after removal : " + str(bookwords))

# def limit_read(html):
#     string = "End of Project Gutenberg"
#     f = (html)
#     for word in f:
#         if word.find(string) == -1:
#             print (word)
#         else:
#             break
# limit_read(html)

# from nltk import word_tokenize

# text_tokens = word_tokenize(bookwords)

# # tokens_without_sw = [word for word in text_tokens if not word in ]

# print(text_tokens) #fakeittillyoumakeit

from gensim.parsing.preprocessing import remove_stopwords

filtered_sentence = remove_stopwords(bookwords)

# print(filtered_sentence)


# from gensim.parsing.preprocessing import STOPWORDS

# all_stopwords_gensim = STOPWORDS.union(set(['and', 'The', 'I']))

# text = bookwords
# tokens_without_sw = [word for word in text if not word in all_stopwords_gensim]

# print(filtered_sentence)

split_it = filtered_sentence.split()
  
# Pass the split_it list to instance of Counter class.
Counter = Counter(split_it)
  
# most_common() produces k frequently encountered
# input values and their respective counts.
most_occur = Counter.most_common(1000)
  
# print(most_occur)
# with open(url) as f:
#     lines = f.readlines()

# frequency = []
# def frequency_of_words(words):
#     for i in words:
#         if type(i) == str:
#             frequency.append(i)
#     Dfrequency = collections.Counter(frequency)
#     topword = max(Dfrequency.values())
#     topword = []
#     return topword

# List = [2, 1, 2, 2, 1, 3]
# print(most_frequent(Years))

# print(frequency_of_words(words))
