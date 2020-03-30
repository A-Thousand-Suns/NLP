#coding = utf-8
import re
import threading

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

        print(sentenceList)
        return sentenceList

    def readDic(self):
        dicList = []

        with open(self.dicPath, 'r', encoding='utf-8') as file:
            for i in file.readlines():
                dicList.append(i.replace('\n', '').replace(' ', ''))

        return dicList

    def dicIndex(self):
        flag = 0
        dicIndex = {}
        with open(self.dicPath, 'r', encoding='utf-8') as file:
            for i in file.readlines():
                if(dicIndex.get(i[0])):
                    dicIndex[i[0]][1] = flag
                else:
                    dicIndex[i[0]] = [flag, flag]
                flag = flag + 1
        print(dicIndex)
        return dicIndex

    def maxMatch(self, sentence, dicList):
        print('******do function*******\n')
        wirteLock = threading.Lock()
        search = False
        pos = 0
        word = ''
        dicIndex = self.dicIndex()
        wirteLock.acquire()
        file = open('result.txt', 'a')

        while (sentence.__len__() != 0):
            print('rest sentence:' + sentence)
            print('pos is:' + str(pos))
            char = sentence[pos]
            pos = pos + 1

            if(not search):
                if(dicIndex.get(char)):
                    search = True
                    listToChoose = dicList[dicIndex[char][0]: dicIndex[char][1] + 1]
                    if sentence in listToChoose:
                        print('result is :' + sentence)
                        file.write(sentence + '\n')
                        return
                else:
                    file.write(char + '\n')
                    print('result is :' + char)
                    sentence = sentence[pos: ]
                    pos = 0
                    word = ''
                    search = False
                    continue

            word = word + char

            for j in listToChoose[:]:
                if (not(j.startswith(word))):
                    listToChoose.remove(j)

            if( word == sentence):
                file.write(word + '\n')
                print('result is :' + word)
                print('------------')
                return

            if(listToChoose.__len__() == 0):
                word = word[:pos-1]
                file.write(word + '\n')
                sentence = sentence[pos-1:]
                print('result is :' + word)
                print('------------')
                search = False
                pos = 0
                word = ''




        file.close()
        wirteLock.release()
        return

    def run(self):
        sentenceList = self.cutSentence()
        dicList = self.readDic()

        for i in sentenceList:
            t = threading.Thread(target=self.maxMatch, args=(i, dicList,))
            t.run()





if __name__ == '__main__':
    filePath = 'testCase.txt'
    dicPth = 'dictionary.txt'
    c = wordSehmentation(filePath, dicPth)
    c.run()
