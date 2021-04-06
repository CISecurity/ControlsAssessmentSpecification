13.2: Deploy a Host-Based Intrusion Detection Solution
=============================================================================
Deploy a host-based intrusion detection solution on enterprise assets, where appropriate and/or supported.

.. list-table::
	:header-rows: 1

	* - Asset Type
	  - Security Function
	  - Implementation Groups
	* - Devices
	  - Detect
	  - 2, 3

Dependencies
------------
* Safeguard 1.1: Establish and Maintain Detailed Enterprise Asset Inventory
* Safeguard 2.1: Establish and Maintain a Software Inventory

Inputs
-----------
#. :code:`GV1`: Enterprise asset inventory
#. :code:`GV5`: Authorized software inventory

Operations
----------
#. Use :code:`GV1` to identify and enumerate assets capable of supporting host based intrusion detection systems (M1)
#. Use: code:`GV5` to identify authorized host based intrusion detection software
#. For each asset identified in Operation 1 check if it is covered by at least one authorized host based intrusion detection software
	#. Identify and enumerate assets with host based intrusion detection software installed (M2)
	#. Identify and enumerate assets without host based intrusion detection software installed (M3)

Measures
--------
* M1 = Count of enterprise assets capable of supporting host based intrusion detection systems
* M2 = Count of assets with host based intrusion detection systems
* M3 = Count of assets without host based intrusion detection systems

Metrics
-------

Coverage
^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The percentage of assets capable of supporting host based intrusion detection systems 
	  - | with host based intrusion detection software installed
	* - **Calculation**
	  - :code:`M2 / M1`

.. history
.. authors
.. license
