13.7: Manage USB Devices
=========================================================
If USB storage devices are required, enterprise software should be used that can configure systems to allow the use of specific devices.  An inventory of such devices should be maintained.

.. list-table::
	:header-rows: 1

	* - Asset Type
	  - Security Function
	  - Implementation Groups
	* - Data
	  - Protect
	  - 2, 3

Dependencies
------------
* Sub-control 1.4: Maintain Detailed Asset Inventory
* Sub-control 1.5: Maintain Asset Inventory Information
* Sub-control 2.1: Maintain Inventory of Authorized Software
* Sub-control 2.5: Integrate Software and Hardware Asset Inventories

Inputs
-----------
#. The list of endpoints
#. The list of authorized USB storage devices
#. Enterprise software which can configure systems to allow the use of specific devices

Operations
----------
#. For each endpoint "i", determine if the software specified by Input 3 is installed (M2(i))
#. For each endpoint "i", collect the whitelist of USB devices allowed for use (M3(i))
#. For each endpoint's whitelist, calculate the intersection with the authorized USB device inventory from Input 2. The "right-side" of the calculation indicates USB devices on the endpoint's whitelist which are not contained in the authorized USB device inventory.

Measures
--------
* M1 = Count of endpoints
* M2(i) = (For each endpoint "i") 1 if Operation 1 indicates the appropriate software is installed on device "i"; 0 otherwise
* M3 = (For each endpoint) The number of USB devices allowed
* M4 = (For each endpoint) The number of USB devices contained in the whitelist which are not in the authorized USB device inventory
* M5(i) = (For each endpoint "i") 1 if M4 > 0 for device "i"; 0 otherwise

Metrics
-------

Whitelisting Software Coverage
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The ratio of endpoints with whitelisting software installed to the total number
	    | of endpoints.
	* - **Calculation**
	  - :code:`(SUM from i=1..M1 (M2(i))) / M1`

Non-Inventoried but Whitelisted
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The ratio of endpoints with non-inventories but whitelisted USB device allowance
	    | to the total number of endpoints.
	* - **Calculation**
	  - :code:`(SUM from i=1..M1 (M5(i))) / M1`

Full Coverage
^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The ratio of endpoints with inventoried USB storage device capability and USB
	    | whitelisting software installed to the total number of endpoints.
	* - **Calculation**
	  - :code:`(SUM from i=1..M1 (M2(i) * M5(i))) / M1`

.. history
.. authors
.. license
