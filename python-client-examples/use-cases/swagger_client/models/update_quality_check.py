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

class UpdateQualityCheck(object):
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
        'description': 'str',
        'coverage': 'float',
        'filter': 'str',
        'properties': 'QualityCheckProperties',
        'tags': 'list[str]',
        'favorite': 'bool'
    }

    attribute_map = {
        'description': 'description',
        'coverage': 'coverage',
        'filter': 'filter',
        'properties': 'properties',
        'tags': 'tags',
        'favorite': 'favorite'
    }

    def __init__(self, description=None, coverage=None, filter=None, properties=None, tags=None, favorite=None):  # noqa: E501
        """UpdateQualityCheck - a model defined in Swagger"""  # noqa: E501
        self._description = None
        self._coverage = None
        self._filter = None
        self._properties = None
        self._tags = None
        self._favorite = None
        self.discriminator = None
        self.description = description
        if coverage is not None:
            self.coverage = coverage
        if filter is not None:
            self.filter = filter
        if properties is not None:
            self.properties = properties
        if tags is not None:
            self.tags = tags
        if favorite is not None:
            self.favorite = favorite

    @property
    def description(self):
        """Gets the description of this UpdateQualityCheck.  # noqa: E501


        :return: The description of this UpdateQualityCheck.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdateQualityCheck.


        :param description: The description of this UpdateQualityCheck.  # noqa: E501
        :type: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def coverage(self):
        """Gets the coverage of this UpdateQualityCheck.  # noqa: E501


        :return: The coverage of this UpdateQualityCheck.  # noqa: E501
        :rtype: float
        """
        return self._coverage

    @coverage.setter
    def coverage(self, coverage):
        """Sets the coverage of this UpdateQualityCheck.


        :param coverage: The coverage of this UpdateQualityCheck.  # noqa: E501
        :type: float
        """

        self._coverage = coverage

    @property
    def filter(self):
        """Gets the filter of this UpdateQualityCheck.  # noqa: E501


        :return: The filter of this UpdateQualityCheck.  # noqa: E501
        :rtype: str
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        """Sets the filter of this UpdateQualityCheck.


        :param filter: The filter of this UpdateQualityCheck.  # noqa: E501
        :type: str
        """

        self._filter = filter

    @property
    def properties(self):
        """Gets the properties of this UpdateQualityCheck.  # noqa: E501


        :return: The properties of this UpdateQualityCheck.  # noqa: E501
        :rtype: QualityCheckProperties
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this UpdateQualityCheck.


        :param properties: The properties of this UpdateQualityCheck.  # noqa: E501
        :type: QualityCheckProperties
        """

        self._properties = properties

    @property
    def tags(self):
        """Gets the tags of this UpdateQualityCheck.  # noqa: E501


        :return: The tags of this UpdateQualityCheck.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this UpdateQualityCheck.


        :param tags: The tags of this UpdateQualityCheck.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

    @property
    def favorite(self):
        """Gets the favorite of this UpdateQualityCheck.  # noqa: E501

        If Quality Check is user favorite or not  # noqa: E501

        :return: The favorite of this UpdateQualityCheck.  # noqa: E501
        :rtype: bool
        """
        return self._favorite

    @favorite.setter
    def favorite(self, favorite):
        """Sets the favorite of this UpdateQualityCheck.

        If Quality Check is user favorite or not  # noqa: E501

        :param favorite: The favorite of this UpdateQualityCheck.  # noqa: E501
        :type: bool
        """

        self._favorite = favorite

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
        if issubclass(UpdateQualityCheck, dict):
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
        if not isinstance(other, UpdateQualityCheck):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
