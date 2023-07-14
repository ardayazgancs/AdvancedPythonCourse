import webbrowser

from fpdf import FPDF


class Bill:
    """
    Object that contains data about a bill, such as total amount and period of the bill.
    """

    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Flatmate:
    """
    Create a flatmate person who lives in the flat and pays a share of the bill.
    """

    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill, flatmate2):
        weight = self.days_in_house / (self.days_in_house + flatmate2.days_in_house)
        return weight * bill.amount


class PdfReport:
    """
    Creates a Pdf file that contains data about the flatmates such as their names, their due amounts and the period of
    the bill.
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        flatmate1_pay = str(round(flatmate1.pays(bill, flatmate2), 2))
        flatmate2_pay = str(round(flatmate2.pays(bill, flatmate1), 2))

        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        # Insert icon
        pdf.image('./files/house.png', w=30, h=30)

        # Insert title
        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=0, h=80, txt='Flatmates Bill', border=0, align='C', ln=1)

        # Insert period label and value
        pdf.set_font(family='Times', size=14, style='B')
        pdf.cell(w=100, h=40, txt='Period:', border=0)
        pdf.cell(w=150, h=40, txt=bill.period, border=0, ln=1)

        # Insert name and due amount of the first flatmate
        pdf.set_font(family='Times', size=12)
        pdf.cell(w=100, h=25, txt=flatmate1.name, border=0)
        pdf.cell(w=150, h=25, txt=flatmate1_pay, border=0, ln=1)

        # Insert name and due amount of the second flatmate
        pdf.cell(w=100, h=25, txt=flatmate2.name, border=0)
        pdf.cell(w=150, h=25, txt=flatmate2_pay, border=0, ln=1)

        pdf.output(self.filename)

        webbrowser.open(self.filename)


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
