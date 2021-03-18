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


class SimulationSpec(object):
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
        'simulation_id': 'str',
        'name': 'str',
        'version': 'str',
        'created_at': 'datetime',
        'modified_at': 'datetime',
        'geometry_id': 'str',
        'mesh_id': 'str',
        'model': 'Analysis'
    }

    attribute_map = {
        'simulation_id': 'simulationId',
        'name': 'name',
        'version': 'version',
        'created_at': 'createdAt',
        'modified_at': 'modifiedAt',
        'geometry_id': 'geometryId',
        'mesh_id': 'meshId',
        'model': 'model'
    }

    def __init__(self, simulation_id=None, name=None, version='0.8', created_at=None, modified_at=None, geometry_id=None, mesh_id=None, model=None, local_vars_configuration=None):  # noqa: E501
        """SimulationSpec - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._simulation_id = None
        self._name = None
        self._version = None
        self._created_at = None
        self._modified_at = None
        self._geometry_id = None
        self._mesh_id = None
        self._model = None
        self.discriminator = None

        if simulation_id is not None:
            self.simulation_id = simulation_id
        self.name = name
        self.version = version
        if created_at is not None:
            self.created_at = created_at
        if modified_at is not None:
            self.modified_at = modified_at
        self.geometry_id = geometry_id
        if mesh_id is not None:
            self.mesh_id = mesh_id
        self.model = model

    @property
    def simulation_id(self):
        """Gets the simulation_id of this SimulationSpec.  # noqa: E501


        :return: The simulation_id of this SimulationSpec.  # noqa: E501
        :rtype: str
        """
        return self._simulation_id

    @simulation_id.setter
    def simulation_id(self, simulation_id):
        """Sets the simulation_id of this SimulationSpec.


        :param simulation_id: The simulation_id of this SimulationSpec.  # noqa: E501
        :type: str
        """

        self._simulation_id = simulation_id

    @property
    def name(self):
        """Gets the name of this SimulationSpec.  # noqa: E501


        :return: The name of this SimulationSpec.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SimulationSpec.


        :param name: The name of this SimulationSpec.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def version(self):
        """Gets the version of this SimulationSpec.  # noqa: E501


        :return: The version of this SimulationSpec.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this SimulationSpec.


        :param version: The version of this SimulationSpec.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and version is None:  # noqa: E501
            raise ValueError("Invalid value for `version`, must not be `None`")  # noqa: E501

        self._version = version

    @property
    def created_at(self):
        """Gets the created_at of this SimulationSpec.  # noqa: E501


        :return: The created_at of this SimulationSpec.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this SimulationSpec.


        :param created_at: The created_at of this SimulationSpec.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def modified_at(self):
        """Gets the modified_at of this SimulationSpec.  # noqa: E501


        :return: The modified_at of this SimulationSpec.  # noqa: E501
        :rtype: datetime
        """
        return self._modified_at

    @modified_at.setter
    def modified_at(self, modified_at):
        """Sets the modified_at of this SimulationSpec.


        :param modified_at: The modified_at of this SimulationSpec.  # noqa: E501
        :type: datetime
        """

        self._modified_at = modified_at

    @property
    def geometry_id(self):
        """Gets the geometry_id of this SimulationSpec.  # noqa: E501


        :return: The geometry_id of this SimulationSpec.  # noqa: E501
        :rtype: str
        """
        return self._geometry_id

    @geometry_id.setter
    def geometry_id(self, geometry_id):
        """Sets the geometry_id of this SimulationSpec.


        :param geometry_id: The geometry_id of this SimulationSpec.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and geometry_id is None:  # noqa: E501
            raise ValueError("Invalid value for `geometry_id`, must not be `None`")  # noqa: E501

        self._geometry_id = geometry_id

    @property
    def mesh_id(self):
        """Gets the mesh_id of this SimulationSpec.  # noqa: E501

        The generated mesh ID which is to be used in the simulation. This field should be left empty for analysis types that do not require a generated mesh like 'INCOMPRESSIBLE_PACEFISH', 'WIND_COMFORT', and 'SIMERICS_ANALYSIS'.  # noqa: E501

        :return: The mesh_id of this SimulationSpec.  # noqa: E501
        :rtype: str
        """
        return self._mesh_id

    @mesh_id.setter
    def mesh_id(self, mesh_id):
        """Sets the mesh_id of this SimulationSpec.

        The generated mesh ID which is to be used in the simulation. This field should be left empty for analysis types that do not require a generated mesh like 'INCOMPRESSIBLE_PACEFISH', 'WIND_COMFORT', and 'SIMERICS_ANALYSIS'.  # noqa: E501

        :param mesh_id: The mesh_id of this SimulationSpec.  # noqa: E501
        :type: str
        """

        self._mesh_id = mesh_id

    @property
    def model(self):
        """Gets the model of this SimulationSpec.  # noqa: E501


        :return: The model of this SimulationSpec.  # noqa: E501
        :rtype: Analysis
        """
        return self._model

    @model.setter
    def model(self, model):
        """Sets the model of this SimulationSpec.


        :param model: The model of this SimulationSpec.  # noqa: E501
        :type: Analysis
        """
        if self.local_vars_configuration.client_side_validation and model is None:  # noqa: E501
            raise ValueError("Invalid value for `model`, must not be `None`")  # noqa: E501

        self._model = model

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
        if not isinstance(other, SimulationSpec):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SimulationSpec):
            return True

        return self.to_dict() != other.to_dict()
