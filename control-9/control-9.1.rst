9.1: Associate Active Ports, Services, and Protocols to Asset Inventory
=======================================================================
Associate active ports, services, and protocols to the hardware assets in the asset inventory.

.. list-table::
	:header-rows: 1

	* - Asset Type
	  - Security Function
	  - Implementation Groups
	* - Devices
	  - Identify
	  - 2, 3

Dependencies
------------
* Sub-control 1.4: Maintain Detailed Asset Inventory
* Sub-control 1.5: Maintain Asset Inventory Information

Inputs
------
#. The list of endpoints

Operations
----------
#. For each endpoint, identify necessary detailed information
	#. Active ports
		#. Protocol Served
	#. Installed services (running or not)
#. Identify endpoints with all detailed information identified

Measures
--------
* M1 = Count of endpoints in inventory
* M2 = Count of endpoints with all detailed information
* M3 = List of endpoints with all detailed information
* M4 = List of endpoints missing at least one piece of detailed information
* M5 = Count of endpoints missing at least one piece of detailed information 

Metrics
-------

Quality
^^^^^^^
.. list-table::

	* - **Metric**
	  - | The ratio of endpoints with all detailed information to the total number of endpoints
	    | under management.
	* - **Calculation**
	  - :code:`M2 / M1`

.. history
.. authors
.. license
