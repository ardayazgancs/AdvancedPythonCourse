from flat import Bill, Flatmate
from reports import PdfReport

_amount = float(input('Hey user, enter the bill amount: '))
_period = input('What is the bill period? E.g. December 2020: ')

_name1 = input('What is your name? ')
_days_in_house1 = int(input(f'How many days did {_name1} stay in the house during the bill period? '))

_name2 = input('What is the name of the other flatmate? ')
_days_in_house2 = int(input(f'How many days did {_name2} stay in the house during the bill period? '))

_bill = Bill(amount=_amount, period=_period)
_flatmate1 = Flatmate(name=_name1, days_in_house=_days_in_house1)
_flatmate2 = Flatmate(name=_name2, days_in_house=_days_in_house2)

print(f'{_flatmate1.name} pays: ', _flatmate1.pays(bill=_bill, flatmate2=_flatmate2))
print(f'{_flatmate2.name} pays: ', _flatmate2.pays(bill=_bill, flatmate2=_flatmate1))

pdfReport = PdfReport(filename='PdfReport.pdf')
pdfReport.generate(flatmate1=_flatmate1, flatmate2=_flatmate2, bill=_bill)
