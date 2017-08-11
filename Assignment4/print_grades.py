from read_file import*

def print_grades(file_name):
    results=create_grades_dict(file_name)
    print('{0: ^11}|{1: ^20}| Test_1 | Test_2 | Test_3 | Test_4 |{2: ^8}|'.format('ID','Name','Avg.'))
    for key in results:
        ID=key; name=results[key][0]
        test_1=results[key][1]
        test_2=results[key][2]
        test_3=results[key][3]
        test_4=results[key][4]
        average= results[key][5]
        print('{0:11}|{1:20}|{2:8}|{3:8}|{4:8}|{5:8}|{6:8}|'.format(ID,name,test_1,test_2,test_3,test_4,average))

print(print_grades('test_file.txt'))