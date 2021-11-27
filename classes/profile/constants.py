REQUEST_SCHEMA = {
    "details": {
        "username": {"required": True, "type": str},
        "getUsers": {"required": False, "type": str, "enum": True},
    },
    "posts": {
        "username": {"required": True, "type": str},
        "limit": {"required": False, "type": int,"lowerLimit":0,"upperLimit":20},
        "getLists": {
            "required": False,
            "type": list,
            "elementType": str,
        },
    },
    "topPosts": {
        "username": {"required": True, "type": str},
        "percent": {"required": True, "type": int,"lowerLimit":0,"upperLimit":20},
    },
}
ENUM_VALUES = {
    "getUsers": ["followers", "following", "both"],
}
PROFILE_DETAILS_PARAMETERS = [
    "userid",
    "username",
    "is_private",
    "followed_by_viewer",
    "mediacount",
    "igtvcount",
    "followers",
    "followees",
    "external_url",
    "is_business_account",
    "business_category_name",
    "biography",
    "blocked_by_viewer",
    "follows_viewer",
    "full_name",
    "has_blocked_viewer",
    "has_highlist_reels",
    "has_public_story",
    "has_viewable_story",
    "requested_by_viewer",
    "is_verified",
    "has_requested_viewer",
    "profile_pic_url",
]
