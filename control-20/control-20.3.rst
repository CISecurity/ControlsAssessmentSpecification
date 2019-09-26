20.3: Perform Periodic Red Team Exercises
=========================================================
Perform periodic Red Team exercises to test organizational readiness to identify and stop attacks or to respond quickly and effectively.

.. list-table::
	:header-rows: 1

	* - Asset Type
	  - Security Function
	  - Implementation Groups
	* - N/A
	* - N/A
	  - 3

Dependencies
------------
* Sub-control 20.1: Establish a Penetration Testing Program

Inputs
-----------
#. Enterprise penetration test policy

Operations
----------
#. Examine the enterprise penetration test policy for the following properties:
	#. Red team exercises are specified to occur periodically
#. Note the periodicity of expected red team exercises
#. Interview security operations personnel to determine the last time a red team exercise was performed

Measures
--------
* M1 = (Boolean) 1 if the enterprise penetration testing policy contains periodicity for red team exercises; 0 otherwise
* M2 = Time of last red team exercise
* M3 = Current time
* M3 = Current time - maximum period between red team exercises
* M4 = (Boolean) 1 if the time of last red team exercise is greater than or equal to M3; 0 otherwise

Metrics
-------

Red Team Exercises
^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | Are periodic Red Team exercises required by the enterprise's penetration testing policy?
	* - **Calculation**
	  - :code:`M1`

Frequency
^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | Was the last Red Team exercise performed within the appropriate time period?
	* - **Calculation**
	  - :code:`M4`

.. history
.. authors
.. license
