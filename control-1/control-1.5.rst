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
* M1 = Count of endpoints in inventory
* M2 = Count of endpoints with network connection approval
* M3 = Count of endpoints with all detailed information

Metrics
-------

Endpoint Inventory Quality
^^^^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **The ratio of endpoints with all detailed information to the total number of inventoried endpoints**
	  - :code:`M3 / M1`

Endpoint Inventory Authorization Quality
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **The ratio of endpoints with approval to connect to the network**
	  - :code:`M2 / M1`

.. history
.. authors
.. license