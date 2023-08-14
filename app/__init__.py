from flask import Flask, render_template, redirect
from .forms import SimpleForm
from .config import Configuration
from .models import db, SimplePerson

print("CONFIG", dir(Configuration))

app = Flask(__name__, instance_path="/home/isales/appacademy-2022-Nov-E/6-Module/4-week/practice/assessment-for-sprint-18-practice-a-flask")
app.config.from_object(Configuration)
db.init_app(app)

@app.route("/")
def index():
    return render_template("main_page.html")

@app.route("/simple-form", methods=["POST"])
def post_form():
    form = SimpleForm()
    if form.validate_on_submit():
        # new_person = SimplePerson(
        #     name = form.data["name"],
        #     age = form.data["age"],
        #     bio = form.data["bio"]
        # )
        new_person = SimplePerson()
        form.populate_obj(new_person)
        db.session.add(new_person)
        db.session.commit()
        return redirect("/")
    return "Bad Data"

@app.route("/simple-form")
def get_form():
    form = SimpleForm()
    return render_template("simple_form.html", form=form)

@app.route("/simple-form-data")
def form_data():
    ppl = SimplePerson.query.filter(SimplePerson.name.like("M%"))
    return render_template("simple_form_data.html", people=ppl)