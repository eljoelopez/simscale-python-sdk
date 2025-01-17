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


class Part(object):
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
        'part_identifier': 'str',
        'opacity': 'float',
        'render_mode': 'RenderMode',
        'solid_color': 'Color'
    }

    attribute_map = {
        'part_identifier': 'partIdentifier',
        'opacity': 'opacity',
        'render_mode': 'renderMode',
        'solid_color': 'solidColor'
    }

    def __init__(self, part_identifier=None, opacity=None, render_mode=None, solid_color=None, local_vars_configuration=None):  # noqa: E501
        """Part - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._part_identifier = None
        self._opacity = None
        self._render_mode = None
        self._solid_color = None
        self.discriminator = None

        self.part_identifier = part_identifier
        if opacity is not None:
            self.opacity = opacity
        if render_mode is not None:
            self.render_mode = render_mode
        if solid_color is not None:
            self.solid_color = solid_color

    @property
    def part_identifier(self):
        """Gets the part_identifier of this Part.  # noqa: E501

        The identifier of the part in the result.  # noqa: E501

        :return: The part_identifier of this Part.  # noqa: E501
        :rtype: str
        """
        return self._part_identifier

    @part_identifier.setter
    def part_identifier(self, part_identifier):
        """Sets the part_identifier of this Part.

        The identifier of the part in the result.  # noqa: E501

        :param part_identifier: The part_identifier of this Part.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and part_identifier is None:  # noqa: E501
            raise ValueError("Invalid value for `part_identifier`, must not be `None`")  # noqa: E501

        self._part_identifier = part_identifier

    @property
    def opacity(self):
        """Gets the opacity of this Part.  # noqa: E501


        :return: The opacity of this Part.  # noqa: E501
        :rtype: float
        """
        return self._opacity

    @opacity.setter
    def opacity(self, opacity):
        """Sets the opacity of this Part.


        :param opacity: The opacity of this Part.  # noqa: E501
        :type: float
        """
        if (self.local_vars_configuration.client_side_validation and
                opacity is not None and opacity > 1.0):  # noqa: E501
            raise ValueError("Invalid value for `opacity`, must be a value less than or equal to `1.0`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                opacity is not None and opacity < 0.0):  # noqa: E501
            raise ValueError("Invalid value for `opacity`, must be a value greater than or equal to `0.0`")  # noqa: E501

        self._opacity = opacity

    @property
    def render_mode(self):
        """Gets the render_mode of this Part.  # noqa: E501


        :return: The render_mode of this Part.  # noqa: E501
        :rtype: RenderMode
        """
        return self._render_mode

    @render_mode.setter
    def render_mode(self, render_mode):
        """Sets the render_mode of this Part.


        :param render_mode: The render_mode of this Part.  # noqa: E501
        :type: RenderMode
        """

        self._render_mode = render_mode

    @property
    def solid_color(self):
        """Gets the solid_color of this Part.  # noqa: E501


        :return: The solid_color of this Part.  # noqa: E501
        :rtype: Color
        """
        return self._solid_color

    @solid_color.setter
    def solid_color(self, solid_color):
        """Sets the solid_color of this Part.


        :param solid_color: The solid_color of this Part.  # noqa: E501
        :type: Color
        """

        self._solid_color = solid_color

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
        if not isinstance(other, Part):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Part):
            return True

        return self.to_dict() != other.to_dict()
