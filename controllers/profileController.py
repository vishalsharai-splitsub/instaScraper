import sys
import os
import json
from flask import request

from classes.profile import profileClass
from classes.profile import constants
from utils import utils
import errorConstants as errors

profiles = {}


# Handles all the validations that need to made for the details request
def getDetailsFromUsername(request):
    request = request.get_json()
    processedData = utils.validateRequest(request, constants.REQUEST_SCHEMA["details"])
    if processedData["success"] == False:
        return utils.sendResponse(processedData['success'],processedData['error'],processedData['data'])
    params = {}
    params["username"] = request["username"]
    params["getUsers"] = request["getUsers"] if ("getUsers" in request.keys()) else []
    details = createProfile(params)
    if details["success"] == False:
        return utils.sendResponse(details['success'],details['error'],details['data'])
    return utils.sendResponse(True, "", details["data"])


# Handles all the validations that need to made for the getposts request
def getPostsFromUsername(request):
    request = request.get_json()
    processedData = utils.validateRequest(request, constants.REQUEST_SCHEMA["posts"])
    if processedData["success"] == False:
        return utils.sendResponse(processedData['success'],processedData['error'],processedData['data'])
    params = {}
    params["username"] = request["username"]
    params["n"] = request["limit"]
    params["getLists"] = request["getLists"] if ("getLists" in request.keys()) else []
    posts = structuredPostFromProfile(params)
    if posts["success"] == False:
        return utils.sendResponse(posts['success'],posts['error'],posts['data'])
    return utils.sendResponse(True, "", posts["data"])


# Handles all the validations that need to made for the getTopPosts request
def getTopPostsFromUsername(request):
    request = request.get_json()
    processedData = utils.validateRequest(request, constants.REQUEST_SCHEMA["topPosts"])
    if processedData["success"] == False:
        return utils.sendResponse(processedData['success'],processedData['error'],processedData['data'])
    params = {}
    params["username"] = request["username"]
    params["percent"] = request["percent"]
    posts = getTopPosts(params)
    if posts["success"] == False:
        return utils.sendResponse(posts['success'],posts['error'],posts['data'])
    return utils.sendResponse(True, "", posts["data"])


def profiler(username):
    if username in profiles.keys():
        return
    else:
        profilesData = profileClass.Profile(username)
        profiles[username] = profilesData
        return


def createProfile(params):
    profiler(params["username"])
    profilesData = profiles[params["username"]].getDetails(params["getUsers"])
    if profilesData["success"] == False:
        return utils.sendResponse(profilesData['success'],profilesData['error'],profilesData['data'])
    return utils.classResponse(True, "", profilesData["data"])


def structuredPostFromProfile(params):
    profiler(params["username"])
    posts = profiles[params["username"]].getNPosts(params["n"])
    if posts["success"] == False:
        return utils.sendResponse(posts['success'],posts['error'],posts['data'])
    posts = posts["data"]
    postDetails = {}
    for data in posts:
        element = {}
        element["mediaid"] = data.post.mediaid
        element["shortcode"] = data.post.shortcode
        element["comments"] = data.post.comments
        element["likes"] = data.post.likes
        element["caption"] = data.post.caption
        element["owner_username"] = data.post.owner_username
        element["date_utc"] = data.post.date_utc
        element["url"] = data.post.url
        if "likes" in params["getLists"]:
            likesData = data.getLikeUsernames()
            if likesData["success"] == False:
                return utils.sendResponse(likesData['success'],likesData['error'],likesData['data'])
            element["likesList"] = likesData["data"]
        if "comments" in params["getLists"]:
            commentsData = data.getCommentUsernames()
            if commentsData["success"] == False:
                return utils.sendResponse(commentsData['success'],commentsData['error'],commentsData['data'])
            element["commentsList"] = commentsData["data"]
        if "followersActivity" in params["getLists"]:
            followerActivityData = data.getFollowerActivity()
            if followerActivityData["success"] == False:
                return utils.sendResponse(followerActivityData['success'],followerActivityData['error'],followerActivityData['data'])
            element["followerActivity"] = followerActivityData["data"]
        postDetails[data.post.mediaid] = element
    return utils.classResponse(True, "", postDetails)


def getTopPosts(params):
    profiler(params["username"])
    posts = profiles[params["username"]].getTopPosts(params["percent"])
    if posts["success"] == False:
        return utils.sendResponse(posts['success'],posts['error'],posts['data'])
    return utils.classResponse(True, "", posts["data"])
