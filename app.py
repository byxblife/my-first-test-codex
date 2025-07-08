from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    amount_str = request.form.get('amount', '').strip()
    direction = request.form.get('direction')

    # Validate amount
    if not amount_str:
        return render_template('index.html', error='請輸入金額')
    try:
        amount = float(amount_str)
    except ValueError:
        return render_template('index.html', error='金額必須為數字')

    # Currency conversion
    if direction == 'TWD_to_JPY':
        result = amount * 4.5
    elif direction == 'JPY_to_TWD':
        result = amount * 0.222
    else:
        return render_template('index.html', error='無效的轉換方向')

    formatted = f"{result:.2f}"
    return render_template('index.html', result=formatted)

if __name__ == '__main__':
    app.run(debug=True)
