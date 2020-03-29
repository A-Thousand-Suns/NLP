def spaceTest():
    text = '　　武汉大学医学部病毒研究所教授杨占秋表示'
    for i in text.replace('\t', ''):
        print(ord(i))

def dicProcessTest():
    flag = 0
    path = 'dictionary.txt'
    result = {}
    with open(path, 'r', encoding='utf-8') as file:
        for i in file.readlines():
            if (result.get(i[0])):
                result[i[0]][1] = flag
            else:
                result[i[0]] = [flag, flag]
            flag = flag + 1
    print(result)

def strTest():
    str = 'hello'
    str = str[0:3]
    print(str)



if __name__ == '__main__':
    strTest()