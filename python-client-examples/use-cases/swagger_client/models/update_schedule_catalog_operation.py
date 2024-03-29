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

class UpdateScheduleCatalogOperation(object):
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
        'crontab': 'str',
        'type': 'str',
        'include': 'list[str]',
        'prune': 'bool',
        'recreate': 'bool'
    }

    attribute_map = {
        'crontab': 'crontab',
        'type': 'type',
        'include': 'include',
        'prune': 'prune',
        'recreate': 'recreate'
    }

    def __init__(self, crontab=None, type=None, include=None, prune=True, recreate=False):  # noqa: E501
        """UpdateScheduleCatalogOperation - a model defined in Swagger"""  # noqa: E501
        self._crontab = None
        self._type = None
        self._include = None
        self._prune = None
        self._recreate = None
        self.discriminator = None
        self.crontab = crontab
        self.type = type
        if include is not None:
            self.include = include
        if prune is not None:
            self.prune = prune
        if recreate is not None:
            self.recreate = recreate

    @property
    def crontab(self):
        """Gets the crontab of this UpdateScheduleCatalogOperation.  # noqa: E501


        :return: The crontab of this UpdateScheduleCatalogOperation.  # noqa: E501
        :rtype: str
        """
        return self._crontab

    @crontab.setter
    def crontab(self, crontab):
        """Sets the crontab of this UpdateScheduleCatalogOperation.


        :param crontab: The crontab of this UpdateScheduleCatalogOperation.  # noqa: E501
        :type: str
        """
        if crontab is None:
            raise ValueError("Invalid value for `crontab`, must not be `None`")  # noqa: E501

        self._crontab = crontab

    @property
    def type(self):
        """Gets the type of this UpdateScheduleCatalogOperation.  # noqa: E501

        Operation type  # noqa: E501

        :return: The type of this UpdateScheduleCatalogOperation.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this UpdateScheduleCatalogOperation.

        Operation type  # noqa: E501

        :param type: The type of this UpdateScheduleCatalogOperation.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["catalog"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def include(self):
        """Gets the include of this UpdateScheduleCatalogOperation.  # noqa: E501


        :return: The include of this UpdateScheduleCatalogOperation.  # noqa: E501
        :rtype: list[str]
        """
        return self._include

    @include.setter
    def include(self, include):
        """Sets the include of this UpdateScheduleCatalogOperation.


        :param include: The include of this UpdateScheduleCatalogOperation.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["table", "view"]  # noqa: E501
        if not set(include).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `include` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(include) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._include = include

    @property
    def prune(self):
        """Gets the prune of this UpdateScheduleCatalogOperation.  # noqa: E501

        Delete orphaned datastore containers that are no longer present  # noqa: E501

        :return: The prune of this UpdateScheduleCatalogOperation.  # noqa: E501
        :rtype: bool
        """
        return self._prune

    @prune.setter
    def prune(self, prune):
        """Sets the prune of this UpdateScheduleCatalogOperation.

        Delete orphaned datastore containers that are no longer present  # noqa: E501

        :param prune: The prune of this UpdateScheduleCatalogOperation.  # noqa: E501
        :type: bool
        """

        self._prune = prune

    @property
    def recreate(self):
        """Gets the recreate of this UpdateScheduleCatalogOperation.  # noqa: E501

        Restore any datastore containers that have been previously deleted if they are present  # noqa: E501

        :return: The recreate of this UpdateScheduleCatalogOperation.  # noqa: E501
        :rtype: bool
        """
        return self._recreate

    @recreate.setter
    def recreate(self, recreate):
        """Sets the recreate of this UpdateScheduleCatalogOperation.

        Restore any datastore containers that have been previously deleted if they are present  # noqa: E501

        :param recreate: The recreate of this UpdateScheduleCatalogOperation.  # noqa: E501
        :type: bool
        """

        self._recreate = recreate

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
        if issubclass(UpdateScheduleCatalogOperation, dict):
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
        if not isinstance(other, UpdateScheduleCatalogOperation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
