import sys
import json
import logging
from simplehttp.utils import process_url
from simplehttp.error import HttpError, UnexpectedHttpError
from simplehttp.request import http_get, http_post
#


def make_get_request(url, params):
    """
    Making http GET request for both Python2 and Python3

    Args:
        url (string): URL path
        params (dict, optional):Addtional parameters
            to  be added to the query string.

    Raises:
        HttpError: Client or server error, indicated by
            status code starts with either 4 or 5.

    Returns:
        [dict]: Reponse body in JSON (Python dictionary) format
    """
    url_parts = process_url(url, params)

    try:
        status_code, data = http_get(url_parts)
    except Exception as err:
        logging.error(err)
        raise UnexpectedHttpError(err)
        # raise err

    if status_code.startswith('4') or status_code.startswith('5'):
        raise HttpError(status_code)

    return data


def make_post_request(url, params, data):
    """
    Making http POST request for both Python2 and Python3

    Args:
        url (string): URL path
        params (dict, optional): Addtional parameters
            to  be added to the query string.

    Raises:
        HttpError: Client or server error, indicated by
            status code starts with either 4 or 5.

    Returns:
        [dict]: Reponse body in JSON (Python dictionary) format
    """
    url_parts = process_url(url, params)
    try:
        status_code, data = http_post(url_parts, data)
    except Exception as err:
        logging.error(err)
        raise UnexpectedHttpError(err)
        # raise err

    if status_code.startswith('4') or status_code.startswith('5'):
        raise HttpError(status_code)

    return data


def make_request(method, url, params=None, data=None):
    """[summary]

    Args:
        method (string): Either GET or POST
        url (string): URL path
        params (dict, optional): Addtional parameters
            to  be added to the query string.
        data (dict, optional): Request body for POST request. Defaults to {}.

    Raises:
        HttpError: Client or server error, indicated by
            status code starts with either 4 or 5.

    Returns:
        [dict]: Reponse body in JSON (Python dictionary) format
    """

    params = params or {}
    data = data or {}

    if method == 'GET':
        return make_get_request(url, params)
    if method == 'POST':
        return make_post_request(url, params, data)
    return {}


def get_json(url, params=None):
    """API for sending GET reuqest

    Args:
        url (string): URL path
        params (dict, optional):Addtional parameters
            to  be added to the query string.

    Returns:
        [dict]: Reponse body in JSON (Python dictionary) format
    """
    params = params or {}
    try:
        response = make_request('GET', url, params)

    except Exception as error:
        sys.last_value = error
        # re-raise the exception (allow the caller to handle)
        raise
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
        response = make_request('POST', url, params, data)
    except Exception as error:
        sys.last_value = error
        raise
    return response
