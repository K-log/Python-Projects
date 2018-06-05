import web
from web import form

render = web.template.render('templates/')

urls = (
    '/(.*)', 'index',
    '/login', 'login',
    '/logout', 'logout'
    
    )

#db = web.database(dbn='mysql', user='username', pw='password', db='dbname')

app = web.application(urls, globals())
session = web.session.Session(app, web.session.Diskstore('sessions'), initializer=('count': 0))

class index:
    def Get(self, name):
        return render.index(name)

class login:
    def POST(self)
        session.count += 1
        return str(session.count)

class logout:
    def POST(self):
        session.kill()
        return ""

if __name__ == "__main__": 
    app.run();
