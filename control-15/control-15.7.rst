15.7: Leverage the Advanced Encryption Standard (AES) to Encrypt Wireless Data
==============================================================================
Leverage the Advanced Encryption Standard (AES) to encrypt wireless data in transit.

.. list-table::
	:header-rows: 1

	* - Asset Type
	  - Security Function
	  - Implementation Groups
	* - Network
	  - Protect
	  - 1, 2, 3

Status
------
Draft

Dependencies
------------
* Sub-control 1.4: Maintain Detailed Asset Inventory
* Sub-control 1.5: Maintain Asset Inventory Information

Inputs
-----------
#. List of wireless devices (derived from Endpoint Inventory; sub-control 1.4)
#. List of AES-capable wireless devices (sub-control 1.5)

Operations
----------
#. For each AES-capable wireless device, collect cipher suite configuration

Measures
--------
* M1 = List of wireless devices
* M2 = Count of wireless devices
* M3 = List of AES-capable wireless devices
* M4 = Count of AES-capable wireless devices
* M5 = List of non-AES-capable wireless devices
* M6 = Count of non-AES-capable wireless devices
* M7 = List of appropriately configured AES-capable wireless devices
* M8 = Count of appropriately configured AES-capable wireless devices
* M9 = List of inappropriately configured AES-capable wireless devices
* M10 = Count of inappropriately configured AES-capable wireless devices

Metrics
-------

Coverage
^^^^^^^^
.. list-table::

	* - **Metric**
	  - What percentage of AES-capable devices are configured to use cipher suites leveraging AES?
	* - **Calculation**
	  - :code:`M8 / M4`

.. history
.. authors
.. license
