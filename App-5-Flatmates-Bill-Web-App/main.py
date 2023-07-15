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

    def post(self):
        bill_form = BillForm(request.form)

        bill = flat.Bill(float(bill_form.amount.data), bill_form.period.data)
        flatmate1 = flat.Flatmate(bill_form.name1.data, int(bill_form.days_in_house1.data))
        flatmate2 = flat.Flatmate(bill_form.name2.data, int(bill_form.days_in_house2.data))

        return render_template('bill_form_page.html',
                               name1=flatmate1.name,
                               name2=flatmate2.name,
                               amount1=flatmate1.pays(bill, flatmate2),
                               amount2=flatmate2.pays(bill, flatmate1),
                               billform=bill_form,
                               result=True)


class ResultsPage(MethodView):
    pass
    # def post(self):
    #     bill_form = BillForm(request.form)
    #
    #     bill = flat.Bill(float(bill_form.amount.data), bill_form.period.data)
    #     flatmate1 = flat.Flatmate(bill_form.name1.data, int(bill_form.days_in_house1.data))
    #     flatmate2 = flat.Flatmate(bill_form.name2.data, int(bill_form.days_in_house2.data))
    #
    #     return render_template('results.html',
    #                            name1=flatmate1.name,
    #                            name2=flatmate2.name,
    #                            amount1=flatmate1.pays(bill, flatmate2),
    #                            amount2=flatmate2.pays(bill, flatmate1))


class BillForm(Form):
    amount = StringField('Bill Amount: ', default=100)
    period = StringField('Bill Period: ', default='December 2020')

    name1 = StringField('Name: ', default='John')
    days_in_house1 = StringField('Days in the house: ', default=20)

    name2 = StringField('Name: ', default='Marry')
    days_in_house2 = StringField('Days in the house: ', default=10)

    button = SubmitField('Calculate')


app.add_url_rule('/', view_func=HomePage.as_view('home_page'))
app.add_url_rule('/bill_form', view_func=BillFormPage.as_view('bill_form_page'))
# app.add_url_rule('/results', view_func=ResultsPage.as_view('results_page'))

app.run(debug=True)
