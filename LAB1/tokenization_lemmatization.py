import pandas as pd
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer


lemmatizer = WordNetLemmatizer()
names_list = []

"""
In the below function 
1.First the dataset is read with the help of pandas.
2.Parsed the data set and maintained 2 different variables for the caption data and urls.
3.After partitioning the data the caption is given for the word_tokenize function where it tokenizes the sentences .
4.Now the tokenized words are given to the lemmatizer and the words are joined to form a sentence.
5.The lemmatized line output is written in a text file.
6.The text file which is generated with lemmatized sentences, with that text file the statistics will be done in 
extract_data.py
"""


def tokenization_lemmetization():
    df = pd.read_csv('Dataset/Train.tsv', header=None, usecols=[0])
    dflist = df[0].tolist()
    print(len(df))
    print(len(dflist))
    with open('Dataset/lematization_Words.txt', 'w') as f:
        for i in range(len(dflist)):
            line = str(dflist[i])
            names_list.append(line.rsplit('\t', 2)[0])
            url = line[(line.find("http")):len(line)]
            caption = line.rsplit('\t', 2)[0]
            tokenized_words = word_tokenize(caption)
            lemmatized_output = ' '.join([lemmatizer.lemmatize(w) for w in tokenized_words])
            f.write("%s\n" % lemmatized_output)
            # if(url != ""):
            #     f.write("%s\n" % url)


if __name__ == '__main__':
    tokenization_lemmetization()
