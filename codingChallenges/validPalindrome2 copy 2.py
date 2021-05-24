class Solution:

    
    def validPalindrome(self,s)->bool:

        
        if len(s) < 3:
            return True

        if(s.strip()=='') or len(s) == len(set(s)):
            return False
        

        largo=len(s)-1
        low=0

        def busqueda(s,low,largo):

            if largo>low:

                if s[largo]==s[low]:
                   return busqueda(s,low+1,largo-1)
                else:
                    return False
            return True



        while(largo>=low):

        #Cuando el primero y el ultimo caracter son iguales
            if s[low]==s[largo]:
                low+=1
                largo-=1
            
            else:
                if busqueda(s,low,largo-1) or busqueda(s,low+1,largo):
                    return True
                return False

        return True



x=Solution()
content="yd"
print(x.validPalindrome(content))