17.3: Establish and Maintain an Enterprise Process for Reporting Incidents
=========================================================
Establish and maintain an enterprise process for the workforce to report security incidents. The process includes reporting timeframe, personnel to report to, mechanism for reporting, and the minimum information to be reported. Ensure the process is publicly available to all of the workforce. Review annually, or when significant enterprise changes occur that could impact this Safeguard.

.. list-table::
	:header-rows: 1

	* - Asset Type
	  - Security Function
	  - Implementation Groups
	* - N/A
	  - Respond
	  - 1, 2, 3

Dependencies
------------
* None

Inputs
-----------
#. :code:`GV51`: Enterprise Incident Response Documentation
#. Date of last update or review of the documentation

Operations
----------
#. Determine whether the enterprise documents process for reporting incidents by reviewing Input 1 :code:`GV51`. Input 1 can be an incident response plan or other documentation.
	#. If documentation for reporting incidents exists, M1 = 1
	#. If documentation for reporting incidents does not exist, M1 = 0
#. Determine whether the documentation, at a minimum, outlines the following components: reporting timeframe, personnel to report to, mechanism for reporting, and the minimum information to be reported
	#. For each component included, assign a value of 1. Sum the values. (M2)
#. Compare Input 2 to current date and capture timeframe in months (M3)
#. Determine whether the process documentation is available to the whole workforce
	#. If it is available to all, M4 = 1
	#. If it is not available to all, M4 = 0

Measures
--------
* M1 = Output of Operation 1
* M2 = Count of components included for reporting incidents process documentation
* M3 = Timeframe since last update or review of documentation in months
* M4 = Output of Operation 4

Metrics
-------
* If M1 is 0, this safeguard receives a failing score. The other metrics don't apply.
* If M3 is greater than twelve months, then this safeguard is measured at a 0 and receives a failing score. The other metrics don't apply.
* If M4 is 0, this safeguard receives a failing score for this metric. Other metrics still apply.

Completeness
^^^^^^^
.. list-table::

	* - **Metric**
	  - | The percentage of components included in documentation for 
	    | designated incident handling personnel 
	* - **Calculation**
	  - :code:`M2 / 4`

.. history
.. authors
.. license
