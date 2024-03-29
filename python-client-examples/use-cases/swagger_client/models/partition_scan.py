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

class PartitionScan(object):
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
        'partition': 'Partition',
        'records_processed': 'int',
        'result': 'str',
        'message': 'str',
        'anomalies': 'list[Anomaly]'
    }

    attribute_map = {
        'id': 'id',
        'created': 'created',
        'partition': 'partition',
        'records_processed': 'records_processed',
        'result': 'result',
        'message': 'message',
        'anomalies': 'anomalies'
    }

    def __init__(self, id=None, created=None, partition=None, records_processed=None, result=None, message=None, anomalies=None):  # noqa: E501
        """PartitionScan - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._created = None
        self._partition = None
        self._records_processed = None
        self._result = None
        self._message = None
        self._anomalies = None
        self.discriminator = None
        self.id = id
        self.created = created
        self.partition = partition
        self.records_processed = records_processed
        self.result = result
        if message is not None:
            self.message = message
        if anomalies is not None:
            self.anomalies = anomalies

    @property
    def id(self):
        """Gets the id of this PartitionScan.  # noqa: E501


        :return: The id of this PartitionScan.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PartitionScan.


        :param id: The id of this PartitionScan.  # noqa: E501
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def created(self):
        """Gets the created of this PartitionScan.  # noqa: E501


        :return: The created of this PartitionScan.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this PartitionScan.


        :param created: The created of this PartitionScan.  # noqa: E501
        :type: datetime
        """
        if created is None:
            raise ValueError("Invalid value for `created`, must not be `None`")  # noqa: E501

        self._created = created

    @property
    def partition(self):
        """Gets the partition of this PartitionScan.  # noqa: E501


        :return: The partition of this PartitionScan.  # noqa: E501
        :rtype: Partition
        """
        return self._partition

    @partition.setter
    def partition(self, partition):
        """Sets the partition of this PartitionScan.


        :param partition: The partition of this PartitionScan.  # noqa: E501
        :type: Partition
        """
        if partition is None:
            raise ValueError("Invalid value for `partition`, must not be `None`")  # noqa: E501

        self._partition = partition

    @property
    def records_processed(self):
        """Gets the records_processed of this PartitionScan.  # noqa: E501


        :return: The records_processed of this PartitionScan.  # noqa: E501
        :rtype: int
        """
        return self._records_processed

    @records_processed.setter
    def records_processed(self, records_processed):
        """Sets the records_processed of this PartitionScan.


        :param records_processed: The records_processed of this PartitionScan.  # noqa: E501
        :type: int
        """
        if records_processed is None:
            raise ValueError("Invalid value for `records_processed`, must not be `None`")  # noqa: E501

        self._records_processed = records_processed

    @property
    def result(self):
        """Gets the result of this PartitionScan.  # noqa: E501


        :return: The result of this PartitionScan.  # noqa: E501
        :rtype: str
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this PartitionScan.


        :param result: The result of this PartitionScan.  # noqa: E501
        :type: str
        """
        if result is None:
            raise ValueError("Invalid value for `result`, must not be `None`")  # noqa: E501
        allowed_values = ["success", "failure"]  # noqa: E501
        if result not in allowed_values:
            raise ValueError(
                "Invalid value for `result` ({0}), must be one of {1}"  # noqa: E501
                .format(result, allowed_values)
            )

        self._result = result

    @property
    def message(self):
        """Gets the message of this PartitionScan.  # noqa: E501


        :return: The message of this PartitionScan.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this PartitionScan.


        :param message: The message of this PartitionScan.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def anomalies(self):
        """Gets the anomalies of this PartitionScan.  # noqa: E501


        :return: The anomalies of this PartitionScan.  # noqa: E501
        :rtype: list[Anomaly]
        """
        return self._anomalies

    @anomalies.setter
    def anomalies(self, anomalies):
        """Sets the anomalies of this PartitionScan.


        :param anomalies: The anomalies of this PartitionScan.  # noqa: E501
        :type: list[Anomaly]
        """

        self._anomalies = anomalies

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
        if issubclass(PartitionScan, dict):
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
        if not isinstance(other, PartitionScan):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
