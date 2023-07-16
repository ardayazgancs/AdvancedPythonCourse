from flask.views import MethodView
from wtforms import Form, StringField, SubmitField
from flask import Flask, render_template, request
from calorie import Calorie
from temperature import Temperature

app = Flask(__name__)


class HomePage(MethodView):
    def get(self):
        return render_template('index.html')


class CaloriesFormPage(MethodView):
    def get(self):
        calories_form = CaloriesForm()

        return render_template('calories_form_page.html',
                               caloriesform=calories_form)

    def post(self):
        calories_form = CaloriesForm(request.form)

        temperature = Temperature(calories_form.country.data, calories_form.city.data)
        calorie = Calorie(float(calories_form.weight.data),
                          float(calories_form.height.data),
                          float(calories_form.age.data),
                          temperature.get())

        return render_template('calories_form_page.html',
                               result=True,
                               calories=calorie.calculate(),
                               caloriesform=calories_form)


class CaloriesForm(Form):
    weight = StringField('Weight (in kg): ', default=70)
    height = StringField('Height (in cm): ', default=175)
    age = StringField('Age: ', default=32)
    country = StringField('Country: ', default='USA')
    city = StringField('City: ', default='San Francisco')
    button = SubmitField('Calculate')


app.add_url_rule('/', view_func=HomePage.as_view('home_page'))
app.add_url_rule('/calories_form', view_func=CaloriesFormPage.as_view('calories_form_page'))

app.run(debug=True)
