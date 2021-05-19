3.6: Encrypt Data on End-User Devices
=============================================
Encrypt data on end-user devices containing sensitive data. Example implementations can include, Windows BitLocker®, Apple FileVault®, Linux® dm-crypt.

.. list-table::
	:header-rows: 1

	* - Asset Type
	  - Security Function
	  - Implementation Groups
	* - Devices
	  - Protect
	  - 1, 2, 3

Dependencies
------------
* Safeguard 1.1: Establish and Maintain Detailed Enterprise Asset Inventory
* Safeguard 2.1: Establish and Maintain a Software Inventory
* Safeguard 4.1: Establish and Maintain a Secure Configuration Process

Inputs
------
#. :code:`GV1`: Enterprise asset inventory
#. :code:`GV5`: Authorized software inventory
#. :code:`GV3`: Configuration Standards

Operations
----------
#. For each asset in :code:`GV1`, identify end-user devices 
	#. Enumerate the end-user devices (M1)
	#. Use :code:`GV5` to identify and enumerate the assets that have encryption software installed (M2)
	#. Use :code:`GV5` to identify and enumerate the assets without encryption software (M3)
#. For each encryption software installed on assets (M2), use :code:`GV3` to determine whether the software is properly configured
	#. Enumerate the encryption software that is properly configured (M4)
	#. Enumerate the encryption software that is improperly configured (M5)

Measures
--------
* M1 = Count of approved end-user devices
* M2 = Count of approved end-user devices with encryption software installed
* M3 = Count of approved end-user devices without encryption software
* M4 = Count of properly configured end-user devices
* M5 = Count of improperly configured end-user devices


Metrics
-------

Installed Software Coverage
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The percentage of approved mobile devices that are equipped with approved encryption
	  - | software.
	* - **Calculation**
	  - :code:`M2 / M1`

Appropriately Configured Devices
^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The percentage of approved mobile devices equipped with approved encryption software
	  - | that meet or exceed the approved configuration policy.
	* - **Calculation**
	  - :code:`M3 / M1`

.. history
.. authors
.. license
