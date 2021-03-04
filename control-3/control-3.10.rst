3.10: Encrypt Sensitive Data in Transit
==================================
Encrypt sensitive data in transit. Example implementations can include, Transport Layer Security (TLS) and Open Secure Shell (OpenSSH).

.. list-table::
	:header-rows: 1

	* - Asset Type
	  - Security Function
	  - Implementation Groups
	* - Data
	  - Protect
	  - 2, 3

Dependencies
------------
* Safeguard 3.2: Establish and Maintain a Data Inventory
* Safeguard 4.1: Establish and Maintain a Secure Configuration Process

Inputs
------
#. :code:`GV12`: Sensitive data Inventory
#. :code:`GV5`: Configuration Information

Operations
----------
#. For each item in :code:`GV12`, identify the means and components for encrypting data in transit.
#. Compare the output of Operation 1 with :code:`GV5` to check appropriate approved configurations
	#. Enumerate the data items in :code:`GV12` that are properly configured (M2)
	#. Enumerate the data items in :code:`GV12` that are improperly configured (M3)

Measures
--------
* M1 = Count of items in :code:`GV12` 
* M2 = Count of data with properly configured encryption components
* M3 = Count of data with improperly configured encryption components

Metrics
-------

Coverage
^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The percentage of sensitive data properly configured to be encrypted in
	  - | transit.
	* - **Calculation**
	  - :code:`M2 / M1`


.. history
.. authors
.. license
