from classes.post import postClassFunctions
from classes.post import constants
from utils import utils
import errorConstants as errors


class Post:
    # Posts can be initiated with a shortcode or a post instaloader object if available otherwise the default is set to none
    def __init__(self, shortcode, post=None):
        self.shortcode = shortcode
        if post:
            self.post = post
        else:
            postData = postClassFunctions.getPost(self.shortcode)
            self.post = postData["data"]

    # Function to get comments of a post
    # Returns comment object <instaloader comment class object list>
    def getComments(self):
        commentsData = postClassFunctions.getPostComments(self.post)
        if commentsData["success"] == False:
            return commentsData
        self.comments = commentsData["data"]
        return utils.classResponse(True, "", self.comments)

    # Function to get details of a post
    # Returns comment object <instaloader comment class object list>
    def getDetails(self, getLists=[]):
        detailsData = postClassFunctions.getPostDetails(self.post)
        if detailsData["success"] == False:
            return detailsData
        self.details = detailsData["data"]

        if "comments" in getLists and "commentsWithText" not in getLists:
            commentsData = self.getCommentUsernames()
            if commentsData["success"] == False:
                return commentsData
            self.details["commentsList"] = commentsData["data"]
        if "commentsWithText" in getLists:
            commentsText = self.getCommentsWithText()
            if commentsText['success'] == False:
                return commentsText
            self.details['commentsText'] = commentsText['data']
        if "likes" in getLists:
            likesData = self.getLikeUsernames()
            if likesData["success"] == False:
                return likesData
            self.details["likesList"] = likesData["data"]
        if "followersActivity" in getLists:
            followerActivityData = self.getFollowerActivity()
            if followerActivityData["success"] == False:
                return followerActivityData
            self.details["followerActivity"] = followerActivityData["data"]

        return utils.classResponse(True, "", self.details)

    # Function to get likes of a post
    # Returns like object <instaloader like class object list>
    def getLikes(self):
        likesData = postClassFunctions.getPostLikes(self.post)
        if likesData["success"] == False:
            return likesData
        self.likes = likesData["data"]
        return utils.classResponse(True, "", self.likes)

    # Function to get all the usernames of the users who have liked the post
    # Returns usernames list <list of strings>
    def getLikeUsernames(self):
        likeUsernamesData = postClassFunctions.getPostLikesUsernames(self.post)
        if likeUsernamesData["success"] == False:
            return likeUsernamesData
        self.likeUsernames = likeUsernamesData["data"]
        return utils.classResponse(True, "", self.likeUsernames)

    # Function to get all the usernames of the users who have commented on the post
    # Returns usernames list <list of strings>
    def getCommentUsernames(self):
        commentUsernamesData = postClassFunctions.getPostCommentsUsernames(self.post)
        if commentUsernamesData["success"] == False:
            return commentUsernamesData
        self.commentUsernames = commentUsernamesData["data"]
        return utils.classResponse(True, "", self.commentUsernames)

    # Function to get all the usernames of the users who have commented/liked/both the post and are following the profile as well
    # Returns usernames dictionary <dict>
    def getFollowerActivity(self):
        followerActivityData = postClassFunctions.getPostFollowersActivity(self.post)
        if followerActivityData["success"] == False:
            return followerActivityData
        self.followerActivity = followerActivityData["data"]
        return utils.classResponse(True, "", self.followerActivity)

    # Function to get all comments with text
    # Returns comment object with username and text
    def getCommentsWithText(self):
        commentsWithText = postClassFunctions.getPostCommentsWithText(self.post)
        if commentsWithText['success'] == False:
            return commentsWithText
        self.getCommentsWithText = commentsWithText['data']
        return utils.classResponse(True,"",self.getCommentsWithText)