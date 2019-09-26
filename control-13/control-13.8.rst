13.8: Manage System’s External Removable Media’s Read/Write Configurations
==========================================================================
Configure systems not to write data to external removable media, if there is no business need for supporting such devices.

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

Operations
----------
#. Enumerate all endpoints supporting external removable media
#. Enumerate all endpoints with a business need to support external removable media
#. Enumerate all endpoints without a business need to support external removable media
#. For each endpoint without a business need to support external removable media, examine its external media configuration, noting whether it is appropriately or inappropriately configured
#. Enumerate the inappropriately configured endpoints
#. Enumerate the appropriately configured endpoints

Measures
--------
* M1 = List of all endpoints supporting external removable media
* M2 = List of all endpoints with a business need to support external removable media
* M3 = List of all endpoints without a business need to support external removable media
* M4 = List of appropriately configured endpoints without a need to support external removable media
* M5 = List of inappropriately configured endpoints without a need to support external removable media
* M6 = Count of endpoints supporting external removable media (count of M1)
* M7 = Count of endpoints with a business need to support external removable media (count of M2)
* M8 = Count of endpoints without a business need to support external removable media (count of M3)
* M9 = Count of appropriately configured endpoints without a need to support external removable media (count of M4)
* M10 = Count of inappropriately configured endpoints without a need to support external removable media (count of M5)

Metrics
-------

Coverage
^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The ratio of appropriately configured endpoints to the total number of endpoints without
	    | a business need to support external removable media
	* - **Calculation**
	  - :code:`M9 / M8`

.. history
.. authors
.. license
