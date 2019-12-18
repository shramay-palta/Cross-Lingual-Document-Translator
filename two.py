import numpy as np
import string
from string import digits

def train(turkish_sentences,turkish_word_dict,english_sentences,english_word_dict):

	num_of_tur_word = len(turkish_word_dict)
	num_of_eng_word = len(english_word_dict)
		# em algorithm
	t_e_f_mat = np.full((len(english_word_dict), len(turkish_word_dict)), 1 / len(turkish_word_dict),dtype=float)
	#t_e_f_mat_prev = np.full((len(turkish_word_dict), len(english_word_dict)), 1,dtype=float)

	cnt_iter = 0
	while cnt_iter < 50	 :
		print("cnt_iter: ",end = '')
		print(cnt_iter+1)
		cnt_iter += 1
		#t_e_f_mat_prev = t_e_f_mat.copy()
		count_e_f = np.full((len(english_word_dict), len(turkish_word_dict)), 0, dtype=float)
		total_f = np.full((len(english_word_dict)),0, dtype=float)
		#s_total = np.full((len(tur_sen_words)),0,dtype=float)
		
		for idx_tur, tur_sen in enumerate(turkish_se/Users/anshupalta/Desktop/Lectures/Third Year/3-1/CS F469/Assignment/two.pyntences): #for all sentence pairs (e,f) do
			#compute normalization
			#print(tur_sen)
			tur_sen_words = tur_sen.split()
			s_total = np.full((len(tur_sen_words)),0,dtype=float)
			for idx_word in range(len(tur_sen_words)): #for all words e in e do
				tur_word = tur_sen_words[idx_word]
				idx_tur_in_dict =turkish_word_dict[tur_word]
				s_total[idx_word] = 0
				eng_sen_words = english_sentences[idx_tur].split()
				for eng_word in eng_sen_words: #for all words f in f do
					#idx_tur_in_dict =turkish_word_dict[tur_word]
					idx_eng_in_dict = english_word_dict[eng_word]
					s_total[idx_word] += t_e_f_mat[idx_eng_in_dict][idx_tur_in_dict]
				#end for
			#end for
			
			"""print(s_total,tur_sen)
			print()"""
			
			#collect counts
			tur_sen_words = tur_sen.split()
			for idx_word in range(len(tur_sen_words)): #for all words e in e do
				tur_word = tur_sen_words[idx_word]
				idx_tur_in_dict =turkish_word_dict[tur_word]
				eng_sen_words = english_sentences[idx_tur].split()
				for eng_word in eng_sen_words: #for all words f in f do
					#idx_tur_in_dict =turkish_word_dict[tur_word]
					idx_eng_in_dict = english_word_dict[eng_word]
					count_e_f[idx_eng_in_dict][idx_tur_in_dict] += t_e_f_mat[idx_eng_in_dict][idx_tur_in_dict] / s_total[idx_word]
					total_f[idx_eng_in_dict] += t_e_f_mat[idx_eng_in_dict][idx_tur_in_dict] / s_total[idx_word]
				#end for
			#end for
		#end for
			
			"""print(total_f)
			print()
			print(count_e_f)
			print()"""
		#estimate probabilities
		for eng_idx in  range(num_of_eng_word): #for all foreign words f do
			for tur_idx in range(num_of_tur_word): #for all English words e do
				if count_e_f[eng_idx][tur_idx] != 0 and total_f[eng_idx] != 0:
					t_e_f_mat[eng_idx][tur_idx] = count_e_f[eng_idx][tur_idx] / total_f[eng_idx]
			#end for
		#end for

		#end while

		
		t_e_f_mat = np.round(t_e_f_mat,3)
		#print(t_e_f_mat)
		
	return t_e_f_mat


f1 = open('C:/Users/RIJUL KATIYAR/Desktop/IR/new_english.txt',encoding = "utf8")
f2 = open('C:/Users/RIJUL KATIYAR/Desktop/IR/new_dutch.txt',encoding = "utf8")

list1 = []
list2 = []
for l in f1.readlines():
	list1.append(l)
f1.close()
for l in f2.readlines():
	list2.append(l)
f2.close()

for i in range(len(list1)):	
	#remove_digits = str.maketrans('', '', digits)
	str1 = list1[i].lower()
	str1 = str1.rstrip()
	#str1 = str1.translate(remove_digits)
	str2 = list2[i].lower()
	str2 = str2.rstrip()
	#str2 = str2.translate(remove_digits)
	
	str1 = str1.translate(str.maketrans('','', string.punctuation))
	str2 = str2.translate(str.maketrans('','', string.punctuation))
	list1[i] = str1
	list2[i] = str2
	
list1 = list1[:50000]
list2 = list2[:50000]
	


i = 0
j = 0
dict1 = {}
dict2 = {}
dict3 = {}
dict4 = {}
for l in range(len(list1)):
	res1 = list1[l].split()
	res2 = list2[l].split()
	for x in range(len(res1)):
		if res1[x] not in dict1.keys():
			dict1[res1[x]] = i
			dict3[i] = res1[x]
			i = i + 1
	for x in range(len(res2)):
		if res2[x] not in dict2.keys():
			dict2[res2[x]] = j
			dict4[j] = res2[x]
			j = j + 1
list1 = list1[:50000]
list2 = list2[:50000]
			
np.save("C:/Users/RIJUL KATIYAR/Desktop/IR/eng_dict",dict1)
np.save("C:/Users/RIJUL KATIYAR/Desktop/IR/du_dict",dict2)
np.save("C:/Users/RIJUL KATIYAR/Desktop/IR/eng_dictn",dict3)
np.save("C:/Users/RIJUL KATIYAR/Desktop/IR/du_dictn",dict4)
print(len(dict1.keys()))
print(len(dict2.keys()))


"""print(i)
print(j)
print(dict1["july"])
print(dict2["juli"])"""
"""print(dict2["vraag"])"""
			
'''	
print(list1)
print()
print(dict1)
print()
print(list2)
print()
print(dict2)
'''
#modelDutoEng = train(list1,dict1,list2,dict2)
#modelEngtoDu = train(list2,dict2,list1,dict1)

#np.save('C:/Users/RIJUL KATIYAR/Desktop/IR/modelDutoEng',modelDutoEng)
#np.save('C:/Users/RIJUL KATIYAR/Desktop/IR/modelEngtoDu',modelEngtoDu)

	
	

