#coding = utf-8
import re

class wordSehmentation:
    def __init__(self, filePath, dicPath):
        self.filePath = filePath
        self.dicPath = dicPath

    def readFile(self):
        content = ''
        with open(self.filePath, 'r', encoding='utf-8') as file:
            for i in file.readlines():
                content = content + i.replace('\n', '').replace(' ', '').replace(chr(12288), '')
        return content

    def cutSentence(self):
        content = self.readFile()
        sentenceList = []
        pattern = r'“|”|\n|-|：|？|,|\.|/|;|\'|`|\[|\]|<|>|\?|:|"|\{|\}|\~|!|@|#|\$|%|\^|&|\(|\)|-|=|\_|\+|，|。|、|；|‘|’|【|】|·|！| |…|（|）'

        for i in re.split(pattern, content):
            print(i)
            sentenceList.append(i)

        return sentenceList

    def readDic(self):
        dicList = []

        with open(self.dicPath, 'r', encoding='utf-8') as file:
            for i in file.readlines():
                dicList.append(i.replace('\n', '').replace(' ', ''))

        return dicList





if __name__ == '__main__':
    filePath = 'testCase.txt'
    dicPth = 'dictionary.txt'
    c = wordSehmentation(filePath, dicPth)
    c.cutSentence()