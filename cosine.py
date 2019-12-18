#defining and testing the function.
import re, math
from collections import Counter

WORD = re.compile(r'\w+')

def get_cosine(vec1, vec2):
     intersection = set(vec1.keys()) & set(vec2.keys())
     numerator = sum([vec1[x] * vec2[x] for x in intersection])

     sum1 = sum([vec1[x]**2 for x in vec1.keys()])
     sum2 = sum([vec2[x]**2 for x in vec2.keys()])
     denominator = math.sqrt(sum1) * math.sqrt(sum2)

     if not denominator:
        return 0.0
     else:
        return float(numerator) / denominator

def text_to_vector(text):
      words = WORD.findall(text)
      return Counter(words)

#testing the function
text1 = "Hum dil de chuke sanam"
text2 = "Hum dil de sanam"
vector1 = text_to_vector(text1)
vector2 = text_to_vector(text2)

cosine = get_cosine(vector1, vector2)

print ('Cosine:', cosine)


#applying the function to the datasets.
from itertools import islice
with open(r"C:\Users\Hp\Desktop\doggy.txt", "r") as infile:
    gen_line = islice(infile, 10)
    for line in gen_line:
        print(line)
        a = text_to_vector(line)
        print(a)
        
        with open(r"C:\Users\Hp\Desktop\doggy1.txt", "r") as infile:
            gen_line = islice(infile, 10)
            for line in gen_line:
                print(line)
                b = text_to_vector(line)
                print(b)

                x = get_cosine(a,b)
                if x > 0.75:
                    print ('Cosine:', x)