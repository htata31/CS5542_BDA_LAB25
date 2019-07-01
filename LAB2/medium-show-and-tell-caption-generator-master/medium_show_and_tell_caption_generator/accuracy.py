import nltk
from itertools import zip_longest
from nltk.tokenize import word_tokenize
from nltk.translate.bleu_score import sentence_bleu
from PyRouge.pyrouge import Rouge


from pycocoevalcap.meteor.meteor import Meteor
from pycocoevalcap.cider.cider import Cider

r = Rouge()
list = []


def accuracy():
    scorers = [
        # (Meteor(), "METEOR"),
        (Cider(), "CIDEr")
    ]
    final_scores = {}
    with open("../txtfiles/pred.txt") as f2,  open("../txtfiles/true.txt") as f1:
        k = 0
        j = 0
        for line in f2:
            list.append(line)
        for line1 in f1:
            y_true = []
            y_true_dict = {}
            y_pred_dict = {}
            for i in range(3):
                y_true.append(word_tokenize(list[k]))
                k = k + 1
            y_true_line = list[k-4]
            y_true_dict[j] = str(list[k])
            # print(y_true)
            y_pred = word_tokenize(line1)
            y_pred_line = line1
            y_pred_dict[j] = str(line1)
            j = j+1
            for scorer, method in scorers:
                # print(type(y_pred_dict))
                score, scores = scorer.compute_score(y_true_dict, y_true_dict)
                if type(score) == list:
                    for m, s in zip(method, score):
                        final_scores[m] = s
                else:
                    print("%s: %0.3f" % (method, score))
                    final_scores[method] = score
            BLEUscore = sentence_bleu(y_true, y_pred, weights=(1, 0, 0, 0))
            [precision, recall, f_score] = r.rouge_l([y_true_line], [y_pred_line])
            print("Precision is :"+str(precision)+"\nRecall is :"+str(recall)+"\nF Score is :"+str(f_score))
            print("BLEUscore is: ", BLEUscore)
            # print(final_scores)


if __name__ == "__main__":
    accuracy()
