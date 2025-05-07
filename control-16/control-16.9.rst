16.9: Train Developers in Application Security Concepts and Secure Coding
=================================
Ensure that all software development personnel receive training in writing secure code for their specific development environment and responsibilities. Training can include general security principles and application security standard practices. Conduct training at least annually and design in a way to promote security within the development team, and build a culture of security among the developers.

.. list-table::
	:header-rows: 1

	* - Asset Type
	  - Security Function
	  - Implementation Groups
	* - Applications
	  - Protect
	  - 2, 3

Dependencies
------------
* None

Inputs
-----------
#. List of software developing personnel with assigned roles and development environments
#. List of required courses for each role and development environment 
#. Date of last training course 

Operations
----------
#. For each individual in Input 1, determine whether they have taken the applicable courses per role and environment
	#. Identify and enumerate personnel that have completed the appropriate courses (M2)
	#. Identify and enumerate personnel that have not completed the appropriate courses (M3)
#. For each individual who has completed the appropriate courses, compare the date of last training from Input 3 to current date and capture timeframe in months
	#. Identify and enumerate personnel that have completed all appropriate training within twelve months or less (M4)
	#. Identify and enumerate personnel that have not completed all appropriate training within twelve months or less (M5)

Measures
--------
* M1 = Count of software developing personnel
* M2 = Count of software developing personnel with completed courses
* M3 = Count of software developing personnel without completed courses 
* M4 = Count of software developing personnel with training in scope
* M5 = Count of software developing personnel with training out of scope

Metrics
-------

Compliance
^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The percentage of software developing personnel with
	    | all appropriate training course in scope
	* - **Calculation**
	  - :code:`M4 / M1`


.. history
.. authors
.. license
