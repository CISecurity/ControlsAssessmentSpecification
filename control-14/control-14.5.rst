14.5: Utilize an Active Discovery Tool to Identify Sensitive Data
=========================================================
Utilize an active discovery tool to identify all sensitive information stored, processed, or transmitted by the organization’s technology systems, including those located on-site or at a remote service provider, and update the organization’s sensitive information inventory.

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
* Sub-control 1.4: Maintain Detailed Asset Inventory
* Sub-control 1.5: Maintain Asset Inventory Information
* Sub-control 2.1: Maintain Inventory of Authorized Software
* Sub-control 2.5: Integrate Software and Hardware Asset Inventories

Inputs
-----------
#. The list of endpoints
#. The list of authorized software
#. The inventory of sensitive data

Operations
----------
#. Using the sensitive data inventory, enumerate all endpoints storing, processing, or transmitting sensitive information.
#. Enumerate all sensitive information active monitoring tools from the software inventory
#. For each identified active monitoring tool:
	#. Enumerate the endpoints covered by the system
	#. Examine its configuration to ensure that the system is configured to:
		#. Monitor for sensitive information (noting appropriately and inappropriately configured systems along the way)
#. Enumerate endpoints covered by all sensitive information active monitoring systems
#. Complement the set of covered endpoints with the list of identified endpoints to identify all uncovered endpoints

Assumptions
^^^^^^^^^^^
* Sensitive information monitoring systems are primarily software-based

Measures
--------
* M1 = List of endpoints storing, processing, or transmitting sensitive information
* M2 = List of sensitive information monitoring tools
* M3 = List of monitoring tools appropriately configured
* M4 = List of monitoring tools inappropriately configured
* M5 = List of endpoints covered by at least one monitoring tool
* M6 = List of endpoints not covered by at least one monitoring tool
* M7 = Count of endpoints storing, processing, or transmitting sensitive information (count of M1)
* M8 = Count of sensitive information monitoring tools (count of M2)
* M9 = Count of monitoring tools appropriately configured (count of M3)
* M10 = Count of monitoring tools inappropriately configured (count of M4)
* M11 = Count of endpoints covered by at least one monitoring tool (count of M5)
* M12 = Count of endpoints not covered by at least one monitoring tool (count of M6)

Metrics
-------

Endpoint Coverage
^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The ratio of covered endpoints to the total number of endpoints storing, processing, or
	    | transmitting sensitive information
	* - **Calculation**
	  - :code:`M11 / M7`

Monitoring Coverage
^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The ratio of appropriately configured active sensitive information monitoring tools to
	    | the total number of active sensitive information monitoring tools
	* - **Calculation**
	  - :code:`M9 / M8`

.. history
.. authors
.. license
