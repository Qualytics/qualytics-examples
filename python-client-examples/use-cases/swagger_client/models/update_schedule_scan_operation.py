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

class UpdateScheduleScanOperation(object):
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
        'container_names': 'list[str]',
        'incremental': 'bool',
        'remediation': 'str',
        'max_records_analyzed_per_partition': 'int'
    }

    attribute_map = {
        'crontab': 'crontab',
        'type': 'type',
        'container_names': 'container_names',
        'incremental': 'incremental',
        'remediation': 'remediation',
        'max_records_analyzed_per_partition': 'max_records_analyzed_per_partition'
    }

    def __init__(self, crontab=None, type=None, container_names=None, incremental=True, remediation='none', max_records_analyzed_per_partition=None):  # noqa: E501
        """UpdateScheduleScanOperation - a model defined in Swagger"""  # noqa: E501
        self._crontab = None
        self._type = None
        self._container_names = None
        self._incremental = None
        self._remediation = None
        self._max_records_analyzed_per_partition = None
        self.discriminator = None
        self.crontab = crontab
        self.type = type
        if container_names is not None:
            self.container_names = container_names
        if incremental is not None:
            self.incremental = incremental
        if remediation is not None:
            self.remediation = remediation
        if max_records_analyzed_per_partition is not None:
            self.max_records_analyzed_per_partition = max_records_analyzed_per_partition

    @property
    def crontab(self):
        """Gets the crontab of this UpdateScheduleScanOperation.  # noqa: E501


        :return: The crontab of this UpdateScheduleScanOperation.  # noqa: E501
        :rtype: str
        """
        return self._crontab

    @crontab.setter
    def crontab(self, crontab):
        """Sets the crontab of this UpdateScheduleScanOperation.


        :param crontab: The crontab of this UpdateScheduleScanOperation.  # noqa: E501
        :type: str
        """
        if crontab is None:
            raise ValueError("Invalid value for `crontab`, must not be `None`")  # noqa: E501

        self._crontab = crontab

    @property
    def type(self):
        """Gets the type of this UpdateScheduleScanOperation.  # noqa: E501

        Operation type  # noqa: E501

        :return: The type of this UpdateScheduleScanOperation.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this UpdateScheduleScanOperation.

        Operation type  # noqa: E501

        :param type: The type of this UpdateScheduleScanOperation.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["scan"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def container_names(self):
        """Gets the container_names of this UpdateScheduleScanOperation.  # noqa: E501


        :return: The container_names of this UpdateScheduleScanOperation.  # noqa: E501
        :rtype: list[str]
        """
        return self._container_names

    @container_names.setter
    def container_names(self, container_names):
        """Sets the container_names of this UpdateScheduleScanOperation.


        :param container_names: The container_names of this UpdateScheduleScanOperation.  # noqa: E501
        :type: list[str]
        """

        self._container_names = container_names

    @property
    def incremental(self):
        """Gets the incremental of this UpdateScheduleScanOperation.  # noqa: E501


        :return: The incremental of this UpdateScheduleScanOperation.  # noqa: E501
        :rtype: bool
        """
        return self._incremental

    @incremental.setter
    def incremental(self, incremental):
        """Sets the incremental of this UpdateScheduleScanOperation.


        :param incremental: The incremental of this UpdateScheduleScanOperation.  # noqa: E501
        :type: bool
        """

        self._incremental = incremental

    @property
    def remediation(self):
        """Gets the remediation of this UpdateScheduleScanOperation.  # noqa: E501


        :return: The remediation of this UpdateScheduleScanOperation.  # noqa: E501
        :rtype: str
        """
        return self._remediation

    @remediation.setter
    def remediation(self, remediation):
        """Sets the remediation of this UpdateScheduleScanOperation.


        :param remediation: The remediation of this UpdateScheduleScanOperation.  # noqa: E501
        :type: str
        """
        allowed_values = ["none", "append", "overwrite"]  # noqa: E501
        if remediation not in allowed_values:
            raise ValueError(
                "Invalid value for `remediation` ({0}), must be one of {1}"  # noqa: E501
                .format(remediation, allowed_values)
            )

        self._remediation = remediation

    @property
    def max_records_analyzed_per_partition(self):
        """Gets the max_records_analyzed_per_partition of this UpdateScheduleScanOperation.  # noqa: E501


        :return: The max_records_analyzed_per_partition of this UpdateScheduleScanOperation.  # noqa: E501
        :rtype: int
        """
        return self._max_records_analyzed_per_partition

    @max_records_analyzed_per_partition.setter
    def max_records_analyzed_per_partition(self, max_records_analyzed_per_partition):
        """Sets the max_records_analyzed_per_partition of this UpdateScheduleScanOperation.


        :param max_records_analyzed_per_partition: The max_records_analyzed_per_partition of this UpdateScheduleScanOperation.  # noqa: E501
        :type: int
        """

        self._max_records_analyzed_per_partition = max_records_analyzed_per_partition

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
        if issubclass(UpdateScheduleScanOperation, dict):
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
        if not isinstance(other, UpdateScheduleScanOperation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
