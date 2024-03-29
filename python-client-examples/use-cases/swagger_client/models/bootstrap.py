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

class Bootstrap(object):
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
        'current_user': 'User'
    }

    attribute_map = {
        'current_user': 'current_user'
    }

    def __init__(self, current_user=None):  # noqa: E501
        """Bootstrap - a model defined in Swagger"""  # noqa: E501
        self._current_user = None
        self.discriminator = None
        self.current_user = current_user

    @property
    def current_user(self):
        """Gets the current_user of this Bootstrap.  # noqa: E501


        :return: The current_user of this Bootstrap.  # noqa: E501
        :rtype: User
        """
        return self._current_user

    @current_user.setter
    def current_user(self, current_user):
        """Sets the current_user of this Bootstrap.


        :param current_user: The current_user of this Bootstrap.  # noqa: E501
        :type: User
        """
        if current_user is None:
            raise ValueError("Invalid value for `current_user`, must not be `None`")  # noqa: E501

        self._current_user = current_user

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
        if issubclass(Bootstrap, dict):
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
        if not isinstance(other, Bootstrap):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
