8.10: Retain Audit Logs
=========================================================
Retain audit logs across enterprise assets for a minimum of 90 days.

.. list-table::
	:header-rows: 1

	* - Asset Type
	  - Security Function
	  - Implementation Groups
	* - Network
	  - Protect
	  - 2, 3

Dependencies
------------
* Safeguard 4.1: Establish and Maintain a Secure Configuration Process
* Safeguard 8.9: Centralize Audit Logs

Inputs
------
#. :code:`GV28`: Log aggregating software
#. :code:`GV3`: Configuration standards

Operations
----------
#. For each log aggregating software :code:`GV28` use :code:`GV3` to check configuration standards
	#. Identify and enumerate aggregating software configured to retain logs for 90 days or more (M2)
	#. Identify and enumerate aggregating software configured to retain logs for less than 90 days (M3)

Measures
--------
* M1 = Count of log aggregating software :code:`GV28`
* M2 = Count of aggregating software properly configured to retain logs for 90 days or more
* M3 = Count of aggregating software configured to retainlogs for less than 90 days

Metrics
-------

Compliance
^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The percentage of aggregating software properly configured to retain
	    | logs for 90 days or more.
	* - **Calculation**
	  - :code:`M2 / M1`

.. history
.. authors
.. license
