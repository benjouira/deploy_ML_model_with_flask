from flask import Flask , render_template , request
import model , company_image


app = Flask(__name__)



@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/predict", methods=['POST'])
def predict():
    cmnt = request.form['comment']

    result = model.predict_function(cmnt)
    return render_template('predict.html', data=result)


@app.route("/scraping")
def scraping():
    return render_template('scraping.html')

@app.route("/scraping", methods=['POST'])
def scrapy():
    cmp = request.form['search_company']
    result = list(company_image.scrape_company_info(cmp))
    result.append(cmp)
    return render_template('scraping.html', data=result)


if __name__ == "__main__":
    app.run(debug=True)

# cd app_web_flask
#  python -m flask run