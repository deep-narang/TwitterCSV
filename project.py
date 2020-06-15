punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

#removes any punctuations errors
def strip_punctuation(string):
    for pc in punctuation_chars:
        if pc in punctuation_chars:
            string=string.replace(pc, "")

    return string

#gets positive words into memory
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())

#counts the positive wpords in the sentence
def get_pos(string):
    count=0
    string=strip_punctuation(string)
    
    lst=string.split()

    for pc in positive_words:
        for w in lst:
            if w.lower() == pc:
                count+=1

    return count

#creates list of negative words in the memory
negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

#fn to get count of negative words in string
def get_neg(string):
    count=0

    string=strip_punctuation(string)
    lst=string.split()

    for nw in negative_words:
        for w in lst:
            if w.lower() == nw:
                count+=1

    return count

#opens twitter and data file
twitter=open("project_twitter_data.csv", "r")
data=open("resulting_data.csv", "w")

#fn to write data to file
def write_to_file(data):
    data.write("Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score")
    data.write("\n")

    lst_twitter=twitter.readlines()
    lst_twitter.pop(0)

    for line in lst_twitter:
        line=line.strip().split(",")
        data.write(f"{line[1]}, {line[2]}, {get_pos(line[0])}, {get_neg(line[0])}, {get_pos(line[0]) - get_neg(line[0])}")
        data.write("\n")

    return data

write_to_file(data)
data.close()
twitter.close()
