class VigenereCypher:
    def __init__(self,key):
        self.key=key
        self.PlainText=input("Write the Plain Text:")
        self.PlainText=self.PlainText.lower()
        self.NewKey=self.GenerateKey()
        pass
    def GenerateKey(self):
        if (len(self.PlainText)-len(self.key)==0):
            return self.key
        else:
            TempKey=self.key[:]
            for i in range(len(self.PlainText)-len(self.key)):
                TempKey=TempKey+self.key[i%len(self.key)]
                pass
            return TempKey
    
    def encryption(self):
        encrypted_msg=""
        for i in range(len(self.PlainText)):
            if(self.PlainText[i]==' ' or self.PlainText[i]=='.' or self.PlainText[i]==','):
                encrypted_msg=encrypted_msg+self.PlainText[i]
                pass
            else:
                temp=(ord(self.PlainText[i])+ord(self.NewKey[i]))%26
                temp=temp+ord('a')
                encrypted_msg=encrypted_msg+chr(temp)
                pass
            pass
        print("The cypher is:",encrypted_msg)
        return encrypted_msg
        pass
    def decryption(self,string):
        decrypted_msg=""
        for i in range(len(string)):
            if(string[i]==' ' or string[i]=='.' or string[i]==','):
                decrypted_msg=decrypted_msg+string[i]
                pass
            else:
                temp=(ord(string[i])-ord(self.NewKey[i])+14)%26
                temp=temp+ord('a')
                decrypted_msg=decrypted_msg+chr(temp)
                pass
            pass
        print("The decrypted message is:",decrypted_msg)


    
obj1=VigenereCypher('abcd')
message=obj1.encryption()
obj1.decryption(message)




