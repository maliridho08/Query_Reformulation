#Data and Credit

we use wikipedia dump, date 1-4-2021.
you can download the file for wikidump 1-4-2021 : 
https://dumps.wikimedia.org/idwiki/20210401/idwiki-20210401-pages-articles.xml.bz2

or if you want the lastest version you can go to : 
https://dumps.wikimedia.org/idwiki/latest/
and find file with name "idwiki-latest-pages-articles.xml.bz2 "

you dont need to convert the bz file cause the program can use it directly	


source code :	https://gist.github.com/dieka13
		https://medium.com/@diekanugraha/membuat-model-word2vec-bahasa-indonesia-dari-wikipedia-menggunakan-gensim-e5745b98714d
		(with some changes)

Use the following oder:

- first, run extract_wiki.py,

output:"id.wiki.new.lower". Use this as input for train_word2vec

- then run train_word2vec

result:
- idwiki_word2vec_200_new_lower.model.syn1neg.npy
- idwiki_word2vec_200_new_lower.model.wv.vectors.npy
- idwiki_word2vec_200_new_lower.model	-> MODEL!!!

download the result here : https://drive.google.com/drive/folders/123FInpBbdM1uIzj1Kb1MLy1pR7Hr8A3b?usp=sharing
you need to download all result file to run testing
	
