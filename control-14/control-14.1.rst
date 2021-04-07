14.1: Establish and Maintain a Security Awareness Program
=========================================================
Establish and maintain a security awareness program. The purpose of a security awareness program is to educate the enterprise’s workforce on how to interact with enterprise assets and data in a secure manner. Conduct training at hire and, at a minimum, annually. Review and update content annually, or when significant enterprise changes occur that could impact this Safeguard.

.. list-table::
	:header-rows: 1

	* - Asset Type
	  - Security Function
	  - Implementation Groups
	* - N/A
	  - Protect
	  - 1, 2, 3

Dependencies
------------
* None

Inputs
-----------
#. Security awareness program
#. :code:`GV43`: List of workforce members
#. List of most recent security awareness training completion dates for each workforce member
#. Date of last review or update to security awareness program content

Operations
----------
#. Check enterprise to determine if Input 1 exists
	#. If Input 1 exists, M1 = 1
	#. If Input 1 does not exist, M1 = 0
#. Compare the date in Input 4 to the current date and capture timeframe in months (M2)
#. For every member of the workforce in Input 2 :code:`GV43`, determine whether the member has completed training
	#. Identify and enumerate members who have completed at least initial training (M4)
	#. Identify and enumerate members who have not completed any training (M5)
#. For every member of the workforce identified in Operation 3.1, identify the date of most recently completed security awareness training 
#. For every member of the workforce identified in Operation 3.1, use the output of Operation 4 and compare the date to current date. Capture timeframe in months.
	#. Identify and enumerate members whose most recent training date is less than or equal to twelve months from current date (M6)
	#. Identify and enumerate members whose most recent training date is greater than twelve months from current date (M7)

Measures
--------
* M1 = Output of Operation 1
* M2 = Output of Operation 2
* M3 = Count of Input 2 :code:`GV43`
* M4 = Count of workforce members that have completed training
* M5 = Count of workforce members that have not completed training
* M6 = Count of workforce members whose training is up to date
* M7 = Count of workforce members whose training is not up to date

Metrics
-------
* If M1 is measured at a 0, this safeguard receives a failing score. The other metrics don't apply.
* If M2 is greater than twelve months, then this safeguard is measured at a 0 and receives a failing score. The other metrics don't apply.

Initial Training Compliance
^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The percentage of workforce members that have received initial training
	* - **Calculation**
	  - :code:`M4 / M3`

Up to Date Training
^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The percentage of compliant workforce members
	* - **Calculation**
	  - :code:`M6 / M3`

.. history
.. authors
.. license
