from wordcloud import WordCloud
from wordcloud import ImageColorGenerator
from PIL import Image
import numpy as np

txt = "Python Java C++ JavaScript PHP Ruby Swift Kotlin Go Rust"     # 示例文本

# 创建词云对象，配置参数
c = WordCloud(
    width=400,
    height=400,
    font_path=None,
    repeat=True, # 表示单词是否可以重复出现
    mask=np.array(Image.open("love.png")), # 给词云生成轮廓用的参数,不需要做成轮廓的背景应为白色
    background_color="white", # 背景颜色
    max_words=150 # 词云的最大单词数
)
c.generate(txt)  # 指定词云的文本文件
c.to_file("词云图.jpg")    # 将生成的词云文件输入到一个文件中
