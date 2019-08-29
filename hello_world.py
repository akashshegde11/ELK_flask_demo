# Python 2.7
# ELK Demo - Flask

from flask import Flask
from elasticapm.contrib.flask import ElasticAPM
app = Flask(__name__)
app.config['ELASTIC_APM'] = {
    'SERVICE_NAME': 'my_service'
}
apm = ElasticAPM(app, logging=True)


@app.route('/')
def hello_world():
    return 'Hello, world! Good!'
