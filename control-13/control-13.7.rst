13.7: Deploy a Host-Based Intrusion Prevention Solution
=========================================================
Deploy a host-based intrusion prevention solution on enterprise assets, where appropriate and/or supported. Example implementations include use of an Endpoint Detection and Response (EDR) client or host-based IPS agent.

.. list-table::
	:header-rows: 1

	* - Asset Type
	  - Security Function
	  - Implementation Groups
	* - Devices
	  - Protect
	  - 3

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
#. Use :code:`GV1` to identify and enumerate assets capable of supporting host based intrusion prevention systems (M1)
#. Use: code:`GV5` to identify authorized host based intrusion prevention software
#. For each asset identified in Operation 1 check if it is covered by at least one authorized host based intrusion prevention software
	#. Identify and enumerate assets with host based intrusion prevention software installed (M2)
	#. Identify and enumerate assets without host based intrusion prevention software installed (M3)

Measures
--------
* M1 = Count of enterprise assets capable of supporting host based intrusion prevention systems
* M2 = Count of assets with host based intrusion prevention systems
* M3 = Count of assets without host based intrusion prevention systems

Metrics
-------

Coverage
^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The percentage of assets capable of supporting host based intrusion prevention systems 
	  - | with host based intrusion detection software installed
	* - **Calculation**
	  - :code:`M2 / M1`

.. history
.. authors
.. license
