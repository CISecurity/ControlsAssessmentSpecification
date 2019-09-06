6.6: Deploy SIEM or Log Analytic Tools
=========================================================
Deploy Security Information and Event Management (SIEM) or log analytic tools for log correlation and analysis.

.. list-table::
	:header-rows: 1

	* - Asset Type 
	  - Security Function
	  - Implementation Groups
	* - Network
	  - Detect
	  - 2, 3

Status
------
Draft

Dependencies
------------
* TBD

Inputs
------
#. Install location of SIEM or log analytic tool
#. The number of log producers correlated by a SIEM
#. The total number of log producers

Operations
----------
N/A 

Measures
--------
* M1 = 1 if a SIEM or other log analytics tool is installed/present; 0 otherwise
* M2 = The number of log producers correlated by a SIEM
* M3 = The total number of log producers

Metrics
-------

Quality of SIEM Correlation
^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The ratio of log producers correlated by a SIEM to the total number of log producers
	* - **Calculation**
	  - :code:`IF M1 == 1 THEN M2 / M3; OTHERWISE 0`

.. history
.. authors
.. license