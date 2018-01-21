# coding=utf-8
# 1～3 行分别导入了画图的库，词云生成库和jieba的分词库
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import jieba
# 读取本地的文件
#text_from_file_with_apath = open('./tests/01.txt').read()
text_from_file_with_apath = open('title_acl_2016.txt').read()
# 使用jieba进行分词，并对分词的结果以空格隔开
stoplist = {}.fromkeys([ line.strip() for line in open("stopword.txt") ])
wordlist_after_jieba = jieba.cut(text_from_file_with_apath, cut_all=True)
wordlist_after_jieba = [word.encode('utf-8') for word in list(wordlist_after_jieba)]

wordlist_after_jieba = [word for word in list(wordlist_after_jieba) if word not in stoplist]
# print wordlist_after_jieba

wl_space_split = " ".join(wordlist_after_jieba)
#对分词后的文本生成词云
from PIL import Image
import numpy as np
abel_mask = np.array(Image.open("mumu.jpg"))
my_wordcloud = WordCloud(background_color="white",mask=abel_mask,width=1000,height=860,font_path='/root/zmp/seminar/wordCloud/simfang.ttf',margin=4).generate(wl_space_split)
# 用pyplot展示词云图
plt.imshow(my_wordcloud)
plt.axis("off")
plt.show()