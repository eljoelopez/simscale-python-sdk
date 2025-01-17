# coding: utf-8

"""
    SimScale API

    The version of the OpenAPI document: 0.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from simscale_sdk.configuration import Configuration


class OneOfStaticAnalysisConnectionGroups(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'type': 'str',
        'connections': 'list[OneOfPhysicalContactConnections]',
        'node_merging_bonded': 'bool',
        'settings': 'ConnectionSettingsV36'
    }

    attribute_map = {
        'type': 'type',
        'connections': 'connections',
        'node_merging_bonded': 'nodeMergingBonded',
        'settings': 'settings'
    }

    discriminator_value_class_map = {
        'CONTACT': 'Contact',
        'PHYSICAL_CONTACT_V36': 'PhysicalContact'
    }

    def __init__(self, type='PHYSICAL_CONTACT_V36', connections=None, node_merging_bonded=None, settings=None, local_vars_configuration=None):  # noqa: E501
        """OneOfStaticAnalysisConnectionGroups - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._connections = None
        self._node_merging_bonded = None
        self._settings = None
        self.discriminator = 'type'

        self.type = type
        if connections is not None:
            self.connections = connections
        if node_merging_bonded is not None:
            self.node_merging_bonded = node_merging_bonded
        if settings is not None:
            self.settings = settings

    @property
    def type(self):
        """Gets the type of this OneOfStaticAnalysisConnectionGroups.  # noqa: E501

        Schema name: PhysicalContact  # noqa: E501

        :return: The type of this OneOfStaticAnalysisConnectionGroups.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this OneOfStaticAnalysisConnectionGroups.

        Schema name: PhysicalContact  # noqa: E501

        :param type: The type of this OneOfStaticAnalysisConnectionGroups.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def connections(self):
        """Gets the connections of this OneOfStaticAnalysisConnectionGroups.  # noqa: E501


        :return: The connections of this OneOfStaticAnalysisConnectionGroups.  # noqa: E501
        :rtype: list[OneOfPhysicalContactConnections]
        """
        return self._connections

    @connections.setter
    def connections(self, connections):
        """Sets the connections of this OneOfStaticAnalysisConnectionGroups.


        :param connections: The connections of this OneOfStaticAnalysisConnectionGroups.  # noqa: E501
        :type: list[OneOfPhysicalContactConnections]
        """

        self._connections = connections

    @property
    def node_merging_bonded(self):
        """Gets the node_merging_bonded of this OneOfStaticAnalysisConnectionGroups.  # noqa: E501

        <p>Allow node merging where possible to increase contact accuracy and solution efficiency. For contact pairs where nodes cannot be merged, linear relations will be used with the defined position tolerance.</p>  # noqa: E501

        :return: The node_merging_bonded of this OneOfStaticAnalysisConnectionGroups.  # noqa: E501
        :rtype: bool
        """
        return self._node_merging_bonded

    @node_merging_bonded.setter
    def node_merging_bonded(self, node_merging_bonded):
        """Sets the node_merging_bonded of this OneOfStaticAnalysisConnectionGroups.

        <p>Allow node merging where possible to increase contact accuracy and solution efficiency. For contact pairs where nodes cannot be merged, linear relations will be used with the defined position tolerance.</p>  # noqa: E501

        :param node_merging_bonded: The node_merging_bonded of this OneOfStaticAnalysisConnectionGroups.  # noqa: E501
        :type: bool
        """

        self._node_merging_bonded = node_merging_bonded

    @property
    def settings(self):
        """Gets the settings of this OneOfStaticAnalysisConnectionGroups.  # noqa: E501


        :return: The settings of this OneOfStaticAnalysisConnectionGroups.  # noqa: E501
        :rtype: ConnectionSettingsV36
        """
        return self._settings

    @settings.setter
    def settings(self, settings):
        """Sets the settings of this OneOfStaticAnalysisConnectionGroups.


        :param settings: The settings of this OneOfStaticAnalysisConnectionGroups.  # noqa: E501
        :type: ConnectionSettingsV36
        """

        self._settings = settings

    def get_real_child_model(self, data):
        """Returns the real base class specified by the discriminator"""
        discriminator_key = self.attribute_map[self.discriminator]
        discriminator_value = data[discriminator_key]
        return self.discriminator_value_class_map.get(discriminator_value)

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, OneOfStaticAnalysisConnectionGroups):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OneOfStaticAnalysisConnectionGroups):
            return True

        return self.to_dict() != other.to_dict()
