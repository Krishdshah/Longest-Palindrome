def longestpalindrome(s):
  pal=s[0]
  if 1<=len(s)<=1000 and s.isalnum():
    for i in range(0,len(s)):
      for j in range(0,len(s)):
        k=s[i:j+1]
       
        
        if k==k[-1:-len(k)-1:-1] and len(k)>len(pal):
          pal=k
          
  return pal
      
  
