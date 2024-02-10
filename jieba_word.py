import jieba

s = "中国是一个伟大的国家"

s1 = jieba.lcut(s) # 精确模式
print(s1)

s2 = jieba.lcut(s, cut_all=True) # 全模式
print(s2)

s3 = jieba.lcut_for_search(s) # 搜索引擎模式
print(s3)

# jieba.add_word(str)   向分词词典添加新词 str
