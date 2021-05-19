3.14: Log Sensitive Data Access
==================================
Log sensitive data access, including modification and disposal. 

.. list-table::
	:header-rows: 1

	* - Asset Type
	  - Security Function
	  - Implementation Groups
	* - Data
	  - Detect
	  - 3

Dependencies
------------
* Safeguard 1.1: Establish and Maintain Detailed Enterprise Asset Inventory
* Safeguard 2.1: Establish and Maintain a Software Inventory
* Safeguard 4.1: Establish and Maintain a Secure Configuration Process

Inputs
------
#. :code:`GV5`: Authorized software inventory
#. :code:`GV19`: Enterprise assets storing sensitive data
#. :code:`GV3`: Configuration Standards

Operations
----------
#. Using :code:`GV3` identify authorized logging software 
#. For each asset in :code:`GV19`, use the output from Operation 1
	#. Identify and enumerate assets with logging software installed (M2)
	#. Identify and enumerate assets that do not have logging software installed (M3)
#. For logging software installed check configuration using :code:`GV3`
	#. Identify and enumerate software that is properly configured (M4)
	#. Identify and enumerate software that is improperly configured (M5)

Measures
--------
* M1 = Count of :code:`GV19`
* M2 = Count of assets storing sensitive data with logging software
* M3 = Count of assets storing sensitive data without logging software
* M4 = Count of assets with properly configured logging
* M5 = Count of assets with imporperly configured logging

Metrics
-------
Coverage
^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The percentage of properly configured logging on assets storing
	  - | sensitive data.
	* - **Calculation**
	  - :code:`M4 / M1`


.. history
.. authors
.. license
