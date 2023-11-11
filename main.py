from flask import Flask, render_template, request
from model import Model
from time import time

app = Flask(__name__, template_folder='.')

model = Model()


@app.route('/search', methods=['GET'])
def index():
    start_time = time()
    query = request.args.get('query').strip()
    if query is None or query == '+':
        query = ''

    response = model.answer(model.Request(query))

    return render_template(
        'static/index.html',
        time="%.2f" % (time() - start_time),
        query=query,
        answer=response.answer,
        sources=response.sources,
    )


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
