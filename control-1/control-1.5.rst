.. include:: ../.variable-lookup.rst

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

Dependencies
------------
* Sub-control 1.4: Maintain Detailed Asset Inventory

Inputs
-----------
#. |GV1-label|: |GV1-name|
#. :code:`GV2`: Count of Hardware Asset Inventory

Operations
----------
#. For each endpoint represented in the hardware asset inventory (Input 1 (:code:`GV1`)), identify detailed information, such as:
	* Network Address
	* Hardware Address (applies to virtual endpoints)
	* Machine name
	* Data asset owner
	* Assigned department
#. Identify endpoints with all detailed information identified (from Operation 1)
#. For each endpoint, identify network connection approval (from Input 1 (:code:`GV1`))

Measures
--------
* M1 = List of endpoints with all detailed information
* M2 = Count of endpoints with all detailed information
* M3 = List of endpoints with network connection approval
* M4 = Count of endpoints with network connection approval

Metrics
-------

Endpoint Inventory Quality
^^^^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The ratio of endpoints with all detailed information to the total number of inventoried
	    | endpoints
	* - **Calculation**
	  - :code:`M2 / GV2`

Endpoint Inventory Authorization Quality
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The ratio of endpoints with approval to connect to the network
	* - **Calculation**
	  - :code:`M4 / GV2`

.. history
.. authors
.. license
