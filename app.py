from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/dashboard')
def dashboard():
    stats = {
        'витрати': '₴ 45,230',
        'покази': '1,234,567',
        'кліки': '23,456',
        'конверсії': '1,234',
        'ctr': '1.9%',
        'cpc': '₴ 1.93'
    }
    return render_template('dashboard.html', stats=stats)

@app.route('/campaigns')
def campaigns():
    campaigns_list = [
        {'назва': 'Літній розпродаж', 'статус': 'Активна', 'бюджет': '₴ 5,000', 'витрачено': '₴ 3,420', 'roi': '+24%'},
        {'назва': 'Новий продукт', 'статус': 'Активна', 'бюджет': '₴ 10,000', 'витрачено': '₴ 7,890', 'roi': '+18%'},
        {'назва': 'Ретаргетинг', 'статус': 'Пауза', 'бюджет': '₴ 3,000', 'витрачено': '₴ 2,100', 'roi': '+31%'},
        {'назва': 'Бренд кампанія', 'статус': 'Активна', 'бюджет': '₴ 8,000', 'витрачено': '₴ 4,560', 'roi': '+12%'},
        {'назва': 'Тестова А/Б', 'статус': 'Завершена', 'бюджет': '₴ 2,000', 'витрачено': '₴ 2,000', 'roi': '+8%'},
    ]
    return render_template('campaigns.html', campaigns=campaigns_list)

@app.route('/reports')
def reports():
    return render_template('reports.html')

if __name__ == '__main__':
    app.run(debug=True)
