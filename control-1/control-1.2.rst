1.2: Use a Passive Asset Discovery Tool
=======================================

Utilize a passive discovery tool to identify devices connected to the organization’s network and automatically update the organization’s hardware asset inventory.

.. list-table::
	:header-rows: 1

	* - Asset Type 
	  - Security Function
	  - Implementation Groups
	* - Devices
	  - Identify
	  - 3

Status
------
Draft

Dependencies
------------
* Subcontrol 12.1: Maintain an Inventory of Network Boundaries

Inputs
------
#. The list of the organization's networks
#. The list of passive asset discovery tools in use by the organization. For each, include the location of the tool's configuration information and which networks it covers.
#. Approved configuration(s) for each passive asset discovery tool. Configurations should include the settings necessary for the tool to be able to update the organization's hardware asset inventory.

Operations
----------
#. For each passive asset discovery tool provided in Input 2, check the tool's configuration against the appropriate approved configuration from Input 3.
	#. Create a list of those tools that are properly configured (M1)
	#. Create a list of those tools that are improperly configured (M2) noting the deviations from proper configuration
#. For each of the organization's networks provided in Input 1, check Input 2 and M1 to ensure that at least one properly configured passive asset discovery tool covers that network.
	#. Create a list of the organization's networks that have coverage from at least one properly configured passive asset discovery tool (M3)
	#. Create a list of the organization's networks that do not have coverage from any properly configured passive asset discovery tools (M4)

Measures
--------
* M1 = List of properly configured passive asset discovery tools (compliant tool list)
* M2 = List of improperly configured passive asset discovery tools (non-compliant tool list)
* M3 = List of organization's networks with coverage from at least one properly configured passive asset discovery tool (compliant network list)
* M4 = List of organization's networks that do not have coverage from any properly configured passive asset discovery tool (non-compliant network list)
* M5 = Count of networks with coverage from at least one properly configured passive asset discovery tool (count of M3)
* M6 = Total count of the organization's networks (count of Input 1)

Metrics
-------

Coverage
^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The ratio of the organization's networks with coverage from at least one properly 
	    | configured passive asset discovery tool to the total number of networks
	* - **Calculation**
	  - :code:`M5 / M6`

.. history
.. authors
.. license