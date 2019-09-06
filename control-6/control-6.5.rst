6.5: Central Log Management
=========================================================
Ensure that appropriate logs are being aggregated to a central log management system for analysis and review.

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
#. The total number of log producers (M1)
#. The number of sensors correlated in a central service (M2)

Operations
----------
N/A

Measures
--------
* M1 = The total number of log producers
* M2 = The number of sensors correlated in a central service

Metrics
-------

Quality of Log correlation/aggregation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The ratio of log producers correlated in a central service to the total number 
	    | of log producers.
	* - **Calculation**
	  - :code:`M2 / M1`

.. history
.. authors
.. license