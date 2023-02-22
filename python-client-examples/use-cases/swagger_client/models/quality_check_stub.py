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

class QualityCheckStub(object):
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
        'fields': 'list[FieldStub]',
        'description': 'str',
        'rule_type': 'RuleType',
        'coverage': 'float',
        'properties': 'QualityCheckProperties',
        'deleted_at': 'datetime',
        'last_editor': 'User'
    }

    attribute_map = {
        'id': 'id',
        'fields': 'fields',
        'description': 'description',
        'rule_type': 'rule_type',
        'coverage': 'coverage',
        'properties': 'properties',
        'deleted_at': 'deleted_at',
        'last_editor': 'last_editor'
    }

    def __init__(self, id=None, fields=None, description=None, rule_type=None, coverage=None, properties=None, deleted_at=None, last_editor=None):  # noqa: E501
        """QualityCheckStub - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._fields = None
        self._description = None
        self._rule_type = None
        self._coverage = None
        self._properties = None
        self._deleted_at = None
        self._last_editor = None
        self.discriminator = None
        self.id = id
        if fields is not None:
            self.fields = fields
        if description is not None:
            self.description = description
        self.rule_type = rule_type
        self.coverage = coverage
        if properties is not None:
            self.properties = properties
        if deleted_at is not None:
            self.deleted_at = deleted_at
        if last_editor is not None:
            self.last_editor = last_editor

    @property
    def id(self):
        """Gets the id of this QualityCheckStub.  # noqa: E501


        :return: The id of this QualityCheckStub.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this QualityCheckStub.


        :param id: The id of this QualityCheckStub.  # noqa: E501
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def fields(self):
        """Gets the fields of this QualityCheckStub.  # noqa: E501


        :return: The fields of this QualityCheckStub.  # noqa: E501
        :rtype: list[FieldStub]
        """
        return self._fields

    @fields.setter
    def fields(self, fields):
        """Sets the fields of this QualityCheckStub.


        :param fields: The fields of this QualityCheckStub.  # noqa: E501
        :type: list[FieldStub]
        """

        self._fields = fields

    @property
    def description(self):
        """Gets the description of this QualityCheckStub.  # noqa: E501


        :return: The description of this QualityCheckStub.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this QualityCheckStub.


        :param description: The description of this QualityCheckStub.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def rule_type(self):
        """Gets the rule_type of this QualityCheckStub.  # noqa: E501


        :return: The rule_type of this QualityCheckStub.  # noqa: E501
        :rtype: RuleType
        """
        return self._rule_type

    @rule_type.setter
    def rule_type(self, rule_type):
        """Sets the rule_type of this QualityCheckStub.


        :param rule_type: The rule_type of this QualityCheckStub.  # noqa: E501
        :type: RuleType
        """
        if rule_type is None:
            raise ValueError("Invalid value for `rule_type`, must not be `None`")  # noqa: E501

        self._rule_type = rule_type

    @property
    def coverage(self):
        """Gets the coverage of this QualityCheckStub.  # noqa: E501


        :return: The coverage of this QualityCheckStub.  # noqa: E501
        :rtype: float
        """
        return self._coverage

    @coverage.setter
    def coverage(self, coverage):
        """Sets the coverage of this QualityCheckStub.


        :param coverage: The coverage of this QualityCheckStub.  # noqa: E501
        :type: float
        """
        if coverage is None:
            raise ValueError("Invalid value for `coverage`, must not be `None`")  # noqa: E501

        self._coverage = coverage

    @property
    def properties(self):
        """Gets the properties of this QualityCheckStub.  # noqa: E501


        :return: The properties of this QualityCheckStub.  # noqa: E501
        :rtype: QualityCheckProperties
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this QualityCheckStub.


        :param properties: The properties of this QualityCheckStub.  # noqa: E501
        :type: QualityCheckProperties
        """

        self._properties = properties

    @property
    def deleted_at(self):
        """Gets the deleted_at of this QualityCheckStub.  # noqa: E501


        :return: The deleted_at of this QualityCheckStub.  # noqa: E501
        :rtype: datetime
        """
        return self._deleted_at

    @deleted_at.setter
    def deleted_at(self, deleted_at):
        """Sets the deleted_at of this QualityCheckStub.


        :param deleted_at: The deleted_at of this QualityCheckStub.  # noqa: E501
        :type: datetime
        """

        self._deleted_at = deleted_at

    @property
    def last_editor(self):
        """Gets the last_editor of this QualityCheckStub.  # noqa: E501


        :return: The last_editor of this QualityCheckStub.  # noqa: E501
        :rtype: User
        """
        return self._last_editor

    @last_editor.setter
    def last_editor(self, last_editor):
        """Sets the last_editor of this QualityCheckStub.


        :param last_editor: The last_editor of this QualityCheckStub.  # noqa: E501
        :type: User
        """

        self._last_editor = last_editor

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
        if issubclass(QualityCheckStub, dict):
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
        if not isinstance(other, QualityCheckStub):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
