from flask import Blueprint
from flask import request
from flask import jsonify
import sys
import os

from controllers import postController
from classes.post import constants

postAPI = Blueprint("postAPI", __name__)


@postAPI.route("/details")
def post():
    return postController.getPostFromShortcode(request)


@postAPI.route("/common")
def common():
    return postController.getCommonFromShortcodes(request)
