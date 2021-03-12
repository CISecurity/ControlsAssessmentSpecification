8.5: Collect Detailed Audit Logs
=========================================================
Configure detailed audit logging for enterprise assets containing sensitive data. Include event source, date, username, timestamp, source addresses, destination addresses, and other useful elements that could assist in a forensic investigation.

.. list-table::
	:header-rows: 1

	* - Asset Type
	  - Security Function
	  - Implementation Groups
	* - Network
	  - Detect
	  - 2, 3

Dependencies
------------
* Safeguard 1.1: Establish and Maintain Detailed Enterprise Asset Inventory

Inputs
-----------
#. :code:`GV18`: Enterprise assets storing, processing, and transmitting sensitive data
#. :code:`GV26`: Enterprise's audit log management process
#. :code:`GV3`: Configuration standards

Operations
----------
#. Review :code:`GV26` for detailed logging requirements such as event source, date, username, timestamp, source addresses, and destination addresses. 
	#. For each detailed logging requirement included, assign a value of 1.  Sum all requirements included. (M2)
#. For each asset in :code:`GV18` check configuraions using :code:`GV3` as a guide
	#. Identify and enumerate assets properly configured to collect detailed logging requirements (M3)
	#. Identify and enumerate assets not properly configured to collect detailed logging requirements (M4)

Measures
--------
* M1 = Count of assets capable of supporting logging :code:`GV27`
* M2 = Count of detailed logging requirements included in log management process
* M3 = Count of assets properly configured to collect detailed logs
* M4 = Count of assets not properly configured to collect detailed logs

Metrics
-------

Completeness of Process
^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The percentage of detailed logging requirements included in the 
	  - | logging manangement process.
	* - **Calculation**
	  - :code:`M2 / 6`

Logging Coverage
^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The percentage of assets properly configured to collect 
	  - | detailed logs.
	* - **Calculation**
	  - :code:`M3 / M1`

.. history
.. authors
.. license
