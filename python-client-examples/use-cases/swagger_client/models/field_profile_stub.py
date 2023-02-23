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

class FieldProfileStub(object):
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
        'name': 'str',
        'container_order_index': 'int'
    }

    attribute_map = {
        'name': 'name',
        'container_order_index': 'container_order_index'
    }

    def __init__(self, name=None, container_order_index=None):  # noqa: E501
        """FieldProfileStub - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._container_order_index = None
        self.discriminator = None
        self.name = name
        if container_order_index is not None:
            self.container_order_index = container_order_index

    @property
    def name(self):
        """Gets the name of this FieldProfileStub.  # noqa: E501


        :return: The name of this FieldProfileStub.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this FieldProfileStub.


        :param name: The name of this FieldProfileStub.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def container_order_index(self):
        """Gets the container_order_index of this FieldProfileStub.  # noqa: E501


        :return: The container_order_index of this FieldProfileStub.  # noqa: E501
        :rtype: int
        """
        return self._container_order_index

    @container_order_index.setter
    def container_order_index(self, container_order_index):
        """Sets the container_order_index of this FieldProfileStub.


        :param container_order_index: The container_order_index of this FieldProfileStub.  # noqa: E501
        :type: int
        """

        self._container_order_index = container_order_index

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
        if issubclass(FieldProfileStub, dict):
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
        if not isinstance(other, FieldProfileStub):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
