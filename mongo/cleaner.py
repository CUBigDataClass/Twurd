import pandas as pd
import re
from nltk.tokenize import word_tokenize
import json

df = pd.read_csv('D:\Documents\Twurd\Twurd_temp\\all_annotated.tsv', sep='\t', header=0)
# print(df.columns)

df = df[df['Definitely English'] == 1]
df.drop(df.columns[[4,5,6,7,8,9]], axis=1, inplace=True)
# print(len(df))

freq = {'allc': {}}
# print(df.iloc[1,[1,3]])

def remove_emojis(data): #https://stackoverflow.com/a/58356570
    emoj = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
        u"\U00002500-\U00002BEF"  # chinese char
        u"\U00002702-\U000027B0"
        u"\U00002702-\U000027B0"
        u"\U000024C2-\U0001F251"
        u"\U0001f926-\U0001f937"
        u"\U00010000-\U0010ffff"
        u"\u2640-\u2642" 
        u"\u2600-\u2B55"
        u"\u200d"
        u"\u23cf"
        u"\u23e9"
        u"\u231a"
        u"\ufe0f"  # dingbats
        u"\u3030"
                      "]+", re.UNICODE)
    return re.sub(emoj, ' ', data)

def clean(tweet): #https://stackoverflow.com/q/64719706
    tweet = re.sub(r"(?:\@|http?\://|\\n|https?\://|www)\S+", "", tweet)
    tweet = remove_emojis(tweet)
    regex = re.compile('[^a-zA-Z ]')
    #First parameter is the replacement, second parameter is your input string
    tweet = regex.sub('', tweet)
    tweet = tweet.lower()
    #Out: 'abdE'
    tweetlist = word_tokenize(tweet)
    return tweetlist

for index, row in df.iterrows():
    country = row["Country"]
    # print(country)
    if country not in freq:
        # print("Adding country " + str(country))
        freq[country] = {}
    if country in freq:
        for word in clean(row['Tweet']):
            if word not in freq['allc']:
                freq['allc'][word] = 1
                freq[country][word] = 1
                # print("New word: " + word)
            else:
                freq['allc'][word] += 1
                
                if word not in freq[country]:
                    freq[country][word] = 1
                else:
                    freq[country][word] += 1

sortedfreq = {}                    
for keys in freq:
    sortedfreq[keys] = dict(sorted(freq[keys].items(), key=lambda item: item[1], reverse=True))
                
with open('frequencies.json', 'w') as f:
    json.dump(freq, f)
    
with open('sortedfrequencies.json', 'w') as f:
    json.dump(sortedfreq, f)