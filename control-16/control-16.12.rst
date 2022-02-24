16.12: Implement Code-Level Security Checks
=========================================================
Apply static and dynamic analysis tools within the application life cycle to verify that secure coding practices are being followed.

.. list-table::
	:header-rows: 1

	* - Asset Type
	  - Security Function
	  - Implementation Groups
	* - Applications
	  - Protect
	  - 3

Dependencies
------------
* Safeguard 2.1: Establish and Maintain a Software Inventory

Inputs
-----------
#. :code:`GV5`: Authorized Software Inventory

Operations
----------
#. Use Input 1 :code:`GV5` to identify and enumerate in-house developed software (M1)
#. Use Input 1 :code:`GV5` to identify static analysis tools
#. For each software identified in Operation 1, determine if it is verified by a static tool identified in Operation 2
	#. Identify and enumerate software verified by a static tool (M2)
	#. Identify and enumerate software not verified by a static tool (M3)
#. Use Input 1 :code:`GV5` to identify dynamic analysis tools
#. For each software identified in Operation 1, determine if it is verified by a dynamic tool identified in Operation 4
	#. Identify and enumerate software verified by a dynamic tool (M4)
	#. Identify and enumerate software not verified by a dynamic tool (M5)

Measures
--------
* M1 = Count of in-house developed software
* M2 = Count of in-house developed software verified by a static analysis tool
* M3 = Count of in-house developed software not verified by a static analysis tool
* M4 = Count of in-house developed software verified by a dynamic analysis tool
* M5 = Count of in-house developed software not verified by a dynamic analysis tool

Metrics
-------

Static Analysis Tool Coverage
^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The percentage of in-house developed software verified by a
	    | static analysis tool
	* - **Calculation**
	  - :code:`M2 / M1`

Dynamic Analysis Tool Coverage
^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The percentage of in-house developed software verified by a
	    | dynamic analysis tool
	* - **Calculation**
	  - :code:`M4 / M1`

.. history
.. authors
.. license
