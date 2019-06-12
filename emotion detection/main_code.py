punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())

negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())


# THIS FUNCTION IS USED BY OTHER FUNCTIONS TO REMOVE PUNTUATION MARKS FROM THE STRING
def strip_punctuation(stg):
    for x in stg:
        if x in punctuation_chars:
            stg = stg.replace(x, '')
    return stg


# THIS FUNCTION IS TO COUNT THE NUMBER OF POSITIVE WORDS IN THE TWEET
def get_pos(stg):
    s = strip_punctuation(stg)
    co_pos = 0
    lt = list(s.strip().split())
    for x in lt:
        x = x.lower()
        if x in positive_words:
            co_pos += 1

    return co_pos


# THIS FUNCTION IS TO COUNT THE NUMBER OF NEGATIVE WORDS IN THE TWEET
def get_neg(stg):
    s = strip_punctuation(stg)
    co_neg = 0
    lt = list(s.strip().split())
    for x in lt:
        x = x.lower()

        if x in negative_words:
            co_neg += 1
    return co_neg


# OPEN FILE TO WORK ON
fil = open('project_twitter_data.csv', 'r')
st = fil.readlines()

lst = []
for x in st:
    lst.append(x.split(','))

# MAKING THE LIST OF NUMBER OF POSITIVE  AND NEGATIVE WORDS AND THEIR NET SCORE
positive = []
negative = []
net_score = [' Net Score']

lt = 0

while lt < len(st):
    positive.append(get_pos(lst[lt][0]))

    negative.append(get_neg(lst[lt][0]))
    lt += 1
positive[0] = ' Positive Score'
negative[0] = ' Negative Score'
n = 1
while n < len(positive):
    k = positive[n] - negative[n]
    net_score.append(k)
    n += 1

# GET LIST OF NUMBER OF RETWEETS AND NUMBER OF REPLIES


retweet = []
replies = []
for n in lst:
    retweet.append(n[1])
    replies.append(n[2])
retweet[0] = 'Number of Retweets'
replies[0] = ' Number of Replies '
# CREATING A NEW CSV FILE resulting_data.CSV AND INSERTING DATA IN IT.

new_fil = open('resulting_data.csv', 'w')

m = 0
while m < (len(positive) - 1):
    new_fil.write(
        str(retweet[m]) + ',' + str(replies[m][:-1]) + ',' + str(positive[m]) + ',' + str(negative[m]) + ',' + str(
            net_score[m]) + '\n')
    m += 1
new_fil.write(str(retweet[-1]) + ',' + str(replies[-1]) + ',' + str(positive[-1]) + ',' + str(negative[-1]) + ',' + str(
    net_score[-1]))

new_fil.close()
fil.close()

