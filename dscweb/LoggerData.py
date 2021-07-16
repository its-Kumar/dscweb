import json
import logging
import sys
import uuid
from datetime import datetime


def LogData(
        serverName: str, pubIp: str, apiName: str, result,
        request: dict):
    """Logger to log the information for develepment

    Args:
        serverName (str): Contains the server name
        pubIp (str): contains the public ip of the user
        apiName (str): contains the name of API from which the logger is called
        result ([type]): contains the outcomes, or error if any
        request (dict): contains all the parameters send by the user

    Returns:
        [type]: returns the id of the particular logger
    """
    log_id = str(uuid.uuid4())
    dateTime = str(datetime.today())
    if "Image" in request:
        request['Image'] = str(request['Image'])
    if "File" in request:
        request['File'] = str(request['File'])

    paramData = json.dumps(request)
    errorInfo = sys.exc_info()
    errorMessage = ""
    if errorInfo[2] is not None:
        errorMessage = f'Error at lineNumber: {str(errorInfo[2].tb_lineno)} {str(errorInfo[0])} {str(errorInfo[1])}'
    info = {
        "log_Id": log_id, "ServerName": serverName, "DateTime": dateTime,
        "PublicIP": pubIp, "APIName": apiName,
        "Result": errorMessage + str(result), "ParameterData": str(paramData)

    }
    logger = logging.getLogger(__name__)
    logger.info(f'{info}')
    return log_id
