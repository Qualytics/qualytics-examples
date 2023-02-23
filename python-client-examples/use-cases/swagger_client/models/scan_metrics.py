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

class ScanMetrics(object):
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
        'total_partitions_scanned': 'int',
        'total_records_scanned': 'int',
        'total_anomalies_caught': 'int',
        'range_metrics': 'ScanRangeMetrics',
        'daily_metrics': 'list[ScanDailyMetrics]'
    }

    attribute_map = {
        'total_partitions_scanned': 'total_partitions_scanned',
        'total_records_scanned': 'total_records_scanned',
        'total_anomalies_caught': 'total_anomalies_caught',
        'range_metrics': 'range_metrics',
        'daily_metrics': 'daily_metrics'
    }

    def __init__(self, total_partitions_scanned=None, total_records_scanned=None, total_anomalies_caught=None, range_metrics=None, daily_metrics=None):  # noqa: E501
        """ScanMetrics - a model defined in Swagger"""  # noqa: E501
        self._total_partitions_scanned = None
        self._total_records_scanned = None
        self._total_anomalies_caught = None
        self._range_metrics = None
        self._daily_metrics = None
        self.discriminator = None
        self.total_partitions_scanned = total_partitions_scanned
        self.total_records_scanned = total_records_scanned
        self.total_anomalies_caught = total_anomalies_caught
        self.range_metrics = range_metrics
        self.daily_metrics = daily_metrics

    @property
    def total_partitions_scanned(self):
        """Gets the total_partitions_scanned of this ScanMetrics.  # noqa: E501


        :return: The total_partitions_scanned of this ScanMetrics.  # noqa: E501
        :rtype: int
        """
        return self._total_partitions_scanned

    @total_partitions_scanned.setter
    def total_partitions_scanned(self, total_partitions_scanned):
        """Sets the total_partitions_scanned of this ScanMetrics.


        :param total_partitions_scanned: The total_partitions_scanned of this ScanMetrics.  # noqa: E501
        :type: int
        """
        if total_partitions_scanned is None:
            raise ValueError("Invalid value for `total_partitions_scanned`, must not be `None`")  # noqa: E501

        self._total_partitions_scanned = total_partitions_scanned

    @property
    def total_records_scanned(self):
        """Gets the total_records_scanned of this ScanMetrics.  # noqa: E501


        :return: The total_records_scanned of this ScanMetrics.  # noqa: E501
        :rtype: int
        """
        return self._total_records_scanned

    @total_records_scanned.setter
    def total_records_scanned(self, total_records_scanned):
        """Sets the total_records_scanned of this ScanMetrics.


        :param total_records_scanned: The total_records_scanned of this ScanMetrics.  # noqa: E501
        :type: int
        """
        if total_records_scanned is None:
            raise ValueError("Invalid value for `total_records_scanned`, must not be `None`")  # noqa: E501

        self._total_records_scanned = total_records_scanned

    @property
    def total_anomalies_caught(self):
        """Gets the total_anomalies_caught of this ScanMetrics.  # noqa: E501


        :return: The total_anomalies_caught of this ScanMetrics.  # noqa: E501
        :rtype: int
        """
        return self._total_anomalies_caught

    @total_anomalies_caught.setter
    def total_anomalies_caught(self, total_anomalies_caught):
        """Sets the total_anomalies_caught of this ScanMetrics.


        :param total_anomalies_caught: The total_anomalies_caught of this ScanMetrics.  # noqa: E501
        :type: int
        """
        if total_anomalies_caught is None:
            raise ValueError("Invalid value for `total_anomalies_caught`, must not be `None`")  # noqa: E501

        self._total_anomalies_caught = total_anomalies_caught

    @property
    def range_metrics(self):
        """Gets the range_metrics of this ScanMetrics.  # noqa: E501


        :return: The range_metrics of this ScanMetrics.  # noqa: E501
        :rtype: ScanRangeMetrics
        """
        return self._range_metrics

    @range_metrics.setter
    def range_metrics(self, range_metrics):
        """Sets the range_metrics of this ScanMetrics.


        :param range_metrics: The range_metrics of this ScanMetrics.  # noqa: E501
        :type: ScanRangeMetrics
        """
        if range_metrics is None:
            raise ValueError("Invalid value for `range_metrics`, must not be `None`")  # noqa: E501

        self._range_metrics = range_metrics

    @property
    def daily_metrics(self):
        """Gets the daily_metrics of this ScanMetrics.  # noqa: E501


        :return: The daily_metrics of this ScanMetrics.  # noqa: E501
        :rtype: list[ScanDailyMetrics]
        """
        return self._daily_metrics

    @daily_metrics.setter
    def daily_metrics(self, daily_metrics):
        """Sets the daily_metrics of this ScanMetrics.


        :param daily_metrics: The daily_metrics of this ScanMetrics.  # noqa: E501
        :type: list[ScanDailyMetrics]
        """
        if daily_metrics is None:
            raise ValueError("Invalid value for `daily_metrics`, must not be `None`")  # noqa: E501

        self._daily_metrics = daily_metrics

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
        if issubclass(ScanMetrics, dict):
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
        if not isinstance(other, ScanMetrics):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
