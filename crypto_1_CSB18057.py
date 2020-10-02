class generate_perm:
    def __init__ (self,set_bit): #init method to define parameters
        if (set_bit==1):
            self.string=input("Give String Input:")
            pass
        else:
            self.string="abcdefghijklmnopqrstuvwxyz"
            pass
        self.f=open("test1.txt", "w")


    def convert_to_string(self,list1): # function to convert list to string
        return ''.join(list1)
    
    def permutation(self,list2,l,r): # function to generate permutation using DFS algorithm

        if (l==r):
            self.f.write(self.convert_to_string(list2))
            self.f.write("\n")
            pass

        else:
            for i in range(l,r+1):
                list2[l],list2[i]=list2[i],list2[l]
                self.permutation(list2,l+1,r)
                list2[l],list2[i]=list2[i],list2[l]
                pass
            pass
        pass
    
    def permute(self): #permutation calling function
        list3=list(self.string)
        length_list3=(len(list3)) 
        self.permutation(list3,0,length_list3-1)

a=int(input("Press 1 for user unput  and 2 for all alphabet permutation:"))
obj1=generate_perm(a)
obj1.permute()
