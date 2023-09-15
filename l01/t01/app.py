from flask import Flask, render_template


app = Flask(__name__)


_categories = {
    'jackets-and-coats': {
        'title': 'Jackets & Coats',
        'id': 'jackets-and-coats'
    },
    'sleepwear-and-loungewear': {
        'title': 'Sleepwear & Loungewear',
        'id': 'sleepwear-and-loungewear'
    },
    'underwear-and-socks': {
        'title': 'Underwear & Socks',
        'id': 'underwear-and-socks'
    },
    'cologne-and-body': {
        'title': 'Cologne & Body',
        'id': 'cologne-and-body'
    },
}


@app.get('/')
def home():
    return render_template('home.html')


@app.get('/categories/<string:category_id>')
def category(category_id):
    category = _categories[category_id]

    return render_template('category.html', category=category)


@app.get('/categories')
def categories():
    return render_template('categories.html', categories=_categories.values())


if __name__ == '__main__':
    app.run()
