15.4: Ensure Service Provider Contracts Include Security Requirements
=========================================================
Ensure service provider contracts include security requirements. Example requirements may include minimum security program requirements, security incident and/or data breach notification and response, data encryption requirements, and data disposal commitments. These security requirements must be consistent with the enterprise’s service provider management policy. Review service provider contracts annually to ensure contracts are not missing security requirements.

.. list-table::
	:header-rows: 1

	* - Asset Type
	  - Security Function
	  - Implementation Groups
	* - N/A
	  - Protect
	  - 2, 3

Dependencies
------------
* Safeguard 15.1: Establish and Maintain an Inventory of Service Providers
* Safeguard 15.2: Establish and Maintain a Service Provider Management Policy

Inputs
-----------
#. :code:`GV44`: Service Provider Inventory List
#. :code:`GV45`: Service Provider Management Policy
#. Date of last update or review of contracts


Operations
----------
#. Use Input 2 :code:`GV45` to determine if the enterprise policy includes security program requirements for service providers
	#. If the security requirements exist, M1 = 1
	#. If the security requirements do not exist, M1 = 0 
#. Use Input 1 :code:`GV44` to determine if each listed service provider has a contract
	#. Identify and enumerate service providers with contracts (M3)
	#. Identify and enumerate service providers without contracts (M4)
#. For each service provider with a contract identified in Operation 2.1, compare the date from input 3 to current date and capture timeframe in months
	#. Identify and enumerate service providers whose contract has been reviewed within twelve months or less (M5)
	#. Identify and enumerate service providers whose contract has been reviewed outside the twelve month window (M6)

Measures
--------
* M1 = Output of Operation 1
* M2 = Count of service providers in inventory
* M3 = Count of service providers with contracts
* M4 = Count of service providers without contracts
* M5 = Count of service providers with up to date contracts
* M6 = Count of service providers without out dated contracts

Metrics
-------
* If M1 is a 0, this safeguard receives a failing score. The other metrics don't apply.

Compliance
^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The percentage of service providers with up to date contract 
	* - **Calculation**
	  - :code:`M5 / M2`

.. history
.. authors
.. license
