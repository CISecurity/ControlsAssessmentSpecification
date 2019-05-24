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

Assumptions
-----------
* The "weight" indicates the criticality (importance) of an endpoint, and will be defined by the organization

Measures
--------
* w(i) = weight of machine i
* a(i) = detailed (1) or not detailed (0); "detailed" if and only if all specified information is there.
* M1 = # of devices and machines in asset inventory
* M2 = # of device or machine with connection approval

Metrics
-------

Asset Inventory Quality
^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Question**
	  - 
	* - **Answer**
	  - Percentage of assets that are tracked in the asset inventory which contain detailed information, such as network address, hardware address, asset owner, etc.
	* - **Calculation**
	  - :code:`(SUM from i to M1 (w(i) * a(i))) / M1`

Asset Inventory Precision
^^^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Question**
	  - 
	* - **Answer**
	  - Percentage of devices with connection approval that are currently tracked in the asset inventory
	* - **Calculation**
	  - :code:`(M2 / M1) * 100`

.. history
.. authors
.. license