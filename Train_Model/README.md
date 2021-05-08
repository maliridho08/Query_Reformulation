#Data and Credit

dataset wikipedia dump tgl 1-4-2021

you can also download file
	"idwiki-latest-pages-articles.xml.bz2" on wikipedia dump for lastest wiki dump
	
or you can download from this page if you want use from date 1-4-2021

source code :	https://gist.github.com/dieka13
		https://medium.com/@diekanugraha/membuat-model-word2vec-bahasa-indonesia-dari-wikipedia-menggunakan-gensim-e5745b98714d
		(with some changes)

idwiki-latest-pages-articles.xml.bz2	-> wikidump tgl 1-4-2021

- first, run extract_wiki.py, 
output:"id.wiki.new.lower". Use this as input for:
- then run train_word2vec

result:
- idwiki_word2vec_200_new_lower.model.syn1neg.npy
- idwiki_word2vec_200_new_lower.model.wv.vectors.npy
- idwiki_word2vec_200_new_lower.model	-> MODEL!!!
