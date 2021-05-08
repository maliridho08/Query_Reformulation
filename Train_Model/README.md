#Data and Credit

dataset wikipedia dump tgl 1-4-2021
ypu can download file
	"idwiki-latest-pages-articles.xml.bz2" on wikipedia dump

source code :	https://gist.github.com/dieka13
		https://medium.com/@diekanugraha/membuat-model-word2vec-bahasa-indonesia-dari-wikipedia-menggunakan-gensim-e5745b98714d
		(dengan beberapa perubahan)

idwiki-latest-pages-articles.xml.bz2	-> wikidump tgl 1-4-2021

run extract_wiki.py
then
run train_word2vec

result:
idwiki_word2vec_200_new_lower.model.syn1neg.npy
idwiki_word2vec_200_new_lower.model.wv.vectors.npy
idwiki_word2vec_200_new_lower.model	-> MODEL!!!
