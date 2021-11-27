import sys
import os
import json
from flask import request

from classes.post import postClass
from classes.post import postClassFunctions
from classes.post import constants
from utils import utils
import errorConstants as errors

posts = {}

# Handler for details endpoint
def getPostFromShortcode(request):
    request = request.get_json()
    processedData = utils.validateRequest(request, constants.REQUEST_SCHEMA["details"])
    if processedData["success"] == False:
        return utils.sendResponse(processedData['success'],processedData['error'],processedData['data'])
    params = {}
    params["shortcode"] = request["shortcode"]
    params["getLists"] = request["getLists"] if "getLists" in request.keys() else []

    detailsData = createPost(params)
    if detailsData["success"] == False:
        return utils.sendResponse(detailsData['success'],detailsData['error'],detailsData['data'])
    return utils.sendResponse(True, "", detailsData["data"])


# Handler for the common posts endpoint
def getCommonFromShortcodes(request):
    request = request.get_json()
    processedData = utils.validateRequest(request, constants.REQUEST_SCHEMA["common"])
    if processedData["success"] == False:
        return utils.sendResponse(processedData['success'],processedData['error'],processedData['data'])
    params = {}
    params["shortcodes"] = (
        request["shortcodes"] if "shortcodes" in request.keys() else []
    )
    commonData = getCommon(params)
    if commonData["success"] == False:
        return utils.sendResponse(commonData['success'],commonData['error'],commonData['data'])
    common = commonData["data"]
    return utils.sendResponse(True, "", common)


# Create a post object if it does not alreadt exists then return
def postMaker(shortcode):
    if shortcode in posts.keys():
        return
    else:
        postData = postClass.Post(shortcode)
        posts[shortcode] = postData
        return


# This functions sends back the details of a newly created or old post object
def createPost(params):
    postMaker(params["shortcode"])

    postsData = posts[params["shortcode"]].getDetails(params["getLists"])
    if postsData["success"] == False:
        return utils.sendResponse(postsData['success'],postsData['error'],postsData['data'])
    return utils.sendResponse(True, "", postsData["data"])


# This function finds the common username of people who have liked/commented/both on a list of instagram posts
def getCommon(params):
    postsList = []
    for shortcode in params["shortcodes"]:
        postMaker(shortcode)
        postsList.append(posts[shortcode])

    commonUsersData = postClassFunctions.getCommonUser(postsList)

    if commonUsersData["success"] == False:
        return utils.sendResponse(commonUsersData['success'],commonUsersData['error'],commonUsersData['data'])
    commonUsers = commonUsersData["data"]

    return utils.sendResponse(True, "", commonUsers)
