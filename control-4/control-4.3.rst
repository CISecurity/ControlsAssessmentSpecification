4.3: Configure Automatic Session Locking on Enterprise Assets
=========================================================
Configure automatic session locking on enterprise assets after a defined period of inactivity. For general purpose operating systems, the period must not exceed 15 minutes. For mobile end-user devices, the period must not exceed 2 minutes.

.. list-table::
	:header-rows: 1

	* - Asset Type
	  - Security Function
	  - Implementation Groups
	* - Users
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
#. :code:`GV5`: Authorized software Inventory
#. :code:`GV3`: Configuration standard

Operations
----------
#. Identify and enumerate assets within :code:`GV1` that support automatic locking due to inactivity (M1)
#. Use :code:`GV5` to identify and enumerate assets from Operation 1 with authorized software installed (M2)
#. Check the configurations for the software using :code:`GV3` 
	#. For general computing assets, enumerate those assets with properly configured automatic locking (15 minutes or less) (M3)
	#. For general computing assets, enumerate those assets with improperly configured automatic locking (greater than 15 minutes) (M4)
	#. For mobile assets, enumerate those assets with properly configured automatic locking (2 minutes or less) (M5)
	#. For mobile assets, enumerate those assets with improperly configured automatic locking (greater than 2 minutes) (M6)

Measures
--------
* M1 = Count of assets capable of supporting automatic lockout
* M2 = Count of assets with authorized software installed to allow lockout
* M3 = Count of general computing assets with properly configured lockout
* M4 = Count of general computing assets with improperly configured lockout
* M5 = Count of mobile assets with properly configured lockout
* M6 = Count of mobile assets with improperly configured lockout

Metrics
-------

Properly Configured Assets
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The percentage of assets properly configured for automatic lockout.
	* - **Calculation**
	  - :code:`(M3 + M5) / M1`


.. history
.. authors
.. license
