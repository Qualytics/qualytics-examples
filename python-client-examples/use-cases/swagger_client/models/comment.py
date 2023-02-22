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

class Comment(object):
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
        'message': 'str',
        'user': 'User'
    }

    attribute_map = {
        'id': 'id',
        'created': 'created',
        'message': 'message',
        'user': 'user'
    }

    def __init__(self, id=None, created=None, message=None, user=None):  # noqa: E501
        """Comment - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._created = None
        self._message = None
        self._user = None
        self.discriminator = None
        self.id = id
        self.created = created
        self.message = message
        self.user = user

    @property
    def id(self):
        """Gets the id of this Comment.  # noqa: E501


        :return: The id of this Comment.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Comment.


        :param id: The id of this Comment.  # noqa: E501
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def created(self):
        """Gets the created of this Comment.  # noqa: E501


        :return: The created of this Comment.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this Comment.


        :param created: The created of this Comment.  # noqa: E501
        :type: datetime
        """
        if created is None:
            raise ValueError("Invalid value for `created`, must not be `None`")  # noqa: E501

        self._created = created

    @property
    def message(self):
        """Gets the message of this Comment.  # noqa: E501


        :return: The message of this Comment.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this Comment.


        :param message: The message of this Comment.  # noqa: E501
        :type: str
        """
        if message is None:
            raise ValueError("Invalid value for `message`, must not be `None`")  # noqa: E501

        self._message = message

    @property
    def user(self):
        """Gets the user of this Comment.  # noqa: E501


        :return: The user of this Comment.  # noqa: E501
        :rtype: User
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this Comment.


        :param user: The user of this Comment.  # noqa: E501
        :type: User
        """
        if user is None:
            raise ValueError("Invalid value for `user`, must not be `None`")  # noqa: E501

        self._user = user

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
        if issubclass(Comment, dict):
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
        if not isinstance(other, Comment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other