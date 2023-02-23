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

class UpdateContainerFreshnessSla(object):
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
        'first_starting_time': 'datetime',
        'repeating_duration': 'int',
        'duration_units': 'str'
    }

    attribute_map = {
        'first_starting_time': 'first_starting_time',
        'repeating_duration': 'repeating_duration',
        'duration_units': 'duration_units'
    }

    def __init__(self, first_starting_time=None, repeating_duration=None, duration_units='minutes'):  # noqa: E501
        """UpdateContainerFreshnessSla - a model defined in Swagger"""  # noqa: E501
        self._first_starting_time = None
        self._repeating_duration = None
        self._duration_units = None
        self.discriminator = None
        self.first_starting_time = first_starting_time
        self.repeating_duration = repeating_duration
        if duration_units is not None:
            self.duration_units = duration_units

    @property
    def first_starting_time(self):
        """Gets the first_starting_time of this UpdateContainerFreshnessSla.  # noqa: E501

        Start time of `Freshness SLA`  # noqa: E501

        :return: The first_starting_time of this UpdateContainerFreshnessSla.  # noqa: E501
        :rtype: datetime
        """
        return self._first_starting_time

    @first_starting_time.setter
    def first_starting_time(self, first_starting_time):
        """Sets the first_starting_time of this UpdateContainerFreshnessSla.

        Start time of `Freshness SLA`  # noqa: E501

        :param first_starting_time: The first_starting_time of this UpdateContainerFreshnessSla.  # noqa: E501
        :type: datetime
        """
        if first_starting_time is None:
            raise ValueError("Invalid value for `first_starting_time`, must not be `None`")  # noqa: E501

        self._first_starting_time = first_starting_time

    @property
    def repeating_duration(self):
        """Gets the repeating_duration of this UpdateContainerFreshnessSla.  # noqa: E501

        Repeating duration time of `Freshness SLA`  # noqa: E501

        :return: The repeating_duration of this UpdateContainerFreshnessSla.  # noqa: E501
        :rtype: int
        """
        return self._repeating_duration

    @repeating_duration.setter
    def repeating_duration(self, repeating_duration):
        """Sets the repeating_duration of this UpdateContainerFreshnessSla.

        Repeating duration time of `Freshness SLA`  # noqa: E501

        :param repeating_duration: The repeating_duration of this UpdateContainerFreshnessSla.  # noqa: E501
        :type: int
        """
        if repeating_duration is None:
            raise ValueError("Invalid value for `repeating_duration`, must not be `None`")  # noqa: E501

        self._repeating_duration = repeating_duration

    @property
    def duration_units(self):
        """Gets the duration_units of this UpdateContainerFreshnessSla.  # noqa: E501

        Unit time duration of `Freshness SLA`  # noqa: E501

        :return: The duration_units of this UpdateContainerFreshnessSla.  # noqa: E501
        :rtype: str
        """
        return self._duration_units

    @duration_units.setter
    def duration_units(self, duration_units):
        """Sets the duration_units of this UpdateContainerFreshnessSla.

        Unit time duration of `Freshness SLA`  # noqa: E501

        :param duration_units: The duration_units of this UpdateContainerFreshnessSla.  # noqa: E501
        :type: str
        """
        allowed_values = ["minutes", "hours", "days", "months"]  # noqa: E501
        if duration_units not in allowed_values:
            raise ValueError(
                "Invalid value for `duration_units` ({0}), must be one of {1}"  # noqa: E501
                .format(duration_units, allowed_values)
            )

        self._duration_units = duration_units

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
        if issubclass(UpdateContainerFreshnessSla, dict):
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
        if not isinstance(other, UpdateContainerFreshnessSla):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
