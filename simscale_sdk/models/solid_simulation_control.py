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


class SolidSimulationControl(object):
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
        'auto_load_ramping': 'bool',
        'timestep_definition': 'OneOfSolidSimulationControlTimestepDefinition',
        'pseudo_time_stepping': 'OneOfSolidSimulationControlPseudoTimeStepping',
        'write_control_definition': 'OneOfSolidSimulationControlWriteControlDefinition',
        'excitation_frequencies': 'OneOfSolidSimulationControlExcitationFrequencies',
        'eigenfrequency_scope': 'OneOfSolidSimulationControlEigenfrequencyScope',
        'processors': 'ComputingCore',
        'max_run_time': 'DimensionalTime'
    }

    attribute_map = {
        'auto_load_ramping': 'autoLoadRamping',
        'timestep_definition': 'timestepDefinition',
        'pseudo_time_stepping': 'pseudoTimeStepping',
        'write_control_definition': 'writeControlDefinition',
        'excitation_frequencies': 'excitationFrequencies',
        'eigenfrequency_scope': 'eigenfrequencyScope',
        'processors': 'processors',
        'max_run_time': 'maxRunTime'
    }

    def __init__(self, auto_load_ramping=None, timestep_definition=None, pseudo_time_stepping=None, write_control_definition=None, excitation_frequencies=None, eigenfrequency_scope=None, processors=None, max_run_time=None, local_vars_configuration=None):  # noqa: E501
        """SolidSimulationControl - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._auto_load_ramping = None
        self._timestep_definition = None
        self._pseudo_time_stepping = None
        self._write_control_definition = None
        self._excitation_frequencies = None
        self._eigenfrequency_scope = None
        self._processors = None
        self._max_run_time = None
        self.discriminator = None

        if auto_load_ramping is not None:
            self.auto_load_ramping = auto_load_ramping
        if timestep_definition is not None:
            self.timestep_definition = timestep_definition
        if pseudo_time_stepping is not None:
            self.pseudo_time_stepping = pseudo_time_stepping
        if write_control_definition is not None:
            self.write_control_definition = write_control_definition
        if excitation_frequencies is not None:
            self.excitation_frequencies = excitation_frequencies
        if eigenfrequency_scope is not None:
            self.eigenfrequency_scope = eigenfrequency_scope
        if processors is not None:
            self.processors = processors
        if max_run_time is not None:
            self.max_run_time = max_run_time

    @property
    def auto_load_ramping(self):
        """Gets the auto_load_ramping of this SolidSimulationControl.  # noqa: E501

        Loads will be ramped linearly over the simulation interval to aid solution convergence. Automatic load ramping will only be applied if all boundary conditions (including gravity) are applied with constant values.  # noqa: E501

        :return: The auto_load_ramping of this SolidSimulationControl.  # noqa: E501
        :rtype: bool
        """
        return self._auto_load_ramping

    @auto_load_ramping.setter
    def auto_load_ramping(self, auto_load_ramping):
        """Sets the auto_load_ramping of this SolidSimulationControl.

        Loads will be ramped linearly over the simulation interval to aid solution convergence. Automatic load ramping will only be applied if all boundary conditions (including gravity) are applied with constant values.  # noqa: E501

        :param auto_load_ramping: The auto_load_ramping of this SolidSimulationControl.  # noqa: E501
        :type: bool
        """

        self._auto_load_ramping = auto_load_ramping

    @property
    def timestep_definition(self):
        """Gets the timestep_definition of this SolidSimulationControl.  # noqa: E501


        :return: The timestep_definition of this SolidSimulationControl.  # noqa: E501
        :rtype: OneOfSolidSimulationControlTimestepDefinition
        """
        return self._timestep_definition

    @timestep_definition.setter
    def timestep_definition(self, timestep_definition):
        """Sets the timestep_definition of this SolidSimulationControl.


        :param timestep_definition: The timestep_definition of this SolidSimulationControl.  # noqa: E501
        :type: OneOfSolidSimulationControlTimestepDefinition
        """

        self._timestep_definition = timestep_definition

    @property
    def pseudo_time_stepping(self):
        """Gets the pseudo_time_stepping of this SolidSimulationControl.  # noqa: E501


        :return: The pseudo_time_stepping of this SolidSimulationControl.  # noqa: E501
        :rtype: OneOfSolidSimulationControlPseudoTimeStepping
        """
        return self._pseudo_time_stepping

    @pseudo_time_stepping.setter
    def pseudo_time_stepping(self, pseudo_time_stepping):
        """Sets the pseudo_time_stepping of this SolidSimulationControl.


        :param pseudo_time_stepping: The pseudo_time_stepping of this SolidSimulationControl.  # noqa: E501
        :type: OneOfSolidSimulationControlPseudoTimeStepping
        """

        self._pseudo_time_stepping = pseudo_time_stepping

    @property
    def write_control_definition(self):
        """Gets the write_control_definition of this SolidSimulationControl.  # noqa: E501


        :return: The write_control_definition of this SolidSimulationControl.  # noqa: E501
        :rtype: OneOfSolidSimulationControlWriteControlDefinition
        """
        return self._write_control_definition

    @write_control_definition.setter
    def write_control_definition(self, write_control_definition):
        """Sets the write_control_definition of this SolidSimulationControl.


        :param write_control_definition: The write_control_definition of this SolidSimulationControl.  # noqa: E501
        :type: OneOfSolidSimulationControlWriteControlDefinition
        """

        self._write_control_definition = write_control_definition

    @property
    def excitation_frequencies(self):
        """Gets the excitation_frequencies of this SolidSimulationControl.  # noqa: E501


        :return: The excitation_frequencies of this SolidSimulationControl.  # noqa: E501
        :rtype: OneOfSolidSimulationControlExcitationFrequencies
        """
        return self._excitation_frequencies

    @excitation_frequencies.setter
    def excitation_frequencies(self, excitation_frequencies):
        """Sets the excitation_frequencies of this SolidSimulationControl.


        :param excitation_frequencies: The excitation_frequencies of this SolidSimulationControl.  # noqa: E501
        :type: OneOfSolidSimulationControlExcitationFrequencies
        """

        self._excitation_frequencies = excitation_frequencies

    @property
    def eigenfrequency_scope(self):
        """Gets the eigenfrequency_scope of this SolidSimulationControl.  # noqa: E501


        :return: The eigenfrequency_scope of this SolidSimulationControl.  # noqa: E501
        :rtype: OneOfSolidSimulationControlEigenfrequencyScope
        """
        return self._eigenfrequency_scope

    @eigenfrequency_scope.setter
    def eigenfrequency_scope(self, eigenfrequency_scope):
        """Sets the eigenfrequency_scope of this SolidSimulationControl.


        :param eigenfrequency_scope: The eigenfrequency_scope of this SolidSimulationControl.  # noqa: E501
        :type: OneOfSolidSimulationControlEigenfrequencyScope
        """

        self._eigenfrequency_scope = eigenfrequency_scope

    @property
    def processors(self):
        """Gets the processors of this SolidSimulationControl.  # noqa: E501


        :return: The processors of this SolidSimulationControl.  # noqa: E501
        :rtype: ComputingCore
        """
        return self._processors

    @processors.setter
    def processors(self, processors):
        """Sets the processors of this SolidSimulationControl.


        :param processors: The processors of this SolidSimulationControl.  # noqa: E501
        :type: ComputingCore
        """

        self._processors = processors

    @property
    def max_run_time(self):
        """Gets the max_run_time of this SolidSimulationControl.  # noqa: E501


        :return: The max_run_time of this SolidSimulationControl.  # noqa: E501
        :rtype: DimensionalTime
        """
        return self._max_run_time

    @max_run_time.setter
    def max_run_time(self, max_run_time):
        """Sets the max_run_time of this SolidSimulationControl.


        :param max_run_time: The max_run_time of this SolidSimulationControl.  # noqa: E501
        :type: DimensionalTime
        """

        self._max_run_time = max_run_time

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
        if not isinstance(other, SolidSimulationControl):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SolidSimulationControl):
            return True

        return self.to_dict() != other.to_dict()
