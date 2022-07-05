from flask import Blueprint
routes = Blueprint('routes', __name__)

from .main import *
from .MailSender import *
from .MailingListEditor import *