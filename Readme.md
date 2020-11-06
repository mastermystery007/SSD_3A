Q1)Explanation : Find all the leaders of an employee using recursion .
Store the values in a global list.
Extract the values from global list and then clear it .
Find leaders of all employees and then take intersection of all lists.
Now find the first common leader in any of previos leader list[list[0] in my case(Leaders of employee 0)] with the intersection list. This will be lowest common leader. 
Changes:
a)Instead of taking seperate list for leaders of each employee I made a common list of list. i'th row had leaders of employee i.Previosly had made 2 seperate lists ,one for each employee.
b)Previous I had 2 global lists and would fill in leaders of employee in specific list . Now I have one global list and i clear it after every iteration.
c)Previously  i would just find first person common to both . Now I find the intersection of all bosses lists of each employee  and then find the first common boss in list0(Bosses of employee 0 ) with the final intersection list(Common bosses to all).
ASSUMPTIONS:
a)Employee cant be leader of himself.
b)Employee names are strings.

Q2)Explanation : Same as previous time. Calculated total number of days from 0/0/0000 to current date and then made a subtraction . 
Changes:
a)Took a SINGLE command line argument that will specify which dd/mm/yy or mm/dd/yy for both the dates.
If number of arguments is greater than 0 then check for mm/dd/yy command-line argument and interchange months and days if it is the case . Else do nothing .
Changes-line 149 to 156 . Added the check for command line arguments 
Assumptions:
Only single command line argument will be given which will be common for both dates . 


Q3)Explanation :Free time slot generation is same as before .Just loop theough every file and carry out same procedure as previous question .For common time slot we need to loop over every file and see if all employees are free at that minute (I have divided the working day into 480 minutes.)
Changes: Loop over all files in a directory (line 155)
         Getting common slot from array of arrays as opposed to 2 single arrays(line 95-119)
Assumptions:
1)All the employees will be stored in "Employees' folder.
2)Employees order will not matter.


Github Link:https://github.com/mastermystery007/SSD_3A/tree/PartB
