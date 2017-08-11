def insertion_or_deletion(s1,s2):
    s1_len=len(s1)
    s2_len=len(s2)
    if abs(s1_len-s2_len)>1:
        return 2

    s1=s1.lower()
    s2=s2.lower()

    if s1_len>s2_len :
        for i in range(s2_len):
            if s1[i]!=s2[i]:
                if s1[i+1:]!=s2[i:]:
                    return 2
        return 1
    elif s1_len < s2_len:
        for i in range(s1_len):
            if s1[i] != s2[i]:
                if s1[i:] != s2[i+1:]:
                    return 2
        return 1
    else:
        for i in range(s1_len):
            if s1[i]!=s2[i]:
                return 2
        return 0

#print(insertion_or_deletion('Java','Python'))
#print(insertion_or_deletion('book','boot'))
#print(insertion_or_deletion('sin','sink'))
#print(insertion_or_deletion('dog','Dog'))
#print(insertion_or_deletion('poke','spoke'))
#print(insertion_or_deletion('poker','poke'))
#print(insertion_or_deletion('programing','programming'))
#print(insertion_or_deletion('is','that'))