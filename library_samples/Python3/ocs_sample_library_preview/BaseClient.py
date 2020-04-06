import json

from .SdsError import SdsError

import requests
import time


class BaseClient(object):
    """Handles communication with Sds Service.  Internal Use"""

    def __init__(self, apiversion, tenant, url, clientId, clientSecret,
                 acceptVerbosity=False):
        self.__apiversion = apiversion
        self.__tenant = tenant
        self.__clientId = clientId
        self.__clientSecret = clientSecret
        self.__url = url  # if resource.endswith("/")  else resource + "/"

        self.__token = ""
        self.__expiration = 0
        self.__getToken()
        self.__acceptVerbosity = acceptVerbosity
        self.__requestTimeout = None

        self.__uri_API = url + '/api/' + apiversion

    @property
    def uri(self):
        """
        Gets the base url
        :return:
        """
        return self.__url

    @property
    def uri_API(self):
        """
        Returns the base URL plus api versioning information
        :return:
        """
        return self.__uri_API

    @property
    def api_version(self):
        """
        Returns just the base api versioning information
        :return:
        """
        return self.__apiversion

    @property
    def tenant(self):
        """
        Returns the tenant ID
        :return:
        """
        return self.__tenant

    @property
    def AcceptVerbosity(self):
        return self.__acceptVerbosity

    @AcceptVerbosity.setter
    def AcceptVerbosity(self, accept_verbosity):
        self.__acceptVerbosity = accept_verbosity

    @property
    def RequestTimeout(self):
        return self.__requestTimeout

    @RequestTimeout.setter
    def RequestTimeout(self, timeout):
        self.__requestTimeout = timeout

    def __getToken(self):
        """
        Gets the bearer token
        :return:
        """
        if ((self.__expiration - time.time()) > 5 * 60):
            return self.__token

        tokenEndpoint = self.__url + "/identity/connect/token"

        tokenInformation = requests.post(
            tokenEndpoint,
            data={"client_id": self.__clientId,
                  "client_secret": self.__clientSecret,
                  "grant_type": "client_credentials"})

        token = json.loads(tokenInformation.content)

        expiration = token.get("expires_in", None)
        if expiration is None:
            raise SdsError(
                f"Failed to get token, check client id/secret: {token['error']}")

        self.__expiration = float(expiration) + time.time()
        self.__token = token['access_token']
        return self.__token

    def sdsHeaders(self):
        """
        Gets the base headers needed for OCS call
        :return:
        """
        headers = {"Authorization": "Bearer %s" % self.__getToken(),
                   "Content-type": "application/json",
                   "Accept": "application/json"}
        if (self.__acceptVerbosity):
            headers['Accept-Verbosity'] = "verbose"
        if self.__requestTimeout is not None:
            headers['Request-Timeout'] = str(self.__requestTimeout)

        return headers

    def checkResponse(self, response, main_message):
        if response.status_code < 200 or response.status_code >= 300:
            status = response.status_code
            reason = response.text
            url = response.url
            opId = response.headers["Operation-Id"]
            error = f"  {status}:{reason}.  URL {url}  OperationId {opId}"
            response.close()

            message = main_message + error
            raise SdsError(message)

        # this happens on a collection return that is partially successful
        if response.status_code == 207:
            status = response.status_code
            error = response.json["Error"]
            reason = response.json["Reason"]
            errors = str(response.json["ChildErrors"])
            url = response.url
            opId = response.headers["Operation-Id"]
            errorToWrite = f"  {status}:{error}:{reason}. \n\n{errors}\n\n  URL {url}  OperationId {opId}"
            response.close()

            message = main_message + errorToWrite
            raise SdsError(message)

    def request(self, method, url, params=None, data=None, headers=None, **kwargs):
        if not headers:
            headers = self.sdsHeaders()
        return requests.request(method, url, params=params, data=data, headers=headers, **kwargs)
