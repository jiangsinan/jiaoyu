from mainapp import app
from mainapp.views import user_v
from flask_script import Manager
from flask import render_template
from models.user import db


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/create_db')
def create_database():
    db.create_all()
    return '创建数据库中的所有模型表成功'


@app.route('/drop_db')
def drop_database():
    db.drop_all()
    return '删除库中所有模型类对应的表'


if __name__ == '__main__':
    app.register_blueprint(user_v.blue, url_prefix='/user')

    db.init_app(app)

    manager = Manager(app)
    manager.run()
