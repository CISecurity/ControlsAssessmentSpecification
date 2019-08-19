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
* M1 = The number of software inventory tools
* M2 = The number of endpoints covered by software inventory tools
* M3 = The number of endpoints loadable with software

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
	  - :code:`M2 / M3`

.. history
.. authors
.. license