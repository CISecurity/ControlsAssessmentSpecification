11.5: Manage Network Devices Using Multi-Factor Authentication and Encrypted Sessions
=========================================================
Manage all network devices using multi-factor authentication and encrypted sessions.

.. list-table::
	:header-rows: 1

	* - Asset Type
	  - Security Function
	  - Implementation Groups
	* - Network
	  - Protect
	  - 2, 3

Status
------
Draft

Dependencies
------------
* Sub-control 1.4: Maintain Detailed Asset Inventory
* Sub-control 1.5: Maintain Asset Inventory Information

Inputs
------
#. Network device inventory
#. Network device configuration policy

Assumption
^^^^^^^^^^
* The network device configuration policy (Input 2) details the use of multi-factor authentication and use of encrypted sessions

Operations
----------
#. For each network device, compare its running configuration to the device's configuration policy for use of multi-factor authentication
#. For each network device, compare its running configuration to the device's configuration policy for use of encrypted sessions

Measures
--------
* M1 = Count of network devices
* M2(i) = (For each network device "i") 1 if the network device's running configuration matches the configuration policy for use of multi-factor authentication (Operation 1); 0 otherwise
* M3(i) = (For each network device "i") 1 if the network device's running configuration matches the configuration policy for use of encrypted sessions (Operation 1); 0 otherwise 

Metrics
-------

Multi-Factor Coverage
^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The ratio of network devices properly configured for multi-factor authentication to the total number of network devices.
	* - **Calculation**
	  - :code:`(SUM from i=1..M1 (M2(i))) / M1`

Encrypted Session Coverage
^^^^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The ratio of network devices properly configured for use of encrypted sessions to the total number of network devices.
	* - **Calculation**
	  - :code:`(SUM from i=1..M1 (M3(i))) / M1`

.. history
.. authors
.. license
