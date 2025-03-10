5.6: Centralize Account Management
=========================================================

Centralize account management through a directory or identity service.

.. list-table::
	:header-rows: 1

	* - Asset Type
	  - Security Function
	  - Implementation Groups
	* - Users
	  - Protect
	  - 2, 3

Dependencies
------------
* Safeguard 1.1: Establish and Maintain Detailed Enterprise Asset Inventory
* Safeguard 2.1: Establish and Maintain a Software Inventory

Inputs
------
#. :code:`GV1`: Enterprise asset inventory

Operations
----------
#. Using :code:`GV1` identify and enumerate centralized authentication points (M1)
#. For each centralized authentication point identified in Operation 1, determine whether it is necessary or can be consolidated
	#. Identify and enumerate authentication points that are unnecesary or can be consolidated (M2)
	#. Identify and enumerate authentication points that are necesary and cannot be consolidated (M3)

Measures
--------
* M1 = Count of cetralized authentication points in the enterprise
* M2 = Count of unnecessary centralized authentication points 
* M3 = Count of necessary centralized authentication points

Metrics
-------

Coverage
^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | Percentage of properly centralized aunthentication points
	* - **Calculation**
	  - :code:`M3 / M1`


.. history
.. authors
.. license
