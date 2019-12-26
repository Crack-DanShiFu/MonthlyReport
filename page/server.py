import hashlib

from sqlalchemy import func

from model.model import *


def hex_md5(s):
    m = hashlib.md5()
    m.update(s.encode('UTF-8'))
    return m.hexdigest()

