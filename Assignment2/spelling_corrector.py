from find_mismatch import*
from find_single_insertion_or_deletion import*

def spelling_corrector(s1,list_of_words):
    s1=[i.lower() for i in s1.split()]
    list_of_words=[i.lower()for i in list_of_words]
    output=''

    for string in s1:
        for word in list_of_words:
            if find_mismatch(string,word)==1 or insertion_or_deletion(string,word)==1:
                output+=word+' '
                break
        else: output+=string+' '
    output=output.strip()
    return output

print(spelling_corrector('Thes is the Firs cas',['that','first','case','car']))
print(spelling_corrector('programing is fun and eesy',['programming','this','fun','easy','book']))
print(spelling_corrector('Thes is vary essy',['this','is','very','very','easy']))
print(spelling_corrector('Wee lpve Pythen',['we','Live','In','Python']))
