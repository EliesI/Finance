from flask import Flask, request
from src.user.user import User
from src.finance import Account

app = Flask(__name__)

account = Account(5000)

@app.route('/account', methods=['GET'])
def get_account():
    return account.to_json()

@app.route('/account', methods=['POST'])
def update_account():
    data = request.get_json()
    type = data.get('type')
    price = data.get('price')
    desc = data.get('description')
    account.add_expense(type, price, desc)
    return {'message': 'Expense added successfully'}

@app.route('/account/expense', methods=['GET'])
def get_expense():
    return account.json_expenses()

@app.route('/account/history', methods=['GET'])
def get_history():
    return account.json_history()

if __name__ == '__main__':
    app.run(debug=True)
