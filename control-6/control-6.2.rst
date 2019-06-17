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

Status
------
Draft

Inputs
------
#. The list of endpoints.
#. The list of events that should be logged (an event logging policy).

Assumptions
^^^^^^^^^^^
The assumption is that there could potentially be numerous events which should be logged, and that a checklist verifying the logging policy can be examined per endpoint.

Operations
----------
#. For each endpoint, determine if the configured event logging policy matches the policy defined by Input 2.

Measures
--------
* M1 = 1 if an endpoint implements the logging policy defined by Input 2; otherwise 0.
* M2 = The total number of endpoints.


Metrics
-------

Logging Policy Coverage
^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Question**
	  - | Determine the ratio of endpoints implementing the prescribed event logging policy
	    | to the total number of endpoints.
	* - **Answer**
	  - | Summing the value of M1 across all endpoints indicates the total count of endpoints
	    | correctly enforcing the event logging policy.
	* - **Calculation**
	  - :code:`(SUM(M1) / M2)`

.. history
.. authors
.. license