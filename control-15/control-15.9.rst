15.9: Disable Wireless Peripheral Access to Devices
=========================================================
Disable wireless peripheral access of devices [such as Bluetooth and Near Field Communication (NFC)], unless such access is required for a business purpose.

.. list-table::
	:header-rows: 1

	* - Asset Type 
	  - Security Function
	  - Implementation Groups
	* - Devices
	  - Protect
	  - 2, 3

Status
------
Draft

Dependencies
------------
* Subcontrol 1.4: Maintain Detailed Asset Inventory
* Subcontrol 1.5: Maintain Asset Inventory Information

Inputs
-----------
#. The list of devices capable of wireless peripheral access including Bluetooth and NFC (subset of hardware inventory)
#. Approved configuration(s) to disable wireless peripheral access
#. The list of devices with an approved business purpose to have wireless peripheral access enabled, along with which form(s) of wireless peripheral access are approved (Bluetooth, NFC, etc.)

Operations
----------
#. For each device in Input 1, check to see if that device adheres to the appropriate configuration(s) from Input 2 to disable wireless peripheral access, excluding any form(s) of wireless peripheral access that the device is approved to have enabled according to Input 3.
#. Create a list of devices that are properly configured (M1)
#. Create a list of devices that are not properly configured (M2) noting the deviations from approved configuration.

Measures
--------
* M1 = List of devices that are properly configured to disable wireless peripheral access (compliant list)
* M2 = List of devices that are not properly configured to disable wireless peripheral access (non-compliant list)
* M3 = Count of devices that are properly configured to disable wireless peripheral access (count of M1)
* M4 = Total count of devices capable of wireless peripheral access including Bluetooth and NFC (count of Input 1)

Metrics
-------

Coverage
^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The ratio of devices properly configured to disable wireless peripheral access
	* - **Calculation**
	  - :code:`M3 / M4`

.. history
.. authors
.. license