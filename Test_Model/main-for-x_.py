import csv
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
import itertools #to final result
import gensim
from gensim.models import word2vec




def main():
    #load model
    namaFileModel = "idwiki_word2vec_200_new_lower.model"
    model = gensim.models.Word2Vec.load(namaFileModel)

    #stopword
    stop_factory = StopWordRemoverFactory()
    more_stopword = ['dengan', 'ia', 'bahwa', 'oleh', 'apa', 'siapa', 'dimana', 'kapan', 'mengapa',
                    'bagaimana','saya', 'kamu','kau','kita','engkau','dikau','kami','mereka','dia',
                    'bisa','akan','ingin','mau','harus','mungkin','boleh','perlu','butuh','menjadi',
                    'sudah','belum','telah']
    data_stopword = stop_factory.get_stop_words()+more_stopword
    stopword = stop_factory.create_stop_word_remover()


    #read csv
    input_file = input ("masukkan nama file input\n-jangan lupa tulis .csv-\t:")
    daftar_query = open(input_file)
    query_list = []
    print()
    #input the result file name
    output_file = input("masukkan nama file output\n-jangan lupa tulis .csv-\t:")
    print()
    #how many similiar word we want to search
    total_similar_word = int(input("masukkan jumlah similiar word\nyang ingin dicari per kata\n-input integer-\t:"))
    #containing word search result from all sentence 
    all_wsr = []
    
   
    #looping through document
    for x,query in enumerate(daftar_query):
        #result for every search of similiar word in model
        #make two dimension list, will contain word from current query, eg: [['apa'],['ibukota'],['x_indonesia']]
        word_search_result = [[[]] for i in range(len(query.split()))]
        #looping through sentences word by word , eg apa then ibukota and then indonesia
        for indeks,word in enumerate(query.split()):
            #input original word to indeks 0 | as much as word in sentence
            word_search_result[indeks][0]=word                                  #eg: input apa in index [0][0] then ibukota in index [1][0] then x_indonesia in index [2][0]
            if word not in data_stopword and "x_" not in word:                  #eg: apa will be skipped while ibukota will execute code below, and x_indonesia will be skipped
                hasil = model.wv.most_similar(word, topn=total_similar_word)    #eg: will search similair word of ibukota
                for i in hasil :                                                #eg: 'ibukotanya' and 'kota'
                    word_search_result[indeks].append(i[0])                     #ibukotanya will be in index [1][1] then kota in index [1][2]
            '''
            if "x_" in word:                    
                word_search_result[indeks][0] = word[2:]        #menghilangkan x_ ; x_indonesia -> indonesia ; this is for readable result
            '''
        query_list.append(query)#just copy all original query
        all_wsr.append(word_search_result)                                      #will save all result from [apa],[ibukota,ibukotanya,kota],[indonesia] to all_wsr[index] ;the index is depend on query's order itself
       
    
    
    #for i,query in enumerate(query_list):
        #printSearchResult(query, all_wsr[i], total_similar_word)
    
    #doing combination between word to form new sentence (query)
    final_result = []
    for result in all_wsr:
        for combination in itertools.product(*result):
            final_Sentence = ""
            for j in combination:
                final_Sentence = " ".join([final_Sentence, j])
            final_Sentence = final_Sentence[1:]
            final_result.append(final_Sentence)
            #print("----")
            #print("your query is "+query)
            #print('\n'.join(map(str, final_result)))
    
                    

    #write to csv
    with open(output_file, mode='w', newline="") as qr_file:
        qr_file = csv.writer(qr_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        i=0
        for q in final_result:
            i+=1
            qr_file.writerow([q])
    
    print("task success")
    

def printSearchResult(query, result, total_similar_word):
    print("----")
    print("Hasil pencarian kata yang mirip di Model dari Wikidump \n")
    print(query)
    for i,c in enumerate(result):
        for j,content in enumerate(result[i]):
            if(len(result[i])<total_similar_word):
                print("\033[1m >> {} << \033[0;0m".format(content))
            else:
                if(j==0):
                    print("[{}]".format(content))
                else:
                    print("\t-> {}".format(content))
        




if __name__ == '__main__': main()



