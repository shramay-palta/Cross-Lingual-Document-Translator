import numpy as np
import random
from random import sample
f1 = open('C:/Users/RIJUL KATIYAR/Desktop/IR/English_Updated.txt',encoding = "utf8")
list1 = []
for l in f1.readlines():
	list1.append(l)
f1.close()
f2 = open('C:/Users/RIJUL KATIYAR/Desktop/IR/Dutch_Updated.txt',encoding = "utf8")	
list2 = []
for l in f2.readlines():
	list2.append(l)
f2.close()
print(list2[1])
print(list1[1])
print(len(list1[1].split()))



list3 = []
list4 = []

list3, list4 = zip(*random.sample(list(zip(list1, list2)), 500000))
print(list3[8])
print(list4[8])

list5 = []
list6 = []

for i in range(len(list3)):
	if(len(list3[i].split()) <= 15):
		list5.append(list3[i])
		list6.append(list4[i])
		
		
y = open("new_english.txt","a+",encoding = "utf-8")
z = open("new_dutch.txt","a+",encoding = "utf-8")
for i in range(len(list5)):
	y.write(list5[i])
	z.write(list6[i])
	
y.close()
z.close()

	


		

	

	
		





