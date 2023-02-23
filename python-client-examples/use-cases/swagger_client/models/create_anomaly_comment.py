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

class CreateAnomalyComment(object):
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
        'message': 'str',
        'anomaly_id': 'int'
    }

    attribute_map = {
        'message': 'message',
        'anomaly_id': 'anomaly_id'
    }

    def __init__(self, message='The content of the `Message`', anomaly_id=None):  # noqa: E501
        """CreateAnomalyComment - a model defined in Swagger"""  # noqa: E501
        self._message = None
        self._anomaly_id = None
        self.discriminator = None
        if message is not None:
            self.message = message
        self.anomaly_id = anomaly_id

    @property
    def message(self):
        """Gets the message of this CreateAnomalyComment.  # noqa: E501


        :return: The message of this CreateAnomalyComment.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this CreateAnomalyComment.


        :param message: The message of this CreateAnomalyComment.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def anomaly_id(self):
        """Gets the anomaly_id of this CreateAnomalyComment.  # noqa: E501

        The `Anomaly` specific id  # noqa: E501

        :return: The anomaly_id of this CreateAnomalyComment.  # noqa: E501
        :rtype: int
        """
        return self._anomaly_id

    @anomaly_id.setter
    def anomaly_id(self, anomaly_id):
        """Sets the anomaly_id of this CreateAnomalyComment.

        The `Anomaly` specific id  # noqa: E501

        :param anomaly_id: The anomaly_id of this CreateAnomalyComment.  # noqa: E501
        :type: int
        """
        if anomaly_id is None:
            raise ValueError("Invalid value for `anomaly_id`, must not be `None`")  # noqa: E501

        self._anomaly_id = anomaly_id

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
        if issubclass(CreateAnomalyComment, dict):
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
        if not isinstance(other, CreateAnomalyComment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
