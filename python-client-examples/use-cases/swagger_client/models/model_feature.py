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

class ModelFeature(object):
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
        'field_profile': 'FieldProfileCorrelation',
        'coefficient': 'float'
    }

    attribute_map = {
        'id': 'id',
        'created': 'created',
        'field_profile': 'field_profile',
        'coefficient': 'coefficient'
    }

    def __init__(self, id=None, created=None, field_profile=None, coefficient=None):  # noqa: E501
        """ModelFeature - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._created = None
        self._field_profile = None
        self._coefficient = None
        self.discriminator = None
        self.id = id
        self.created = created
        self.field_profile = field_profile
        self.coefficient = coefficient

    @property
    def id(self):
        """Gets the id of this ModelFeature.  # noqa: E501


        :return: The id of this ModelFeature.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ModelFeature.


        :param id: The id of this ModelFeature.  # noqa: E501
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def created(self):
        """Gets the created of this ModelFeature.  # noqa: E501


        :return: The created of this ModelFeature.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this ModelFeature.


        :param created: The created of this ModelFeature.  # noqa: E501
        :type: datetime
        """
        if created is None:
            raise ValueError("Invalid value for `created`, must not be `None`")  # noqa: E501

        self._created = created

    @property
    def field_profile(self):
        """Gets the field_profile of this ModelFeature.  # noqa: E501


        :return: The field_profile of this ModelFeature.  # noqa: E501
        :rtype: FieldProfileCorrelation
        """
        return self._field_profile

    @field_profile.setter
    def field_profile(self, field_profile):
        """Sets the field_profile of this ModelFeature.


        :param field_profile: The field_profile of this ModelFeature.  # noqa: E501
        :type: FieldProfileCorrelation
        """
        if field_profile is None:
            raise ValueError("Invalid value for `field_profile`, must not be `None`")  # noqa: E501

        self._field_profile = field_profile

    @property
    def coefficient(self):
        """Gets the coefficient of this ModelFeature.  # noqa: E501


        :return: The coefficient of this ModelFeature.  # noqa: E501
        :rtype: float
        """
        return self._coefficient

    @coefficient.setter
    def coefficient(self, coefficient):
        """Sets the coefficient of this ModelFeature.


        :param coefficient: The coefficient of this ModelFeature.  # noqa: E501
        :type: float
        """
        if coefficient is None:
            raise ValueError("Invalid value for `coefficient`, must not be `None`")  # noqa: E501

        self._coefficient = coefficient

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
        if issubclass(ModelFeature, dict):
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
        if not isinstance(other, ModelFeature):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
