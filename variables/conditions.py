# if applicant has high income AND good cradits then Elidable for Lone..
 
print('Using AND operator')
highIncome=True
goodCradit=True

if highIncome and goodCradit:
    print('Elidable for lone..\n')

print('Using OR operator')
highIncome=False
goodCradit=True

if highIncome or goodCradit:
    print('Elidable for lone..\n')


# NOT Operator
# It's inverts any Boolen value given to it.

# Let's implement it like goodCardit and noCriminalRecords then 
# Elidable for lone..

print('Using NOT operator')
goodCardit=True
hasCriminalRecords=False

if goodCardit and not hasCriminalRecords:
    print('Elidable for lone..')

