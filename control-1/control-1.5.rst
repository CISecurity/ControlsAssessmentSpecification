1.5: Maintain Asset Inventory Information
=========================================================
Ensure that the hardware asset inventory records the network address, hardware address, machine name, data asset owner, and department for each asset and whether the hardware asset has been approved to connect to the network.

.. list-table::
	:header-rows: 1

	* - Asset Type
	  - Security Function
	  - Implementation Groups
	* - Devices
	  - Identify
	  - 2, 3

Status
------
Draft

Dependencies
------------
* Sub-control 1.4: Maintain Detailed Asset Inventory

Inputs
-----------
#. Detailed endpoint inventory

Operations
----------
#. For each endpoint, identify detailed information, such as:
	* Network Address
	* Hardware Address (applies to virtual endpoints)
	* Machine name
	* Data asset owner
	* Assigned department
#. Identify endpoints with all detailed information identified
#. For each endpoint, identify network connection approval

Measures
--------
* M1 = List of endpoints in inventory
* M2 = Count of M1
* M3 = List of endpoints with network connection approval
* M4 = Count of M3
* M5 = List of endpoints with all detailed information
* M6 = Count of M5

Metrics
-------

Endpoint Inventory Quality
^^^^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The ratio of endpoints with all detailed information to the total number of inventoried
	    | endpoints
	* - **Calculation**
	  - :code:`M6 / M2`

Endpoint Inventory Authorization Quality
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The ratio of endpoints with approval to connect to the network
	* - **Calculation**
	  - :code:`M4 / M2`

.. history
.. authors
.. license
