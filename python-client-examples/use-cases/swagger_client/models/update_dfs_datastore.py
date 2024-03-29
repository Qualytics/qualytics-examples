# coding: utf-8

"""
    Surveillance Hub

    Qualytics API  # noqa: E501

    OpenAPI spec version: 5ca80d8
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class UpdateDfsDatastore(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'type': 'str',
        'name': 'str',
        'enrich_only': 'bool',
        'enrich_container_prefix': 'str',
        'tags': 'list[str]',
        'favorite': 'bool',
        'uri': 'str',
        'access_key': 'str',
        'secret_key': 'str'
    }

    attribute_map = {
        'type': 'type',
        'name': 'name',
        'enrich_only': 'enrich_only',
        'enrich_container_prefix': 'enrich_container_prefix',
        'tags': 'tags',
        'favorite': 'favorite',
        'uri': 'uri',
        'access_key': 'access_key',
        'secret_key': 'secret_key'
    }

    def __init__(self, type=None, name=None, enrich_only=None, enrich_container_prefix=None, tags=None, favorite=None, uri=None, access_key=None, secret_key=None):  # noqa: E501
        """UpdateDfsDatastore - a model defined in Swagger"""  # noqa: E501
        self._type = None
        self._name = None
        self._enrich_only = None
        self._enrich_container_prefix = None
        self._tags = None
        self._favorite = None
        self._uri = None
        self._access_key = None
        self._secret_key = None
        self.discriminator = None
        self.type = type
        self.name = name
        self.enrich_only = enrich_only
        self.enrich_container_prefix = enrich_container_prefix
        if tags is not None:
            self.tags = tags
        if favorite is not None:
            self.favorite = favorite
        if uri is not None:
            self.uri = uri
        if access_key is not None:
            self.access_key = access_key
        if secret_key is not None:
            self.secret_key = secret_key

    @property
    def type(self):
        """Gets the type of this UpdateDfsDatastore.  # noqa: E501

        Type of the DFS `Datastore`  # noqa: E501

        :return: The type of this UpdateDfsDatastore.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this UpdateDfsDatastore.

        Type of the DFS `Datastore`  # noqa: E501

        :param type: The type of this UpdateDfsDatastore.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["s3", "gcs", "wasb", "abfs"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def name(self):
        """Gets the name of this UpdateDfsDatastore.  # noqa: E501

        Name of the `Datastore`  # noqa: E501

        :return: The name of this UpdateDfsDatastore.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateDfsDatastore.

        Name of the `Datastore`  # noqa: E501

        :param name: The name of this UpdateDfsDatastore.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def enrich_only(self):
        """Gets the enrich_only of this UpdateDfsDatastore.  # noqa: E501

        If is a `Datastore`=`false` or `Enrichment Datastore`=`true`  # noqa: E501

        :return: The enrich_only of this UpdateDfsDatastore.  # noqa: E501
        :rtype: bool
        """
        return self._enrich_only

    @enrich_only.setter
    def enrich_only(self, enrich_only):
        """Sets the enrich_only of this UpdateDfsDatastore.

        If is a `Datastore`=`false` or `Enrichment Datastore`=`true`  # noqa: E501

        :param enrich_only: The enrich_only of this UpdateDfsDatastore.  # noqa: E501
        :type: bool
        """
        if enrich_only is None:
            raise ValueError("Invalid value for `enrich_only`, must not be `None`")  # noqa: E501

        self._enrich_only = enrich_only

    @property
    def enrich_container_prefix(self):
        """Gets the enrich_container_prefix of this UpdateDfsDatastore.  # noqa: E501

        The `Enrichment Datastore` prefix name  # noqa: E501

        :return: The enrich_container_prefix of this UpdateDfsDatastore.  # noqa: E501
        :rtype: str
        """
        return self._enrich_container_prefix

    @enrich_container_prefix.setter
    def enrich_container_prefix(self, enrich_container_prefix):
        """Sets the enrich_container_prefix of this UpdateDfsDatastore.

        The `Enrichment Datastore` prefix name  # noqa: E501

        :param enrich_container_prefix: The enrich_container_prefix of this UpdateDfsDatastore.  # noqa: E501
        :type: str
        """
        if enrich_container_prefix is None:
            raise ValueError("Invalid value for `enrich_container_prefix`, must not be `None`")  # noqa: E501

        self._enrich_container_prefix = enrich_container_prefix

    @property
    def tags(self):
        """Gets the tags of this UpdateDfsDatastore.  # noqa: E501

        The list of `Tags` of the `Datastore`  # noqa: E501

        :return: The tags of this UpdateDfsDatastore.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this UpdateDfsDatastore.

        The list of `Tags` of the `Datastore`  # noqa: E501

        :param tags: The tags of this UpdateDfsDatastore.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

    @property
    def favorite(self):
        """Gets the favorite of this UpdateDfsDatastore.  # noqa: E501

        If the `Datastore` is favorite or not  # noqa: E501

        :return: The favorite of this UpdateDfsDatastore.  # noqa: E501
        :rtype: bool
        """
        return self._favorite

    @favorite.setter
    def favorite(self, favorite):
        """Sets the favorite of this UpdateDfsDatastore.

        If the `Datastore` is favorite or not  # noqa: E501

        :param favorite: The favorite of this UpdateDfsDatastore.  # noqa: E501
        :type: bool
        """

        self._favorite = favorite

    @property
    def uri(self):
        """Gets the uri of this UpdateDfsDatastore.  # noqa: E501

        URI of the DFS `Datastore`  # noqa: E501

        :return: The uri of this UpdateDfsDatastore.  # noqa: E501
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this UpdateDfsDatastore.

        URI of the DFS `Datastore`  # noqa: E501

        :param uri: The uri of this UpdateDfsDatastore.  # noqa: E501
        :type: str
        """

        self._uri = uri

    @property
    def access_key(self):
        """Gets the access_key of this UpdateDfsDatastore.  # noqa: E501

        Access Key of the DFS `Datastore`  # noqa: E501

        :return: The access_key of this UpdateDfsDatastore.  # noqa: E501
        :rtype: str
        """
        return self._access_key

    @access_key.setter
    def access_key(self, access_key):
        """Sets the access_key of this UpdateDfsDatastore.

        Access Key of the DFS `Datastore`  # noqa: E501

        :param access_key: The access_key of this UpdateDfsDatastore.  # noqa: E501
        :type: str
        """

        self._access_key = access_key

    @property
    def secret_key(self):
        """Gets the secret_key of this UpdateDfsDatastore.  # noqa: E501

        Secret Key of the DFS `Datastore`  # noqa: E501

        :return: The secret_key of this UpdateDfsDatastore.  # noqa: E501
        :rtype: str
        """
        return self._secret_key

    @secret_key.setter
    def secret_key(self, secret_key):
        """Sets the secret_key of this UpdateDfsDatastore.

        Secret Key of the DFS `Datastore`  # noqa: E501

        :param secret_key: The secret_key of this UpdateDfsDatastore.  # noqa: E501
        :type: str
        """

        self._secret_key = secret_key

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(UpdateDfsDatastore, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, UpdateDfsDatastore):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
