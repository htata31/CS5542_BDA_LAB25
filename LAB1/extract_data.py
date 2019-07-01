import matplotlib.pyplot as plt
import numpy as np
words_list = ["traffic", "signal", "highway", "intersection", "crosswalk"]

traffic_count = 0
signal_count = 0
highway_count = 0
intersection_count = 0
crosswalk_count = 0

"""
In the below funtion:
1.First I have initialized a list above with specific words which are needed for the statistics.
2.Searched each word in the line and doing the word count with the help of a counter.
3.Writing all the captions in which the words are present so that the pre processing of the data is done for our project 
theme.
"""


def extract():
    # prev_line = " "
    global traffic_count
    global signal_count
    global highway_count
    global intersection_count
    global crosswalk_count
    with open("Dataset/lematization_words.txt") as openfile:
        with open('Dataset/extracted_captions.txt', 'w') as f:
            for line in openfile:
                for i in range(len(words_list)):
                    # print(words_list[i])
                    if words_list[i] in line:
                        # print(line)
                        # if prev_line != line:
                        #     prev_line = line
                        f.write("%s" % line)
                        if words_list[i] == "traffic":
                            traffic_count = traffic_count + 1
                        elif words_list[i] == "signal":
                            signal_count = signal_count + 1
                        elif words_list[i] == "highway":
                            highway_count = highway_count + 1
                        elif words_list[i] == "intersection":
                            intersection_count = intersection_count + 1
                        elif words_list[i] == "crosswalk":
                            crosswalk_count = crosswalk_count+ 1


"""
1.For printing the counts this function is used 
"""


def printCounts():
    print("traffic_count", traffic_count)
    print("signal_count", signal_count)
    print("highway_count", highway_count)
    print("intersection_count", intersection_count)
    print("crosswalk_count", crosswalk_count)


"""
1. For plotting the counts in a bar plot Matplotlib is used and plotted it.
2. Took the counts in y-axis and labels in the x-axis.
3. Defined the colors for each bar.
4. Font size and the labels are mentioned in the plot.
"""


def plot_bar():
    labels = ["Traffic", "Signal", "Highway", "Intersection", "Crosswalk"]
    counts = [traffic_count, signal_count, highway_count, intersection_count, crosswalk_count ]
    my_colors = ['blue', 'green', 'red', 'orange', 'cyan']
    index = np.arange(len(labels))
    plt.bar(index, counts, color=my_colors)
    plt.xlabel('Words', fontsize=10)
    plt.ylabel('Count', fontsize=10)
    plt.xticks(index, labels, fontsize=10, rotation=30)
    plt.title('Counts of the following Words present in dataset')
    plt.show()


if __name__ == '__main__':
    extract()
    printCounts()
    plot_bar()


