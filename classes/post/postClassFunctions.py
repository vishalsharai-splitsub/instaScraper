import sys
import os

# Importing the module from an absolute path
from thirdParty import instaloaderFunctions
from classes.profile import profileClass
from utils import utils
import errorConstants as errors

# Function to fetch instagram post using instaloader function Post.from_shortcode
# Parameter: shortcode for the post <string>
# Returns: post object <instaloader post object>
def getPost(shortcode):
    return instaloaderFunctions.getInstaShortcodePost(shortcode)


# Function to fetch instagram post using instaloader function Post.get_comments
# Parameter: post object <instaloader post object>
# Returns: comments list <instaloader comment object list>
def getPostComments(post):
    return instaloaderFunctions.getInstaComments(post)


# Function to fetch instagram post using instaloader function Post.get_likes
# Parameter: post object <instaloader post object>
# Returns: likes list <instaloader like object list>
def getPostLikes(post):
    return instaloaderFunctions.getInstaLikes(post)


# Function to fetch instagram c mment usernames
# Parameter: post object <instaloader post object>
# Returns: comments list <string list>
def getPostCommentsUsernames(post):
    postCommentsUsernames = []
    postComments = instaloaderFunctions.getInstaComments(post)
    if postComments["success"] == False:
        return postComments
    for comment in postComments["data"]:
        postCommentsUsernames.append(comment.owner.username)
    return utils.classResponse(True, "", postCommentsUsernames)


# Function to fetch instagram comment usernames
# Parameter: post object <instaloader post object>
# Returns: usernames list<string list>
def getPostLikesUsernames(post):
    postLikesUsernames = []
    postLikes = instaloaderFunctions.getInstaLikes(post)
    if postLikes["success"] == False:
        return postLikes
    for like in postLikes["data"]:
        postLikesUsernames.append(like.username)
    return utils.classResponse(True, "", postLikesUsernames)


# Function to get user who has liked and commented on N number of posts
# Parameter: post object list <instaloader post object>
# Returns: commonUsers dictionary <dict>
def getCommonUser(listOfPosts):
    comments = []
    likes = []
    commonUsers = {"comments": [], "likes": [], "both": [], "posts": []}
    for index, post in enumerate(listOfPosts):
        commentData = getPostCommentsUsernames(post.post)
        if commentData["success"] == False:
            return commentData

        commentList = set(commentData["data"])

        likeData = getPostLikesUsernames(post.post)

        if likeData["success"] == False:
            return likeData

        likeList = set(likeData["data"])

        if index == 0:
            commonUsers["comments"] = commentList
            commonUsers["likes"] = likeList
            commonUsers["both"] = commentList.intersection(likeList)
        else:
            commonUsers["comments"] = commonUsers["comments"].intersection(commentList)
            commonUsers["likes"] = commonUsers["likes"].intersection(likeList)
            commonUsers["both"] = commonUsers["both"].intersection(
                commentList, likeList
            )

        postData = getPostDetails(post.post)
        if postData["success"] == False:
            return postData
        commonUsers["posts"].append(postData["data"])

    for key in commonUsers.keys():
        commonUsers[key] = list(commonUsers[key])

    return utils.classResponse(True, "", commonUsers)


# This function gets the details of the post
# Parameter: post object <instaloader post object>
# Returns: details dictionary <dict>
def getPostDetails(post):
    postDetails = {}
    postDetails["mediaid"] = post.mediaid
    postDetails["shortcode"] = post.shortcode
    postDetails["comments"] = post.comments
    postDetails["likes"] = post.likes
    postDetails["caption"] = post.caption
    postDetails["owner_username"] = post.owner_username
    postDetails["date_utc"] = str(post.date_utc)
    postDetails["url"] = post.url
    return utils.classResponse(True, "", postDetails)


def getPostFollowersActivity(post):
    commentsData = getPostCommentsUsernames(post)

    if commentsData["success"] == False:
        return commentsData
    comments = set(commentsData["data"])

    likesData = getPostLikesUsernames(post)
    if likesData["success"] == False:
        return likesData
    likes = set(likesData["data"])

    profileData = profileClass.Profile("", post.owner_profile)
    followersData = profileData.getStructuredFollowers()
    if followersData["success"] == False:
        return followersData
    followers = set(followersData["data"])

    profileFollowersActivity = {
        "commentedAndFollowingProfile": list(followers.intersection(comments)),
        "likedAndFollowingProfile": list(followers.intersection(likes)),
        "likedCommentedAndFollowing": list(followers.intersection(likes, comments)),
        "likedButNotFollowing": list(likes - followers),
        "commentedButNotFollowing": list(comments - followers),
        "likedCommentedButNotFollowing": list(comments.intersection(likes) - followers),
    }
    return utils.classResponse(True, "", profileFollowersActivity)

# Function to fetch instagram comment usernames and the text in the comment
# Parameter: post object <instaloader post object>
# Returns: comments object list with username and the text <object list>
def getPostCommentsWithText(post):
    comments = []
    mentions = 0
    postDetailedComments = {"comments":[],"unique": None,"mentions": None}
    postCommentsWithText = instaloaderFunctions.getInstaComments(post)
    if postCommentsWithText["success"] == False:
        return postCommentsWithText
    for comment in postCommentsWithText["data"]:
        postDetailedComments['comments'].append(
            {"username": comment.owner.username, "commentText": comment.text}
        )
        comments.append(comment.owner.username)
        for i in comment.text:
            if i == "@":
                mentions = mentions + 1
    comments = set(comments)
    comments = list(comments)
    postDetailedComments['unique'] = len(comments)
    postDetailedComments['mentions'] = mentions
    return utils.classResponse(True, "", postDetailedComments)
