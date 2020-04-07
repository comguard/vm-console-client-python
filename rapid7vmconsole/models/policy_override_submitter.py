# coding: utf-8

"""
    Python InsightVM API Client

    OpenAPI spec version: 3
    Contact: support@rapid7.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class PolicyOverrideSubmitter(object):
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
        'comment': 'str',
        '_date': 'str',
        'links': 'list[Link]',
        'name': 'str',
        'user': 'int'
    }

    attribute_map = {
        'comment': 'comment',
        '_date': 'date',
        'links': 'links',
        'name': 'name',
        'user': 'user'
    }

    def __init__(self, comment=None, _date=None, links=None, name=None, user=None):  # noqa: E501
        """PolicyOverrideSubmitter - a model defined in Swagger"""  # noqa: E501

        self._comment = None
        self.__date = None
        self._links = None
        self._name = None
        self._user = None
        self.discriminator = None

        self.comment = comment
        if _date is not None:
            self._date = _date
        if links is not None:
            self.links = links
        if name is not None:
            self.name = name
        if user is not None:
            self.user = user

    @property
    def comment(self):
        """Gets the comment of this PolicyOverrideSubmitter.  # noqa: E501

        A comment from the submitter as to why the policy override was submitted. Cannot exceed 1024 characters.  # noqa: E501

        :return: The comment of this PolicyOverrideSubmitter.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this PolicyOverrideSubmitter.

        A comment from the submitter as to why the policy override was submitted. Cannot exceed 1024 characters.  # noqa: E501

        :param comment: The comment of this PolicyOverrideSubmitter.  # noqa: E501
        :type: str
        """
        if comment is None:
            raise ValueError("Invalid value for `comment`, must not be `None`")  # noqa: E501

        self._comment = comment

    @property
    def _date(self):
        """Gets the _date of this PolicyOverrideSubmitter.  # noqa: E501

        The date the policy override was submitted.  # noqa: E501

        :return: The _date of this PolicyOverrideSubmitter.  # noqa: E501
        :rtype: str
        """
        return self.__date

    @_date.setter
    def _date(self, _date):
        """Sets the _date of this PolicyOverrideSubmitter.

        The date the policy override was submitted.  # noqa: E501

        :param _date: The _date of this PolicyOverrideSubmitter.  # noqa: E501
        :type: str
        """

        self.__date = _date

    @property
    def links(self):
        """Gets the links of this PolicyOverrideSubmitter.  # noqa: E501


        :return: The links of this PolicyOverrideSubmitter.  # noqa: E501
        :rtype: list[Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this PolicyOverrideSubmitter.


        :param links: The links of this PolicyOverrideSubmitter.  # noqa: E501
        :type: list[Link]
        """

        self._links = links

    @property
    def name(self):
        """Gets the name of this PolicyOverrideSubmitter.  # noqa: E501

        The login name of the user that submitted the policy override.  # noqa: E501

        :return: The name of this PolicyOverrideSubmitter.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PolicyOverrideSubmitter.

        The login name of the user that submitted the policy override.  # noqa: E501

        :param name: The name of this PolicyOverrideSubmitter.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def user(self):
        """Gets the user of this PolicyOverrideSubmitter.  # noqa: E501

        The identifier of the user that submitted the policy override.  # noqa: E501

        :return: The user of this PolicyOverrideSubmitter.  # noqa: E501
        :rtype: int
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this PolicyOverrideSubmitter.

        The identifier of the user that submitted the policy override.  # noqa: E501

        :param user: The user of this PolicyOverrideSubmitter.  # noqa: E501
        :type: int
        """

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
        if issubclass(PolicyOverrideSubmitter, dict):
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
        if not isinstance(other, PolicyOverrideSubmitter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
