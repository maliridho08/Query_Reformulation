model file can be downloaded in Train_Model Folder
https://github.com/maliridho08/Query_Reformulation/tree/main/Train_Model

you need to download all train result file to run the testing:
- idwiki_word2vec_200_new_lower.model.syn1neg.npy
- idwiki_word2vec_200_new_lower.model.wv.vectors.npy
- idwiki_word2vec_200_new_lower.model -> MODEL!!!



main_for_baseline will reformulate all word except some word we have listed in stopword.


main for x_ 
we have modify the query for this type of reformulation.
some word that unlikely to be reformulated is added x_ in front of it.
example : siapa nama lengkap soekarno
become : siapa nama lengkap x_soekarno

the program won't reformulate the word soekarno
so in the result query, the word "soekarno" still remain soekarno


program will ask input for number similiar word you want to generate of each word.
this will effect the total result query
because the program will do combination of all old word and new word
but the order of result query just follow the initial query
