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


class StatisticalAveragingResultControlV2(object):
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
        'fraction_from_end': 'float',
        'sampling_interval': 'OneOfStatisticalAveragingResultControlV2SamplingInterval',
        'export_fluid': 'bool',
        'export_surface': 'bool',
        'geometry_primitive_uuids': 'list[str]'
    }

    attribute_map = {
        'type': 'type',
        'fraction_from_end': 'fractionFromEnd',
        'sampling_interval': 'samplingInterval',
        'export_fluid': 'exportFluid',
        'export_surface': 'exportSurface',
        'geometry_primitive_uuids': 'geometryPrimitiveUuids'
    }

    def __init__(self, type='STATISTICAL_AVERAGING_V2', fraction_from_end=None, sampling_interval=None, export_fluid=True, export_surface=False, geometry_primitive_uuids=None, local_vars_configuration=None):  # noqa: E501
        """StatisticalAveragingResultControlV2 - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._fraction_from_end = None
        self._sampling_interval = None
        self._export_fluid = None
        self._export_surface = None
        self._geometry_primitive_uuids = None
        self.discriminator = None

        self.type = type
        if fraction_from_end is not None:
            self.fraction_from_end = fraction_from_end
        if sampling_interval is not None:
            self.sampling_interval = sampling_interval
        self.export_fluid = export_fluid
        self.export_surface = export_surface
        if geometry_primitive_uuids is not None:
            self.geometry_primitive_uuids = geometry_primitive_uuids

    @property
    def type(self):
        """Gets the type of this StatisticalAveragingResultControlV2.  # noqa: E501


        :return: The type of this StatisticalAveragingResultControlV2.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this StatisticalAveragingResultControlV2.


        :param type: The type of this StatisticalAveragingResultControlV2.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def fraction_from_end(self):
        """Gets the fraction_from_end of this StatisticalAveragingResultControlV2.  # noqa: E501

        It defines the point in simulation where the result output data extraction starts. For instance, <i>Fraction from end</i> of 1 (100%) extracts all data from the beginning of the simulation while default 0.2 extracts 20% data from the end of the simulation.  # noqa: E501

        :return: The fraction_from_end of this StatisticalAveragingResultControlV2.  # noqa: E501
        :rtype: float
        """
        return self._fraction_from_end

    @fraction_from_end.setter
    def fraction_from_end(self, fraction_from_end):
        """Sets the fraction_from_end of this StatisticalAveragingResultControlV2.

        It defines the point in simulation where the result output data extraction starts. For instance, <i>Fraction from end</i> of 1 (100%) extracts all data from the beginning of the simulation while default 0.2 extracts 20% data from the end of the simulation.  # noqa: E501

        :param fraction_from_end: The fraction_from_end of this StatisticalAveragingResultControlV2.  # noqa: E501
        :type: float
        """
        if (self.local_vars_configuration.client_side_validation and
                fraction_from_end is not None and fraction_from_end > 1):  # noqa: E501
            raise ValueError("Invalid value for `fraction_from_end`, must be a value less than or equal to `1`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                fraction_from_end is not None and fraction_from_end < 0):  # noqa: E501
            raise ValueError("Invalid value for `fraction_from_end`, must be a value greater than or equal to `0`")  # noqa: E501

        self._fraction_from_end = fraction_from_end

    @property
    def sampling_interval(self):
        """Gets the sampling_interval of this StatisticalAveragingResultControlV2.  # noqa: E501


        :return: The sampling_interval of this StatisticalAveragingResultControlV2.  # noqa: E501
        :rtype: OneOfStatisticalAveragingResultControlV2SamplingInterval
        """
        return self._sampling_interval

    @sampling_interval.setter
    def sampling_interval(self, sampling_interval):
        """Sets the sampling_interval of this StatisticalAveragingResultControlV2.


        :param sampling_interval: The sampling_interval of this StatisticalAveragingResultControlV2.  # noqa: E501
        :type: OneOfStatisticalAveragingResultControlV2SamplingInterval
        """

        self._sampling_interval = sampling_interval

    @property
    def export_fluid(self):
        """Gets the export_fluid of this StatisticalAveragingResultControlV2.  # noqa: E501

        When this switch is activated, simulation data of the flow-field enclosed in the assignments will be exported  # noqa: E501

        :return: The export_fluid of this StatisticalAveragingResultControlV2.  # noqa: E501
        :rtype: bool
        """
        return self._export_fluid

    @export_fluid.setter
    def export_fluid(self, export_fluid):
        """Sets the export_fluid of this StatisticalAveragingResultControlV2.

        When this switch is activated, simulation data of the flow-field enclosed in the assignments will be exported  # noqa: E501

        :param export_fluid: The export_fluid of this StatisticalAveragingResultControlV2.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and export_fluid is None:  # noqa: E501
            raise ValueError("Invalid value for `export_fluid`, must not be `None`")  # noqa: E501

        self._export_fluid = export_fluid

    @property
    def export_surface(self):
        """Gets the export_surface of this StatisticalAveragingResultControlV2.  # noqa: E501

        When this switch is activated, simulation data on all surfaces enclosed in the assignments will be exported  # noqa: E501

        :return: The export_surface of this StatisticalAveragingResultControlV2.  # noqa: E501
        :rtype: bool
        """
        return self._export_surface

    @export_surface.setter
    def export_surface(self, export_surface):
        """Sets the export_surface of this StatisticalAveragingResultControlV2.

        When this switch is activated, simulation data on all surfaces enclosed in the assignments will be exported  # noqa: E501

        :param export_surface: The export_surface of this StatisticalAveragingResultControlV2.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and export_surface is None:  # noqa: E501
            raise ValueError("Invalid value for `export_surface`, must not be `None`")  # noqa: E501

        self._export_surface = export_surface

    @property
    def geometry_primitive_uuids(self):
        """Gets the geometry_primitive_uuids of this StatisticalAveragingResultControlV2.  # noqa: E501


        :return: The geometry_primitive_uuids of this StatisticalAveragingResultControlV2.  # noqa: E501
        :rtype: list[str]
        """
        return self._geometry_primitive_uuids

    @geometry_primitive_uuids.setter
    def geometry_primitive_uuids(self, geometry_primitive_uuids):
        """Sets the geometry_primitive_uuids of this StatisticalAveragingResultControlV2.


        :param geometry_primitive_uuids: The geometry_primitive_uuids of this StatisticalAveragingResultControlV2.  # noqa: E501
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
        if not isinstance(other, StatisticalAveragingResultControlV2):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, StatisticalAveragingResultControlV2):
            return True

        return self.to_dict() != other.to_dict()