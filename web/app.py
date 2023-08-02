from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    keyword = request.form['search_query']
    # 여기서 검색을 수행하거나 다른 원하는 작업을 수행할 수 있습니다.
    return f'검색어 "{keyword}"로 검색 결과를 보여줍니다.'

if __name__ == '__main__':
    app.run(debug=True)
