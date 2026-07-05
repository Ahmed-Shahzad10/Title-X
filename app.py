import os
import re

from flask import Flask, redirect, render_template, request, session, url_for
from API import get_listings

app = Flask(__name__)
app.secret_key = os.environ.get('FLASK_SECRET_KEY', 'listiq-dev-secret')


def parse_titles(result):
    return [
        re.sub(r'^\s*\d+[\).\-\s]+', '', line).strip()
        for line in result.splitlines()
        if re.sub(r'^\s*\d+[\).\-\s]+', '', line).strip()
    ]


def add_recent_title(product):
    recent_titles = session.get('recent_titles', [])
    clean_product = product.strip()

    if clean_product:
        recent_titles = [title for title in recent_titles if title != clean_product]
        recent_titles.insert(0, clean_product)
        session['recent_titles'] = recent_titles[:10]


@app.route('/')
def home():
    return render_template('landing.html')


@app.route('/tool')
def tool():
    return render_template(
        'tool.html',
        recent_titles=session.get('recent_titles', []),
        product='',
        titles=[],
    )

@app.route('/optimize', methods=['POST'])
def optimize():
    product = request.form.get('product', '').strip()

    if not product:
        return redirect(url_for('tool'))

    result = get_listings(product)
    add_recent_title(product)

    return render_template(
        'tool.html',
        recent_titles=session.get('recent_titles', []),
        product=product,
        titles=parse_titles(result),
    )


@app.route('/faq')
def faq():
    return render_template('faq.html')

if __name__ == '__main__':
    app.run(debug=True)


