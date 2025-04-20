from flask import Blueprint, render_template

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    return render_template('index.html')

@main_bp.route('/menu')
def menu():
    return render_template('menu.html')

@main_bp.route('/info')
def info():
    return render_template('info.html')

@main_bp.route('/story')
def story():
    return render_template('story.html')

@main_bp.route('/news')
def news():
    return render_template('news.html')

@main_bp.route('/sns')
def sns():
    return render_template('sns.html')

@main_bp.route('/parking')
def parking():
    return render_template('parking.html')
