#coding = utf-8
import re
import copy

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
            sentenceList.append(i)

        return sentenceList

    def readDic(self):
        dicList = []

        with open(self.dicPath, 'r', encoding='utf-8') as file:
            for i in file.readlines():
                dicList.append(i.replace('\n', '').replace(' ', ''))

        return dicList

    def maxMatch(self, sentence, dicList):
        print(sentence, dicList)
        word = ''
        file = open('result.txt', 'w')
        listToChoose = copy.deepcopy(dicList)

        if sentence in dicList:
            print(sentence)
            file.write(sentence + ' ')
            return

        for i in sentence[:]:
            print('----------------------')
            word = word + i
            for j in listToChoose[:]:
                print(word)
                print('old dic:')
                print(listToChoose)
                if (not(j.startswith(word))):
                    listToChoose.remove(j)
                print('new dic:')
                print(listToChoose)

            if((word == sentence) or (listToChoose.__len__() == 0) or ((listToChoose.__len__() == 1) and (word in listToChoose))):
                listToChoose = copy.deepcopy(dicList)
                file.write(word + ' ')

                print('result is :' + word)
                word = ''

        file.close()
        return

    def run(self):
        sentenceList = self.cutSentence()
        dicList = self.readDic()

        for i in sentenceList:
            self.maxMatch(i,dicList)





if __name__ == '__main__':
    filePath = 'testCase.txt'
    dicPth = 'dictionary.txt'
    c = wordSehmentation(filePath, dicPth)
    c.run()