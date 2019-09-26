8.5: Configure Devices to Not Auto-Run Content
=========================================================
Configure devices to not auto-run content from removable media.

.. list-table::
	:header-rows: 1

	* - Asset Type
	  - Security Function
	  - Implementation Groups
	* - Devices
	  - Protect
	  - 1, 2, 3

Dependencies
------------
* Sub-control 1.4: Maintain Detailed Asset Inventory
* Sub-control 5.1: Establish Secure Configurations

Inputs
-----------
#. EI: Endpoint inventory
#. Desired configuration(s) to disable auto-run. There may be multiple configurations targeted at different types of endpoints (for instance, a different configuration might be provided for each type of operating system used on the endpoints in the provided inventory). If the endpoints are capable of performing multiple types of auto-run behavior (i.e., auto-run vs. auto-play), appropriate configurations should be provided for each type.

Operations
----------
#. For each endpoint in Input 1, compare the endpoint's configuration to the appropriate configuration from Input 2. Generate a list of endpoints that adhere to the specified configuration (M1) and a list of the endpoints that do not adhere to the specified configuration (M2).

Assumption
^^^^^^^^^^
Endpoints that are not capable of performing any type of auto-run behavior would be included in the compliant list (M1).

Measures
--------
* M1 = List of endpoints adhering to the specified configuration (compliant list)
* M2 = List of endpoints not adhering to the specified configuration (non-compliant list)
* M3 = Count of endpoints in M1 (number of compliant endpoints)
* M4 = Count of endpoints in M2 (number of non-compliant endpoints)
* M5 = Count of endpoints in the endpoint inventory (Input 1)

Metrics
-------
.. list-table::

	* - **Metric**
	  - The ratio of endpoints properly disabling auto-run to the total number of endpoints?
	* - **Calculation**
	  - :code:`M3 / M5`

.. history
.. authors
.. license
