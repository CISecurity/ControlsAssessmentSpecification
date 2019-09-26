6.2: Activate Audit Logging
=========================================================
Ensure that local logging has been enabled on all systems and networking devices.

.. list-table::
	:header-rows: 1

	* - Asset Type
	  - Security Function
	  - Implementation Groups
	* - Network
	  - Detect
	  - 1, 2, 3

Dependencies
------------
* Sub-control 1.4: Maintain Detailed Asset Inventory
* Sub-control 5.1: Establish Secure Configurations

Inputs
------
#. EI: The list of endpoints from the endpoint inventory
#. The list of events that should be logged (an event logging policy).

Assumptions
^^^^^^^^^^^
The assumption is that there could potentially be numerous events which should be logged, and that a checklist verifying the logging policy can be examined per endpoint.

Operations
----------
#. For each endpoint, determine if the configured event logging policy matches the policy defined by Input 2, noting appropriately and inappropriately configured endpoints.

Measures
--------
* M1 = The list of endpoints
* M2 = Count of M1
* M3 = The list of appropriately configured endpoints
* M4 = Count of M3
* M5 = The list of inappropriately configured endpoints
* M6 = Count of M5

Metrics
-------

Logging Policy Coverage
^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | Determine the ratio of endpoints implementing the prescribed event logging policy
	    | to the total number of endpoints.
	* - **Calculation**
	  - :code:`M4 / M6)`

.. history
.. authors
.. license
