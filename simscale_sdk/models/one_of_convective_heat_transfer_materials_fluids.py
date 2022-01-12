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


class OneOfConvectiveHeatTransferMaterialsFluids(object):
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
        'associated_phase': 'str',
        'viscosity_model': 'OneOfIncompressibleMaterialViscosityModel',
        'density': 'DimensionalDensity',
        'thermal_expansion_coefficient': 'DimensionalThermalExpansionRate',
        'reference_temperature': 'DimensionalTemperature',
        'laminar_prandtl_number': 'float',
        'turbulent_prandtl_number': 'float',
        'specific_heat': 'DimensionalSpecificHeat',
        'molar_weight': 'DimensionalMolarMass',
        'topological_reference': 'TopologicalReference',
        'geometry_primitive_uuids': 'list[str]',
        'built_in_material': 'str',
        'material_library_reference': 'MaterialLibraryReference',
        'specie': 'SpecieDefault',
        'transport': 'OneOfFluidCompressibleMaterialTransport'
    }

    attribute_map = {
        'type': 'type',
        'name': 'name',
        'associated_phase': 'associatedPhase',
        'viscosity_model': 'viscosityModel',
        'density': 'density',
        'thermal_expansion_coefficient': 'thermalExpansionCoefficient',
        'reference_temperature': 'referenceTemperature',
        'laminar_prandtl_number': 'laminarPrandtlNumber',
        'turbulent_prandtl_number': 'turbulentPrandtlNumber',
        'specific_heat': 'specificHeat',
        'molar_weight': 'molarWeight',
        'topological_reference': 'topologicalReference',
        'geometry_primitive_uuids': 'geometryPrimitiveUuids',
        'built_in_material': 'builtInMaterial',
        'material_library_reference': 'materialLibraryReference',
        'specie': 'specie',
        'transport': 'transport'
    }

    discriminator_value_class_map = {
        'INCOMPRESSIBLE': 'IncompressibleMaterial',
        'COMPRESSIBLE': 'FluidCompressibleMaterial'
    }

    def __init__(self, type='COMPRESSIBLE', name=None, associated_phase=None, viscosity_model=None, density=None, thermal_expansion_coefficient=None, reference_temperature=None, laminar_prandtl_number=None, turbulent_prandtl_number=None, specific_heat=None, molar_weight=None, topological_reference=None, geometry_primitive_uuids=None, built_in_material=None, material_library_reference=None, specie=None, transport=None, local_vars_configuration=None):  # noqa: E501
        """OneOfConvectiveHeatTransferMaterialsFluids - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._name = None
        self._associated_phase = None
        self._viscosity_model = None
        self._density = None
        self._thermal_expansion_coefficient = None
        self._reference_temperature = None
        self._laminar_prandtl_number = None
        self._turbulent_prandtl_number = None
        self._specific_heat = None
        self._molar_weight = None
        self._topological_reference = None
        self._geometry_primitive_uuids = None
        self._built_in_material = None
        self._material_library_reference = None
        self._specie = None
        self._transport = None
        self.discriminator = 'type'

        self.type = type
        if name is not None:
            self.name = name
        if associated_phase is not None:
            self.associated_phase = associated_phase
        if viscosity_model is not None:
            self.viscosity_model = viscosity_model
        if density is not None:
            self.density = density
        if thermal_expansion_coefficient is not None:
            self.thermal_expansion_coefficient = thermal_expansion_coefficient
        if reference_temperature is not None:
            self.reference_temperature = reference_temperature
        if laminar_prandtl_number is not None:
            self.laminar_prandtl_number = laminar_prandtl_number
        if turbulent_prandtl_number is not None:
            self.turbulent_prandtl_number = turbulent_prandtl_number
        if specific_heat is not None:
            self.specific_heat = specific_heat
        if molar_weight is not None:
            self.molar_weight = molar_weight
        if topological_reference is not None:
            self.topological_reference = topological_reference
        if geometry_primitive_uuids is not None:
            self.geometry_primitive_uuids = geometry_primitive_uuids
        if built_in_material is not None:
            self.built_in_material = built_in_material
        if material_library_reference is not None:
            self.material_library_reference = material_library_reference
        if specie is not None:
            self.specie = specie
        if transport is not None:
            self.transport = transport

    @property
    def type(self):
        """Gets the type of this OneOfConvectiveHeatTransferMaterialsFluids.  # noqa: E501

        Schema name: FluidCompressibleMaterial  # noqa: E501

        :return: The type of this OneOfConvectiveHeatTransferMaterialsFluids.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this OneOfConvectiveHeatTransferMaterialsFluids.

        Schema name: FluidCompressibleMaterial  # noqa: E501

        :param type: The type of this OneOfConvectiveHeatTransferMaterialsFluids.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def name(self):
        """Gets the name of this OneOfConvectiveHeatTransferMaterialsFluids.  # noqa: E501


        :return: The name of this OneOfConvectiveHeatTransferMaterialsFluids.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this OneOfConvectiveHeatTransferMaterialsFluids.


        :param name: The name of this OneOfConvectiveHeatTransferMaterialsFluids.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def associated_phase(self):
        """Gets the associated_phase of this OneOfConvectiveHeatTransferMaterialsFluids.  # noqa: E501

        <p>Select the corresponding phase for this material:</p><p><b>Phase 0</b> would mean this material is represented by the phase fraction value of 0. Hence, a phase fraction of '0' in your setup corresponds to 100% of this fluid material.</p><p><b>Phase 1</b> would mean this material is represented by the phase fraction value of 1. Hence, a phase fraction of '1' in your setup corresponds to 100% of this fluid material.</p>  # noqa: E501

        :return: The associated_phase of this OneOfConvectiveHeatTransferMaterialsFluids.  # noqa: E501
        :rtype: str
        """
        return self._associated_phase

    @associated_phase.setter
    def associated_phase(self, associated_phase):
        """Sets the associated_phase of this OneOfConvectiveHeatTransferMaterialsFluids.

        <p>Select the corresponding phase for this material:</p><p><b>Phase 0</b> would mean this material is represented by the phase fraction value of 0. Hence, a phase fraction of '0' in your setup corresponds to 100% of this fluid material.</p><p><b>Phase 1</b> would mean this material is represented by the phase fraction value of 1. Hence, a phase fraction of '1' in your setup corresponds to 100% of this fluid material.</p>  # noqa: E501

        :param associated_phase: The associated_phase of this OneOfConvectiveHeatTransferMaterialsFluids.  # noqa: E501
        :type: str
        """
        allowed_values = ["PHASE_0", "PHASE_1"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and associated_phase not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `associated_phase` ({0}), must be one of {1}"  # noqa: E501
                .format(associated_phase, allowed_values)
            )

        self._associated_phase = associated_phase

    @property
    def viscosity_model(self):
        """Gets the viscosity_model of this OneOfConvectiveHeatTransferMaterialsFluids.  # noqa: E501


        :return: The viscosity_model of this OneOfConvectiveHeatTransferMaterialsFluids.  # noqa: E501
        :rtype: OneOfIncompressibleMaterialViscosityModel
        """
        return self._viscosity_model

    @viscosity_model.setter
    def viscosity_model(self, viscosity_model):
        """Sets the viscosity_model of this OneOfConvectiveHeatTransferMaterialsFluids.


        :param viscosity_model: The viscosity_model of this OneOfConvectiveHeatTransferMaterialsFluids.  # noqa: E501
        :type: OneOfIncompressibleMaterialViscosityModel
        """

        self._viscosity_model = viscosity_model

    @property
    def density(self):
        """Gets the density of this OneOfConvectiveHeatTransferMaterialsFluids.  # noqa: E501


        :return: The density of this OneOfConvectiveHeatTransferMaterialsFluids.  # noqa: E501
        :rtype: DimensionalDensity
        """
        return self._density

    @density.setter
    def density(self, density):
        """Sets the density of this OneOfConvectiveHeatTransferMaterialsFluids.


        :param density: The density of this OneOfConvectiveHeatTransferMaterialsFluids.  # noqa: E501
        :type: DimensionalDensity
        """

        self._density = density

    @property
    def thermal_expansion_coefficient(self):
        """Gets the thermal_expansion_coefficient of this OneOfConvectiveHeatTransferMaterialsFluids.  # noqa: E501


        :return: The thermal_expansion_coefficient of this OneOfConvectiveHeatTransferMaterialsFluids.  # noqa: E501
        :rtype: DimensionalThermalExpansionRate
        """
        return self._thermal_expansion_coefficient

    @thermal_expansion_coefficient.setter
    def thermal_expansion_coefficient(self, thermal_expansion_coefficient):
        """Sets the thermal_expansion_coefficient of this OneOfConvectiveHeatTransferMaterialsFluids.


        :param thermal_expansion_coefficient: The thermal_expansion_coefficient of this OneOfConvectiveHeatTransferMaterialsFluids.  # noqa: E501
        :type: DimensionalThermalExpansionRate
        """

        self._thermal_expansion_coefficient = thermal_expansion_coefficient

    @property
    def reference_temperature(self):
        """Gets the reference_temperature of this OneOfConvectiveHeatTransferMaterialsFluids.  # noqa: E501


        :return: The reference_temperature of this OneOfConvectiveHeatTransferMaterialsFluids.  # noqa: E501
        :rtype: DimensionalTemperature
        """
        return self._reference_temperature

    @reference_temperature.setter
    def reference_temperature(self, reference_temperature):
        """Sets the reference_temperature of this OneOfConvectiveHeatTransferMaterialsFluids.


        :param reference_temperature: The reference_temperature of this OneOfConvectiveHeatTransferMaterialsFluids.  # noqa: E501
        :type: DimensionalTemperature
        """

        self._reference_temperature = reference_temperature

    @property
    def laminar_prandtl_number(self):
        """Gets the laminar_prandtl_number of this OneOfConvectiveHeatTransferMaterialsFluids.  # noqa: E501

        Laminar Prandtl number is used to calculate the heat transfer in the domain.  # noqa: E501

        :return: The laminar_prandtl_number of this OneOfConvectiveHeatTransferMaterialsFluids.  # noqa: E501
        :rtype: float
        """
        return self._laminar_prandtl_number

    @laminar_prandtl_number.setter
    def laminar_prandtl_number(self, laminar_prandtl_number):
        """Sets the laminar_prandtl_number of this OneOfConvectiveHeatTransferMaterialsFluids.

        Laminar Prandtl number is used to calculate the heat transfer in the domain.  # noqa: E501

        :param laminar_prandtl_number: The laminar_prandtl_number of this OneOfConvectiveHeatTransferMaterialsFluids.  # noqa: E501
        :type: float
        """

        self._laminar_prandtl_number = laminar_prandtl_number

    @property
    def turbulent_prandtl_number(self):
        """Gets the turbulent_prandtl_number of this OneOfConvectiveHeatTransferMaterialsFluids.  # noqa: E501

        Turbulent Prandtl number is used to calculate the heat transfer due to turbulent effects in the domain.  # noqa: E501

        :return: The turbulent_prandtl_number of this OneOfConvectiveHeatTransferMaterialsFluids.  # noqa: E501
        :rtype: float
        """
        return self._turbulent_prandtl_number

    @turbulent_prandtl_number.setter
    def turbulent_prandtl_number(self, turbulent_prandtl_number):
        """Sets the turbulent_prandtl_number of this OneOfConvectiveHeatTransferMaterialsFluids.

        Turbulent Prandtl number is used to calculate the heat transfer due to turbulent effects in the domain.  # noqa: E501

        :param turbulent_prandtl_number: The turbulent_prandtl_number of this OneOfConvectiveHeatTransferMaterialsFluids.  # noqa: E501
        :type: float
        """

        self._turbulent_prandtl_number = turbulent_prandtl_number

    @property
    def specific_heat(self):
        """Gets the specific_heat of this OneOfConvectiveHeatTransferMaterialsFluids.  # noqa: E501


        :return: The specific_heat of this OneOfConvectiveHeatTransferMaterialsFluids.  # noqa: E501
        :rtype: DimensionalSpecificHeat
        """
        return self._specific_heat

    @specific_heat.setter
    def specific_heat(self, specific_heat):
        """Sets the specific_heat of this OneOfConvectiveHeatTransferMaterialsFluids.


        :param specific_heat: The specific_heat of this OneOfConvectiveHeatTransferMaterialsFluids.  # noqa: E501
        :type: DimensionalSpecificHeat
        """

        self._specific_heat = specific_heat

    @property
    def molar_weight(self):
        """Gets the molar_weight of this OneOfConvectiveHeatTransferMaterialsFluids.  # noqa: E501


        :return: The molar_weight of this OneOfConvectiveHeatTransferMaterialsFluids.  # noqa: E501
        :rtype: DimensionalMolarMass
        """
        return self._molar_weight

    @molar_weight.setter
    def molar_weight(self, molar_weight):
        """Sets the molar_weight of this OneOfConvectiveHeatTransferMaterialsFluids.


        :param molar_weight: The molar_weight of this OneOfConvectiveHeatTransferMaterialsFluids.  # noqa: E501
        :type: DimensionalMolarMass
        """

        self._molar_weight = molar_weight

    @property
    def topological_reference(self):
        """Gets the topological_reference of this OneOfConvectiveHeatTransferMaterialsFluids.  # noqa: E501


        :return: The topological_reference of this OneOfConvectiveHeatTransferMaterialsFluids.  # noqa: E501
        :rtype: TopologicalReference
        """
        return self._topological_reference

    @topological_reference.setter
    def topological_reference(self, topological_reference):
        """Sets the topological_reference of this OneOfConvectiveHeatTransferMaterialsFluids.


        :param topological_reference: The topological_reference of this OneOfConvectiveHeatTransferMaterialsFluids.  # noqa: E501
        :type: TopologicalReference
        """

        self._topological_reference = topological_reference

    @property
    def geometry_primitive_uuids(self):
        """Gets the geometry_primitive_uuids of this OneOfConvectiveHeatTransferMaterialsFluids.  # noqa: E501


        :return: The geometry_primitive_uuids of this OneOfConvectiveHeatTransferMaterialsFluids.  # noqa: E501
        :rtype: list[str]
        """
        return self._geometry_primitive_uuids

    @geometry_primitive_uuids.setter
    def geometry_primitive_uuids(self, geometry_primitive_uuids):
        """Sets the geometry_primitive_uuids of this OneOfConvectiveHeatTransferMaterialsFluids.


        :param geometry_primitive_uuids: The geometry_primitive_uuids of this OneOfConvectiveHeatTransferMaterialsFluids.  # noqa: E501
        :type: list[str]
        """

        self._geometry_primitive_uuids = geometry_primitive_uuids

    @property
    def built_in_material(self):
        """Gets the built_in_material of this OneOfConvectiveHeatTransferMaterialsFluids.  # noqa: E501


        :return: The built_in_material of this OneOfConvectiveHeatTransferMaterialsFluids.  # noqa: E501
        :rtype: str
        """
        return self._built_in_material

    @built_in_material.setter
    def built_in_material(self, built_in_material):
        """Sets the built_in_material of this OneOfConvectiveHeatTransferMaterialsFluids.


        :param built_in_material: The built_in_material of this OneOfConvectiveHeatTransferMaterialsFluids.  # noqa: E501
        :type: str
        """

        self._built_in_material = built_in_material

    @property
    def material_library_reference(self):
        """Gets the material_library_reference of this OneOfConvectiveHeatTransferMaterialsFluids.  # noqa: E501


        :return: The material_library_reference of this OneOfConvectiveHeatTransferMaterialsFluids.  # noqa: E501
        :rtype: MaterialLibraryReference
        """
        return self._material_library_reference

    @material_library_reference.setter
    def material_library_reference(self, material_library_reference):
        """Sets the material_library_reference of this OneOfConvectiveHeatTransferMaterialsFluids.


        :param material_library_reference: The material_library_reference of this OneOfConvectiveHeatTransferMaterialsFluids.  # noqa: E501
        :type: MaterialLibraryReference
        """

        self._material_library_reference = material_library_reference

    @property
    def specie(self):
        """Gets the specie of this OneOfConvectiveHeatTransferMaterialsFluids.  # noqa: E501


        :return: The specie of this OneOfConvectiveHeatTransferMaterialsFluids.  # noqa: E501
        :rtype: SpecieDefault
        """
        return self._specie

    @specie.setter
    def specie(self, specie):
        """Sets the specie of this OneOfConvectiveHeatTransferMaterialsFluids.


        :param specie: The specie of this OneOfConvectiveHeatTransferMaterialsFluids.  # noqa: E501
        :type: SpecieDefault
        """

        self._specie = specie

    @property
    def transport(self):
        """Gets the transport of this OneOfConvectiveHeatTransferMaterialsFluids.  # noqa: E501


        :return: The transport of this OneOfConvectiveHeatTransferMaterialsFluids.  # noqa: E501
        :rtype: OneOfFluidCompressibleMaterialTransport
        """
        return self._transport

    @transport.setter
    def transport(self, transport):
        """Sets the transport of this OneOfConvectiveHeatTransferMaterialsFluids.


        :param transport: The transport of this OneOfConvectiveHeatTransferMaterialsFluids.  # noqa: E501
        :type: OneOfFluidCompressibleMaterialTransport
        """

        self._transport = transport

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
        if not isinstance(other, OneOfConvectiveHeatTransferMaterialsFluids):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OneOfConvectiveHeatTransferMaterialsFluids):
            return True

        return self.to_dict() != other.to_dict()
