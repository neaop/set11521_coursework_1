import nltk

# import data set
raw_data = open('training.txt').read()
# minor preprocessing to ensure nltk compatibility
utf8_data = raw_data.decode('utf-8')

# tokenize the preprocessed data
tokens = nltk.word_tokenize(utf8_data)
# calculate frequency of each tokens
token_freq = nltk.FreqDist(tokens)

# output the 5 most common tokens
print token_freq.most_common()[0:5]

'''
The  task  of  locating  the  most  common  word  in  a corpus was completed
using the nltk python library.
First the raw text file was important via the stan- dard python read function.
The raw data was then converted  to  UTF-8  to  ensure  compatibility.   
nltk was then used to tokenize the data and calculate fre- quency.  
The most common word (not punctuation or number) was ’I’ with a count of 3873
'''

