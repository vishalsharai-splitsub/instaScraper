import instaloader
import sys
import os

# Importing the module froma  relative path
from config import config
from utils import utils

import errorConstants as errors

L = instaloader.Instaloader(user_agent=config.USER_AGENT)


def initializeInstaloder():
    try:
        L.interactive_login(config.USER)
    except Exception as e:

        print(errors.INSTALOADER_ERRORS["login_error"])


# This function calls the instaloaderFunction Profile.from_username
# Parameter: username <string>
# Returns: Profile <instaloader profile object> this can be further used for different things
def getInstaProfile(username):
    try:
        profile = instaloader.Profile.from_username(L.context, username)
        return utils.classResponse(True, "", profile)
    except Exception as e:

        return utils.classResponse(
            False, errors.INSTALOADER_ERRORS["get_profile_error"], {}
        )


# This function calls the instaloaderFunction Profile.from_username
# Parameter: Profile <instaloader profile object>
# Returns: followers -  List of followers of the profile <list>
def getInstaFollowers(profile):
    try:
        followers = profile.get_followers()
        return utils.classResponse(True, "", followers)
    except Exception as e:

        return utils.classResponse(
            False, errors.INSTALOADER_ERRORS["get_followers_error"], {}
        )


# This function calls the instaloaderFunction Profile.from_username
# Parameter: Profile <instaloader profile object>
# Returns: following - List of following of the profile <list>
def getInstaFollowing(profile):
    try:
        following = profile.get_followees()
        return utils.classResponse(True, "", following)
    except Exception as e:
        return utils.classResponse(
            False, errors.INSTALOADER_ERRORS["get_following_error"], {}
        )


# This function calls the instaloaderFunction Profile.from_username
# Parameter: Profile <instaloader profile object>
# Returns: posts <instaloader Post class object>
def getInstaProfilePosts(profile):
    try:
        posts = profile.get_posts()
        return utils.classResponse(True, "", posts)
    except Exception as e:
        return utils.classResponse(
            False, errors.INSTALOADER_ERRORS["get_profile_posts_error"], {}
        )


# This function calls the instaloaderFunction Profile.from_shortcode to get a post using it's shortcode
# Parameter: shortcode <string>
# Returns: posts <instaloader Post class object>
def getInstaShortcodePost(shortcode):
    try:
        post = instaloader.Post.from_shortcode(L.context, shortcode)
        return utils.classResponse(True, "", post)
    except Exception as e:

        return utils.classResponse(
            False, errors.INSTALOADER_ERRORS["get_post_shortcode_error"], {}
        )


# This function calls the instaloaderFunction Post.get_comments
# Parameter: Post <instaloader Post class object>
# Returns: list of comments <instaloader Comment class object>
def getInstaComments(post):
    try:
        comments = post.get_comments()
        return utils.classResponse(True, "", comments)
    except Exception as e:

        return utils.classResponse(
            False, errors.INSTALOADER_ERRORS["get_post_comments_error"], {}
        )


# This function calls the instaloaderFunction Profile.from_username
# Parameter: Post <instaloader Post class object>
# Returns: List of profiles that have liked the post <instaloader Profile class object list>
def getInstaLikes(post):
    try:
        likes = post.get_likes()
        return utils.classResponse(True, "", likes)
    except Exception as e:

        return utils.classResponse(
            False, errors.INSTALOADER_ERRORS["get_post_likes_error"], {}
        )
