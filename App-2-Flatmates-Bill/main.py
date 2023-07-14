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
        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        # Insert title
        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=0, h=80, txt='Flatmates Bill', border=1, align='C', ln=1)

        # Insert period label and value
        pdf.cell(w=100, h=40, txt='Period:', border=1)
        pdf.cell(w=150, h=40, txt=bill.period, border=1, ln=1)

        # Insert name and due amount of the first flatmate
        pdf.cell(w=100, h=40, txt=flatmate1.name, border=1)
        pdf.cell(w=150, h=40, txt=flatmate1.pays(bill), border=1, ln=1)

        # Insert name and due amount of the first flatmate
        pdf.cell(w=100, h=40, txt=flatmate1.name, border=1)
        pdf.cell(w=150, h=40, txt=str(round(flatmate1.pays(bill, flatmate2), 2)), border=1, ln=1)

        # Insert name and due amount of the second flatmate
        pdf.cell(w=100, h=40, txt=flatmate2.name, border=1)
        pdf.cell(w=150, h=40, txt=str(round(flatmate2.pays(bill, flatmate1), 2)), border=1, ln=1)

        pdf.output(self.filename)


_bill = Bill(amount=120, period='April 2021')
_flatmate1 = Flatmate(name='John', days_in_house=20)
_flatmate2 = Flatmate(name='Marry', days_in_house=25)

PdfReport = PdfReport('PdfReport.pdf')
PdfReport.generate(_flatmate1, _flatmate2, _bill)
