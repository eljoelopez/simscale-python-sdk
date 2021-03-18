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


class DerivedHeatFlux(object):
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
        'heat_transfer_coefficient': 'DimensionalThermalTransmittance',
        'ambient_temperature': 'DimensionalTemperature',
        'additional_heat_flux': 'DimensionalHeatFlux',
        'wall_thermal': 'OneOfDerivedHeatFluxWallThermal',
        'outer_surface_emissivity': 'float',
        'receives_external_solar_load': 'bool'
    }

    attribute_map = {
        'type': 'type',
        'heat_transfer_coefficient': 'heatTransferCoefficient',
        'ambient_temperature': 'ambientTemperature',
        'additional_heat_flux': 'additionalHeatFlux',
        'wall_thermal': 'wallThermal',
        'outer_surface_emissivity': 'outerSurfaceEmissivity',
        'receives_external_solar_load': 'receivesExternalSolarLoad'
    }

    def __init__(self, type='DERIVED', heat_transfer_coefficient=None, ambient_temperature=None, additional_heat_flux=None, wall_thermal=None, outer_surface_emissivity=None, receives_external_solar_load=None, local_vars_configuration=None):  # noqa: E501
        """DerivedHeatFlux - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._heat_transfer_coefficient = None
        self._ambient_temperature = None
        self._additional_heat_flux = None
        self._wall_thermal = None
        self._outer_surface_emissivity = None
        self._receives_external_solar_load = None
        self.discriminator = None

        self.type = type
        if heat_transfer_coefficient is not None:
            self.heat_transfer_coefficient = heat_transfer_coefficient
        if ambient_temperature is not None:
            self.ambient_temperature = ambient_temperature
        if additional_heat_flux is not None:
            self.additional_heat_flux = additional_heat_flux
        if wall_thermal is not None:
            self.wall_thermal = wall_thermal
        if outer_surface_emissivity is not None:
            self.outer_surface_emissivity = outer_surface_emissivity
        if receives_external_solar_load is not None:
            self.receives_external_solar_load = receives_external_solar_load

    @property
    def type(self):
        """Gets the type of this DerivedHeatFlux.  # noqa: E501


        :return: The type of this DerivedHeatFlux.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this DerivedHeatFlux.


        :param type: The type of this DerivedHeatFlux.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def heat_transfer_coefficient(self):
        """Gets the heat_transfer_coefficient of this DerivedHeatFlux.  # noqa: E501


        :return: The heat_transfer_coefficient of this DerivedHeatFlux.  # noqa: E501
        :rtype: DimensionalThermalTransmittance
        """
        return self._heat_transfer_coefficient

    @heat_transfer_coefficient.setter
    def heat_transfer_coefficient(self, heat_transfer_coefficient):
        """Sets the heat_transfer_coefficient of this DerivedHeatFlux.


        :param heat_transfer_coefficient: The heat_transfer_coefficient of this DerivedHeatFlux.  # noqa: E501
        :type: DimensionalThermalTransmittance
        """

        self._heat_transfer_coefficient = heat_transfer_coefficient

    @property
    def ambient_temperature(self):
        """Gets the ambient_temperature of this DerivedHeatFlux.  # noqa: E501


        :return: The ambient_temperature of this DerivedHeatFlux.  # noqa: E501
        :rtype: DimensionalTemperature
        """
        return self._ambient_temperature

    @ambient_temperature.setter
    def ambient_temperature(self, ambient_temperature):
        """Sets the ambient_temperature of this DerivedHeatFlux.


        :param ambient_temperature: The ambient_temperature of this DerivedHeatFlux.  # noqa: E501
        :type: DimensionalTemperature
        """

        self._ambient_temperature = ambient_temperature

    @property
    def additional_heat_flux(self):
        """Gets the additional_heat_flux of this DerivedHeatFlux.  # noqa: E501


        :return: The additional_heat_flux of this DerivedHeatFlux.  # noqa: E501
        :rtype: DimensionalHeatFlux
        """
        return self._additional_heat_flux

    @additional_heat_flux.setter
    def additional_heat_flux(self, additional_heat_flux):
        """Sets the additional_heat_flux of this DerivedHeatFlux.


        :param additional_heat_flux: The additional_heat_flux of this DerivedHeatFlux.  # noqa: E501
        :type: DimensionalHeatFlux
        """

        self._additional_heat_flux = additional_heat_flux

    @property
    def wall_thermal(self):
        """Gets the wall_thermal of this DerivedHeatFlux.  # noqa: E501


        :return: The wall_thermal of this DerivedHeatFlux.  # noqa: E501
        :rtype: OneOfDerivedHeatFluxWallThermal
        """
        return self._wall_thermal

    @wall_thermal.setter
    def wall_thermal(self, wall_thermal):
        """Sets the wall_thermal of this DerivedHeatFlux.


        :param wall_thermal: The wall_thermal of this DerivedHeatFlux.  # noqa: E501
        :type: OneOfDerivedHeatFluxWallThermal
        """

        self._wall_thermal = wall_thermal

    @property
    def outer_surface_emissivity(self):
        """Gets the outer_surface_emissivity of this DerivedHeatFlux.  # noqa: E501

        Emissivity of the outer side of the surface or the last wall thermal layer.  # noqa: E501

        :return: The outer_surface_emissivity of this DerivedHeatFlux.  # noqa: E501
        :rtype: float
        """
        return self._outer_surface_emissivity

    @outer_surface_emissivity.setter
    def outer_surface_emissivity(self, outer_surface_emissivity):
        """Sets the outer_surface_emissivity of this DerivedHeatFlux.

        Emissivity of the outer side of the surface or the last wall thermal layer.  # noqa: E501

        :param outer_surface_emissivity: The outer_surface_emissivity of this DerivedHeatFlux.  # noqa: E501
        :type: float
        """
        if (self.local_vars_configuration.client_side_validation and
                outer_surface_emissivity is not None and outer_surface_emissivity > 1):  # noqa: E501
            raise ValueError("Invalid value for `outer_surface_emissivity`, must be a value less than or equal to `1`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                outer_surface_emissivity is not None and outer_surface_emissivity < 0):  # noqa: E501
            raise ValueError("Invalid value for `outer_surface_emissivity`, must be a value greater than or equal to `0`")  # noqa: E501

        self._outer_surface_emissivity = outer_surface_emissivity

    @property
    def receives_external_solar_load(self):
        """Gets the receives_external_solar_load of this DerivedHeatFlux.  # noqa: E501


        :return: The receives_external_solar_load of this DerivedHeatFlux.  # noqa: E501
        :rtype: bool
        """
        return self._receives_external_solar_load

    @receives_external_solar_load.setter
    def receives_external_solar_load(self, receives_external_solar_load):
        """Sets the receives_external_solar_load of this DerivedHeatFlux.


        :param receives_external_solar_load: The receives_external_solar_load of this DerivedHeatFlux.  # noqa: E501
        :type: bool
        """

        self._receives_external_solar_load = receives_external_solar_load

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
        if not isinstance(other, DerivedHeatFlux):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DerivedHeatFlux):
            return True

        return self.to_dict() != other.to_dict()
