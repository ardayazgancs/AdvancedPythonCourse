from flask import Flask, render_template, request
from flask.views import MethodView
from wtforms import Form, StringField, SubmitField
from flatmates_bill import flat

app = Flask(__name__)


class HomePage(MethodView):
    def get(self):
        return render_template('index.html')


class BillFormPage(MethodView):
    def get(self):
        bill_form = BillForm()
        return render_template('bill_form_page.html', billform=bill_form)


class ResultsPage(MethodView):
    def post(self):
        bill_form = BillForm(request.form)

        bill = flat.Bill(float(bill_form.amount.data), bill_form.period.data)
        flatmate1 = flat.Flatmate(bill_form.name1.data, int(bill_form.days_in_house1.data))
        flatmate2 = flat.Flatmate(bill_form.name2.data, int(bill_form.days_in_house2.data))

        return f"{flatmate1.name} pays {flatmate1.pays(bill, flatmate2)}"


class BillForm(Form):
    amount = StringField('Bill Amount: ')
    period = StringField('Bill Period: ')

    name1 = StringField('Name: ')
    days_in_house1 = StringField('Days in the house: ')

    name2 = StringField('Name: ')
    days_in_house2 = StringField('Days in the house: ')

    button = SubmitField('Calculate')


app.add_url_rule('/', view_func=HomePage.as_view('home_page'))
app.add_url_rule('/bill_form', view_func=BillFormPage.as_view('bill_form_page'))
app.add_url_rule('/results', view_func=ResultsPage.as_view('results_page'))

app.run(debug=True)
