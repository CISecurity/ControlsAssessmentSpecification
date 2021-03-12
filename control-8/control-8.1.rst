8.1: Establish and Maintain an Audit Log Management Process
=========================================================
Establish and maintain an audit log management process that defines the enterprise’s logging requirements. At a minimum, address the collection, review, and retention of audit logs for enterprise assets. Review and update documentation annually, or when significant enterprise changes occur that could impact this Safeguard.

.. list-table::
	:header-rows: 1

	* - Asset Type
	  - Security Function
	  - Implementation Groups
	* - Network
	  - Protect
	  - 1, 2, 3

Dependencies
------------
* None

Inputs
------
#. :code:`GV26`: Enterprise's audit log management process
#. Date of last review of the audit log management process

Operations
----------
#. Check if :code:`GV26`the audit log management process exists
	#. If it exists, M1 = 1
	#. If it does not exist, M1 = 0
#. Review :code:`GV26` for elements of the process, at a minimum, address the collection, review, and retention of audit logs for enterprise assets.
	#. For each element that exists, assign a value of 1. Sum the values of existing elements. (M2) 
#. Compare the date from Input 2 and the current date. Capture the timeframe in terms of months. (M3)


Measures
--------
* M1 = Output of Operation 1
* M2 = Count of elements included in the audit log management process
* M3 = Timeframe since last review of the autid log management process

Metrics
-------
If M1 is 0, this safeguard receives a failing a score. The other metrics don't apply.
If M3 is greater than twelve, this safeguard is measured at a 0 and receives a failing score. THe other metrics don't apply.

Completeness
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The percentage of elements included in the audit log
	  - | management process.
	* - **Calculation**
	  - :code:`M2 / 3`


.. history
.. authors
.. license
