12.1: Maintain an Inventory of Network Boundaries
=========================================================
Maintain an up-to-date inventory of all of the organization’s network boundaries.

.. list-table::
	:header-rows: 1

	* - Asset Type 
	  - Security Function
	  - Implementation Groups
	* - Network
	  - Identify
	  - 1, 2, 3

Status
------
Draft

Inputs
-----------
#. An inventory of expected boundary devices (M1)

Operations
----------
#. Utilize a discovery tool or process to examine the network topology to collect the list of devices considered boundary devices (M2).
#. Evaluate the complement of Input 1 and Operation 1 to get the list of non-inventoried boundary devices (M3).

Measures
--------
* M1 = The number of expected network boundary devices
* M2 = The number of discovered network boundary devices
* M3 = Number of non-inventoried boundary devices

Metrics
-------

Coverage
^^^^^^^^
.. list-table::

	* - **Question**
	  - | What is the ratio of non-inventoried boundary devices to expected boundary devices?
	    | If the calculated value is greater than zero, the inventory is not current.
	* - **Answer**
	  - 
	* - **Calculation**
	  - :code:`M3 / M1`

.. history
.. authors
.. license