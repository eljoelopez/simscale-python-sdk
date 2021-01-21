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


class FluidSolvers(object):
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
        'phase_fraction_solver': 'MULESSolver',
        'velocity_solver': 'OneOfFluidSolversVelocitySolver',
        'velocity_final_solver': 'OneOfFluidSolversVelocityFinalSolver',
        'density_solver': 'OneOfFluidSolversDensitySolver',
        'density_final_solver': 'OneOfFluidSolversDensityFinalSolver',
        'pressure_solver': 'OneOfFluidSolversPressureSolver',
        'pressure_final_solver': 'OneOfFluidSolversPressureFinalSolver',
        'temperature_solver': 'OneOfFluidSolversTemperatureSolver',
        'temperature_final_solver': 'OneOfFluidSolversTemperatureFinalSolver',
        'pressure_rgh_solver': 'OneOfFluidSolversPressureRghSolver',
        'pressure_rgh_final_solver': 'OneOfFluidSolversPressureRghFinalSolver',
        'solid_enthalpy_solver': 'OneOfFluidSolversSolidEnthalpySolver',
        'solid_enthalpy_final_solver': 'OneOfFluidSolversSolidEnthalpyFinalSolver',
        'enthalpy_solver': 'OneOfFluidSolversEnthalpySolver',
        'enthalpy_final_solver': 'OneOfFluidSolversEnthalpyFinalSolver',
        'internal_energy_solver': 'OneOfFluidSolversInternalEnergySolver',
        'internal_energy_final_solver': 'OneOfFluidSolversInternalEnergyFinalSolver',
        'turbulent_kinetic_energy_solver': 'OneOfFluidSolversTurbulentKineticEnergySolver',
        'turbulent_kinetic_energy_final_solver': 'OneOfFluidSolversTurbulentKineticEnergyFinalSolver',
        'nu_tilda_solver': 'OneOfFluidSolversNuTildaSolver',
        'nu_tilda_final_solver': 'OneOfFluidSolversNuTildaFinalSolver',
        'omega_dissipation_rate_solver': 'OneOfFluidSolversOmegaDissipationRateSolver',
        'omega_dissipation_rate_final_solver': 'OneOfFluidSolversOmegaDissipationRateFinalSolver',
        'epsilon_dissipation_rate_solver': 'OneOfFluidSolversEpsilonDissipationRateSolver',
        'epsilon_dissipation_rate_final_solver': 'OneOfFluidSolversEpsilonDissipationRateFinalSolver',
        'passive_scalar_solver': 'OneOfFluidSolversPassiveScalarSolver',
        'radiative_intensity_ray_solver': 'OneOfFluidSolversRadiativeIntensityRaySolver'
    }

    attribute_map = {
        'phase_fraction_solver': 'phaseFractionSolver',
        'velocity_solver': 'velocitySolver',
        'velocity_final_solver': 'velocityFinalSolver',
        'density_solver': 'densitySolver',
        'density_final_solver': 'densityFinalSolver',
        'pressure_solver': 'pressureSolver',
        'pressure_final_solver': 'pressureFinalSolver',
        'temperature_solver': 'temperatureSolver',
        'temperature_final_solver': 'temperatureFinalSolver',
        'pressure_rgh_solver': 'pressureRghSolver',
        'pressure_rgh_final_solver': 'pressureRghFinalSolver',
        'solid_enthalpy_solver': 'solidEnthalpySolver',
        'solid_enthalpy_final_solver': 'solidEnthalpyFinalSolver',
        'enthalpy_solver': 'enthalpySolver',
        'enthalpy_final_solver': 'enthalpyFinalSolver',
        'internal_energy_solver': 'internalEnergySolver',
        'internal_energy_final_solver': 'internalEnergyFinalSolver',
        'turbulent_kinetic_energy_solver': 'turbulentKineticEnergySolver',
        'turbulent_kinetic_energy_final_solver': 'turbulentKineticEnergyFinalSolver',
        'nu_tilda_solver': 'nuTildaSolver',
        'nu_tilda_final_solver': 'nuTildaFinalSolver',
        'omega_dissipation_rate_solver': 'omegaDissipationRateSolver',
        'omega_dissipation_rate_final_solver': 'omegaDissipationRateFinalSolver',
        'epsilon_dissipation_rate_solver': 'epsilonDissipationRateSolver',
        'epsilon_dissipation_rate_final_solver': 'epsilonDissipationRateFinalSolver',
        'passive_scalar_solver': 'passiveScalarSolver',
        'radiative_intensity_ray_solver': 'radiativeIntensityRaySolver'
    }

    def __init__(self, phase_fraction_solver=None, velocity_solver=None, velocity_final_solver=None, density_solver=None, density_final_solver=None, pressure_solver=None, pressure_final_solver=None, temperature_solver=None, temperature_final_solver=None, pressure_rgh_solver=None, pressure_rgh_final_solver=None, solid_enthalpy_solver=None, solid_enthalpy_final_solver=None, enthalpy_solver=None, enthalpy_final_solver=None, internal_energy_solver=None, internal_energy_final_solver=None, turbulent_kinetic_energy_solver=None, turbulent_kinetic_energy_final_solver=None, nu_tilda_solver=None, nu_tilda_final_solver=None, omega_dissipation_rate_solver=None, omega_dissipation_rate_final_solver=None, epsilon_dissipation_rate_solver=None, epsilon_dissipation_rate_final_solver=None, passive_scalar_solver=None, radiative_intensity_ray_solver=None, local_vars_configuration=None):  # noqa: E501
        """FluidSolvers - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._phase_fraction_solver = None
        self._velocity_solver = None
        self._velocity_final_solver = None
        self._density_solver = None
        self._density_final_solver = None
        self._pressure_solver = None
        self._pressure_final_solver = None
        self._temperature_solver = None
        self._temperature_final_solver = None
        self._pressure_rgh_solver = None
        self._pressure_rgh_final_solver = None
        self._solid_enthalpy_solver = None
        self._solid_enthalpy_final_solver = None
        self._enthalpy_solver = None
        self._enthalpy_final_solver = None
        self._internal_energy_solver = None
        self._internal_energy_final_solver = None
        self._turbulent_kinetic_energy_solver = None
        self._turbulent_kinetic_energy_final_solver = None
        self._nu_tilda_solver = None
        self._nu_tilda_final_solver = None
        self._omega_dissipation_rate_solver = None
        self._omega_dissipation_rate_final_solver = None
        self._epsilon_dissipation_rate_solver = None
        self._epsilon_dissipation_rate_final_solver = None
        self._passive_scalar_solver = None
        self._radiative_intensity_ray_solver = None
        self.discriminator = None

        if phase_fraction_solver is not None:
            self.phase_fraction_solver = phase_fraction_solver
        if velocity_solver is not None:
            self.velocity_solver = velocity_solver
        if velocity_final_solver is not None:
            self.velocity_final_solver = velocity_final_solver
        if density_solver is not None:
            self.density_solver = density_solver
        if density_final_solver is not None:
            self.density_final_solver = density_final_solver
        if pressure_solver is not None:
            self.pressure_solver = pressure_solver
        if pressure_final_solver is not None:
            self.pressure_final_solver = pressure_final_solver
        if temperature_solver is not None:
            self.temperature_solver = temperature_solver
        if temperature_final_solver is not None:
            self.temperature_final_solver = temperature_final_solver
        if pressure_rgh_solver is not None:
            self.pressure_rgh_solver = pressure_rgh_solver
        if pressure_rgh_final_solver is not None:
            self.pressure_rgh_final_solver = pressure_rgh_final_solver
        if solid_enthalpy_solver is not None:
            self.solid_enthalpy_solver = solid_enthalpy_solver
        if solid_enthalpy_final_solver is not None:
            self.solid_enthalpy_final_solver = solid_enthalpy_final_solver
        if enthalpy_solver is not None:
            self.enthalpy_solver = enthalpy_solver
        if enthalpy_final_solver is not None:
            self.enthalpy_final_solver = enthalpy_final_solver
        if internal_energy_solver is not None:
            self.internal_energy_solver = internal_energy_solver
        if internal_energy_final_solver is not None:
            self.internal_energy_final_solver = internal_energy_final_solver
        if turbulent_kinetic_energy_solver is not None:
            self.turbulent_kinetic_energy_solver = turbulent_kinetic_energy_solver
        if turbulent_kinetic_energy_final_solver is not None:
            self.turbulent_kinetic_energy_final_solver = turbulent_kinetic_energy_final_solver
        if nu_tilda_solver is not None:
            self.nu_tilda_solver = nu_tilda_solver
        if nu_tilda_final_solver is not None:
            self.nu_tilda_final_solver = nu_tilda_final_solver
        if omega_dissipation_rate_solver is not None:
            self.omega_dissipation_rate_solver = omega_dissipation_rate_solver
        if omega_dissipation_rate_final_solver is not None:
            self.omega_dissipation_rate_final_solver = omega_dissipation_rate_final_solver
        if epsilon_dissipation_rate_solver is not None:
            self.epsilon_dissipation_rate_solver = epsilon_dissipation_rate_solver
        if epsilon_dissipation_rate_final_solver is not None:
            self.epsilon_dissipation_rate_final_solver = epsilon_dissipation_rate_final_solver
        if passive_scalar_solver is not None:
            self.passive_scalar_solver = passive_scalar_solver
        if radiative_intensity_ray_solver is not None:
            self.radiative_intensity_ray_solver = radiative_intensity_ray_solver

    @property
    def phase_fraction_solver(self):
        """Gets the phase_fraction_solver of this FluidSolvers.  # noqa: E501


        :return: The phase_fraction_solver of this FluidSolvers.  # noqa: E501
        :rtype: MULESSolver
        """
        return self._phase_fraction_solver

    @phase_fraction_solver.setter
    def phase_fraction_solver(self, phase_fraction_solver):
        """Sets the phase_fraction_solver of this FluidSolvers.


        :param phase_fraction_solver: The phase_fraction_solver of this FluidSolvers.  # noqa: E501
        :type: MULESSolver
        """

        self._phase_fraction_solver = phase_fraction_solver

    @property
    def velocity_solver(self):
        """Gets the velocity_solver of this FluidSolvers.  # noqa: E501


        :return: The velocity_solver of this FluidSolvers.  # noqa: E501
        :rtype: OneOfFluidSolversVelocitySolver
        """
        return self._velocity_solver

    @velocity_solver.setter
    def velocity_solver(self, velocity_solver):
        """Sets the velocity_solver of this FluidSolvers.


        :param velocity_solver: The velocity_solver of this FluidSolvers.  # noqa: E501
        :type: OneOfFluidSolversVelocitySolver
        """

        self._velocity_solver = velocity_solver

    @property
    def velocity_final_solver(self):
        """Gets the velocity_final_solver of this FluidSolvers.  # noqa: E501


        :return: The velocity_final_solver of this FluidSolvers.  # noqa: E501
        :rtype: OneOfFluidSolversVelocityFinalSolver
        """
        return self._velocity_final_solver

    @velocity_final_solver.setter
    def velocity_final_solver(self, velocity_final_solver):
        """Sets the velocity_final_solver of this FluidSolvers.


        :param velocity_final_solver: The velocity_final_solver of this FluidSolvers.  # noqa: E501
        :type: OneOfFluidSolversVelocityFinalSolver
        """

        self._velocity_final_solver = velocity_final_solver

    @property
    def density_solver(self):
        """Gets the density_solver of this FluidSolvers.  # noqa: E501


        :return: The density_solver of this FluidSolvers.  # noqa: E501
        :rtype: OneOfFluidSolversDensitySolver
        """
        return self._density_solver

    @density_solver.setter
    def density_solver(self, density_solver):
        """Sets the density_solver of this FluidSolvers.


        :param density_solver: The density_solver of this FluidSolvers.  # noqa: E501
        :type: OneOfFluidSolversDensitySolver
        """

        self._density_solver = density_solver

    @property
    def density_final_solver(self):
        """Gets the density_final_solver of this FluidSolvers.  # noqa: E501


        :return: The density_final_solver of this FluidSolvers.  # noqa: E501
        :rtype: OneOfFluidSolversDensityFinalSolver
        """
        return self._density_final_solver

    @density_final_solver.setter
    def density_final_solver(self, density_final_solver):
        """Sets the density_final_solver of this FluidSolvers.


        :param density_final_solver: The density_final_solver of this FluidSolvers.  # noqa: E501
        :type: OneOfFluidSolversDensityFinalSolver
        """

        self._density_final_solver = density_final_solver

    @property
    def pressure_solver(self):
        """Gets the pressure_solver of this FluidSolvers.  # noqa: E501


        :return: The pressure_solver of this FluidSolvers.  # noqa: E501
        :rtype: OneOfFluidSolversPressureSolver
        """
        return self._pressure_solver

    @pressure_solver.setter
    def pressure_solver(self, pressure_solver):
        """Sets the pressure_solver of this FluidSolvers.


        :param pressure_solver: The pressure_solver of this FluidSolvers.  # noqa: E501
        :type: OneOfFluidSolversPressureSolver
        """

        self._pressure_solver = pressure_solver

    @property
    def pressure_final_solver(self):
        """Gets the pressure_final_solver of this FluidSolvers.  # noqa: E501


        :return: The pressure_final_solver of this FluidSolvers.  # noqa: E501
        :rtype: OneOfFluidSolversPressureFinalSolver
        """
        return self._pressure_final_solver

    @pressure_final_solver.setter
    def pressure_final_solver(self, pressure_final_solver):
        """Sets the pressure_final_solver of this FluidSolvers.


        :param pressure_final_solver: The pressure_final_solver of this FluidSolvers.  # noqa: E501
        :type: OneOfFluidSolversPressureFinalSolver
        """

        self._pressure_final_solver = pressure_final_solver

    @property
    def temperature_solver(self):
        """Gets the temperature_solver of this FluidSolvers.  # noqa: E501


        :return: The temperature_solver of this FluidSolvers.  # noqa: E501
        :rtype: OneOfFluidSolversTemperatureSolver
        """
        return self._temperature_solver

    @temperature_solver.setter
    def temperature_solver(self, temperature_solver):
        """Sets the temperature_solver of this FluidSolvers.


        :param temperature_solver: The temperature_solver of this FluidSolvers.  # noqa: E501
        :type: OneOfFluidSolversTemperatureSolver
        """

        self._temperature_solver = temperature_solver

    @property
    def temperature_final_solver(self):
        """Gets the temperature_final_solver of this FluidSolvers.  # noqa: E501


        :return: The temperature_final_solver of this FluidSolvers.  # noqa: E501
        :rtype: OneOfFluidSolversTemperatureFinalSolver
        """
        return self._temperature_final_solver

    @temperature_final_solver.setter
    def temperature_final_solver(self, temperature_final_solver):
        """Sets the temperature_final_solver of this FluidSolvers.


        :param temperature_final_solver: The temperature_final_solver of this FluidSolvers.  # noqa: E501
        :type: OneOfFluidSolversTemperatureFinalSolver
        """

        self._temperature_final_solver = temperature_final_solver

    @property
    def pressure_rgh_solver(self):
        """Gets the pressure_rgh_solver of this FluidSolvers.  # noqa: E501


        :return: The pressure_rgh_solver of this FluidSolvers.  # noqa: E501
        :rtype: OneOfFluidSolversPressureRghSolver
        """
        return self._pressure_rgh_solver

    @pressure_rgh_solver.setter
    def pressure_rgh_solver(self, pressure_rgh_solver):
        """Sets the pressure_rgh_solver of this FluidSolvers.


        :param pressure_rgh_solver: The pressure_rgh_solver of this FluidSolvers.  # noqa: E501
        :type: OneOfFluidSolversPressureRghSolver
        """

        self._pressure_rgh_solver = pressure_rgh_solver

    @property
    def pressure_rgh_final_solver(self):
        """Gets the pressure_rgh_final_solver of this FluidSolvers.  # noqa: E501


        :return: The pressure_rgh_final_solver of this FluidSolvers.  # noqa: E501
        :rtype: OneOfFluidSolversPressureRghFinalSolver
        """
        return self._pressure_rgh_final_solver

    @pressure_rgh_final_solver.setter
    def pressure_rgh_final_solver(self, pressure_rgh_final_solver):
        """Sets the pressure_rgh_final_solver of this FluidSolvers.


        :param pressure_rgh_final_solver: The pressure_rgh_final_solver of this FluidSolvers.  # noqa: E501
        :type: OneOfFluidSolversPressureRghFinalSolver
        """

        self._pressure_rgh_final_solver = pressure_rgh_final_solver

    @property
    def solid_enthalpy_solver(self):
        """Gets the solid_enthalpy_solver of this FluidSolvers.  # noqa: E501


        :return: The solid_enthalpy_solver of this FluidSolvers.  # noqa: E501
        :rtype: OneOfFluidSolversSolidEnthalpySolver
        """
        return self._solid_enthalpy_solver

    @solid_enthalpy_solver.setter
    def solid_enthalpy_solver(self, solid_enthalpy_solver):
        """Sets the solid_enthalpy_solver of this FluidSolvers.


        :param solid_enthalpy_solver: The solid_enthalpy_solver of this FluidSolvers.  # noqa: E501
        :type: OneOfFluidSolversSolidEnthalpySolver
        """

        self._solid_enthalpy_solver = solid_enthalpy_solver

    @property
    def solid_enthalpy_final_solver(self):
        """Gets the solid_enthalpy_final_solver of this FluidSolvers.  # noqa: E501


        :return: The solid_enthalpy_final_solver of this FluidSolvers.  # noqa: E501
        :rtype: OneOfFluidSolversSolidEnthalpyFinalSolver
        """
        return self._solid_enthalpy_final_solver

    @solid_enthalpy_final_solver.setter
    def solid_enthalpy_final_solver(self, solid_enthalpy_final_solver):
        """Sets the solid_enthalpy_final_solver of this FluidSolvers.


        :param solid_enthalpy_final_solver: The solid_enthalpy_final_solver of this FluidSolvers.  # noqa: E501
        :type: OneOfFluidSolversSolidEnthalpyFinalSolver
        """

        self._solid_enthalpy_final_solver = solid_enthalpy_final_solver

    @property
    def enthalpy_solver(self):
        """Gets the enthalpy_solver of this FluidSolvers.  # noqa: E501


        :return: The enthalpy_solver of this FluidSolvers.  # noqa: E501
        :rtype: OneOfFluidSolversEnthalpySolver
        """
        return self._enthalpy_solver

    @enthalpy_solver.setter
    def enthalpy_solver(self, enthalpy_solver):
        """Sets the enthalpy_solver of this FluidSolvers.


        :param enthalpy_solver: The enthalpy_solver of this FluidSolvers.  # noqa: E501
        :type: OneOfFluidSolversEnthalpySolver
        """

        self._enthalpy_solver = enthalpy_solver

    @property
    def enthalpy_final_solver(self):
        """Gets the enthalpy_final_solver of this FluidSolvers.  # noqa: E501


        :return: The enthalpy_final_solver of this FluidSolvers.  # noqa: E501
        :rtype: OneOfFluidSolversEnthalpyFinalSolver
        """
        return self._enthalpy_final_solver

    @enthalpy_final_solver.setter
    def enthalpy_final_solver(self, enthalpy_final_solver):
        """Sets the enthalpy_final_solver of this FluidSolvers.


        :param enthalpy_final_solver: The enthalpy_final_solver of this FluidSolvers.  # noqa: E501
        :type: OneOfFluidSolversEnthalpyFinalSolver
        """

        self._enthalpy_final_solver = enthalpy_final_solver

    @property
    def internal_energy_solver(self):
        """Gets the internal_energy_solver of this FluidSolvers.  # noqa: E501


        :return: The internal_energy_solver of this FluidSolvers.  # noqa: E501
        :rtype: OneOfFluidSolversInternalEnergySolver
        """
        return self._internal_energy_solver

    @internal_energy_solver.setter
    def internal_energy_solver(self, internal_energy_solver):
        """Sets the internal_energy_solver of this FluidSolvers.


        :param internal_energy_solver: The internal_energy_solver of this FluidSolvers.  # noqa: E501
        :type: OneOfFluidSolversInternalEnergySolver
        """

        self._internal_energy_solver = internal_energy_solver

    @property
    def internal_energy_final_solver(self):
        """Gets the internal_energy_final_solver of this FluidSolvers.  # noqa: E501


        :return: The internal_energy_final_solver of this FluidSolvers.  # noqa: E501
        :rtype: OneOfFluidSolversInternalEnergyFinalSolver
        """
        return self._internal_energy_final_solver

    @internal_energy_final_solver.setter
    def internal_energy_final_solver(self, internal_energy_final_solver):
        """Sets the internal_energy_final_solver of this FluidSolvers.


        :param internal_energy_final_solver: The internal_energy_final_solver of this FluidSolvers.  # noqa: E501
        :type: OneOfFluidSolversInternalEnergyFinalSolver
        """

        self._internal_energy_final_solver = internal_energy_final_solver

    @property
    def turbulent_kinetic_energy_solver(self):
        """Gets the turbulent_kinetic_energy_solver of this FluidSolvers.  # noqa: E501


        :return: The turbulent_kinetic_energy_solver of this FluidSolvers.  # noqa: E501
        :rtype: OneOfFluidSolversTurbulentKineticEnergySolver
        """
        return self._turbulent_kinetic_energy_solver

    @turbulent_kinetic_energy_solver.setter
    def turbulent_kinetic_energy_solver(self, turbulent_kinetic_energy_solver):
        """Sets the turbulent_kinetic_energy_solver of this FluidSolvers.


        :param turbulent_kinetic_energy_solver: The turbulent_kinetic_energy_solver of this FluidSolvers.  # noqa: E501
        :type: OneOfFluidSolversTurbulentKineticEnergySolver
        """

        self._turbulent_kinetic_energy_solver = turbulent_kinetic_energy_solver

    @property
    def turbulent_kinetic_energy_final_solver(self):
        """Gets the turbulent_kinetic_energy_final_solver of this FluidSolvers.  # noqa: E501


        :return: The turbulent_kinetic_energy_final_solver of this FluidSolvers.  # noqa: E501
        :rtype: OneOfFluidSolversTurbulentKineticEnergyFinalSolver
        """
        return self._turbulent_kinetic_energy_final_solver

    @turbulent_kinetic_energy_final_solver.setter
    def turbulent_kinetic_energy_final_solver(self, turbulent_kinetic_energy_final_solver):
        """Sets the turbulent_kinetic_energy_final_solver of this FluidSolvers.


        :param turbulent_kinetic_energy_final_solver: The turbulent_kinetic_energy_final_solver of this FluidSolvers.  # noqa: E501
        :type: OneOfFluidSolversTurbulentKineticEnergyFinalSolver
        """

        self._turbulent_kinetic_energy_final_solver = turbulent_kinetic_energy_final_solver

    @property
    def nu_tilda_solver(self):
        """Gets the nu_tilda_solver of this FluidSolvers.  # noqa: E501


        :return: The nu_tilda_solver of this FluidSolvers.  # noqa: E501
        :rtype: OneOfFluidSolversNuTildaSolver
        """
        return self._nu_tilda_solver

    @nu_tilda_solver.setter
    def nu_tilda_solver(self, nu_tilda_solver):
        """Sets the nu_tilda_solver of this FluidSolvers.


        :param nu_tilda_solver: The nu_tilda_solver of this FluidSolvers.  # noqa: E501
        :type: OneOfFluidSolversNuTildaSolver
        """

        self._nu_tilda_solver = nu_tilda_solver

    @property
    def nu_tilda_final_solver(self):
        """Gets the nu_tilda_final_solver of this FluidSolvers.  # noqa: E501


        :return: The nu_tilda_final_solver of this FluidSolvers.  # noqa: E501
        :rtype: OneOfFluidSolversNuTildaFinalSolver
        """
        return self._nu_tilda_final_solver

    @nu_tilda_final_solver.setter
    def nu_tilda_final_solver(self, nu_tilda_final_solver):
        """Sets the nu_tilda_final_solver of this FluidSolvers.


        :param nu_tilda_final_solver: The nu_tilda_final_solver of this FluidSolvers.  # noqa: E501
        :type: OneOfFluidSolversNuTildaFinalSolver
        """

        self._nu_tilda_final_solver = nu_tilda_final_solver

    @property
    def omega_dissipation_rate_solver(self):
        """Gets the omega_dissipation_rate_solver of this FluidSolvers.  # noqa: E501


        :return: The omega_dissipation_rate_solver of this FluidSolvers.  # noqa: E501
        :rtype: OneOfFluidSolversOmegaDissipationRateSolver
        """
        return self._omega_dissipation_rate_solver

    @omega_dissipation_rate_solver.setter
    def omega_dissipation_rate_solver(self, omega_dissipation_rate_solver):
        """Sets the omega_dissipation_rate_solver of this FluidSolvers.


        :param omega_dissipation_rate_solver: The omega_dissipation_rate_solver of this FluidSolvers.  # noqa: E501
        :type: OneOfFluidSolversOmegaDissipationRateSolver
        """

        self._omega_dissipation_rate_solver = omega_dissipation_rate_solver

    @property
    def omega_dissipation_rate_final_solver(self):
        """Gets the omega_dissipation_rate_final_solver of this FluidSolvers.  # noqa: E501


        :return: The omega_dissipation_rate_final_solver of this FluidSolvers.  # noqa: E501
        :rtype: OneOfFluidSolversOmegaDissipationRateFinalSolver
        """
        return self._omega_dissipation_rate_final_solver

    @omega_dissipation_rate_final_solver.setter
    def omega_dissipation_rate_final_solver(self, omega_dissipation_rate_final_solver):
        """Sets the omega_dissipation_rate_final_solver of this FluidSolvers.


        :param omega_dissipation_rate_final_solver: The omega_dissipation_rate_final_solver of this FluidSolvers.  # noqa: E501
        :type: OneOfFluidSolversOmegaDissipationRateFinalSolver
        """

        self._omega_dissipation_rate_final_solver = omega_dissipation_rate_final_solver

    @property
    def epsilon_dissipation_rate_solver(self):
        """Gets the epsilon_dissipation_rate_solver of this FluidSolvers.  # noqa: E501


        :return: The epsilon_dissipation_rate_solver of this FluidSolvers.  # noqa: E501
        :rtype: OneOfFluidSolversEpsilonDissipationRateSolver
        """
        return self._epsilon_dissipation_rate_solver

    @epsilon_dissipation_rate_solver.setter
    def epsilon_dissipation_rate_solver(self, epsilon_dissipation_rate_solver):
        """Sets the epsilon_dissipation_rate_solver of this FluidSolvers.


        :param epsilon_dissipation_rate_solver: The epsilon_dissipation_rate_solver of this FluidSolvers.  # noqa: E501
        :type: OneOfFluidSolversEpsilonDissipationRateSolver
        """

        self._epsilon_dissipation_rate_solver = epsilon_dissipation_rate_solver

    @property
    def epsilon_dissipation_rate_final_solver(self):
        """Gets the epsilon_dissipation_rate_final_solver of this FluidSolvers.  # noqa: E501


        :return: The epsilon_dissipation_rate_final_solver of this FluidSolvers.  # noqa: E501
        :rtype: OneOfFluidSolversEpsilonDissipationRateFinalSolver
        """
        return self._epsilon_dissipation_rate_final_solver

    @epsilon_dissipation_rate_final_solver.setter
    def epsilon_dissipation_rate_final_solver(self, epsilon_dissipation_rate_final_solver):
        """Sets the epsilon_dissipation_rate_final_solver of this FluidSolvers.


        :param epsilon_dissipation_rate_final_solver: The epsilon_dissipation_rate_final_solver of this FluidSolvers.  # noqa: E501
        :type: OneOfFluidSolversEpsilonDissipationRateFinalSolver
        """

        self._epsilon_dissipation_rate_final_solver = epsilon_dissipation_rate_final_solver

    @property
    def passive_scalar_solver(self):
        """Gets the passive_scalar_solver of this FluidSolvers.  # noqa: E501


        :return: The passive_scalar_solver of this FluidSolvers.  # noqa: E501
        :rtype: OneOfFluidSolversPassiveScalarSolver
        """
        return self._passive_scalar_solver

    @passive_scalar_solver.setter
    def passive_scalar_solver(self, passive_scalar_solver):
        """Sets the passive_scalar_solver of this FluidSolvers.


        :param passive_scalar_solver: The passive_scalar_solver of this FluidSolvers.  # noqa: E501
        :type: OneOfFluidSolversPassiveScalarSolver
        """

        self._passive_scalar_solver = passive_scalar_solver

    @property
    def radiative_intensity_ray_solver(self):
        """Gets the radiative_intensity_ray_solver of this FluidSolvers.  # noqa: E501


        :return: The radiative_intensity_ray_solver of this FluidSolvers.  # noqa: E501
        :rtype: OneOfFluidSolversRadiativeIntensityRaySolver
        """
        return self._radiative_intensity_ray_solver

    @radiative_intensity_ray_solver.setter
    def radiative_intensity_ray_solver(self, radiative_intensity_ray_solver):
        """Sets the radiative_intensity_ray_solver of this FluidSolvers.


        :param radiative_intensity_ray_solver: The radiative_intensity_ray_solver of this FluidSolvers.  # noqa: E501
        :type: OneOfFluidSolversRadiativeIntensityRaySolver
        """

        self._radiative_intensity_ray_solver = radiative_intensity_ray_solver

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
        if not isinstance(other, FluidSolvers):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FluidSolvers):
            return True

        return self.to_dict() != other.to_dict()