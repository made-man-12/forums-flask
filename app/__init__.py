from flask import Flask
import stores
app = Flask(__name__)
member_store = stores.MemberStore()
post_store = stores.PostStore()

from views import *
