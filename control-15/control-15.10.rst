15.10: Create Separate Wireless Network for Personal and Untrusted Devices
==========================================================================
Create a separate wireless network for personal or untrusted devices. Enterprise access from this network should be treated as untrusted and filtered and audited accordingly.

.. list-table::
	:header-rows: 1

	* - Asset Type
	  - Security Function
	  - Implementation Groups
	* - Network
	  - Protect
	  - 1, 2, 3

Dependencies
------------
* Sub-control 1.4: Maintain Detailed Asset Inventory
* Sub-control 1.5: Maintain Asset Inventory Information

Inputs
-----------
#. Isolated wireless network SSID(s)
#. List of corporate wireless network SSID(s)

Operations
----------
#. For each corporate wireless network SSID, attempt to connect non-corporate device (M2)
#. Determine access policy for other wireless network

Measures
--------
* M1 = 1 if the separate wireless network exists for personal/non-corporate devices; 0 otherwise.
* M2 = List of corporate wireless network SSID(s) accepting non-corporate devices
* M3 = Count of M2
* M4 = List of corporate wireless network SSID(s)
* M5 = Count of M4

Metrics
-------

Logical Isolation
^^^^^^^^^^^^^^^^^
The overall measure fails if there is no separate network for personal/non-corporate devices (M1 = 0)

Coverage
^^^^^^^^
.. list-table::

	* - **Metric**
	  - What percentage of the total number of wireless networks exist but are misconfigured?
	* - **Calculation**
	  - :code:`M3 / M5`

.. history
.. authors
.. license
