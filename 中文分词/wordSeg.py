#coding = utf-8
class wordSehmentation:
    def __init__(self, filePath, dicPath):
        self.filePath = filePath
        self.dicPath = dicPath

    def readFile(self):
        str = ''
        with open(self.filePath, 'r', encoding='utf-8') as file:
            for i in file.readlines():
                str = str + i
        print(str)



if __name__ == '__main__':
    a = 'testCase.txt'
    b = 0
    c = wordSehmentation(a, b)
    c.readFile()