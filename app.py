from flask import Flask, render_template

app = Flask(__name__)

# Predefined list of wheel segments.
SEGMENTS = [
    "放鬆一下",
    "喝口水",
    "做伸展",
    "打給朋友",
    "出去走走",
    "寫日記",
    "聽音樂",
    "吃點心",
    "閱讀十分鐘",
    "冥想練習",
]


@app.route('/', methods=['GET'])
def index():
    """Render the spinning wheel game."""
    return render_template('index.html', segments=SEGMENTS)


if __name__ == '__main__':
    app.run(debug=True)
