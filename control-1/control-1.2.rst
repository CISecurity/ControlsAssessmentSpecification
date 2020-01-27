.. include:: ../.variable-lookup.rst

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

Dependencies
------------
* Sub-control 12.1: Maintain an Inventory of Network Boundaries

Inputs
------
#. :code:`GV4`: Organizational Networks
#. The list of passive asset discovery tools in use by the organization. For each, include the location of the tool's configuration information and which networks it covers. May be derived from :code:`GV3`, Asset Discovery Tools
#. Approved configuration(s) for each passive asset discovery tool. Configurations should include the settings necessary for the tool to be able to update the organization's hardware asset inventory. May be derived from :code:`GV8`, Approved Security Configurations.
#. :code:`GV67`: Count of Organizational Networks

Operations
----------
#. For each passive asset discovery tool provided in Input 2, check the tool's configuration against the appropriate approved configuration from Input 3.
	#. Create a list of those tools that are properly configured (becomes M1)
	#. Create a list of those tools that are improperly configured (becomes M2) noting the deviations from proper configuration
#. For each of the organization's networks provided by Input 4 (:code:`GV4`) check Input 2 and M1 to ensure that at least one properly configured passive asset discovery tool covers that network.
	#. Create a list of the organization's networks that have coverage from at least one properly configured passive asset discovery tool (becomes M3)
	#. Create a list of the organization's networks that do not have coverage from any properly configured passive asset discovery tools (becomes M4)

Measures
--------
* M1 = List of properly configured passive asset discovery tools (compliant tool list)
* M2 = List of improperly configured passive asset discovery tools (non-compliant tool list)
* M3 = List of organization's networks with coverage from at least one properly configured passive asset discovery tool (compliant network list)
* M4 = List of organization's networks that do not have coverage from any properly configured passive asset discovery tool (non-compliant network list)
* M5 = Count of networks with coverage from at least one properly configured passive asset discovery tool (count of M3)

Metrics
-------

Coverage
^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The ratio of the organization's networks with coverage from at least one properly
	    | configured passive asset discovery tool to the total number of networks
	* - **Calculation**
	  - :code:`M5 / GV67`

.. history
.. authors
.. license
