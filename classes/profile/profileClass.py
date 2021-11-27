from classes.profile import functions
from classes.profile import constants
from utils import utils
import errorConstants as errors


class Profile:
    # Init function for the class that creates a profile if a username is provided but if
    # a profile object of instaloader is provided then that profile is used
    def __init__(self, username, profile=None):
        self.structuredFollowers = []
        self.structuredFollowing = []
        if profile:
            self.profile = profile
        else:
            self.username = username
            profileData = functions.newProfile(self.username)
            self.profile = profileData["data"]

    # Get N number of posts made by the user
    def getNPosts(self, n):
        try:
            username = self.profile.username
        except:
            return utils.classResponse(False,errors.INSTALOADER_ERRORS['get_profile_error'],{})
        nPostsData = functions.getProfileNPosts(self.profile, n)
        if nPostsData["success"] == False:
            return nPostsData
        self.nPosts = nPostsData["data"]
        return utils.classResponse(True, "", self.nPosts)

    # Get the list of usernames that are following the user, not that in the function below
    # We get the profile object and in this case we get the string
    def getStructuredFollowers(self):
        
        followersData = self.getFollowers()

        if followersData["success"] == False:
            return followersData

        structuredFollowersData = functions.getStructuredList(followersData["data"])

        if structuredFollowersData["success"] == False:
            return structuredFollowersData

        self.structuredFollowers = structuredFollowersData["data"]

        return utils.classResponse(True, "", self.structuredFollowers)

    # Get the list of usernames that are following the user, not that in the function below
    # We get the profile object and in this case we get the string
    def getStructuredFollowing(self):
        followingData = self.getFollowing(self.profile)

        if followingData["success"] == False:
            return followingData

        structuredFollowingData = functions.getStructuredList(followingData)

        if structuredFollowingData["success"] == False:
            return structuredFollowingData

        self.structuredFollowing = structuredFollowingData["data"]

        return utils.classResponse(True, "", self.structuredFollowing)

    # Get the list of profiles that are following the user
    def getFollowers(self):
        followersData = functions.getProfileAssociatedUsers(self.profile, "follower")
        if followersData["success"] == False:
            return followersData
        self.followers = followersData["data"]
        return utils.classResponse(True, "", self.followers)

    # Get the list of profiles that the user is following
    def getFollowing(self):
        followingsData = functions.getProfileAssociatedUsers(self.profile, "following")

        if followingsData["success"] == False:
            return followingsData
        self.followings = followingsData["data"]

        return utils.classResponse(True, "", self.followings)

    # Get the count of followers that the profile has
    def getFollowersCount(self):
        try:
            self.followerCount = self.profile.followers
            return utils.classResponse(True, "", self.followerCount)
        except Exception as e:

            return utils.classResponse(
                False, errors.PROFILE_CLASS_ERRORS["get_follower_count_error"], {}
            )

    # Get the count of profile that the user is following
    def getFollowingCount(self):
        try:
            self.followingCount = self.profile.followees
            return utils.classResponse(True, "", self.followerCount)
        except Exception as e:

            return utils.classResponse(
                False, errors.PROFILE_CLASS_ERRORS["get_following_count_error"], {}
            )

    # Get the details of the profile like username, post count, profile url etc.
    # Parameters: getUsers <enum> Can be of values ['following','followers','both']
    def getDetails(self, getUsers=None):
        try:
            username = self.profile.username
        except:
            return utils.classResponse(False,errors.INSTALOADER_ERRORS['get_profile_error'],{})
        detailsData = functions.getProfileDetails(self.profile, getUsers)
        if detailsData["success"] == False:
            return detailsData
        self.details = detailsData["data"]
        return utils.classResponse(True, "", self.details)

    # Get the top N posts of a profile
    def getTopPosts(self, percent):
        try:
            username = self.profile.username
        except:
            return utils.classResponse(False,errors.INSTALOADER_ERRORS['get_profile_error'],{})
        topPostsResponse = functions.getProfileTopPosts(self.profile, percent)
        if topPostsResponse["success"] == False:
            return topPostsResponse
        self.topPosts = topPostsResponse["data"]
        return utils.classResponse(True, "", self.topPosts)
