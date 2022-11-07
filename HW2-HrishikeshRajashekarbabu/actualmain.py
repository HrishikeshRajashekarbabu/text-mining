from urllib.request import urlopen #package to find, open, and read files
import re #package to find characters in html file, in this case, numbers
import collections #package to count number of words
from collections import Counter #counter api

url = "https://www.gutenberg.org/cache/epub/12058/pg12058.txt" #can be replaced with any (utf-8) webpage from Project Gutenberg.

page = urlopen(url)
page
html_bytes = page.read()
html = html_bytes.decode("utf-8")

Years = []
Years = re.findall(r"\d+", html) #re api used to find and store all instances of numbers in the text

# print(Years)

NewYears = []

""" Program to find the year of setting of book/written date"""

def most_frequent(Years):
    for i in Years:
        if int(i) >= 100 and int(i) <= 2022: #As these books have origins as early as thousands of years ago, the function will only register numbers (years) from 100 to 2022 AD/BC. This allows the program to ignore all numbers between 0 - 100 which there are no doubt, a lot of, and not a valid year.
            NewYears.append(i)
    NewYearsDict = collections.Counter(NewYears)
   
    topfrequency = max(NewYearsDict.values()) #creates a list to eventually store the maximum occuring "year"
    topfreqList = []
   
    #print(topfrequency) #fakeittillyoumake it
   
    for x in NewYearsDict:
        if topfrequency == NewYearsDict[x]: #in case of multiple most occuring "years", choose a random year data
            topfreqList.append(x)
   
    lowestYear = 2023 #will not accept a year after 2023 as the book might be talking about something else, rather than date
    for x in topfreqList:
        if lowestYear > int(x):
            lowestYear = int(x)   
    print(lowestYear)

most_frequent(Years)

""" Now ensuring that the program no longer reads the text after the phrase "End of the Project Gutenberg" which is the ending
for every book before they include unnecessary details about the publishers etc"""

test_str = html #do not want to tamper with source code
 
sub_str = "End of the Project Gutenberg" #end phrase
 
bookwords = test_str[:test_str.index(sub_str) + len(sub_str)]

# print(str(bookwords)) #fakeittillyoumakeit

"""Now using API for removing stopwords"""

import nltk
nltk.download('stopwords')
nltk.download('punkt')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


# my new custom stopwords
my_extra = ['.', ',', '!', '?', 'thou', "'", "'s", 'one', 'thy', 'thee', '~~', "''", '()', '--', '[]']
# add the new custom stopwrds to my stopwords


my_txt = bookwords
filtered_list = []
stop_words = nltk.corpus.stopwords.words('english')
stop_words.extend(my_extra)
# Tokenize the sentence
words = word_tokenize(my_txt)
for w in words:
    if w.lower() not in stop_words:
        filtered_list.append(w)
        
# print(filtered_list)

"""Now creating list of most common words"""

from collections import Counter
words = filtered_list
most_common_words= [word for word, word_count in Counter(words).most_common(50)]
print (most_common_words)

from nltk.sentiment.vader import SentimentIntensityAnalyzer

listToStr = ' '.join([str(elem) for elem in most_common_words])
 
print(listToStr)

score = SentimentIntensityAnalyzer().polarity_scores(listToStr)
print(score)

if __name__ == "__main__":
    most_frequent(Years)