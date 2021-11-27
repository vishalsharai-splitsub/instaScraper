from flask import Blueprint
from flask import request
import sys
import os

from controllers import profileController

profileAPI = Blueprint("profileAPI", __name__)


@profileAPI.route("/details")
def profile():
    return profileController.getDetailsFromUsername(request)


@profileAPI.route("/getposts")
def posts():
    return profileController.getPostsFromUsername(request)


@profileAPI.route("/topposts")
def topPosts():
    return profileController.getTopPostsFromUsername(request)
