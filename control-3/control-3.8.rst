3.8: Document Data Flows
==================================
Document data flows. Data flow documentation includes service provider data flows and should be based on the enterprise’s data management process. Review and update documentation annually, or when significant enterprise changes occur that could impact this Safeguard.

.. list-table::
	:header-rows: 1

	* - Asset Type
	  - Security Function
	  - Implementation Groups
	* - Data
	  - Identify
	  - 2, 3

Dependencies
------------
* Safeguard 3.1: Establish and Maintain a Data Management Process
* Safeguard 3.2: Establish and Maintain a Data Inventory 

Inputs
------
#. Documentation outlining data flow for enterprise owned data. Documentation should include, at a minimum, data flows to external enterprises.
#. :code:`GV12`: Sensitive Data Inventory
#. Date of last review of the data flow documentation

Operations
----------
#. Check if the enterprise has data flow documentation (Input 1).
	#. If Input 1 exists M = 1
	#. Otherwise M1 = 0
#. Using :code:`GV12`and identify data that flows to external enterprises
	#. Enumerate the data that flows to external enterprises (M2)
#. Compare Input 1 and the output of Operation 2
	#. Enumerate data flows from Operation 2 that are included in Input 1 (M3)
	#. Enumerate data flows from Operation 2 that are not included in Input 1 (M4)
#. Compare the current date to that provided in Input 3.  Note the timeframe in months (M5)

Measures
--------
* M1 = Output of Operation 1 
* M2 = Count of data flows to external enterprises
* M3 = Count of data flows included in the data flow doumentaion
* M4 = Count of data flows not included in the data flow documentation
* M5 = Count of months since last review of the data flow documentation

Metrics
-------
* If M1 is 0, this safeguard receives a failing score. The other metrics don't apply.
* If M5 is greater than twelve, this safeguard receives a failing score. The other metrics don't apply.

Coverage of Data Flow Documentation
^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The percentage of existing data flows in the enterprise's data flow
	  - | documentation.
	* - **Calculation**
	  - :code:`M3 / M2`


.. history
.. authors
.. license
