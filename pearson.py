#pearson coefficient

import re,math
from collections import Counter

WORD = re.compile(r'\w+')

def pearson_correlation(vec1, vec2):
    if vec1:
        mean1 = sum(vec1)/len(vec1)
        mean2 = sum(vec2)/len(vec2)

        sub1 = [i - mean1 for i in vec1]
        sub2 = [i - mean2 for i in vec2]

        xy = [a * b for a, b in list(zip(sub1, sub2))]

        xsquared = [i * i for i in vec1]
        ysquared = [i * i for i in vec2]

        return sum(xy) / math.sqrt(sum(xsquared) * sum(ysquared))
     
 
def text_to_vector(text):
	words = WORD.findall(text)
	return Counter(words)

file1 = open(r"C:\Users\Hp\Desktop\doggy.txt", "r")
file2 = open(r"C:\Users\Hp\Desktop\doggy1.txt", "r")

text1 = 1


while text1:
    text1 = file1.readline()
    text2 = file2.readline()
    vector1 = text_to_vector(text1)
    vector2 = text_to_vector(text2)
    #print((vector1.values()))
    v1 = list(vector1.values())
    v2 = list(vector2.values())
    temp = pearson_correlation(v1,v2)
    print(temp)