9.2: Ensure Only Approved Ports, Protocols, and Services Are Running
====================================================================
Ensure that only network ports, protocols, and services listening on a system with validated business needs are running on each system.

.. list-table::
	:header-rows: 1

	* - Asset Type
	  - Security Function
	  - Implementation Groups
	* - Devices
	  - Protect
	  - 2, 3

Status
------
Draft

Dependencies
------------
* Sub-control 1.4: Maintain Detailed Asset Inventory
* Sub-control 1.5: Maintain Asset Inventory Information

Inputs
------
#. List of authorized ports with validated business need
#. List of authorized protocols with validated business need
#. List of authorized services with validated business need
#. List of endpoints

Operations
----------
#. For each endpoint perform the following to build sets of information:
	#. Scan for open ports
	#. For each open port
		#. Test protocol running on that port
	#. Enumerate installed services
#. Enumerate discovered ports
#. Enumerate discovered services
#. Determine set of unauthorized ports
#. Determine set of unauthorized services

Measures
--------
* M1 = Set of open ports
* M2 = Set of unauthorized ports
* M3 = Set of discovered services
* M4 = Set of unauthorized services
* M5 = Set of unexpected protocols discovered on open ports

Metrics
-------

Ports
^^^^^
.. list-table::

	* - **Metric**
	  - | Ratio of unauthorized ports to open ports
	* - **Calculation**
	  - :code:`M2 / M1`

Services
^^^^^^^^
.. list-table::

	* - **Metric**
	  - | Ratio of unauthorized services to discovered services
	* - **Calculation**
	  - :code:`M4 / M3`

Unexpected Protocols
^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | Ratio of unexpected protocols discovered on open ports to total number of open ports
	* - **Calculation**
	  - :code:`M5 / M1`

.. history
.. authors
.. license
