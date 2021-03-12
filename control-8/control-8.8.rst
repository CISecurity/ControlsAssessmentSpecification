8.8: Collect Command-Line Audit Logs
=========================================================
Collect command-line audit logs. Example implementations include collecting audit logs from PowerShell®, BASH™, and remote administrative terminals..

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
* Safeguard 4.1: Establish and Maintain a Secure Configuration Process

Inputs
------
#. :code:`GV1`: Enterprise asset inventory
#. :code:`GV3`: Configuration standards

Operations
----------
#. Use :code:`GV1` to identify and enumerate assets that support command line auditing of command shells (M1)
#. For each asset identified in Operation 1, use :code:`GV3` to check configurations for command line auditing of command shells
	#. Identify and enumerate assets properly configured (M2)
	#. Identify and enumerate assets not properly configured (M3)

Measures
--------
* M1 = Count of assets capable of supporting command line auditing of command shells
* M2 = Count of assets properly configured for command line auditing of command shells
* M3 = Count of assets not properly configured for command line auditing of command shells

Metrics
-------

Configuration Coverage
^^^^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The percentage of assets properly cofigured for 
	    | command line auditing of command shells.
	* - **Calculation**
	  - :code:`M2 / M1`

.. history
.. authors
.. license
