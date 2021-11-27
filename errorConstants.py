VALIDATION_ERRORS = {
    "type_error": " is of the wrong type it should be ",
    "required_error": " is a required field and was not sent",
    "invalid_argument": " is an invalid argument, it should be one of these: ",
    "enum_value_error": " is not part of the possible value, it should be one of these: ",
    "element_type_error": " contains one of more elements of the incorrect datatype, they should be of type : ",
    "limit_error": " amount is out of limits, it should be between "
}
INSTALOADER_ERRORS = {
    "login_error": " Insaloader could not login to instagram from Instagram ",
    "get_profile_error": " Insaloader could not get profile from Instagram ",
    "get_followers_error": " Insaloader could not get followers from Instagram ",
    "get_following_error": " Insaloader could not get following from Instagram ",
    "get_profile_posts_error": " Insaloader could not get profile posts from Instagram ",
    "get_post_shortcode_error": " Insaloader could not get post shortcode from Instagram ",
    "get_post_comments_error": " Insaloader could not get post comments from Instagram",
}
POST_CLASS_FUNCTIONS_ERRORS = {
    "details_error": " Could not get the details from post object in class functions  ",
    "follower_activity_error": " Could not get follower activity from post object in class function ",
}
POST_CLASS_ERRORS = {
    "follower_activity_error": " Could not get follower activity from post object in class function ",
    "get_details_error": " Could not get details from post object in class function check parameters",
}
POST_CONTROLLER_ERRORS = {
    "get_post_details": " Could not get post details from controller check request ",
    "common_posts_error": " Could not get common posts from controller check request",
    "create_post_error": " Could not create post from controller check request",
}
PROFILE_CLASS_FUNCTIONS_ERRORS = {
    "get_profile_posts_error": " Could not get posts from the profile object in class function ",
    "associated_users_error": " Could not get followers/following because of parameter error in getProfileAssociatedUsers  in class function ",
    "get_structured_list_error": " Could not get structured list because of invalid data, data should be of instaloader object type ",
    "get_details_error": " Could not get profile details because of parameters error in getProfileDetails in class function ",
    "get_top_posts_error": " Could not get top posts because of parameters error in getTopPosts in class function ",
}
PROFILE_CLASS_ERRORS = {
    "get_follower_count_error": " Could not get follower count from the instaloader profile object ",
    "get_following_count_error": " Could not get following count from the instaloader profile object ",
    "get_details_error": " Could not get details from the Profile class ",
    "get_posts_error": " Could not get posts please check the type/value of parameter ",
    "get_top_posts_error": " Could not get the top posts from the profile class please check request object "
}
PROFILE_CONTROLLER_ERRORS = {
    "get_details_error": " Could not get the details from the handler in profile controller please check request object ",
    "get_posts_error": " Could not get the posts from the handler in profile controller please check request object ",
    "get_top_posts_error": " Could not get the top posts from the handler in profile contorller please check request object ",
    "create_profile_error": " Could not create Profile in the controller please check the request object ",
    "get_posts_from_profile_error": " Could not get Posts in the controller please check the request object ",
}