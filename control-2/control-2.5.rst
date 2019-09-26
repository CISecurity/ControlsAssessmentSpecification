2.5: Integrate Software and Hardware Asset Inventories
=========================================================
The software inventory system should be tied into the hardware asset inventory so all devices and associated software are tracked from a single location.

.. list-table::
	:header-rows: 1

	* - Asset Type
	  - Security Function
	  - Implementation Groups
	* - Applications
	  - Identify
	  - 3

Dependencies
------------
* Sub-control 1.4: Maintain Detailed Asset Inventory
* Sub-control 1.5: Maintain Asset Inventory Information

Inputs
------
#. The list of endpoints

Operations
----------
#. Enumerate software inventory systems from the endpoint inventory
#. Enumerate hardware inventory systems from the endpoint inventory
#. For each software inventory system, examine its configuration to ensure that it is tied to at least one hardware inventory system, noting appropriately and inappropriately configured software inventory systems

Measures
--------
* M1 = List of software inventory systems
* M2 = List of hardware inventory systems
* M3 = List of appropriately configured software inventory systems
* M4 = List of inappropriately configured software inventory systems
* M5 = Count of software inventory systems (count of M1)
* M6 = Count of hardware inventory systems (count of M2)
* M7 = Count of appropriately configured software inventory systems (count of M3)
* M8 = Count of inappropriately configured software inventory systems (count of M4)

Metrics
-------

Coverage
^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The ratio of appropriately configured software inventory systems to the number of
	    | software inventory systems
	* - **Calculation**
	  - :code:`M7 / M5`

.. history
.. authors
.. license
