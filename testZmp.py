# coding=utf-8
# 1～3 行分别导入了画图的库，词云生成库和jieba的分词库
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import jieba
# 读取本地的文件
#text_from_file_with_apath = open('/root/zmp/seminar/wordCloud/LDA&textrank.txt').read()
text_from_file_with_apath = open('./tests/01.txt').read()
# 使用jieba进行分词，并对分词的结果以空格隔开
wordlist_after_jieba = jieba.cut(text_from_file_with_apath, cut_all=True)
wl_space_split = " ".join(wordlist_after_jieba)
#对分词后的文本生成词云
from PIL import Image
import numpy as np
abel_mask = np.array(Image.open("alice-color.png"))
my_wordcloud = WordCloud(background_color="white",mask=abel_mask,width=1000,height=860,font_path='/root/zmp/seminar/wordCloud/simfang.ttf',margin=4).generate(wl_space_split)
# 用pyplot展示词云图
plt.imshow(my_wordcloud)
plt.axis("off")
plt.show()