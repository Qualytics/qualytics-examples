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

class CreateScheduleCatalogOperation(object):
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
        'recreate': 'bool',
        'datastore_id': 'int'
    }

    attribute_map = {
        'crontab': 'crontab',
        'type': 'type',
        'include': 'include',
        'prune': 'prune',
        'recreate': 'recreate',
        'datastore_id': 'datastore_id'
    }

    def __init__(self, crontab=None, type='catalog', include=None, prune=True, recreate=False, datastore_id=None):  # noqa: E501
        """CreateScheduleCatalogOperation - a model defined in Swagger"""  # noqa: E501
        self._crontab = None
        self._type = None
        self._include = None
        self._prune = None
        self._recreate = None
        self._datastore_id = None
        self.discriminator = None
        self.crontab = crontab
        if type is not None:
            self.type = type
        if include is not None:
            self.include = include
        if prune is not None:
            self.prune = prune
        if recreate is not None:
            self.recreate = recreate
        self.datastore_id = datastore_id

    @property
    def crontab(self):
        """Gets the crontab of this CreateScheduleCatalogOperation.  # noqa: E501


        :return: The crontab of this CreateScheduleCatalogOperation.  # noqa: E501
        :rtype: str
        """
        return self._crontab

    @crontab.setter
    def crontab(self, crontab):
        """Sets the crontab of this CreateScheduleCatalogOperation.


        :param crontab: The crontab of this CreateScheduleCatalogOperation.  # noqa: E501
        :type: str
        """
        if crontab is None:
            raise ValueError("Invalid value for `crontab`, must not be `None`")  # noqa: E501

        self._crontab = crontab

    @property
    def type(self):
        """Gets the type of this CreateScheduleCatalogOperation.  # noqa: E501


        :return: The type of this CreateScheduleCatalogOperation.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CreateScheduleCatalogOperation.


        :param type: The type of this CreateScheduleCatalogOperation.  # noqa: E501
        :type: str
        """
        allowed_values = ["catalog"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def include(self):
        """Gets the include of this CreateScheduleCatalogOperation.  # noqa: E501


        :return: The include of this CreateScheduleCatalogOperation.  # noqa: E501
        :rtype: list[str]
        """
        return self._include

    @include.setter
    def include(self, include):
        """Sets the include of this CreateScheduleCatalogOperation.


        :param include: The include of this CreateScheduleCatalogOperation.  # noqa: E501
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
        """Gets the prune of this CreateScheduleCatalogOperation.  # noqa: E501

        Delete orphaned datastore containers that are no longer present  # noqa: E501

        :return: The prune of this CreateScheduleCatalogOperation.  # noqa: E501
        :rtype: bool
        """
        return self._prune

    @prune.setter
    def prune(self, prune):
        """Sets the prune of this CreateScheduleCatalogOperation.

        Delete orphaned datastore containers that are no longer present  # noqa: E501

        :param prune: The prune of this CreateScheduleCatalogOperation.  # noqa: E501
        :type: bool
        """

        self._prune = prune

    @property
    def recreate(self):
        """Gets the recreate of this CreateScheduleCatalogOperation.  # noqa: E501

        Restore any datastore containers that have been previously deleted if they are present  # noqa: E501

        :return: The recreate of this CreateScheduleCatalogOperation.  # noqa: E501
        :rtype: bool
        """
        return self._recreate

    @recreate.setter
    def recreate(self, recreate):
        """Sets the recreate of this CreateScheduleCatalogOperation.

        Restore any datastore containers that have been previously deleted if they are present  # noqa: E501

        :param recreate: The recreate of this CreateScheduleCatalogOperation.  # noqa: E501
        :type: bool
        """

        self._recreate = recreate

    @property
    def datastore_id(self):
        """Gets the datastore_id of this CreateScheduleCatalogOperation.  # noqa: E501

        Datastore `Id`  # noqa: E501

        :return: The datastore_id of this CreateScheduleCatalogOperation.  # noqa: E501
        :rtype: int
        """
        return self._datastore_id

    @datastore_id.setter
    def datastore_id(self, datastore_id):
        """Sets the datastore_id of this CreateScheduleCatalogOperation.

        Datastore `Id`  # noqa: E501

        :param datastore_id: The datastore_id of this CreateScheduleCatalogOperation.  # noqa: E501
        :type: int
        """
        if datastore_id is None:
            raise ValueError("Invalid value for `datastore_id`, must not be `None`")  # noqa: E501

        self._datastore_id = datastore_id

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
        if issubclass(CreateScheduleCatalogOperation, dict):
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
        if not isinstance(other, CreateScheduleCatalogOperation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
