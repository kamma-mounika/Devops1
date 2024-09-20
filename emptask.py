emp = {'eno':[1,2,3], 'ename':['a','b','c'], 'esal':[10000,22000,30000]}
print("\n The employee data set is:")
print(emp)
print("-------------------------------------")
print("\n The employee name is:",emp['ename'])
print("----------------------------------------")
print("\n employee salaries are:")
print("---------------------------------------")
for i in emp['esal']:
    print(i)
    