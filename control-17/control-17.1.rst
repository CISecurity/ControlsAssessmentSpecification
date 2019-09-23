17.1: Perform a Skills Gap Analysis
===================================
Perform a skills gap analysis to understand the skills and behaviors workforce members are not adhering to, using this information to build a baseline education roadmap.

.. list-table::
	:header-rows: 1

	* - Asset Type 
	  - Security Function
	  - Implementation Groups
	* - N/A
	  - N/A
	  - 2, 3

Status
------
Draft

Dependencies
------------
* None

Inputs
-----------
#. Security awareness skill topic areas to be assessed
#. Set of exams/exercises mapped to the topics in Input 1
#. Minimum acceptable score

Operations
----------
#. For each workforce member, administer the exams/exercises from Input 2
#. Score each of the exams/exercises
#. For each security awareness skill topic area in Input 1, average the results of the exams/exercises mapped to that topic area to generate an organizational average for that topic area.
	#. Generate a list of topic areas and the organizational averages that are greater than or equal to the minimum acceptable score provided as Input 3 (M1).
	#. Generate a list of topic areas and organizational averages that are below the minimum acceptable score (M2).

Measures
--------
* M1 = List of security awareness topic areas with averages in the acceptable range (compliant list)
* M2 = List of security awareness topic areas with averages below the acceptable range (non-compliant list)
* M3 = Count of security awareness topic areas with averages in the acceptable range (count of M1)
* M4 = Total count of security awareness topic areas assessed (count of Input 1)

Metrics
-------

Scoring
^^^^^^^
.. list-table::

	* - **Metric**
	  - | The ratio of security awareness topic areas with organizational averages in the 
	    | acceptable range
	* - **Calculation**
	  - :code:`M3 / M4`

.. history
.. authors
.. license