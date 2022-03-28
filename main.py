from flask import Flask, render_template, url_for

from data import db_session
from data.jobs import Jobs
from data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    # db_session.global_init('db/blogs.db')
    # db_sess = db_session.create_session()

    # user1 = User()
    # user1.name = "Пользователь 1"
    # user1.surname = 'фамилия1'
    # user1.about = "биография пользователя 1"
    # user1.email = "email@email.ru"
    # db_sess.add(user1)
    #
    # user2 = User()
    # user2.name = "Пользователь 2"
    # user2.surname = 'фамилия2'
    # user2.about = "биография пользователя 2"
    # user2.email = "email@email2.ru"
    # db_sess.add(user2)
    #
    # job1 = Jobs()
    # job1.team_leader = 1
    # job1.job = 'Это такая строка'
    # job1.work_size = 25
    # job1.collaborators = '2'
    # job1.is_finished = False
    # db_sess.add(job1)
    #
    # job2 = Jobs()
    # job2.team_leader = 2
    # job2.job = 'Это такая строка2'
    # job2.work_size = 256
    # job2.collaborators = '1, 2'
    # job2.is_finished = True
    # db_sess.add(job2)
    #
    # db_sess.commit()

    app.run(port=8081, host='127.0.0.1')


@app.route('/')
def main_page():
    db_session.global_init('db/blogs.db')
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).all()
    return render_template('index.html', jobs=jobs)


if __name__ == '__main__':
    main()
