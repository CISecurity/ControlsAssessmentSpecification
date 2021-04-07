14.6: Train Workforce Members on Recognizing and Reporting Security Incidents
=========================================================
Train workforce members to be able to recognize a potential incident and be able to report such an incident.

.. list-table::
	:header-rows: 1

	* - Asset Type
	  - Security Function
	  - Implementation Groups
	* - Data
	  - Protect
	  - 1, 2, 3

Dependencies
------------
* None

Inputs
-----------
#. Recognizing and Reporting Security Incidents training module
#. :code:`GV43`: List of workforce members
#. List of most recent module training completion dates for each workforce member


Operations
----------
#. Check enterprise to determine if Input 1 exists
	#. If Input 1 exists, M1 = 1
	#. If Input 1 does not exist, M1 = 0
#. For every member of the workforce in Input 2 :code:`GV43`, determine whether the member has completed training
	#. Identify and enumerate members who have completed at least initial training (M3)
	#. Identify and enumerate members who have not completed any training (M4)
#. For every member of the workforce identified in Operation 2.1, identify the date of most recently completed module training 
#. For every member of the workforce identified in Operation 2.1, use the output of Operation 4 and compare the date to current date. Capture timeframe in months.
	#. Identify and enumerate members whose most recent training date is less than or equal to twelve months from current date (M5)
	#. Identify and enumerate members whose most recent training date is greater than twelve months from current date (M6)

Measures
--------
* M1 = Output of Operation 1
* M2 = Count of Input 1 :code:`GV43` 
* M3 = Count of workforce members that have completed training
* M4 = Count of workforce members that have not completed training
* M5 = Count of workforce members whose training is up to date
* M6 = Count of workforce members whose training is not up to date

Metrics
-------
* If M1 is measured at a 0, this safeguard receives a failing score. The other metrics don't apply.

Initial Training Compliance
^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The percentage of workforce members that have received initial training
	* - **Calculation**
	  - :code:`M2 / M1`

Up to Date Training
^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The percentage of compliant workforce members
	* - **Calculation**
	  - :code:`M4 / M1`

.. history
.. authors
.. license
