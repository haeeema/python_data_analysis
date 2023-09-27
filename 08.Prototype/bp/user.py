from flask import Blueprint, session, redirect, flash

user_bp = Blueprint('user_bp', __name__)

menu = {'ho': 0, 'us': 1, 'cr': 0, 'ma': 0, 'sc': 0}


@user_bp.route('/login', methods=['GET', 'POST'])
def login():
    # admin, 관리자로 로그인했다고 가정
    flash('관리자님 환영합니다.')
    session['uid'] = 'admin'
    session['uname'] = '관리자'
    return redirect('/')


@user_bp.route('/logout')
def logout():
    session.pop('uid', None)
    session.pop('uname', None)
    # session.pop('quote', None)
    # session.pop('addr', None)
    return redirect('/')
