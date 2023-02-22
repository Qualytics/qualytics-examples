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

class KllStore(object):
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
        'data': 'object',
        'parameters': 'KllParameters',
        'high': 'float'
    }

    attribute_map = {
        'id': 'id',
        'created': 'created',
        'data': 'data',
        'parameters': 'parameters',
        'high': 'high'
    }

    def __init__(self, id=None, created=None, data=None, parameters=None, high=None):  # noqa: E501
        """KllStore - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._created = None
        self._data = None
        self._parameters = None
        self._high = None
        self.discriminator = None
        self.id = id
        self.created = created
        self.data = data
        self.parameters = parameters
        self.high = high

    @property
    def id(self):
        """Gets the id of this KllStore.  # noqa: E501


        :return: The id of this KllStore.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this KllStore.


        :param id: The id of this KllStore.  # noqa: E501
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def created(self):
        """Gets the created of this KllStore.  # noqa: E501


        :return: The created of this KllStore.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this KllStore.


        :param created: The created of this KllStore.  # noqa: E501
        :type: datetime
        """
        if created is None:
            raise ValueError("Invalid value for `created`, must not be `None`")  # noqa: E501

        self._created = created

    @property
    def data(self):
        """Gets the data of this KllStore.  # noqa: E501


        :return: The data of this KllStore.  # noqa: E501
        :rtype: object
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this KllStore.


        :param data: The data of this KllStore.  # noqa: E501
        :type: object
        """
        if data is None:
            raise ValueError("Invalid value for `data`, must not be `None`")  # noqa: E501

        self._data = data

    @property
    def parameters(self):
        """Gets the parameters of this KllStore.  # noqa: E501


        :return: The parameters of this KllStore.  # noqa: E501
        :rtype: KllParameters
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this KllStore.


        :param parameters: The parameters of this KllStore.  # noqa: E501
        :type: KllParameters
        """
        if parameters is None:
            raise ValueError("Invalid value for `parameters`, must not be `None`")  # noqa: E501

        self._parameters = parameters

    @property
    def high(self):
        """Gets the high of this KllStore.  # noqa: E501


        :return: The high of this KllStore.  # noqa: E501
        :rtype: float
        """
        return self._high

    @high.setter
    def high(self, high):
        """Sets the high of this KllStore.


        :param high: The high of this KllStore.  # noqa: E501
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
        if issubclass(KllStore, dict):
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
        if not isinstance(other, KllStore):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other