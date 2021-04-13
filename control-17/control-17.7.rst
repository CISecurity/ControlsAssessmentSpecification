17.7: Conduct Routine Incident Response Exercises
=========================================================
Plan and conduct routine incident response exercises and scenarios for key personnel involved in the incident response process to prepare for responding to real-world incidents. Exercises need to test communication channels, decision making, and workflows. Conduct testing on an annual basis, at a minimum.

.. list-table::
	:header-rows: 1

	* - Asset Type
	  - Security Function
	  - Implementation Groups
	* - N/A
	  - Recover
	  - 2, 3

Dependencies
------------
* Safeguard 17.4: Establish and Maintain an Incident Response Process

Inputs
-----------
#. :code:`GV52`: Incident response process
#. Date of last exercise or test

Operations
----------
#. Determine whether the enterprise's incident response process includes routine incident response exercises by reviewing Input 1 :code:`GV52`
	#. If the documentation includes exercises, M1 = 1
	#. If the documentation does not include exercises, M1 = 0
#. Determine whether the documentation for exercises, at a minimum, outlines test communication channels, decision making, and workflows
	#. For each mechanism included, assign a value of 1. Sum the values. (M2)
#. Compare Input 2 to current date and capture timeframe in months (M3)

Measures
--------
* M1 = Output of Operation 1
* M2 = Count of components included in documentation
* M3 = Timeframe since last exercise or test in months

Metrics
-------
* If M1 is 0, this safeguard receives a failing score. The other metrics don't apply.
* If M3 is greater than twelve months, then this safeguard is measured at a 0 and receives a failing score. The other metrics don't apply.

Completeness
^^^^^^^
.. list-table::

	* - **Metric**
	  - | The percentage of components included in documentation for 
	    | incident response exercises
	* - **Calculation**
	  - :code:`M2 / 3`

.. history
.. authors
.. license
