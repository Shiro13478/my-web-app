from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    message = ""
    if request.method == 'POST':
        # フォームから送信されたデータを受け取る（サーバーサイド処理）
        user_name = request.form.get('username')
        if user_name:
            message = f"こんにちは、{user_name}さん！サーバーが処理しました。"
    return render_template('index.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)