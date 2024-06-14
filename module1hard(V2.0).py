grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
a = sum(grades[0]) / len(grades[0])
b = sum(grades[1]) / len(grades[1])
c = sum(grades[2]) / len(grades[2])
d = sum(grades[3]) / len(grades[3])
e = sum(grades[4]) / len(grades[4])
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
s = sorted(list(students))
print(s)
my_dict = {s[0] : a, s[1] : b, s[2] : c, s[3] : d, s[4] : e}
print(my_dict)