import random,sys
class SubCipher:
    def __init__(self):
        self.PlainText=input("Write the Plain Text:")
        self.Alpha="abcdefghijklmnopqrstuvwxyz"

    def GenerateKey(self):
        list1= list(self.Alpha)
        random.shuffle(list1)
        self.key= ''.join(list1)

    def translate(self,mode,cypher=""):
        translate1=""
        char1=self.Alpha
        char2=self.key
        if mode=='D':
            char1,char2=char2,char1
            self.PlainText=cypher
            pass
        for char in self.PlainText:
            #print(char)
            if (char==' ' or char==',' or char=='.'):
                translate1 = translate1 + char
                pass
            else:
                temp=char1.find(char)
                #print(temp)
                translate1=translate1+char2[temp]
                pass
            pass
        print(translate1)
        return translate1
        pass
    pass

obj1=SubCipher()
obj1.GenerateKey()
print("The cyphertext is: ",end="")
msg1=obj1.translate('E')
print("The decrypted text is: ",end="")
msg2=obj1.translate('D',msg1)


