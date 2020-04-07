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


class PolicyItem(object):
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
        'assets': 'AssetPolicyAssessment',
        'description': 'str',
        'has_override': 'bool',
        'id': 'int',
        'is_unscored': 'bool',
        'links': 'list[Link]',
        'name': 'str',
        'policy': 'PolicyMetadataResource',
        'rules': 'PolicyRuleAssessmentResource',
        'scope': 'str',
        'status': 'str',
        'title': 'str',
        'type': 'str'
    }

    attribute_map = {
        'assets': 'assets',
        'description': 'description',
        'has_override': 'hasOverride',
        'id': 'id',
        'is_unscored': 'isUnscored',
        'links': 'links',
        'name': 'name',
        'policy': 'policy',
        'rules': 'rules',
        'scope': 'scope',
        'status': 'status',
        'title': 'title',
        'type': 'type'
    }

    def __init__(self, assets=None, description=None, has_override=None, id=None, is_unscored=None, links=None, name=None, policy=None, rules=None, scope=None, status=None, title=None, type=None):  # noqa: E501
        """PolicyItem - a model defined in Swagger"""  # noqa: E501

        self._assets = None
        self._description = None
        self._has_override = None
        self._id = None
        self._is_unscored = None
        self._links = None
        self._name = None
        self._policy = None
        self._rules = None
        self._scope = None
        self._status = None
        self._title = None
        self._type = None
        self.discriminator = None

        if assets is not None:
            self.assets = assets
        if description is not None:
            self.description = description
        if has_override is not None:
            self.has_override = has_override
        if id is not None:
            self.id = id
        if is_unscored is not None:
            self.is_unscored = is_unscored
        if links is not None:
            self.links = links
        if name is not None:
            self.name = name
        if policy is not None:
            self.policy = policy
        if rules is not None:
            self.rules = rules
        if scope is not None:
            self.scope = scope
        if status is not None:
            self.status = status
        if title is not None:
            self.title = title
        if type is not None:
            self.type = type

    @property
    def assets(self):
        """Gets the assets of this PolicyItem.  # noqa: E501

        A summary of asset compliance.  # noqa: E501

        :return: The assets of this PolicyItem.  # noqa: E501
        :rtype: AssetPolicyAssessment
        """
        return self._assets

    @assets.setter
    def assets(self, assets):
        """Sets the assets of this PolicyItem.

        A summary of asset compliance.  # noqa: E501

        :param assets: The assets of this PolicyItem.  # noqa: E501
        :type: AssetPolicyAssessment
        """

        self._assets = assets

    @property
    def description(self):
        """Gets the description of this PolicyItem.  # noqa: E501

        A description of the policy rule or group.  # noqa: E501

        :return: The description of this PolicyItem.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PolicyItem.

        A description of the policy rule or group.  # noqa: E501

        :param description: The description of this PolicyItem.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def has_override(self):
        """Gets the has_override of this PolicyItem.  # noqa: E501

        A flag indicating whether the policy rule has an active override applied to it. This field only applies to resources representing policy rules.   # noqa: E501

        :return: The has_override of this PolicyItem.  # noqa: E501
        :rtype: bool
        """
        return self._has_override

    @has_override.setter
    def has_override(self, has_override):
        """Sets the has_override of this PolicyItem.

        A flag indicating whether the policy rule has an active override applied to it. This field only applies to resources representing policy rules.   # noqa: E501

        :param has_override: The has_override of this PolicyItem.  # noqa: E501
        :type: bool
        """

        self._has_override = has_override

    @property
    def id(self):
        """Gets the id of this PolicyItem.  # noqa: E501

        The identifier of the policy rule or group.  # noqa: E501

        :return: The id of this PolicyItem.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PolicyItem.

        The identifier of the policy rule or group.  # noqa: E501

        :param id: The id of this PolicyItem.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def is_unscored(self):
        """Gets the is_unscored of this PolicyItem.  # noqa: E501

        A flag indicating whether the policy rule has a role of `\"unscored\"`. This field only applies to resources representing policy rules.  # noqa: E501

        :return: The is_unscored of this PolicyItem.  # noqa: E501
        :rtype: bool
        """
        return self._is_unscored

    @is_unscored.setter
    def is_unscored(self, is_unscored):
        """Sets the is_unscored of this PolicyItem.

        A flag indicating whether the policy rule has a role of `\"unscored\"`. This field only applies to resources representing policy rules.  # noqa: E501

        :param is_unscored: The is_unscored of this PolicyItem.  # noqa: E501
        :type: bool
        """

        self._is_unscored = is_unscored

    @property
    def links(self):
        """Gets the links of this PolicyItem.  # noqa: E501

        Hypermedia links to corresponding or related resources.  # noqa: E501

        :return: The links of this PolicyItem.  # noqa: E501
        :rtype: list[Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this PolicyItem.

        Hypermedia links to corresponding or related resources.  # noqa: E501

        :param links: The links of this PolicyItem.  # noqa: E501
        :type: list[Link]
        """

        self._links = links

    @property
    def name(self):
        """Gets the name of this PolicyItem.  # noqa: E501

        The name of the policy rule or group.  # noqa: E501

        :return: The name of this PolicyItem.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PolicyItem.

        The name of the policy rule or group.  # noqa: E501

        :param name: The name of this PolicyItem.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def policy(self):
        """Gets the policy of this PolicyItem.  # noqa: E501

        Information about the policy.  # noqa: E501

        :return: The policy of this PolicyItem.  # noqa: E501
        :rtype: PolicyMetadataResource
        """
        return self._policy

    @policy.setter
    def policy(self, policy):
        """Sets the policy of this PolicyItem.

        Information about the policy.  # noqa: E501

        :param policy: The policy of this PolicyItem.  # noqa: E501
        :type: PolicyMetadataResource
        """

        self._policy = policy

    @property
    def rules(self):
        """Gets the rules of this PolicyItem.  # noqa: E501

        A summary of rule compliance for multiple policy rules. This field only applies to resources representing policy groups.  # noqa: E501

        :return: The rules of this PolicyItem.  # noqa: E501
        :rtype: PolicyRuleAssessmentResource
        """
        return self._rules

    @rules.setter
    def rules(self, rules):
        """Sets the rules of this PolicyItem.

        A summary of rule compliance for multiple policy rules. This field only applies to resources representing policy groups.  # noqa: E501

        :param rules: The rules of this PolicyItem.  # noqa: E501
        :type: PolicyRuleAssessmentResource
        """

        self._rules = rules

    @property
    def scope(self):
        """Gets the scope of this PolicyItem.  # noqa: E501

        The textual representation of the policy rule/group scope. Policy rules or groups that are automatically available have `\"Built-in\"` scope, whereas policy rules or groups created by users have scope as `\"Custom\"`.  # noqa: E501

        :return: The scope of this PolicyItem.  # noqa: E501
        :rtype: str
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """Sets the scope of this PolicyItem.

        The textual representation of the policy rule/group scope. Policy rules or groups that are automatically available have `\"Built-in\"` scope, whereas policy rules or groups created by users have scope as `\"Custom\"`.  # noqa: E501

        :param scope: The scope of this PolicyItem.  # noqa: E501
        :type: str
        """

        self._scope = scope

    @property
    def status(self):
        """Gets the status of this PolicyItem.  # noqa: E501

        The overall compliance status of the policy rule or group.  # noqa: E501

        :return: The status of this PolicyItem.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this PolicyItem.

        The overall compliance status of the policy rule or group.  # noqa: E501

        :param status: The status of this PolicyItem.  # noqa: E501
        :type: str
        """
        allowed_values = ["PASS", "FAIL", "NOT_APPLICABLE"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def title(self):
        """Gets the title of this PolicyItem.  # noqa: E501

        The title of the policy rule, or group, as visible to the user.  # noqa: E501

        :return: The title of this PolicyItem.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this PolicyItem.

        The title of the policy rule, or group, as visible to the user.  # noqa: E501

        :param title: The title of this PolicyItem.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def type(self):
        """Gets the type of this PolicyItem.  # noqa: E501

        Indicates whether the resource represents either a policy rule or group.  # noqa: E501

        :return: The type of this PolicyItem.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this PolicyItem.

        Indicates whether the resource represents either a policy rule or group.  # noqa: E501

        :param type: The type of this PolicyItem.  # noqa: E501
        :type: str
        """
        allowed_values = ["rule", "group"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

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
        if issubclass(PolicyItem, dict):
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
        if not isinstance(other, PolicyItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
