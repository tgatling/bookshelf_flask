from flask import Flask
import logging

app = Flask(__name__)

# Set up logging
logging.basicConfig(filename='bookshelf.log', level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')

log = logging.getLogger('werkzeug')
log.disabled = True

from app import db, routes
