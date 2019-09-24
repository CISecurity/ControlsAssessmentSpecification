2.8: Implement Application Whitelisting of Libraries
=========================================================
The organization’s application whitelisting software must ensure that only authorized software libraries (such as *.dll, *.ocx, *.so, etc.) are allowed to load into a system process.

.. list-table::
	:header-rows: 1

	* - Asset Type
	  - Security Function
	  - Implementation Groups
	* - Applications
	  - Protect
	  - 3

Status
------
Draft

Dependencies
------------
* Sub-control 2.1: Maintain Inventory of Authorized Software
* Sub-control 2.7: Utilize Application Whitelisting

Inputs
------
#. The list of authorized software
#. The list of authorized software libraries

Operations
----------
#. Enumerate all instances of whitelisting software from the software inventory
#. For each instance of whitelisting software, examine its configuration to ensure that it is configured to allow process loading of authorized libraries found in the authorized software library list, noting appropriately and inappropriately configured whitelisting software

Measures
--------
* M1 = List of all instances of whitelisting software found in the software inventory
* M2 = List of appropriately configured whitelisting software instances
* M3 = List of inappropriately configured whitelisting software instances
* M4 = Count of all instances of whitelisting software found in the software inventory (count of M1)
* M5 = Count of appropriately configured whitelisting software instances (count of M2)
* M6 = Count of inappropriately configured whitelisting software instances (count of M3)

Metrics
-------

Coverage
^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The ratio of appropriately configured whitelisting software instances to the total
	    | number of whitelisting software instances in the enterprise
	* - **Calculation**
	  - :code:`M5 / M4`

.. history
.. authors
.. license
