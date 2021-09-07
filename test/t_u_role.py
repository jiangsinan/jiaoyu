from mainapp import app
from models.user import *
from utils import crypt


def add_user():
    u1 = User()
    u1.phone = '18895399920'
    u1.auth_key = crypt.pwd('123456')
    u1.nick_name = 'Jsn@666'

    db.session.add(u1)
    print('add user-id:', u1.id)
    db.session.commit()
    print('commit user-id:', u1.id)


def add_roles():
    r1 = Role(name='系统管理员')
    r2 = Role(name='普通用户')
    db.session.add_all((r1, r2))
    db.session.commit()
    print(r1.id, r2.id)


def add_user_role():
    u = User.query.get(1)
    admin_role = Role.query.filter(Role.name.__eq__('系统管理员'))[0]
    print(u.nick_name, admin_role.name)
    u.roles.append(admin_role)
    db.session.commit()
    print('ok')


def query_user_role(user_id=1):
    u = User.query.get(user_id)
    for role in u.roles:
        print(role.name)


if __name__ == '__main__':
    app.app_context().push()
    db.init_app(app)
    # add_user()
    # add_roles()
    # add_user_role()
    query_user_role(1)
