17.8: Conduct Post-Incident Reviews
==============================================================
Conduct post-incident reviews. Post-incident reviews help prevent incident recurrence through identifying lessons learned and follow-up action.

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
#. Last post-incident review 

Operations
----------
#. Determine whether the enterprise's incident response process includes post-incident reviews by reviewing Input 1 :code:`GV52`
	#. If the documentation includes post-indicent reviews, M1 = 1
	#. If the documentation does not include post-incident reviews, M1 = 0
#. Use Input 2 to determine if post-incident reviews include,  at a minimum, the following components: lessons learned and follow-up actions
	#. For each component included, assign a value of 1. Sum the values. (M2)

Measures
--------
* M1 = Output of Operation 1
* M2 = Count of components included in documentation

Metrics
-------
* If M1 is 0, this safeguard receives a failing score. The other metrics don't apply.

Completeness
^^^^^^^
.. list-table::

	* - **Metric**
	  - | The percentage of components included in post-incident reviews
	    | incident response exercises
	* - **Calculation**
	  - :code:`M2 / 2`

.. history
.. authors
.. license
