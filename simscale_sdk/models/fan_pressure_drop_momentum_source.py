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


class FanPressureDropMomentumSource(object):
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
        'name': 'str',
        'fan_direction': 'DimensionalVectorDimensionless',
        'fan_pressure': 'DimensionalFunctionPressure',
        'geometry_primitive_uuids': 'list[str]'
    }

    attribute_map = {
        'type': 'type',
        'name': 'name',
        'fan_direction': 'fanDirection',
        'fan_pressure': 'fanPressure',
        'geometry_primitive_uuids': 'geometryPrimitiveUuids'
    }

    def __init__(self, type='FAN_PRESSURE_DROP', name=None, fan_direction=None, fan_pressure=None, geometry_primitive_uuids=None, local_vars_configuration=None):  # noqa: E501
        """FanPressureDropMomentumSource - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._name = None
        self._fan_direction = None
        self._fan_pressure = None
        self._geometry_primitive_uuids = None
        self.discriminator = None

        self.type = type
        if name is not None:
            self.name = name
        if fan_direction is not None:
            self.fan_direction = fan_direction
        if fan_pressure is not None:
            self.fan_pressure = fan_pressure
        if geometry_primitive_uuids is not None:
            self.geometry_primitive_uuids = geometry_primitive_uuids

    @property
    def type(self):
        """Gets the type of this FanPressureDropMomentumSource.  # noqa: E501

        Schema name: FanPressureDropMomentumSource  # noqa: E501

        :return: The type of this FanPressureDropMomentumSource.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this FanPressureDropMomentumSource.

        Schema name: FanPressureDropMomentumSource  # noqa: E501

        :param type: The type of this FanPressureDropMomentumSource.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def name(self):
        """Gets the name of this FanPressureDropMomentumSource.  # noqa: E501


        :return: The name of this FanPressureDropMomentumSource.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this FanPressureDropMomentumSource.


        :param name: The name of this FanPressureDropMomentumSource.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def fan_direction(self):
        """Gets the fan_direction of this FanPressureDropMomentumSource.  # noqa: E501


        :return: The fan_direction of this FanPressureDropMomentumSource.  # noqa: E501
        :rtype: DimensionalVectorDimensionless
        """
        return self._fan_direction

    @fan_direction.setter
    def fan_direction(self, fan_direction):
        """Sets the fan_direction of this FanPressureDropMomentumSource.


        :param fan_direction: The fan_direction of this FanPressureDropMomentumSource.  # noqa: E501
        :type: DimensionalVectorDimensionless
        """

        self._fan_direction = fan_direction

    @property
    def fan_pressure(self):
        """Gets the fan_pressure of this FanPressureDropMomentumSource.  # noqa: E501


        :return: The fan_pressure of this FanPressureDropMomentumSource.  # noqa: E501
        :rtype: DimensionalFunctionPressure
        """
        return self._fan_pressure

    @fan_pressure.setter
    def fan_pressure(self, fan_pressure):
        """Sets the fan_pressure of this FanPressureDropMomentumSource.


        :param fan_pressure: The fan_pressure of this FanPressureDropMomentumSource.  # noqa: E501
        :type: DimensionalFunctionPressure
        """

        self._fan_pressure = fan_pressure

    @property
    def geometry_primitive_uuids(self):
        """Gets the geometry_primitive_uuids of this FanPressureDropMomentumSource.  # noqa: E501


        :return: The geometry_primitive_uuids of this FanPressureDropMomentumSource.  # noqa: E501
        :rtype: list[str]
        """
        return self._geometry_primitive_uuids

    @geometry_primitive_uuids.setter
    def geometry_primitive_uuids(self, geometry_primitive_uuids):
        """Sets the geometry_primitive_uuids of this FanPressureDropMomentumSource.


        :param geometry_primitive_uuids: The geometry_primitive_uuids of this FanPressureDropMomentumSource.  # noqa: E501
        :type: list[str]
        """

        self._geometry_primitive_uuids = geometry_primitive_uuids

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
        if not isinstance(other, FanPressureDropMomentumSource):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FanPressureDropMomentumSource):
            return True

        return self.to_dict() != other.to_dict()
