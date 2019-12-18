import numpy as np
import string

eng_dict = np.load('C:/Users/RIJUL KATIYAR/Desktop/IR/eng_dict.npy',allow_pickle = 'TRUE').item()
du_dict = np.load('C:/Users/RIJUL KATIYAR/Desktop/IR/du_dict.npy',allow_pickle = 'TRUE').item()
mat = np.load('C:/Users/RIJUL KATIYAR/Desktop/IR/modelEngtoDu.npy')
eng_dictn = np.load('C:/Users/RIJUL KATIYAR/Desktop/IR/eng_dictn.npy',allow_pickle = 'TRUE').item()
du_dictn = np.load('C:/Users/RIJUL KATIYAR/Desktop/IR/du_dictn.npy',allow_pickle = 'TRUE').item()

f1 = open('C:/Users/RIJUL KATIYAR/Desktop/IR/test_e_to_d.txt',encoding = "utf8")
list1 = []
for l in f1.readlines():
	list1.append(l)
f1.close()
for i in range(len(list1)):	
	#remove_digits = str.maketrans('', '', digits)
	str1 = list1[i].lower()
	str1 = str1.rstrip()
	#str1 = str1.translate(remove_digits)
	
	
	str1 = str1.translate(str.maketrans('','', string.punctuation))
	list1[i] = str1
y = open("result_e_to_d.txt","a+",encoding = "utf-8")
y.seek(0)
y.truncate()
print(list1)
for input1 in list1:
	input1 = input1.lower()
	input1 = input1.rstrip()
	input1 = input1.translate(str.maketrans('','', string.punctuation))
	print(input1)


	l = input1.split()
	output = list()
	for x in (l):
		if x in eng_dict.keys():
			output.append(du_dictn[np.argmax(mat[eng_dict[x]])])
			#output.append(x)
			
	var = str()
	for i in (output):
		var += i
		var += " "
	y.write(var)
	y.write("\n")
y.close()
	