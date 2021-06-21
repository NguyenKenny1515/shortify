from flask import render_template, url_for, redirect, request
from shortify import app
from shortify.forms import UrlForm
import requests
import os

url = "https://api.rebrandly.com/v1/links"
headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "apikey": os.environ.get("SHORTIFY_API_KEY")
}

@app.route("/", methods=['GET', 'POST'])
def home():
    form = UrlForm()
    if form.validate_on_submit():
        response = requests.request("POST", url, 
            json={"destination": form.url.data}, headers=headers)
        response_json = response.json()

        return redirect(url_for("shortened", 
                                orig_url=response_json.get("destination"), 
                                short_url=response_json.get("shortUrl")))
    return render_template("home.html", form=form)

@app.route("/shortened")
def shortened():
    return render_template("shortened.html", 
                            title="Shortened URL", 
                            orig_url=request.args.get("orig_url"), 
                            short_url=request.args.get("short_url"))