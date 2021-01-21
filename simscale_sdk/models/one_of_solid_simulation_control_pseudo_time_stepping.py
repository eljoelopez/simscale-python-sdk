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


class OneOfSolidSimulationControlPseudoTimeStepping(object):
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
        'static_timesteps': 'DimensionalTime',
        'simulation_intervals': 'DimensionalTime',
        'timestep_length': 'RestrictedDimensionalFunctionTime'
    }

    attribute_map = {
        'type': 'type',
        'static_timesteps': 'staticTimesteps',
        'simulation_intervals': 'simulationIntervals',
        'timestep_length': 'timestepLength'
    }

    discriminator_value_class_map = {
        'SINGLE_STEP': 'SingleStepPseudoTimeStepping',
        'STEPPING_LIST_V18': 'SteppingListPseudoTimeStepping'
    }

    def __init__(self, type='STEPPING_LIST_V18', static_timesteps=None, simulation_intervals=None, timestep_length=None, local_vars_configuration=None):  # noqa: E501
        """OneOfSolidSimulationControlPseudoTimeStepping - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._static_timesteps = None
        self._simulation_intervals = None
        self._timestep_length = None
        self.discriminator = 'type'

        self.type = type
        if static_timesteps is not None:
            self.static_timesteps = static_timesteps
        if simulation_intervals is not None:
            self.simulation_intervals = simulation_intervals
        if timestep_length is not None:
            self.timestep_length = timestep_length

    @property
    def type(self):
        """Gets the type of this OneOfSolidSimulationControlPseudoTimeStepping.  # noqa: E501


        :return: The type of this OneOfSolidSimulationControlPseudoTimeStepping.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this OneOfSolidSimulationControlPseudoTimeStepping.


        :param type: The type of this OneOfSolidSimulationControlPseudoTimeStepping.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def static_timesteps(self):
        """Gets the static_timesteps of this OneOfSolidSimulationControlPseudoTimeStepping.  # noqa: E501


        :return: The static_timesteps of this OneOfSolidSimulationControlPseudoTimeStepping.  # noqa: E501
        :rtype: DimensionalTime
        """
        return self._static_timesteps

    @static_timesteps.setter
    def static_timesteps(self, static_timesteps):
        """Sets the static_timesteps of this OneOfSolidSimulationControlPseudoTimeStepping.


        :param static_timesteps: The static_timesteps of this OneOfSolidSimulationControlPseudoTimeStepping.  # noqa: E501
        :type: DimensionalTime
        """

        self._static_timesteps = static_timesteps

    @property
    def simulation_intervals(self):
        """Gets the simulation_intervals of this OneOfSolidSimulationControlPseudoTimeStepping.  # noqa: E501


        :return: The simulation_intervals of this OneOfSolidSimulationControlPseudoTimeStepping.  # noqa: E501
        :rtype: DimensionalTime
        """
        return self._simulation_intervals

    @simulation_intervals.setter
    def simulation_intervals(self, simulation_intervals):
        """Sets the simulation_intervals of this OneOfSolidSimulationControlPseudoTimeStepping.


        :param simulation_intervals: The simulation_intervals of this OneOfSolidSimulationControlPseudoTimeStepping.  # noqa: E501
        :type: DimensionalTime
        """

        self._simulation_intervals = simulation_intervals

    @property
    def timestep_length(self):
        """Gets the timestep_length of this OneOfSolidSimulationControlPseudoTimeStepping.  # noqa: E501


        :return: The timestep_length of this OneOfSolidSimulationControlPseudoTimeStepping.  # noqa: E501
        :rtype: RestrictedDimensionalFunctionTime
        """
        return self._timestep_length

    @timestep_length.setter
    def timestep_length(self, timestep_length):
        """Sets the timestep_length of this OneOfSolidSimulationControlPseudoTimeStepping.


        :param timestep_length: The timestep_length of this OneOfSolidSimulationControlPseudoTimeStepping.  # noqa: E501
        :type: RestrictedDimensionalFunctionTime
        """

        self._timestep_length = timestep_length

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
        if not isinstance(other, OneOfSolidSimulationControlPseudoTimeStepping):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OneOfSolidSimulationControlPseudoTimeStepping):
            return True

        return self.to_dict() != other.to_dict()