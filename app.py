from flask import Flask, jsonify, request
from products import get_products

app = Flask(__name__)


@app.route('/query')
def index():
    consumption = int(request.args['consumption'])

    lst = []
    for product in get_products():
        lst.append({'name': product.name, 'annual_costs': product.calculate_annual_costs(consumption=consumption)})

    return jsonify(sorted(lst, key=lambda elem: elem['annual_costs']))  # Сортировка по annual_costs


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
