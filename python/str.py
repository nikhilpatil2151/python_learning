#mystr= "nikhil r patil"
#print(mystr[0:5])
#print(len(mystr))
#print(mystr.endswith("patil"))
#print(mystr.count('i'))
#print(mystr.capitalize())
#print(mystr.find("r"))
#print(mystr.upper())
#print(mystr.replace("r", "raj"))
print("Basic salary") 
n1=input ()

TA=(15*int(n1)/100)
DA=(70*int(n1)/100)
HRA=(20*int(n1)/100)
total_sal=(n1+TA+DA+HRA)

print("Tralleving Allowance=",float(TA))
print("Day Allowance=",float(DA))
print("House Rent Allowance=",float(HRA))
print("Total Salary=",float(total_sal))