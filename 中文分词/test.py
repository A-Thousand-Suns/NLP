def spaceTest():
    text = '　　武汉大学医学部病毒研究所教授杨占秋表示'
    for i in text.replace('\t', ''):
        print(ord(i))


if __name__ == '__main__':
    spaceTest()