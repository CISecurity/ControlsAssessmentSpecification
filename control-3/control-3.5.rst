3.5: Securely Dispose of Data
=====================================================
Securely dispose of data as outlined in the enterprise’s data management process. Ensure the disposal process and method are commensurate with the data sensitivity.

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
#. :code:`GV16`: Data disposal requirement portion of data management process
#. :code:`GV11`: Portion of data management process addressing data sensitivity
#. :code:`GV17`: Count of Sensitive data types
#. :code:`GV12`: Sensitive Data Inventory

Operations
----------
#. For each sensitive data type covered in :code:`GV17`
	#. Identify and enumerate each type has a disposal method and process as defined by :code:`GV16` (M2)
	#. Identify and enumerate each type that does not have a disposal method and process as defined by :code:`GV16`(M3)
#. For each item in :code:`GV12`determine wether they data complies with the disposal requirements outlined in :code:`GV17`
	#. Enumerate data that does not comply with disposal requirements (M4)
	#. Enumerate data that complies with disposal requirements (M5)

Measures
--------
* M1 = :code:`GV17`
* M2 = Count of sensitive data types with an outlined disposal method
* M3 = Count of sensitive data types without an outlined disposal method
* M4 = Count of data in inventory that does not comply with disposal requirement
* M5 = Count of data in inventory that complies with disposal requirement
* M6 = Count of items in :code:`GV12`

Metrics
-------
* If :code:`GV16` is 0, this safeguard receives a failing score. The other metrics don't apply.

Completeness of disposal process 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The percentage of data sensitivity types that contain a disposal method and process
	* - **Calculation**
	  - | :code:`M2 / M1`

Compliance to disposal process
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The percentage of compliance to the data disposal process
	* - **Calculation**
	  - | :code:`M5 / M6`

.. history
.. authors
.. license
