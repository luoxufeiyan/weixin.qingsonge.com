""" 怼骚扰电话的蓝本 """
from flask import Blueprint

api_v1 = Blueprint('api_v1', __name__)

from . import diss_call