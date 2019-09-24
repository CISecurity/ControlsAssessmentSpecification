15.4: Disable Wireless Access on Devices if Not Required
=========================================================
Disable wireless access on devices that do not have a business purpose for wireless access.

.. list-table::
	:header-rows: 1

	* - Asset Type 
	  - Security Function
	  - Implementation Groups
	* - Devices
	  - Protect
	  - 3

Status
------
Draft

Dependencies
------------
* Subcontrol 1.4: Maintain Detailed Asset Inventory
* Subcontrol 1.5: Maintain Asset Inventory Information

Inputs
-----------
#. The list of endpoints

Operations
----------
#. Enumerate all wireless-access-capable endpoints
#. For each identified endpoint:
	#. Determine whether the device has an identified business purpose for wireless access
	#. Examine the endpoint's configuration to determine whether wireless access is enabled
#. Enumerate all endpoints with wireless access enabled and without an identified business purpose for wireless access
#. Enumerate all endpoints without wireless access enabled and without an identified business purpose for wireless access
#. Enumerate all endpoints with wireless access enabled and with an identified business purpose for wireless access

Measures
--------
* M1 = List of all wireless-access-capable endpoints
* M2 = List of endpoints with wireless access enabled and without an identified business purpose for wireless access
* M3 = List of endpoints without wireless access enabled and without an identified business purpose
* M4 = List of endpoints with wireless access enabled and with an identified business purpose for wireless access
* M5 = The number of wireless-access-capable endpoints (count of M1)
* M6 = The number of endpoints with wireless access enabled and without an identified business purpose for wireless access (count of M2)
* M7 = The number of endpoints without wireless access enabled and without an identified business purpose (count of M3)
* M8 = The number of endpoints with wireless access enabled and with an identified business purpose for wireless access (count of M4)
* M9 = M7 + M8

Metrics
-------

Coverage
^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The ratio of appropriately configured wireless-access-capable endpoints to the total
	    | number of wireless-access-capable endpoints
	* - **Calculation**
	  - :code:`M9 / M5`

.. history
.. authors
.. license