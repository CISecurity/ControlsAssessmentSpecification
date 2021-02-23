2.1: Establish and Maintain a Software Inventory
==============================================
Establish and maintain a detailed inventory of all licensed software installed on enterprise assets. The software inventory must document the title, publisher, initial install/use date, and business purpose for each entry; where appropriate, include the Uniform Resource Locator (URL), app store(s), version(s), deployment mechanism, and decommission date. Review and update the software inventory bi-annually, or more frequently.

.. list-table::
	:header-rows: 1

	* - Asset Type
	  - Security Function
	  - Implementation Groups
	* - Applications
	  - Identify
	  - 1, 2, 3

Dependencies
------------
* None

Inputs
------
#. The authorized software inventory with detailed information including: timestamp indicating both last updated and last verified values, timestamp indicating installation date, operating system, software name, software version, software publisher, authorization status, business purpose, supported/unsupported. Where applicable, additionally include URL, app store(s), deployment mechanism, and decommission date.Authorized Software List: The authorized software list (containing a timestamp indicating both last updated and last verified values).
#. The date of the last update to the authorized software inventory.

Operations
----------
#. Check the authorized software inventory for completeness of deteailed information.
	#. Note items that have complete detailed information (M2).
	#. Note items that having missing or incomplete information (M3).
#. Compare the current date to the last date of update to the authorized software inventory in months (M4).

Measures
--------

* M1 = Count of Input 1
* M2 = Count of items in Input 1 with complete information
* M3 = Count of items in Input 1 with incomplete or missing information
* M4 = Timeframe in months of since last update to the authorized software inventory


Metrics
-------

* If M1 is not provided or available, then this safeguard is measured at a 0 and receives a failing score. The other metrics don't apply.
* If M4 is greater than six months, then this safeguard is measured at a 0 and receives a failing score. The other metrics don't apply.


Accuracy Score
^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | What percentage of the current enterprise asset inventory contains necessary detailed information?
	* - **Calculation**
	  - :code:`M2 / M1`

.. history
.. authors
.. license
