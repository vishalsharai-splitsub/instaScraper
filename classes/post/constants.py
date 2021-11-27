REQUEST_SCHEMA = {
    "details": {
        "shortcode": {"required": True, "type": str},
        "getLists": {"required": False, "type": list, "elementType": str},
    },
    "common": {"shortcodes": {"required": True, "type": list, "elementType": str}},
}