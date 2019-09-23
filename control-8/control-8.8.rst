8.8: Enable Command-Line Audit Logging
=========================================================
Enable command-line audit logging for command shells, such as Microsoft PowerShell and Bash.

.. list-table::
	:header-rows: 1

	* - Asset Type
	  - Security Function
	  - Implementation Groups
	* - Devices
	  - Detect
	  - 2, 3

Status
------
Draft

Dependencies
------------
* Sub-control 1.4: Maintain Detailed Asset Inventory
* Sub-control 5.1: Establish Secure Configurations

Inputs
------
#. The list of endpoints
#. Approved configuration(s) for command line auditing of command shells (note: there may be multiple configurations based on the various types of endpoints, including various operating systems, etc.)

Operations
----------
#. For each endpoint in Input 1, examine the endpoint to see if it is configured according to the appropriate approved configuration(s) from Input 2.
#. Create a list of endpoints that meet the approved configuration (M1)
#. Create a list of endpoints that do not meet the approved configuration (M3), noting the deviations.

Measures
--------
* M1 = List of endpoints that meet the approved command shell logging configurations (compliant list)
* M2 = Count of endpoints (count of Input 1)
* M3 (Optional) = List of endpoints that do not meet the approved command shell logging configurations (non-compliant list)
* M4 (Optional) = Count of non-compliant endpoints (count of M3)

Metrics
-------

Coverage
^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The ratio of endpoints compliant with command shell logging configurations to the
	    | total number of endpoints
	* - **Calculation**
	  - :code:`M1 / M2`

.. history
.. authors
.. license
