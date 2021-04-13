import gensim
from gensim.models import word2vec

namaFileModel = "idwiki_word2vec_100_new_lower.model"
model = gensim.models.Word2Vec.load(namaFileModel)


#https://stackoverflow.com/questions/2358045/how-can-i-implement-a-tree-in-python
#from anytree import Node, RenderTree

from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory

import itertools



#query = input("Enter your query: ")
query = "apa itu penjual gorengan bakwan sayur" 
print("your query is: "+query) 

result = [[[]] for i in range(len(query.split()))]


total_similar_word = 2

stop_factory = StopWordRemoverFactory()
more_stopword = ['dengan', 'ia','bahwa','oleh','apa','siapa','dimana','kapan','mengapa','bagaimana','itu']
data_stopword = stop_factory.get_stop_words()+more_stopword
stopword = stop_factory.create_stop_word_remover()



for indeks,content in enumerate(query.split()):
    result[indeks][0]=content
    keyword = content       
    if keyword not in data_stopword:
        #print(indeks)
        hasil = model.most_similar(keyword, topn=total_similar_word)
        #print(type(hasil))
        #print(hasil)
        #print("Kata-kata yang mirip "+keyword+" :\n")
        #print('\n'.join(map(str, hasil)))
        for i in hasil :
            print(i[0])
            result[indeks].append(i[0])
        #hasil = model.most_similar_cosmul(positive=['perempuan', 'raja'], negative=['lelaki'])
        #print("lelaki-raja, perempuan-?:{}".format(hasil)
   
print("----")
print("Hasil pencarian kata yang mirip di Model dari Wikidump \n")
for i,c in enumerate(result):
    for j,content in enumerate(result[i]):
        if(len(result[i])<2):
            print("\033[1m >> {} << \033[0;0m".format(content))
        else:
            if(j==0):
                print("[{}]".format(content))
            else:
                print("\t-> {}".format(content))
    
            


print("----")
print("Hasil kombinasi query: \n")


final_result = []

for combination in itertools.product(*result):
    final_Sentence = ""
    for j in combination:
        final_Sentence = " ".join([final_Sentence, j])
    final_result.append(final_Sentence)
print("----")
print("your query is "+query)
print('\n'.join(map(str, final_result)))




























'''
def get_Final_Result(result, final_result, sumSimiliarWord, i):
    if(i<sumSimiliarWord):
        for j in range (0,3):
            get_Final_Result(result, finalResult, sumSimiliarWord, +1)
    else:
        for j in range(1, totalSimilarWord+2):
            do_Whatever(i,j)


def do_Whatever(i,j):
    sentenceResult = "{} {} {}".format(result[0][1],result[1][i],result[2][j])
    print(sentenceResult)
    print(i, j)



finalResult=get_Final_Result(result, finalResult, sumSimiliarWord, 0)
'''

'''
print(result[0][1],result[1][1],result[2][1])
print(result[0][1],result[1][1],result[2][2])
print(result[0][1],result[1][1],result[2][3])

print(result[0][1],result[1][2],result[2][1])
print(result[0][1],result[1][2],result[2][2])
print(result[0][1],result[1][2],result[2][3])

print(result[0][1],result[1][3],result[2][1])
print(result[0][1],result[1][3],result[2][2]) 
print(result[0][1],result[1][3],result[2][3]) 
'''
'''
print(result[0][0],result[1][0])
print(result[0][0],result[1][1])
print(result[0][0],result[1][2])
'''


'''
for i,c in enumerate(result):
    for j,content in enumerate(result[i]):
        print(result[0][0], result[1][j], result[2][j])
'''

'''
for i in range(1, totalSimilarWord+2):
    for j in range(1, totalSimilarWord+2):
        sentenceResult = "{} {} {}".format(result[0][1],result[1][i],result[2][j])
        finalResult.append(sentenceResult)
'''
'''
for i in finalResult:
    print(i)
'''          
                



'''
def printResult(list2d, earlySentence, newSentence, i, j, totalSimilarWord):
    
    if(i<len(list2d)):
        for j in range(len(list2d[i])):
            newSentence = earlySentence+" "+list2d[i][j]
            printResult(list2d, earlySentence, newSentence, )

printResult(result, result[0][0], '', 1, 0, totalSimilarWord)
'''

#for i in result[1]:
 #   print(i)



