class InvertedFile:
    def __init__(self, file_name):
        self.file = open(file_name, "r")
        self.file2 = self.file.read()

        lst = []
        file2 = self.file2

        for row in self.file2.split():
            if row != []:
                row = row.replace(',', '')
                row = row.replace('.', '')
                row = row.replace('!', '')
                row = row.replace('', '')
                row = row.replace(';', '')
                row = row.lower()
                lst.append(row)
        self.dic = dict()
        for i in range(0, len(lst)):
            if lst[i] not in self.dic:
                self.dic[lst[i]] = [i]
            elif lst[i] in self.dic:
                old = self.dic[lst[i]]
                old.append(i)

    def indices(self, word):

        if word in self.dic:
            return self.dic[word]
        else:
            return []




