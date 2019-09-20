2.3: Utilize Software Inventory Tools
=========================================================
Utilize software inventory tools throughout the organization to automate the documentation of all software on business systems.

.. list-table::
	:header-rows: 1

	* - Asset Type
	  - Security Function
	  - Implementation Groups
	* - Applications
	  - Identify
	  - 2, 3

Status
------
Draft

Dependencies
------------
* Sub-control 1.4: Maintain Detailed Asset Inventory

Assumptions
^^^^^^^^^^^
* The documentation referenced by this sub-control intends to mean an enumeration of software load on endpoints capable of running installed software
* A business system is any endpoint owned or operated by the enterprise/organization
* The CMDB does not contain and up-to-date software load for each endpoint in its inventory

Inputs
------
#. Endpoint inventory
#. List of software inventory tools

Operations
----------
#. For each software inventory, count covered endpoints and calculate the aggregate (becomes M2)
#. Count number of endpoints loadable with software (becomes M3)

Measures
--------
* M1 = Count of software inventory tools (from Input 2)
* M2 = List of endpoints covered by software inventory tools
* M3 = Count of M2
* M4 = List of endpoints not covered by software inventory tools
* M5 = Count of M4
* M6 = List of endpoints loadable with software
* M7 = Count of M6
* M8 = List of endpoints not loadable with software
* M9 = Count of M8


Metrics
-------

Software Inventory Tool Usage
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | Are software inventory tools used?
	* - **Calculation**
	  - :code:`(M1 == 0) OR (M1 == 1)`

Inventory Tool Coverage
^^^^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The ratio of endpoints covered by automated software inventory tools to the total
	    | number of applicable endpoints
	* - **Calculation**
	  - :code:`M3 / M7`

.. history
.. authors
.. license
