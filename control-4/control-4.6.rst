4.6: Use Dedicated Workstations For All Administrative Tasks
============================================================
Ensure administrators use a dedicated machine for all administrative tasks or tasks requiring administrative access. This machine will be segmented from the organization’s primary network and not be allowed Internet access.  This machine will not be used for reading email, composing documents, or browsing the Internet.

.. list-table::
	:header-rows: 1

	* - Asset Type
	  - Security Function
	  - Implementation Groups
	* - Users
	  - Protect
	  - 3

Status
------
Draft

Dependencies
------------
* Sub-control 1.4: Maintain Detailed Asset Inventory
* Sub-control 1.5: Maintain Asset Inventory Information
* Sub-control 2.1: Maintain Inventory of Authorized Software
* Sub-control 2.5: Integrate Software and Hardware Asset Inventories

Inputs
-----------
#. The list of endpoints
#. The list of authorized software

Operations
----------
#. Enumerate the devices used for administrative purposes based on the endpoint inventory
#. Enumerate all software identified as administrative from the software inventory
#. For each identified device:
	#. Enumerate the devices configured/managed by this device
	#. Examine its configuration noting whether it is appropriately or inappropriately configured:
		#. The device has internet access
		#. The device can run unauthorized software
		#. The device can be reached by any device not in the enumeration identified above

Measures
--------
* M1 = List of devices used for administrative purposes
* M2 = List of administrative software
* M3 = List of appropriately configured devices
* M4 = List of inappropriately configured devices
* M5 = Count of devices used for administrative purposes (count of M1)
* M6 = Count of administrative software (count of M2)
* M7 = Count of appropriately configured devices (count of M3)
* M8 = Count of inappropriately configured devices (count of M4)

Metrics
-------

Coverage
^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The ratio of appropriately configured administrative devices to the total number of
	    | administrative devices
	* - **Calculation**
	  - :code:`M7 / M5`

.. history
.. authors
.. license
