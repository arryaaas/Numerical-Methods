from flask import Flask, render_template, request
from scripts import *
from task import *
import os

app = Flask(__name__)

content_json = read_json("data/content_data.json")
method_json = read_json("data/method_data.json")
input_json = read_json("data/input_data.json")

@app.route("/")
def home():
    content = content_json["metode numerik"]
    return render_template(
        "home.html",
        content=content
    )

@app.route("/menu/<group>")
def menu(group):
    content = content_json[group]
    return render_template(
        "menu.html",
        content=content
    )

@app.route("/form/<group>/<member>")
def form(group, member):
    template = content_json[group][4]
    return render_template(
        template,
        group=group,
        member=member
    )

@app.route("/result/<group>/<member>", methods=["POST"])
def result(group, member):
    template = content_json[group][5]
    form_data = {}
    keys = content_json[group][3]
    for item in keys:
        form_data[item] = eval(input_json[group][item])
    final_result = eval(method_json[group][member])
    if len(final_result) == 3:
        return render_template(
            template,
            member=member,
            content=final_result[0],
            tables=[
                final_result[1].to_html(
                    classes="data", 
                    header="true", 
                    index=False
                )
            ],
            conclusion=final_result[2]
        )
    else:
        return render_template(
            template,
            member=member,
            content=final_result[0],
            message=final_result[1]
        )

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, port=port)