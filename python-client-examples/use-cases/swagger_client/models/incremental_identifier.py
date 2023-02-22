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

class IncrementalIdentifier(object):
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
        'identifier_type': 'str',
        'field_name': 'str'
    }

    attribute_map = {
        'identifier_type': 'identifier_type',
        'field_name': 'field_name'
    }

    def __init__(self, identifier_type=None, field_name=None):  # noqa: E501
        """IncrementalIdentifier - a model defined in Swagger"""  # noqa: E501
        self._identifier_type = None
        self._field_name = None
        self.discriminator = None
        self.identifier_type = identifier_type
        if field_name is not None:
            self.field_name = field_name

    @property
    def identifier_type(self):
        """Gets the identifier_type of this IncrementalIdentifier.  # noqa: E501


        :return: The identifier_type of this IncrementalIdentifier.  # noqa: E501
        :rtype: str
        """
        return self._identifier_type

    @identifier_type.setter
    def identifier_type(self, identifier_type):
        """Sets the identifier_type of this IncrementalIdentifier.


        :param identifier_type: The identifier_type of this IncrementalIdentifier.  # noqa: E501
        :type: str
        """
        if identifier_type is None:
            raise ValueError("Invalid value for `identifier_type`, must not be `None`")  # noqa: E501
        allowed_values = ["last-modified", "batch-value", "postgresql"]  # noqa: E501
        if identifier_type not in allowed_values:
            raise ValueError(
                "Invalid value for `identifier_type` ({0}), must be one of {1}"  # noqa: E501
                .format(identifier_type, allowed_values)
            )

        self._identifier_type = identifier_type

    @property
    def field_name(self):
        """Gets the field_name of this IncrementalIdentifier.  # noqa: E501


        :return: The field_name of this IncrementalIdentifier.  # noqa: E501
        :rtype: str
        """
        return self._field_name

    @field_name.setter
    def field_name(self, field_name):
        """Sets the field_name of this IncrementalIdentifier.


        :param field_name: The field_name of this IncrementalIdentifier.  # noqa: E501
        :type: str
        """

        self._field_name = field_name

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
        if issubclass(IncrementalIdentifier, dict):
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
        if not isinstance(other, IncrementalIdentifier):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
