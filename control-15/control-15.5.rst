15.5: Limit Wireless Access on Client Devices
=========================================================
Configure wireless access on client machines that do have an essential wireless business purpose, to allow access only to authorized wireless networks and to restrict access to other wireless networks.

.. list-table::
	:header-rows: 1

	* - Asset Type
	  - Security Function
	  - Implementation Groups
	* - Devices
	  - Protect
	  - 3

Dependencies
------------
* Sub-control 1.4: Maintain Detailed Asset Inventory
* Sub-control 1.5: Maintain Asset Inventory Information

Inputs
-----------
#. The list of endpoints
#. The list of authorized wireless networks

Operations
----------
#. Enumerate wireless-client-capable endpoints
#. Enumerate authorized wireless networks
#. For each identified endpoint:
	#. Determine whether the endpoint is identified as having a business purpose for wireless access
	#. Examine the endpoint's configuration as follows:
		#. Access is only allowed to authorized wireless networks
		#. Access to any other wireless network is restricted
#. Enumerate all endpoints having a business purpose for wireless access
#. Enumerate all appropriately configured endpoints
#. Enumerate all inappropriately configured endpoints

Measures
--------
* M1 = List of wireless-client-capable endpoints
* M2 = List of authorized wireless networks
* M3 = List of endpoints authorized for wireless access
* M4 = List of appropriately configured endpoints
* M5 = List of inappropriately configured endpoints
* M6 = Count of wireless-client-capable endpoints (count of M1)
* M7 = Count of authorized wireless networks (count of M2)
* M8 = Count of endpoints authorized for wireless access (count of M3)
* M9 = Count of appropriately configured endpoints (count of M4)
* M10 = Count of inappropriately configured endpoints (count of M5)

Metrics
-------

Configuration Coverage
^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The ratio of appropriately configured endpoints to the total number of authorized
	    | wireless-client-capable endpoints
	* - **Calculation**
	  - :code:`M9 / M8`

Authorization Coverage
^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The ratio of authorized wireless-client-capable endpoints to the total number of
	    | wireless-client-capable endpoints
	* - **Calculation**
	  - :code:`M8 / M6`
.. history
.. authors
.. license
