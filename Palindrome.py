n=1345431
org=n
ans=0
while(n!=0):
    rem=n%10
    ans=ans*10+rem
    n=n//10
if(org==ans):
    print("Palindrome",ans)
else:
    print(" not palindrome",ans)

