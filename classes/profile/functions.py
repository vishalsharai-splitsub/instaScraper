import sys
import os
from itertools import islice
from math import ceil

# Importing the module from a  absolute path
from thirdParty import instaloaderFunctions
from classes.post import postClassFunctions
from classes.post import postClass as postFile
import classes.profile.profileClass as profile
from classes.profile import constants
import errorConstants as errors
from utils import utils

# This function calls the instaloaderFunction Profile.from_username
# Parameter: username <string>
# Returns: Profile <instaloader profile object> this can be further used for different things
def newProfile(username):
    return instaloaderFunctions.getInstaProfile(username)


# This function calls the instaloaderFunction Profile.get_posts
# Parameter: profile <instaloader Profile class object> , n number of posts that are required<integer>
# Return: list of posts <Post class objects list>
def getProfileNPosts(profile, n):
    i = 0
    postsData = instaloaderFunctions.getInstaProfilePosts(profile)
    if postsData["success"] == False:
        return postsData
    posts = postsData["data"]
    nPosts = []
    if n == -1:
        return utils.classResponse(True, "", posts)
    for element in posts:
        newPost = postFile.Post("", element)
        nPosts.append(newPost)
        i = i + 1
        if i == n:
            break
    return utils.classResponse(True, "", nPosts)


# This function is used to get the lost of followees or following for a profile
# Parameter: profile <instaloader Profile class object>
# Return: list of users <string list>
def getProfileAssociatedUsers(profileObject, type):
    if type == "following":
        usersData = instaloaderFunctions.getInstaFollowing(profileObject)
        if usersData["success"] == False:
            return usersData
        else:
            return utils.classResponse(True, "", usersData["data"])
    elif type == "follower":
        usersData = instaloaderFunctions.getInstaFollowers(profileObject)
        if usersData["success"] == False:
            return usersData
        else:
            return utils.classResponse(True, "", usersData["data"])


# This function takes a list of profile objects and returns their usernames
# Parameter: profile list <instaloader profile class objects list>
# Return: list of usernames <list of strings>
def getStructuredList(data):
    structuredList = []
    for element in data:
        structuredList.append(element.username)
    return utils.classResponse(True, "", structuredList)


# This function returns all the available parameters in a profile and put them in a dictionary
# Parameter: Profile object <instaloader profile class object>
# Return: dictionary of parameters <dict>
def getProfileDetails(data, getUsers):
    profileDetails = {}
    for key, value in (data._node).items():
        parameters = constants.PROFILE_DETAILS_PARAMETERS
        if str(key) in parameters:
            profileDetails[key] = value
    if getUsers == "followers" or getUsers == "both":
        followerData = getProfileAssociatedUsers(data, "follower")
        if followerData["success"] == False:
            return followerData

        followerStructuredData = getStructuredList(followerData["data"])
        if followerStructuredData["success"] == False:
            return followerStructuredData
        profileDetails["followerList"] = followerStructuredData["data"]

    if getUsers == "following" or getUsers == "both":
        followingData = getProfileAssociatedUsers(data, "following")

        if followingData["success"] == False:
            return followingData

        followingStructuredData = getStructuredList(followingData["data"])

        if followingStructuredData["success"] == False:
            return followingStructuredData

        profileDetails["followingList"] = followingStructuredData["data"]
    return utils.classResponse(True, "", profileDetails)


# This function returns the top posts of a profile based on percent
# Parameters: profile object <instaloader profile object>, percent <integer>
# Returns details of top posts in a dictionary
def getProfileTopPosts(profile, percent):
    topPosts = {}
    i = 0

    profileNPostsData = getProfileNPosts(profile, -1)

    if profileNPostsData["success"] == False:
        return profileNPostsData
    posts_sorted_by_likes = sorted(
        profileNPostsData["data"], key=lambda p: p.likes + p.comments, reverse=True
    )

    for post in islice(posts_sorted_by_likes, ceil(profile.mediacount * percent / 100)):
        currentPost = postFile.Post("", post)
        currentPostDetails = currentPost.getDetails()
        if currentPostDetails["success"] == False:
            return currentPostDetails
        topPosts[i + 1] = currentPostDetails["data"]
        i = i + 1
    return utils.classResponse(True, "", topPosts)
