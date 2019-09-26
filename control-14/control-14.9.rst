14.9: Enforce Detail Logging for Access or Changes to Sensitive Data
====================================================================
Enforce detailed audit logging for access to sensitive data or changes to sensitive data (utilizing tools such as File Integrity Monitoring or Security Information and Event Monitoring).

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
#. The list of sensitive information

Operations
----------
#. Enumerate all endpoints storing sensitive information using the endpoint inventory and the sensitive information inventory
#. For each identified endpoint, examine its configuration as follows noting appropriately and inappropriately configured endpoints along the way:
	#. Detailed audit logging is enabled for access to sensitive data
	#. Detailed audit logging is enabled for changes to sensitive data
#. Enumerate appropriately configured endpoints
#. Enumerate inappropriately configured endpoints
#. Enumerate endpoints inappropriately configured to log access to sensitive data
#. Enumerate endpoints inappropriately configured to log changes to sensitive data

Measures
--------
* M1 = List of all endpoints storing sensitive information
* M2 = List of appropriately configured endpoints (those that have detailed audit logging enabled for access and changes to sensitive data)
* M3 = List of inappropriately configured endpoints (those that do not have detailed audit logging enabled for access or changes to sensitive data)
* M4 = List of endpoints inappropriately configured to log access to sensitive data
* M5 = List of endpoints inappropriately configured to log changes to sensitive data
* M6 = Count of endpoints storing sensitive information (count of M1)
* M7 = Count of appropriately configured endpoints (count of M2)
* M8 = Count of inappropriately configured endpoints (count of M3)
* M9 = Count of endpoints inappropriately configured to log access to sensitive data (count of M4)
* M10 = Count of endpoints inappropriately configured to log changes to sensitive data (count of M5)

Metrics
-------

Coverage
^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The ratio of appropriately configured endpoints to the total number of endpoints storing
	    | sensitive information
	* - **Calculation**
	  - :code:`M7 / M6`

.. history
.. authors
.. license
