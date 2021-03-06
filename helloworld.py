from google.appengine.api import users

def application(environ, start_response):
    user = users.get_current_user()
    if user:
        start_response('200 OK', [('Content-Type','text/plain')])
        return ['Hello, {}!'.format(user.nickname())]
    else:
        start_response('302 Found', [('Location', users.create_login_url('/'))])
        return []
