from flask import Flask, request, render_template
from faq_manager import FAQManager

app = Flask(__name__)
faq_manager = FAQManager()
faq_manager.load_faqs('funderpro_faqs')
faq_manager.build_index()

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    user_query = request.form['query']
    results = faq_manager.search(user_query)
    return render_template('index.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)
