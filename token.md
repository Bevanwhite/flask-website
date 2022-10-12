>>> from itsdangerous import URLSafeTimedSerializer
>>> from origami import app
/home/beva/Documents/python/flask-website/venv/lib/python3.10/site-packages/flask_sqlalchemy/__init__.py:872: FSADeprecationWarning: SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead and will be disabled by default in the future.  Set it to True or False to suppress this warning.
  warnings.warn(FSADeprecationWarning(
>>> serial = URLSafeTimedSerializer(app.config['SECRET_KEY'])
>>> serial
<itsdangerous.url_safe.URLSafeTimedSerializer object at 0x7fcaa2bb3520>
>>> token = s.dumps({'user_id':2})
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 's' is not defined
>>> token = serial.dumps({'user_id':2})
>>> print(token)
eyJ1c2VyX2lkIjoyfQ.Y0csWA.tkUMfiVoFd9U9Z2w5iJy_k_LRyg
>>> token
'eyJ1c2VyX2lkIjoyfQ.Y0csWA.tkUMfiVoFd9U9Z2w5iJy_k_LRyg'
>>> serial.loads(token,max_age=20)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/beva/Documents/python/flask-website/venv/lib/python3.10/site-packages/itsdangerous/timed.py", line 210, in loads
    base64d, timestamp = signer.unsign(
  File "/home/beva/Documents/python/flask-website/venv/lib/python3.10/site-packages/itsdangerous/timed.py", line 148, in unsign
    raise SignatureExpired(
itsdangerous.exc.SignatureExpired: Signature age 121 > 20 seconds
>>> serial.loads(token,max_age=6000)
{'user_id': 2}
>>> serial.loads(token,max_age=150)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/beva/Documents/python/flask-website/venv/lib/python3.10/site-packages/itsdangerous/timed.py", line 210, in loads
    base64d, timestamp = signer.unsign(
  File "/home/beva/Documents/python/flask-website/venv/lib/python3.10/site-packages/itsdangerous/timed.py", line 148, in unsign
    raise SignatureExpired(
itsdangerous.exc.SignatureExpired: Signature age 152 > 150 seconds
>>> serial.loads(token,max_age=154)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/beva/Documents/python/flask-website/venv/lib/python3.10/site-packages/itsdangerous/timed.py", line 210, in loads
    base64d, timestamp = signer.unsign(
  File "/home/beva/Documents/python/flask-website/venv/lib/python3.10/site-packages/itsdangerous/timed.py", line 148, in unsign
    raise SignatureExpired(
itsdangerous.exc.SignatureExpired: Signature age 159 > 154 seconds
>>> exit()