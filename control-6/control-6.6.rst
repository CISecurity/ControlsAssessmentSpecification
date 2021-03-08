6.6: Establish and Maintain an Inventory of Authentication and Authorization Systems
=========================================================
Establish and maintain an inventory of the enterprise’s authentication and authorization systems, including those hosted on-site or at a remote service provider. Review and update the inventory, at a minimum, annually, or more frequently.

.. list-table::
	:header-rows: 1

	* - Asset Type
	  - Security Function
	  - Implementation Groups
	* - Users
	  - Identify
	  - 2, 3

Dependencies
------------
* Safeguard 1.1: Establish and Maintain Detailed Enterprise Asset Inventory
* Safeguard 2.1: Establish and Maintain a Software Inventory

Inputs
------
#. :code:`GV23`: Authentication and Authorization System Inventory
#. :code:`GV5`: Authorized software inventory
#. Date of last update to the authentication and authorization system inventory

Operations
----------
#. Check if enterprise maintains an :code:`GV23` Authentication and Authorization System Inventory of all on-site and remote service providers
	#. If the inventory exists, M1 = 1
	#. If the inventory does not exist or is not provided, M1 = 0
#. Use :code:`GV5` identify and enumerate authorized authentication and authorization systems within the enterprise 
#. Use the output of Operation 2 to compare to the existing inventory :code:`GV23`
	#. Identify and enumerate systems that are authorized and currently in the inventory (M2)
	#. Identify and enumerate systems that are authorized and not currently in the inventory (M3)
	#. Identify and enumarate systems that are not authorized but listed in the current inventory (M4)
#. Compare the date of Input 3 to the current date and capture timeframe in months (M6)

Measures
--------
* M1 = Ouptut of Operation 1
* M2 = Count of authorized and properly inventoried systems 
* M3 = Count of authorized but not properly inventoried systems
* M4 = Count of unauthorized but inventoried systems
* M5 = Count of systems in the current inventory :code:`GV23`
* M6 = Timeframe since last update of inventory

Metrics
-------
* If M1 is 0, this safeguard receives a failing score. The other metrics don't apply.
* If M6 is greater than twelve months, then this safeguard is measured at a 0 and receives a failing score. The other metrics don't apply.

Accuracy Score
^^^^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | What percentage of the authorized authentication and authorization systems
	  - | are accounted for in the current enterprise inventory?
	* - **Calculation**
	  - :code:`M2 / M5`

	* - **Metric**
	  - | What percentage of unauthorized authentication and authorization systems
	  - | are accounted for in the current enterprise inventory?
	* - **Calculation**
	  - :code:`M4 / M5`

.. history
.. authors
.. license
