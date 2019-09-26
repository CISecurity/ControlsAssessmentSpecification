13.9: Encrypt Data on USB Storage Devices
=========================================================
If USB storage devices are required, all data stored on such devices must be encrypted while at rest.

.. list-table::
	:header-rows: 1

	* - Asset Type
	  - Security Function
	  - Implementation Groups
	* - Data
	  - Protect
	  - 3

Dependencies
------------
* Sub-control 1.4: Maintain Detailed Asset Inventory
* Sub-control 1.5: Maintain Asset Inventory Information

Inputs
-----------
#. The list of endpoints

Assumptions
^^^^^^^^^^^
* Asset inventory includes USB storage devices.

Operations
----------
#. Enumerate all endpoints capable of supporting USB storage devices
#. For each identified endpoint
	#. Examine the endpoint's configuration to determine its USB storage device encryption configuration, noting along the way those that are appropriately and inappropriately configured

Measures
--------
* M1 = List of endpoints capable of supporting USB storage devices
* M2 = List of endpoints appropriately configured
* M3 = List of endpoints inappropriately configured
* M4 = Count of endpoints capable of supporting USB storage devices (count of M1)
* M5 = Count of endpoints appropriately configured (count of M2)
* M6 = Count of endpoints inappropriately configured (count of M3)

Metrics
-------

Coverage
^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The ratio of appropriately configured endpoints to the total number of endpoints
	    | supporting USB storage devices
	* - **Calculation**
	  - :code:`M5 / M4`

.. history
.. authors
.. license
