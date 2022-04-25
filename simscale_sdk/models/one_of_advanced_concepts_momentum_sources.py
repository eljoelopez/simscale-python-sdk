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


class OneOfAdvancedConceptsMomentumSources(object):
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
        'average_velocity': 'DimensionalVectorSpeed',
        'topological_reference': 'TopologicalReference',
        'geometry_primitive_uuids': 'list[str]',
        'fan_direction': 'DimensionalVectorDimensionless',
        'fan_pressure': 'DimensionalFunctionPressure'
    }

    attribute_map = {
        'type': 'type',
        'name': 'name',
        'average_velocity': 'averageVelocity',
        'topological_reference': 'topologicalReference',
        'geometry_primitive_uuids': 'geometryPrimitiveUuids',
        'fan_direction': 'fanDirection',
        'fan_pressure': 'fanPressure'
    }

    discriminator_value_class_map = {
        'AVERAGE_VELOCITY': 'AverageVelocityMomentumSource',
        'FAN_PRESSURE_DROP': 'FanPressureDropMomentumSource'
    }

    def __init__(self, type='FAN_PRESSURE_DROP', name=None, average_velocity=None, topological_reference=None, geometry_primitive_uuids=None, fan_direction=None, fan_pressure=None, local_vars_configuration=None):  # noqa: E501
        """OneOfAdvancedConceptsMomentumSources - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._name = None
        self._average_velocity = None
        self._topological_reference = None
        self._geometry_primitive_uuids = None
        self._fan_direction = None
        self._fan_pressure = None
        self.discriminator = 'type'

        self.type = type
        if name is not None:
            self.name = name
        if average_velocity is not None:
            self.average_velocity = average_velocity
        if topological_reference is not None:
            self.topological_reference = topological_reference
        if geometry_primitive_uuids is not None:
            self.geometry_primitive_uuids = geometry_primitive_uuids
        if fan_direction is not None:
            self.fan_direction = fan_direction
        if fan_pressure is not None:
            self.fan_pressure = fan_pressure

    @property
    def type(self):
        """Gets the type of this OneOfAdvancedConceptsMomentumSources.  # noqa: E501

        Schema name: FanPressureDropMomentumSource  # noqa: E501

        :return: The type of this OneOfAdvancedConceptsMomentumSources.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this OneOfAdvancedConceptsMomentumSources.

        Schema name: FanPressureDropMomentumSource  # noqa: E501

        :param type: The type of this OneOfAdvancedConceptsMomentumSources.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def name(self):
        """Gets the name of this OneOfAdvancedConceptsMomentumSources.  # noqa: E501


        :return: The name of this OneOfAdvancedConceptsMomentumSources.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this OneOfAdvancedConceptsMomentumSources.


        :param name: The name of this OneOfAdvancedConceptsMomentumSources.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def average_velocity(self):
        """Gets the average_velocity of this OneOfAdvancedConceptsMomentumSources.  # noqa: E501


        :return: The average_velocity of this OneOfAdvancedConceptsMomentumSources.  # noqa: E501
        :rtype: DimensionalVectorSpeed
        """
        return self._average_velocity

    @average_velocity.setter
    def average_velocity(self, average_velocity):
        """Sets the average_velocity of this OneOfAdvancedConceptsMomentumSources.


        :param average_velocity: The average_velocity of this OneOfAdvancedConceptsMomentumSources.  # noqa: E501
        :type: DimensionalVectorSpeed
        """

        self._average_velocity = average_velocity

    @property
    def topological_reference(self):
        """Gets the topological_reference of this OneOfAdvancedConceptsMomentumSources.  # noqa: E501


        :return: The topological_reference of this OneOfAdvancedConceptsMomentumSources.  # noqa: E501
        :rtype: TopologicalReference
        """
        return self._topological_reference

    @topological_reference.setter
    def topological_reference(self, topological_reference):
        """Sets the topological_reference of this OneOfAdvancedConceptsMomentumSources.


        :param topological_reference: The topological_reference of this OneOfAdvancedConceptsMomentumSources.  # noqa: E501
        :type: TopologicalReference
        """

        self._topological_reference = topological_reference

    @property
    def geometry_primitive_uuids(self):
        """Gets the geometry_primitive_uuids of this OneOfAdvancedConceptsMomentumSources.  # noqa: E501


        :return: The geometry_primitive_uuids of this OneOfAdvancedConceptsMomentumSources.  # noqa: E501
        :rtype: list[str]
        """
        return self._geometry_primitive_uuids

    @geometry_primitive_uuids.setter
    def geometry_primitive_uuids(self, geometry_primitive_uuids):
        """Sets the geometry_primitive_uuids of this OneOfAdvancedConceptsMomentumSources.


        :param geometry_primitive_uuids: The geometry_primitive_uuids of this OneOfAdvancedConceptsMomentumSources.  # noqa: E501
        :type: list[str]
        """

        self._geometry_primitive_uuids = geometry_primitive_uuids

    @property
    def fan_direction(self):
        """Gets the fan_direction of this OneOfAdvancedConceptsMomentumSources.  # noqa: E501


        :return: The fan_direction of this OneOfAdvancedConceptsMomentumSources.  # noqa: E501
        :rtype: DimensionalVectorDimensionless
        """
        return self._fan_direction

    @fan_direction.setter
    def fan_direction(self, fan_direction):
        """Sets the fan_direction of this OneOfAdvancedConceptsMomentumSources.


        :param fan_direction: The fan_direction of this OneOfAdvancedConceptsMomentumSources.  # noqa: E501
        :type: DimensionalVectorDimensionless
        """

        self._fan_direction = fan_direction

    @property
    def fan_pressure(self):
        """Gets the fan_pressure of this OneOfAdvancedConceptsMomentumSources.  # noqa: E501


        :return: The fan_pressure of this OneOfAdvancedConceptsMomentumSources.  # noqa: E501
        :rtype: DimensionalFunctionPressure
        """
        return self._fan_pressure

    @fan_pressure.setter
    def fan_pressure(self, fan_pressure):
        """Sets the fan_pressure of this OneOfAdvancedConceptsMomentumSources.


        :param fan_pressure: The fan_pressure of this OneOfAdvancedConceptsMomentumSources.  # noqa: E501
        :type: DimensionalFunctionPressure
        """

        self._fan_pressure = fan_pressure

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
        if not isinstance(other, OneOfAdvancedConceptsMomentumSources):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OneOfAdvancedConceptsMomentumSources):
            return True

        return self.to_dict() != other.to_dict()
