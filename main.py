from flask import Flask, render_template
import requests

url = "https://worldwide-restaurants.p.rapidapi.com/search"

payload = {
	"language": "en_US",
	"limit": "100",
	"location_id": "297704",
	"currency": "USD"
}
headers = {
	"content-type": "application/x-www-form-urlencoded",
	"X-RapidAPI-Key": "a3eadde3c3msh1bc9661213fdecap10b701jsn1d429a73165f",
	"X-RapidAPI-Host": "worldwide-restaurants.p.rapidapi.com"
}

response = requests.post(url, data=payload, headers=headers)
app = Flask(__name__)

data = response.json()
size = len(data['results']['data'])

@app.route("/")
def home():
    return render_template("index.html", data=data, size=size)


if __name__ == "__main__":
    app.run(debug=True,port=8080)
