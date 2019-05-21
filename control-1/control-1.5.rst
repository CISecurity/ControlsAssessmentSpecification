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
* We need to define what "weight" is in this context
* Calculation below indicates SUM from i to M.  What is "M" in this context?

Measures
--------
* w_i = weight of machine i
* a_i = detailed (1) or not detailed (0); "detailed" if and only if all specified information is there.
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
	  - 
	* - **Calculation**
	  - :code:`(SUM from i to M (w_i * a_i)) / M1`

.. history
.. authors
.. license