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

class KllBucket(object):
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
        'id': 'int',
        'created': 'datetime',
        'low': 'float',
        'count': 'int',
        'high': 'float'
    }

    attribute_map = {
        'id': 'id',
        'created': 'created',
        'low': 'low',
        'count': 'count',
        'high': 'high'
    }

    def __init__(self, id=None, created=None, low=None, count=None, high=None):  # noqa: E501
        """KllBucket - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._created = None
        self._low = None
        self._count = None
        self._high = None
        self.discriminator = None
        self.id = id
        self.created = created
        self.low = low
        self.count = count
        self.high = high

    @property
    def id(self):
        """Gets the id of this KllBucket.  # noqa: E501


        :return: The id of this KllBucket.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this KllBucket.


        :param id: The id of this KllBucket.  # noqa: E501
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def created(self):
        """Gets the created of this KllBucket.  # noqa: E501


        :return: The created of this KllBucket.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this KllBucket.


        :param created: The created of this KllBucket.  # noqa: E501
        :type: datetime
        """
        if created is None:
            raise ValueError("Invalid value for `created`, must not be `None`")  # noqa: E501

        self._created = created

    @property
    def low(self):
        """Gets the low of this KllBucket.  # noqa: E501


        :return: The low of this KllBucket.  # noqa: E501
        :rtype: float
        """
        return self._low

    @low.setter
    def low(self, low):
        """Sets the low of this KllBucket.


        :param low: The low of this KllBucket.  # noqa: E501
        :type: float
        """
        if low is None:
            raise ValueError("Invalid value for `low`, must not be `None`")  # noqa: E501

        self._low = low

    @property
    def count(self):
        """Gets the count of this KllBucket.  # noqa: E501


        :return: The count of this KllBucket.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this KllBucket.


        :param count: The count of this KllBucket.  # noqa: E501
        :type: int
        """
        if count is None:
            raise ValueError("Invalid value for `count`, must not be `None`")  # noqa: E501

        self._count = count

    @property
    def high(self):
        """Gets the high of this KllBucket.  # noqa: E501


        :return: The high of this KllBucket.  # noqa: E501
        :rtype: float
        """
        return self._high

    @high.setter
    def high(self, high):
        """Sets the high of this KllBucket.


        :param high: The high of this KllBucket.  # noqa: E501
        :type: float
        """
        if high is None:
            raise ValueError("Invalid value for `high`, must not be `None`")  # noqa: E501

        self._high = high

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
        if issubclass(KllBucket, dict):
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
        if not isinstance(other, KllBucket):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
