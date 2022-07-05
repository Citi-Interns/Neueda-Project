from flask import Blueprint
routes = Blueprint('routes', __name__)

from .AreaSelector import *
from .MailSender import *
from .MailingListEditor import *