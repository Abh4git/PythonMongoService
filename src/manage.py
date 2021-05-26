import os
import unittest

from app.main.model import products

from flask_script import Manager
from app.main import create_app, db
from flask_cors import CORS, cross_origin
#importing additional routes
from app.main import routes
app = create_app(os.getenv('BOILERPLATE_ENV') or 'dev')
app.app_context().push()
#CORS(app,resources={ r'/*': {'origins': '*'}}, supports_credentials=True)
# Set CORS options on app configuration
CORS(app, resources={ r'/*': {'origins': [
    'http://localhost:3000'  # React
      # React
  ]}}, supports_credentials=True)
app.config['CORS_HEADERS'] = 'Content-Type'
#Adding additional routes
app.add_url_rule('/api/test', view_func=routes.test)
app.add_url_rule('/api/product', view_func=routes.getProductsList)
app.add_url_rule('/api/product/add', view_func=routes.addProduct,methods=['POST'])

#@app.after_request
#def after_request(response):
#  response.headers.add('Access-Control-Allow-Origin', 'http://localhost:3000')
#  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
#  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
#  response.headers.add('Access-Control-Allow-Credentials', 'true')
#  return response

manager = Manager(app)
#migrate = Migrate(app, db)
@manager.command
def run():
    db.connect('productinfo')
    app.run(debug=True, host='0.0.0.0')

#from app.main import create_app

#A default route here
@app.route('/')
def home():
   return "RetailStore API!"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port=5000)

@manager.command
def test():
    """Runs the unit tests."""
    tests = unittest.TestLoader().discover('app/test', pattern='test*')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1
if __name__ == '__main__':
    manager.run()