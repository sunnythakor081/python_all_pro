def vow(lis):
    vowel = ("A","E","I","O","U")
    count = 0
    for i in lis:
      if i in vowel:
          count = count + 1
    return count

def rev(lis):
   rev_lis = lis[::-1]
   #print(rev_lis)
   return rev_lis

def peli(lis,lis2):
   if(lis==lis2):
      return True
   else:
      return False
   
    
