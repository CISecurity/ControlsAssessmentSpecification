12.5: Centralize Network Authentication, Authorization, and Auditing (AAA)
=============================================================
Centralize network AAA.

.. list-table::
	:header-rows: 1

	* - Asset Type
	  - Security Function
	  - Implementation Groups
	* - Network
	  - Protect
	  - 2, 3

Dependencies
------------
* Safeguard 2.1: Establish and Maintain a Software Inventory

Inputs
-----------
#. :code:`GV5`: Authorized Software Inventory
#. :code:`GV35`: Assets that are part of the network infrastructure


Operations
----------
#. Use Input 1 :code:`GV5` to identify and enumerate all AAA services within the enterprise :code:`GV38` (M1)
#. For each centralized AAA point indentifed in Operation 1, determine whether it is necessary or can be consolidated
	#. Identify and enumerate authentication points that are unnecesary or can be consolidated (M2)
	#. Identify and enumerate authentication points that are necesary and cannot be consolidated (M3)
#. Use the output of Operation 1 to check if each asset in Input 2 :code:`GV35` is covered by at least one AAA system
	#. Identify and enumerate network infrastructure assets that are covered by at least one AAA system (M4)
	#. Identify and enumerate network infrastructure assets that are not covered by an AAA system (M5)

Measures
--------
* M1 = Count of AAA services within the enterprise
* M2 = Count of unnecessary AAA services 
* M3 = Count of necessary AAA services 
* M4 = Count of network infrastructure covered by AAA services
* M5 = Count of network infrastructure not covered by AAA services
* M6 = Count of :code:`GV35`
 

Metrics
-------

Centralized AAA
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | Percentage of properly centralized AAA services
	* - **Calculation**
	  - :code:`M3 / M1`

Network Coverage
^^^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | Percentage of network infrastructure assets managed through AAA
	* - **Calculation**
	  - :code:`M4 / M6`

.. history
.. authors
.. license
