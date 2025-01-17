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


class SolidCoil(object):
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
        'net_current': 'DimensionalElectricCurrent',
        'entry_port': 'TopologicalReference',
        'exit_port': 'TopologicalReference'
    }

    attribute_map = {
        'type': 'type',
        'net_current': 'netCurrent',
        'entry_port': 'entryPort',
        'exit_port': 'exitPort'
    }

    def __init__(self, type='SOLID_COIL', net_current=None, entry_port=None, exit_port=None, local_vars_configuration=None):  # noqa: E501
        """SolidCoil - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._net_current = None
        self._entry_port = None
        self._exit_port = None
        self.discriminator = None

        self.type = type
        if net_current is not None:
            self.net_current = net_current
        if entry_port is not None:
            self.entry_port = entry_port
        if exit_port is not None:
            self.exit_port = exit_port

    @property
    def type(self):
        """Gets the type of this SolidCoil.  # noqa: E501

        Schema name: SolidCoil  # noqa: E501

        :return: The type of this SolidCoil.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this SolidCoil.

        Schema name: SolidCoil  # noqa: E501

        :param type: The type of this SolidCoil.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def net_current(self):
        """Gets the net_current of this SolidCoil.  # noqa: E501


        :return: The net_current of this SolidCoil.  # noqa: E501
        :rtype: DimensionalElectricCurrent
        """
        return self._net_current

    @net_current.setter
    def net_current(self, net_current):
        """Sets the net_current of this SolidCoil.


        :param net_current: The net_current of this SolidCoil.  # noqa: E501
        :type: DimensionalElectricCurrent
        """

        self._net_current = net_current

    @property
    def entry_port(self):
        """Gets the entry_port of this SolidCoil.  # noqa: E501


        :return: The entry_port of this SolidCoil.  # noqa: E501
        :rtype: TopologicalReference
        """
        return self._entry_port

    @entry_port.setter
    def entry_port(self, entry_port):
        """Sets the entry_port of this SolidCoil.


        :param entry_port: The entry_port of this SolidCoil.  # noqa: E501
        :type: TopologicalReference
        """

        self._entry_port = entry_port

    @property
    def exit_port(self):
        """Gets the exit_port of this SolidCoil.  # noqa: E501


        :return: The exit_port of this SolidCoil.  # noqa: E501
        :rtype: TopologicalReference
        """
        return self._exit_port

    @exit_port.setter
    def exit_port(self, exit_port):
        """Sets the exit_port of this SolidCoil.


        :param exit_port: The exit_port of this SolidCoil.  # noqa: E501
        :type: TopologicalReference
        """

        self._exit_port = exit_port

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
        if not isinstance(other, SolidCoil):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SolidCoil):
            return True

        return self.to_dict() != other.to_dict()
