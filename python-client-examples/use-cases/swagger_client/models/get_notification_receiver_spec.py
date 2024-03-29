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

class GetNotificationReceiverSpec(object):
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
        'display_name': 'str',
        'type': 'NotificationReceiverType',
        'properties': 'list[GetNotificationReceiverSpecProperties]',
        'auth_supported': 'bool',
        'auth_type': 'str',
        'secret': 'str'
    }

    attribute_map = {
        'display_name': 'display_name',
        'type': 'type',
        'properties': 'properties',
        'auth_supported': 'auth_supported',
        'auth_type': 'auth_type',
        'secret': 'secret'
    }

    def __init__(self, display_name=None, type=None, properties=None, auth_supported=False, auth_type=None, secret=None):  # noqa: E501
        """GetNotificationReceiverSpec - a model defined in Swagger"""  # noqa: E501
        self._display_name = None
        self._type = None
        self._properties = None
        self._auth_supported = None
        self._auth_type = None
        self._secret = None
        self.discriminator = None
        self.display_name = display_name
        self.type = type
        self.properties = properties
        if auth_supported is not None:
            self.auth_supported = auth_supported
        if auth_type is not None:
            self.auth_type = auth_type
        if secret is not None:
            self.secret = secret

    @property
    def display_name(self):
        """Gets the display_name of this GetNotificationReceiverSpec.  # noqa: E501


        :return: The display_name of this GetNotificationReceiverSpec.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this GetNotificationReceiverSpec.


        :param display_name: The display_name of this GetNotificationReceiverSpec.  # noqa: E501
        :type: str
        """
        if display_name is None:
            raise ValueError("Invalid value for `display_name`, must not be `None`")  # noqa: E501

        self._display_name = display_name

    @property
    def type(self):
        """Gets the type of this GetNotificationReceiverSpec.  # noqa: E501


        :return: The type of this GetNotificationReceiverSpec.  # noqa: E501
        :rtype: NotificationReceiverType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this GetNotificationReceiverSpec.


        :param type: The type of this GetNotificationReceiverSpec.  # noqa: E501
        :type: NotificationReceiverType
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def properties(self):
        """Gets the properties of this GetNotificationReceiverSpec.  # noqa: E501


        :return: The properties of this GetNotificationReceiverSpec.  # noqa: E501
        :rtype: list[GetNotificationReceiverSpecProperties]
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this GetNotificationReceiverSpec.


        :param properties: The properties of this GetNotificationReceiverSpec.  # noqa: E501
        :type: list[GetNotificationReceiverSpecProperties]
        """
        if properties is None:
            raise ValueError("Invalid value for `properties`, must not be `None`")  # noqa: E501

        self._properties = properties

    @property
    def auth_supported(self):
        """Gets the auth_supported of this GetNotificationReceiverSpec.  # noqa: E501


        :return: The auth_supported of this GetNotificationReceiverSpec.  # noqa: E501
        :rtype: bool
        """
        return self._auth_supported

    @auth_supported.setter
    def auth_supported(self, auth_supported):
        """Sets the auth_supported of this GetNotificationReceiverSpec.


        :param auth_supported: The auth_supported of this GetNotificationReceiverSpec.  # noqa: E501
        :type: bool
        """

        self._auth_supported = auth_supported

    @property
    def auth_type(self):
        """Gets the auth_type of this GetNotificationReceiverSpec.  # noqa: E501


        :return: The auth_type of this GetNotificationReceiverSpec.  # noqa: E501
        :rtype: str
        """
        return self._auth_type

    @auth_type.setter
    def auth_type(self, auth_type):
        """Sets the auth_type of this GetNotificationReceiverSpec.


        :param auth_type: The auth_type of this GetNotificationReceiverSpec.  # noqa: E501
        :type: str
        """
        allowed_values = ["basic", "digest", "bearer"]  # noqa: E501
        if auth_type not in allowed_values:
            raise ValueError(
                "Invalid value for `auth_type` ({0}), must be one of {1}"  # noqa: E501
                .format(auth_type, allowed_values)
            )

        self._auth_type = auth_type

    @property
    def secret(self):
        """Gets the secret of this GetNotificationReceiverSpec.  # noqa: E501


        :return: The secret of this GetNotificationReceiverSpec.  # noqa: E501
        :rtype: str
        """
        return self._secret

    @secret.setter
    def secret(self, secret):
        """Sets the secret of this GetNotificationReceiverSpec.


        :param secret: The secret of this GetNotificationReceiverSpec.  # noqa: E501
        :type: str
        """

        self._secret = secret

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
        if issubclass(GetNotificationReceiverSpec, dict):
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
        if not isinstance(other, GetNotificationReceiverSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
