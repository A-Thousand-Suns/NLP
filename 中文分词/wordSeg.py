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
                content = content + i
        content.replace('\n', '')
        content.replace('\r', '')
        #print(content)
        return content

    def cutSentence(self):
        content = self.readFile()
        pattern = r'：|？|,|\.|/|;|\'|`|\[|\]|<|>|\?|:|"|\{|\}|\~|!|@|#|\$|%|\^|&|\(|\)|-|=|\_|\+|，|。|、|；|‘|’|【|】|·|！| |…|（|）'
        for i in re.split(pattern, content):
            print(i)

if __name__ == '__main__':
    a = 'testCase.txt'
    b = 0
    c = wordSehmentation(a, b)
    c.cutSentence()