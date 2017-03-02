#Python program to find most nunmber common words in a text file

#impoting the required libraries
import re
from collections import Counter

#find words in the specified text and converting them into lowercase letters
words = re.findall(r'\w+', open('C:\\Users\\mono\\Desktop\\hd.txt').read().lower())

#finding out the most common words
count = Counter(words).most_common(20) #change the value of the argument to increase or decrease the number of common words 
print count

