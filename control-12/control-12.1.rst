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

Dependencies
------------
* Sub-control 1.4: Maintain Detailed Asset Inventory
* Sub-control 1.5: Maintain Asset Inventory Information

Inputs
-----------
#. An inventory of expected boundary devices (M1) as derived from the endpoint inventory (see sub-control 1.4)

Operations
----------
#. Utilize a discovery tool or process to examine the network topology to collect the list of devices considered boundary devices (M2).
#. Evaluate the complement of Input 1 and Operation 1 to get the list of non-inventoried boundary devices (M3).

Measures
--------
* M1 = List of expected network boundary devices
* M2 = Count of M1
* M3 = List of discovered network boundary devices
* M4 = Count of M3
* M5 = List of non-inventoried boundary devices
* M6 = Count of M5

Metrics
-------

Coverage
^^^^^^^^
.. list-table::

	* - **Metric**
	  - | What is the ratio of non-inventoried boundary devices to expected boundary devices?
	    | If the calculated value is greater than zero, the inventory is not current.
	* - **Calculation**
	  - :code:`M6 / M2`

.. history
.. authors
.. license
