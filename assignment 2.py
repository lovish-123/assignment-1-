#person income tax
flattaxrate = 20
standardDeduction= 10000
additionaldeductionallowed=3000
a = int(input("number of dependents is "))
b = int(input("gross income to the nearest penny is"))
taxableincome=(b) - (standardDeduction) - (additionaldeductionallowed*a)
tax = taxableincome*0.2
print(tax)