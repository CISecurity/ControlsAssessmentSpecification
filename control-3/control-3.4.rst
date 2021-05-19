3.4: Enforce Data Retention
=============================================================
Retain data according to the enterprise’s data management process. Data retention must include both minimum and maximum timelines. 

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
* Safeguard 3.1: Establish and Maintain a Data Management Process
* Safeguard 3.2: Establish and Maintain a Data Inventory

Inputs
------
#. :code:`GV15`: Data Retention Limits outlined in the data management process
#. :code:`GV11`: Portion of data management process addressing data sensitivity
#. :code:`GV12`: Sensitive Data Inventory

Operations
----------
#. For each sensitive data type covered in :code:`GV11`
	#. Enumerate the number of types of sensitivity (:code:`GV17`: M1), at a minimum one to deferrentiate sensitive data from other data
	#. Identify and enumerate if each type has a minimum retention time (M2) as defined by :code:`GV15`
	#. Identify and enumerate if each type has a maximum retention time (M3) as defined by :code:`GV15
#. Using the output of Operation 1.1 and 1.2, check the data inventory :code:`GV12` for enforcement of data retention
	#. Identify and enumerate items in the inventory that comply with retention timelines (M4)
	#. Identify and enumerate items in the inventory that do not comply with retention timelines (M5)

Measures
--------
* M1 = Count of sensitivity types that require retention timelines
* M2 = Count of sensitivity types that ainclude minimum retention times
* M3 = Count of sensitivity types that ainclude maximum retention times
* M4 = Count of data in inventory that comply with retention policy
* M5 = Count of data in inventory that do not comply with retention policy
* M6 = Count of :code:`GV12`

Metrics
-------
If :code:`GV15` is 0, this safeguard receives a failing score. The other metrics don't apply.

Completeness of Policy
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The percentage of sensitivity types that include minimum retention timelines
	* - **Calculation**
	  - | :code: `M2 / M1`

	* - **Metric**
	  - | The percentage of sensitivity types that include maximum retention timelines
	* - **Calculation**
	  - | :code: `M3 / M1`

Enforcement of Retention Policy
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The percentage of sensitivity data that complies with retention policy
	* - **Calculation**
	  - | :code:`M4 / M6`

.. history
.. authors
.. license
