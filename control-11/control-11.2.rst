11.2: Document Traffic Configuration Rules
=========================================================
All configuration rules that allow traffic to flow through network devices should be documented in a configuration management system with a specific business reason for each rule, a specific individual’s name responsible for that business need, and an expected duration of the need

.. list-table::
	:header-rows: 1

	* - Asset Type 
	  - Security Function
	  - Implementation Groups
	* - Network
	  - Identify
	  - 2, 3

Status
------
Draft

Dependencies
------------
* Subcontrol 1.4: Maintain Detailed Asset Inventory
* Subcontrol 1.5: Maintain Asset Inventory Information

Inputs
------
#. The list of traffic flow configurations for network devices. (M5)
#. The inventory of configuration rules pertaining to traffic flow through network devices. (M4)

Operations
----------
#. Perform a set calculation, computing the Intersection (M1) of Input 1 and Input 2
#. Examine the inventory of configuration rules to manually determine those traffic flow rules which do not contain complete information (such as names, business needs, etc) (M6)

Measures
--------
* M1 = The intersection of Input 1 and Input 2.  This intersection measures which of the inventoried configuration rules are contained in the enterprise's security configuration standards.
* M2 = The "left" side of the set calculation measures the traffic flow configuration which are not documented in the inventory.
* M3 = The "right" side of the set calculation measures any configuration rules in the inventory which are not currently configured on the network device.
* M4 = The number of traffic flow configuration rules in the inventory.
* M5 = The current traffic flow configuration for the network device
* M6 = The number of traffic flow rules in the inventory that are incomplete

Metrics
-------

* If M2 > 0 then there are traffic flows configured on the device which are not documented in the inventory.
* If M3 > 0, there are configuration items in the inventory no longer configured in the device's configuration.

Coverage
^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The ratio of undocumented traffic flow configurations to the current total traffic 
	    | flow configurations
	* - **Calculation**
	  - :code:`M2 / M5`

Completeness
^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The ratio of inventoried but incomplete traffic flow rules to the total set of traffic
	    | flow rules.
	* - **Calculation**
	  - :code:`M6 / M4`

.. history
.. authors
.. license