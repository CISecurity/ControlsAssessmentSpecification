8.7: Collect URL Request Audit Logs
=========================================================
Collect URL request audit logs on enterprise assets, where appropriate and supported.

.. list-table::
	:header-rows: 1

	* - Asset Type
	  - Security Function
	  - Implementation Groups
	* - Network
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
#. Use :code:`GV1` to identify and enumerate assets that support URL logging (M1)
#. For each asset identified in Operation 1, use :code:`GV3` to check configurations for URL logging
	#. Identify and enumerate assets properly configured for logging (M2)
	#. Identify and enumerate assets not properly configured for logging (M3)

Measures
--------
* M1 = Count of assets capable of supporting URL logging
* M2 = Count of assets properly configured for URL logging
* M3 = Count of assets not properly configured for URL logging

Metrics
-------

Configuration Coverage
^^^^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The percentage of assets properly cofigured for 
	    | URL logging
	* - **Calculation**
	  - :code:`M2 / M1`

.. history
.. authors
.. license
