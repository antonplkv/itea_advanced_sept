import shelve

filename = "mydb"
def create_user(username):

    with shelve.open(filename) as db:
        db.has_key(username)#Если есть такой юзер - эксепшн

        db[f'{username}_posts'] = ['post_1', 'post2']


def get_posts(username):

    with shelve.open(filename) as db:
        user_posts = db.get(f'{username}_posts')





