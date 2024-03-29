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

class UserStub(object):
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
        'user_id': 'str',
        'email': 'str',
        'name': 'str',
        'role': 'UserRoleType'
    }

    attribute_map = {
        'id': 'id',
        'created': 'created',
        'user_id': 'user_id',
        'email': 'email',
        'name': 'name',
        'role': 'role'
    }

    def __init__(self, id=None, created=None, user_id=None, email=None, name=None, role=None):  # noqa: E501
        """UserStub - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._created = None
        self._user_id = None
        self._email = None
        self._name = None
        self._role = None
        self.discriminator = None
        self.id = id
        self.created = created
        self.user_id = user_id
        if email is not None:
            self.email = email
        if name is not None:
            self.name = name
        if role is not None:
            self.role = role

    @property
    def id(self):
        """Gets the id of this UserStub.  # noqa: E501


        :return: The id of this UserStub.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UserStub.


        :param id: The id of this UserStub.  # noqa: E501
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def created(self):
        """Gets the created of this UserStub.  # noqa: E501


        :return: The created of this UserStub.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this UserStub.


        :param created: The created of this UserStub.  # noqa: E501
        :type: datetime
        """
        if created is None:
            raise ValueError("Invalid value for `created`, must not be `None`")  # noqa: E501

        self._created = created

    @property
    def user_id(self):
        """Gets the user_id of this UserStub.  # noqa: E501


        :return: The user_id of this UserStub.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this UserStub.


        :param user_id: The user_id of this UserStub.  # noqa: E501
        :type: str
        """
        if user_id is None:
            raise ValueError("Invalid value for `user_id`, must not be `None`")  # noqa: E501

        self._user_id = user_id

    @property
    def email(self):
        """Gets the email of this UserStub.  # noqa: E501


        :return: The email of this UserStub.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this UserStub.


        :param email: The email of this UserStub.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def name(self):
        """Gets the name of this UserStub.  # noqa: E501


        :return: The name of this UserStub.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UserStub.


        :param name: The name of this UserStub.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def role(self):
        """Gets the role of this UserStub.  # noqa: E501


        :return: The role of this UserStub.  # noqa: E501
        :rtype: UserRoleType
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this UserStub.


        :param role: The role of this UserStub.  # noqa: E501
        :type: UserRoleType
        """

        self._role = role

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
        if issubclass(UserStub, dict):
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
        if not isinstance(other, UserStub):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
