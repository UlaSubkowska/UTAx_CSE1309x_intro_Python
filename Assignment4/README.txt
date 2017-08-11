 Part 1: Read file and create dictionary

Write a function that accepts a string as the name of a file. Assuming that the file is a text file which includes
name and grades of students, your function should read the file and return a dictionary with the exact format 
as shown below: The format of the input file is: 

Student ID, Last_name,  Test_x, grade, Test_x, grade, ..
Student ID, Last_name,  Test_x, grade, Test_x, grade, ..
.... 

An example of the input file is shown below.
1000123456, Rubble, Test_3,  80, Test_4 , 80
1000123459, Chipmunk, Test_4, 96, Test_1, 86 , Quiz_1 , 88

OUTPUT: {'1000123456': ['Rubble', 0, 0, 80, 80, 40.0], '1000123459': ['Chipmunk', 86, 0, 0, 96, 45.5]}

 

Part 2: Print grades

Write a function called print_grades that accepts the name of a file (string) as input argument. Assuming the 
format of the file is the same as the file in part 1. Using the grades dictionary, your function should print the 
names, grades, and averages of students with the exact format shown below. Your function should return 
None after printing the grades.

     ID            |       Name       | Test_1 | Test_2 | Test_3 | Test_4 |    Avg.  |
1000123210 | Bunny            |    100 |      100 |     100 |     100 |  100.00 |
1000123456 | Rubble           |        0 |          0 |       80 |       80 |    40.00 |
1000123458 | Duck              |      86 |        93 |         0 |       94 |    68.25 |
