import sys
import logging
from simplehttp.error import HttpError, UnexpectedHttpError
from simplehttp.request import http_get, http_post


def get_json(url, params=None):
    """API for sending GET reuqest

    Args:
        url (string): URL path
        params (dict, optional):Addtional parameters
            to  be added to the query string.

    Raises:
        UnexpectedHttpError: Get raised when one of the following is raised.
            1.ConnectionError from http.client.HTTPConnection.getresponse().
            2.urllib2.URLError from urllib2.urlopen().
            3.urllib2.HTTPError from urllib2.urlopen().

    Returns:
        [dict]: Reponse body in JSON (Python dictionary) format
    """
    params = params or {}
    try:
        # response = make_request('GET', url, params)

        response = http_get(url, params)

    except HttpError as error:
        sys.last_value = error
        # re-raise the exception (allow the caller to handle)
        raise
    except Exception as error:
        raise UnexpectedHttpError(error)
    return response


def post_json(url, params=None, data=None):
    """API for sending POST reuqest

    Args:
        url (string): URL path
        params (dict, optional): Addtional parameters
            to  be added to the query string.
        data (dict, optional): Request body.

    Returns:
        [dict]: Reponse body in JSON (Python dictionary) format
    """

    params = params or {}
    data = data or {}
    try:
        # response = make_request('POST', url, params, data)
        response = http_post(url, params, data)
    except HttpError as error:
        sys.last_value = error
        # re-raise the exception (allow the caller to handle)
        raise
    except Exception as error:
        raise UnexpectedHttpError(error)
    return response
