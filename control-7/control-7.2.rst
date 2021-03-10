7.2: Establish and Maintain a Remediation Process
========================================================================
Establish and maintain a risk-based remediation strategy documented in a remediation process, with monthly, or more frequent, reviews.

.. list-table::
	:header-rows: 1

	* - Asset Type
	  - Security Function
	  - Implementation Groups
	* - Applications
	  - Respond
	  - 1, 2, 3

Dependencies
------------
* None

Inputs
------
#. Enterprise remediation strategy process
#. Date of last review of the process
#. :code:`GV18`: Enterprise assets storing, processing, and transmitting sensitive data

Operations
----------
#. Determine whether the enterprise maintains a documented remediation process
	#. If the process exists, M1 = 1
	#. If the process does not exist, M1 = 0
#. Check the documented remediation process to identify whether it includes a risk based process based on the following elements: Sensitive assets :code:`GV18` and criticality of vulnerability
	#. Each element, if included, gets a value of 1. Sum all elements (M2) 
#. Compare the date from Input 2 and current date. Enumerate the timeframe in terms of days (M3)

Measures
--------
* M1 = Output of Operation 1
* M2 = Sum of elements included in the remediation process
* M3 = Timeframe since last review of process in days

Metrics
-------
If M1 is 0, the safeguard receives a failing score. The other metrics don't apply.
If M3 is greater than thirty, the safeguard receives a failing score. The other metrics don't apply.

Completenes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The percentage of elements included in the process
	* - **Calculation**
	  - :code:`M2 / 2`


.. history
.. authors
.. license
