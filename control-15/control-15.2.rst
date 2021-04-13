15.2: Establish and Maintain a Service Provider Management Policy
==================================================================
Establish and maintain a service provider management policy. Ensure the policy addresses the classification, inventory, assessment, monitoring, and decommissioning of service providers. Review and update the policy annually, or when significant enterprise changes occur that could impact this Safeguard.

.. list-table::
	:header-rows: 1

	* - Asset Type
	  - Security Function
	  - Implementation Groups
	* - N/A
	  - Identify
	  - 2, 3

Dependencies
------------
* None

Inputs
-----------
#. :code:`GV45`: Service Provider Management Policy
#. Date of last review or update of the policy

Operations
----------
#. Determine whether the enterprise maintains a service provider management policy by checking for Input 1,
	#. If Input 1 exists, M1 = 1
	#. If Input 2 does not exist, M1 = 0 
#. Review Input 1 and determine if it includes, at a minimum, the following components: service provider inventory, classification, assessment, monitoring, and decommissioning of service providers
	#. For each component included, assign a value of 1. Sum all values. (M2)
#. Compare the date from Input 2 with the current date and capture the time frame in months (M3) 

Measures
--------
* M1 = Output of Operation 1
* M2 = Count of components included in the policy
* M3 = Timeframe since last update or review of the policy

Metrics
-------
* If M1 is a 0, this safeguard receives a failing score. The other metrics don't apply.
* If M3 is greater than twelve months, then this safeguard is measured at a 0 and receives a failing score. The other metrics don't apply.

Completeness of Policy
^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The percentage of components included in the policy
	* - **Calculation**
	  - :code:`M2 / 5`

.. history
.. authors
.. license
