from classes.profile.constants import ENUM_VALUES
import errorConstants


def errorCreator(error, key, value):
    return str(key) + str(error) + str(value)


def validateRequest(data, config):
    valid = {}
    for key in data.keys():
        if key not in config.keys():
            return classResponse(
                False,
                errorCreator(
                    errorConstants.VALIDATION_ERRORS["invalid_argument"],
                    str(key),
                    str(list(config.keys())),
                ),
                {},
            )
    for key in config.keys():
        if key in data:
            if isinstance(data[key], config[key]["type"]):
                valid[key] = {"type": config[key]["type"], "valid": True}
            else:
                return classResponse(
                    False,
                    errorCreator(
                        errorConstants.VALIDATION_ERRORS["type_error"],
                        str(key),
                        str(config[key]["type"]),
                    ),
                    {},
                )
            if "enum" in config[key].keys() and config[key]["enum"] == True:
                if data[key] not in ENUM_VALUES[key]:
                    return classResponse(
                        False,
                        errorCreator(
                            errorConstants.VALIDATION_ERRORS["enum_value_error"],
                            str(data[key]),
                            str(list(ENUM_VALUES[key])),
                        ),
                        {},
                    )
            if "upperLimit" in config[key].keys():
                if data[key] <= config[key]['lowerLimit'] or data[key] > config[key]['upperLimit']:
                    return classResponse(
                        False,
                        errorCreator(
                            errorConstants.VALIDATION_ERRORS["limit_error"],
                            str(data[key]),
                            str(list([config[key]['lowerLimit'],config[key]['upperLimit']])),
                        ),
                        {},
                    )
            if config[key]["type"] == list:
                for element in data[key]:
                    if isinstance(element, config[key]["elementType"]):
                        valid[key] = {"type": config[key]["type"], "valid": True}
                    else:
                        return classResponse(
                            False,
                            errorCreator(
                                errorConstants.VALIDATION_ERRORS["element_type_error"],
                                str(key),
                                str(config[key]["type"]),
                            ),
                            {},
                        )

        elif key not in data:
            if config[key]["required"] == True:
                return classResponse(
                    False,
                    errorCreator(
                        errorConstants.VALIDATION_ERRORS["required_error"], ""
                    ),
                    {},
                )
            elif config[key]["required"] == False:
                valid[key] = {"type": config[key]["type"], "valid": True}
    return classResponse(True, "", valid)


def classResponse(success, error, data):
    return {"success": success, "error": error, "data": data}


def sendResponse(success, error, data):
    return {"success": success, "error": error, "data": data}
