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

class GetQualityCheckSpec(object):
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
        'rule': 'str',
        'rule_description': 'str',
        'author': 'bool',
        'fields': 'str',
        'fields_type_filter': 'list[FieldType]',
        'properties': 'list[GetQualityCheckSpecProperties]'
    }

    attribute_map = {
        'rule': 'rule',
        'rule_description': 'rule_description',
        'author': 'author',
        'fields': 'fields',
        'fields_type_filter': 'fields_type_filter',
        'properties': 'properties'
    }

    def __init__(self, rule=None, rule_description=None, author=None, fields=None, fields_type_filter=None, properties=None):  # noqa: E501
        """GetQualityCheckSpec - a model defined in Swagger"""  # noqa: E501
        self._rule = None
        self._rule_description = None
        self._author = None
        self._fields = None
        self._fields_type_filter = None
        self._properties = None
        self.discriminator = None
        self.rule = rule
        self.rule_description = rule_description
        self.author = author
        self.fields = fields
        if fields_type_filter is not None:
            self.fields_type_filter = fields_type_filter
        self.properties = properties

    @property
    def rule(self):
        """Gets the rule of this GetQualityCheckSpec.  # noqa: E501


        :return: The rule of this GetQualityCheckSpec.  # noqa: E501
        :rtype: str
        """
        return self._rule

    @rule.setter
    def rule(self, rule):
        """Sets the rule of this GetQualityCheckSpec.


        :param rule: The rule of this GetQualityCheckSpec.  # noqa: E501
        :type: str
        """
        if rule is None:
            raise ValueError("Invalid value for `rule`, must not be `None`")  # noqa: E501

        self._rule = rule

    @property
    def rule_description(self):
        """Gets the rule_description of this GetQualityCheckSpec.  # noqa: E501


        :return: The rule_description of this GetQualityCheckSpec.  # noqa: E501
        :rtype: str
        """
        return self._rule_description

    @rule_description.setter
    def rule_description(self, rule_description):
        """Sets the rule_description of this GetQualityCheckSpec.


        :param rule_description: The rule_description of this GetQualityCheckSpec.  # noqa: E501
        :type: str
        """
        if rule_description is None:
            raise ValueError("Invalid value for `rule_description`, must not be `None`")  # noqa: E501

        self._rule_description = rule_description

    @property
    def author(self):
        """Gets the author of this GetQualityCheckSpec.  # noqa: E501


        :return: The author of this GetQualityCheckSpec.  # noqa: E501
        :rtype: bool
        """
        return self._author

    @author.setter
    def author(self, author):
        """Sets the author of this GetQualityCheckSpec.


        :param author: The author of this GetQualityCheckSpec.  # noqa: E501
        :type: bool
        """
        if author is None:
            raise ValueError("Invalid value for `author`, must not be `None`")  # noqa: E501

        self._author = author

    @property
    def fields(self):
        """Gets the fields of this GetQualityCheckSpec.  # noqa: E501


        :return: The fields of this GetQualityCheckSpec.  # noqa: E501
        :rtype: str
        """
        return self._fields

    @fields.setter
    def fields(self, fields):
        """Sets the fields of this GetQualityCheckSpec.


        :param fields: The fields of this GetQualityCheckSpec.  # noqa: E501
        :type: str
        """
        if fields is None:
            raise ValueError("Invalid value for `fields`, must not be `None`")  # noqa: E501
        allowed_values = ["single", "multi", "none"]  # noqa: E501
        if fields not in allowed_values:
            raise ValueError(
                "Invalid value for `fields` ({0}), must be one of {1}"  # noqa: E501
                .format(fields, allowed_values)
            )

        self._fields = fields

    @property
    def fields_type_filter(self):
        """Gets the fields_type_filter of this GetQualityCheckSpec.  # noqa: E501


        :return: The fields_type_filter of this GetQualityCheckSpec.  # noqa: E501
        :rtype: list[FieldType]
        """
        return self._fields_type_filter

    @fields_type_filter.setter
    def fields_type_filter(self, fields_type_filter):
        """Sets the fields_type_filter of this GetQualityCheckSpec.


        :param fields_type_filter: The fields_type_filter of this GetQualityCheckSpec.  # noqa: E501
        :type: list[FieldType]
        """

        self._fields_type_filter = fields_type_filter

    @property
    def properties(self):
        """Gets the properties of this GetQualityCheckSpec.  # noqa: E501


        :return: The properties of this GetQualityCheckSpec.  # noqa: E501
        :rtype: list[GetQualityCheckSpecProperties]
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this GetQualityCheckSpec.


        :param properties: The properties of this GetQualityCheckSpec.  # noqa: E501
        :type: list[GetQualityCheckSpecProperties]
        """
        if properties is None:
            raise ValueError("Invalid value for `properties`, must not be `None`")  # noqa: E501

        self._properties = properties

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
        if issubclass(GetQualityCheckSpec, dict):
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
        if not isinstance(other, GetQualityCheckSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
