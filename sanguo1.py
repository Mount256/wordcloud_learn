from wordcloud import WordCloud
from wordcloud import ImageColorGenerator
from PIL import Image
import numpy as np
from jieba import *

def getText(filename):
    text = open("{}".format(filename), encoding='utf-8').read()
    sign = '''！~·@￥……*“”‘’\n（）{}【】；："'「，」。-、？\u3000\ufeff'''
    for ch in sign: # 特殊符号替换成空格
        text = text.replace(ch, ' ')
    return text

def wordCount(text, N):
    words = lcut(text) # 精确分词
    counts = {} # 字典类型

    for word in words:
        if len(word) < 2:
            continue
        if word not in counts:
            counts[word] = 0
        else:
            counts[word] += 1

    temp = sorted(counts.items(), key=lambda d: d[1], reverse=True) # 按计数值逆序排序
    result = dict(temp[1:N+1])

    #fout = open('oops.txt', 'wt')
    #print(result, file=fout)
    #fout.close()

    return result

def drawWordCloud(data, N):
    # 创建词云对象，配置参数
    c = WordCloud(
        width=400,
        height=400,
        font_path="C:\Windows\Fonts\STXINGKA.TTF", # 设置字体
        repeat=False,  # 表示单词是否可以重复出现
        mask=np.array(Image.open("三国.png")),  # 给词云生成轮廓用的参数,不需要做成轮廓的背景应为白色
        background_color="white",  # 背景颜色
        max_words=N  # 词云的最大单词数
    )
    result_str = ' '.join(data.keys())
    c.generate(result_str)  # 指定词云的文本文件
    c.to_file("自制结果1.jpg")  # 将生成的词云文件输入到一个文件中

if __name__ == '__main__':
    N = 200
    text = getText('三国演义utf8.txt')
    result = wordCount(text, N)
    drawWordCloud(result, N)
