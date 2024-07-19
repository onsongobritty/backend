#SPEED DETECTOR

X = int(input("Enter the motorists speed:"))
if X <=70:
     print("Ok")
elif X >=71:
     print("Slow down")
    
    
    
#NET SALARY CALCULATOR
basic_salary = int(input("Enter your basic salary:"))

Payee_tax = 0.35
NHIF_Deductions = 0.06
Housing_Levy = 0.015
Personal_Relief = 2400

Gross_Salary = (basic_salary)
deductions = (NHIF_Deductions * Gross_Salary) + (Housing_Levy * Gross_Salary) + ((Payee_tax * Gross_Salary)- Personal_Relief)
Net_Salary = (basic_salary ) - deductions
print(Net_Salary)