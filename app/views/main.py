from flask import Blueprint, render_template, request, redirect, url_for, flash

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

@main_bp.route('/recruitment')
def recruitment():
    return render_template('recruitment.html')

@main_bp.route('/recruitment/form')
def recruitment_form():
    return render_template('recruitment_form.html')

@main_bp.route('/recruitment/submit', methods=['POST'])
def submit_recruitment():
    # フォームデータの取得
    name = request.form.get('name')
    furigana = request.form.get('furigana')
    phone = request.form.get('phone')
    email = request.form.get('email')
    birthdate = request.form.get('birthdate')
    employment_type = request.form.get('employment_type')
    position = request.form.get('position')
    work_time = request.form.getlist('work_time')
    experience = request.form.get('experience')
    message = request.form.get('message')

    # ここでメール送信などの処理を実装
    # 例: send_email(name, email, ...)

    flash('応募ありがとうございます。内容を確認次第、ご連絡させていただきます。', 'success')
    return redirect(url_for('main.recruitment'))
