def create_grades_dict(file_name):
    my_file = open(file_name, 'r')
    data = my_file.readlines()
    my_file.close()
    my_dict = {}
    for line in data:
        line = line.strip('\n ').split(',')
        stud_ID = line[0]; name = line[1]
        my_dict[stud_ID] = [0] * 6
        my_dict[stud_ID][0] = name
        for inx in range(2, len(line), 2):
            temp_str = line[inx].strip()
            if temp_str == 'Test_1':
                my_dict[stud_ID][1] = int(line[inx + 1])
            elif temp_str == 'Test_2':
                my_dict[stud_ID][2] = int(line[inx + 1])
            elif temp_str == 'Test_3':
                my_dict[stud_ID][3] = int(line[inx + 1])
            elif temp_str == 'Test_4':
                my_dict[stud_ID][4] = int(line[inx + 1])
        average = sum(my_dict[stud_ID][1:5]) / 4
        my_dict[stud_ID][5] = average
    return my_dict

#print(create_grades_dict('test_file.txt'))