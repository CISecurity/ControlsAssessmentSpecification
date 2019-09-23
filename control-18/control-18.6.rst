18.6: Ensure Software Development Personnel Are Trained in Secure Coding
========================================================================
Ensure that all software development personnel receive training in writing secure code for their specific development environment and responsibilities.

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
#. List of software development personnel including assigned development environments and roles
#. List of secure coding training courses required for each development environment and role
#. List of secure coding training courses that each person has completed

Operations
----------
#. For each person in Input 1, use the development environments and roles assigned to that person to determine which secure coding training courses the person is required to take; note these individual lists of required courses in M1.
#. For each person in Input 1, compare the courses that person is required to take from M1 to the courses that person has completed from Input 3.
	#. Create a list of the required courses the person has completed (M2)
	#. Create a list of the required courses the person has not completed (M3).

Measures
--------
* M1 = List of courses that software development personnel are required to take, by individual
* M2 = List of required courses that software development personnel have completed, by individual (compliant list)
* M3 = List of required courses that software development personnel have not completed, by individual (non-compliant list)
* M4 = Count of required courses by individual (count of M1)
* M5 = Count of completed required courses by individual (count of M2)

Metrics
-------

Coverage
^^^^^^^^
.. list-table::

	* - **Metric**
	  - | THe ratio of completed required courses to total required courses by individual
	* - **Calculation**
	  - :code:`Individual's M5 / Individual's M4`

**NOTE**: An organizational average completion rate can be calculated by averaging the individual completion ratios from the above "Coverage" metric.

.. history
.. authors
.. license