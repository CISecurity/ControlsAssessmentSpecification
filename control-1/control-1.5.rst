1.5: Use a Passive Asset Discovery Tool
=========================================================
Use a passive discovery tool to identify assets connected to the enterprise’s network. Review and use scans to update the enterprise’s asset inventory at least weekly, or more frequently.

.. list-table::
	:header-rows: 1

	* - Asset Type
	  - Security Function
	  - Implementation Groups
	* - Devices
	  - Detect
	  - 3

Dependencies
------------
* Safeguard 4.2: Establish and Maintain a Secure Configuration Process for Network Infrastructure
* Safeguard 12.4: Establish and Maintain Architecture Diagram(s)

Inputs
-----------
#. :code:`GV4`: List of the enterprise’s networks
#. List of passive asset discovery tools in use by the organization. For each, include the location of the tool's configuration information and which networks it covers.
#. :code:`GV3`: Approved configuration(s) for each passive asset discovery tool. Configurations should include the settings necessary for the tool to be able to update the enterprise's asset inventory

Operations
----------
#. Identify approved configuratons for passive asset discovery tools using :code:`GV3`
#. For each passive asset discovery tool provided in Input 2, check the tool's configuration against the appropriate approved configuration from :code:`GV3`
	#. Enumerate those tools that are properly configured (M1)
	#. Enumerate those tools that are improperly configured (M2) noting the deviations from proper configuration
#. For each of the enterprise's networks provided in Input 1, check to see if at least one properly configured passive asset discovery tool from M1 covers that network.
	#. Create a list of the organization's networks that have coverage from at least one properly configured passive asset discovery tool (M3)
	#. Create a list of the organization's networks that do not have coverage from any properly configured passive asset discovery tools (M4)

Measures
--------
* M1 = Count of properly configured passive asset discovery tools
* M2 = Count of improperly configured passive asset discovery tools
* M3 = Count of organization's networks that are covered by properly configured passive discovery tools
* M4 = Count of organization's networks that are not covered by properly configured passive discovery tools
* M5 = :code:`GV4`

Metrics
-------

Coverage
^^^^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The ratio of the organization's networks with coverage from at least one properly
	    | configured passive asset discovery tool to the total number of networks
	* - **Calculation**
	  - :code:`M3 / M5`


.. history
.. authors
.. license
