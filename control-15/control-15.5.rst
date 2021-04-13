15.5: Assess Service Providers
=========================================================
Assess service providers consistent with the enterprise’s service provider management policy. Assessment scope may vary based on classification(s), and may include review of standardized assessment reports, such as Service Organization Control 2 (SOC 2) and Payment Card Industry (PCI) Attestation of Compliance (AoC), customized questionnaires, or other appropriately rigorous processes. Reassess service providers annually, at a minimum, or with new and renewed contracts.

.. list-table::
	:header-rows: 1

	* - Asset Type
	  - Security Function
	  - Implementation Groups
	* - N/A
	  - Identify
	  - 3

Dependencies
------------
* Safeguard 15.1: Establish and Maintain an Inventory of Service Providers
* Safeguard 15.2: Establish and Maintain a Service Provider Management Policy

Inputs
-----------
#. :code:`GV44`: Service Provider Inventory List
#. :code:`GV45`: Service Provider Management Policy

Operations
----------
#. Use Input 2 :code:`GV45` to determine if the enterprise policy includes monitoring guidance for service providers
	#. If the assessment scope exist, M1 = 1
	#. If the assessment scope does not exist, M1 = 0 
#. Use Input 1 :code:`GV44` to determine if each listed service provider has monitoring guidance included in the policy
	#. Identify and enumerate service providers with monitoring guidance (M3)
	#. Identify and enumerate service providers without monitoring guidance (M4)

Measures
--------
* M1 = Output of Operation 1
* M2 = Count of service providers in inventory
* M3 = Count of service providers with monitoring guidance
* M4 = Count of service providers without monitoring guidance

Metrics
-------
* If M1 is a 0, this safeguard receives a failing score. The other metrics don't apply.

Compliance
^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The percentage of service providers with monitoring guidance
	  - | included in policy
	* - **Calculation**
	  - :code:`M3 / M2`

.. history
.. authors
.. license
