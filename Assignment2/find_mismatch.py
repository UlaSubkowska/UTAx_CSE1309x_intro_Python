def find_mismatch(s1,s2):
    if len(s1)!=len(s2):
        return 2

    s1=s1.lower()
    s2=s2.lower()
    mistakes=0

    for i in range(len(s1)):
        if s1[i]!=s2[i]:
            mistakes+=1

    if mistakes==0: return 0
    elif mistakes==1: return 1
    else: return 2


#print(find_mismatch('Python','Java'))
#print(find_mismatch('Hello There','helloothere'))
#print(find_mismatch('sin','sink'))
#print(find_mismatch('dog','Dog'))
#print(find_mismatch('is','that'))