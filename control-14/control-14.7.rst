14.7: Enforce Access Control to Data Through Automated Tools
=========================================================
Use an automated tool, such as host-based Data Loss Prevention, to enforce access controls to data even when the data is copied off a system.

.. list-table::
	:header-rows: 1

	* - Asset Type 
	  - Security Function
	  - Implementation Groups
	* - Data
	  - Protect
	  - 3

Status
------
Draft

Dependencies
------------
* Subcontrol 1.4: Maintain Detailed Asset Inventory
* Subcontrol 1.5: Maintain Asset Inventory Information
* Subcontrol 2.1: Maintain Inventory of Authorized Software
* Subcontrol 2.5: Integrate Software and Hardware Asset Inventories

Inputs
-----------
#. The list of endpoints
#. The list of authorized software

Operations
----------
#. Enumerate endpoints capable of storing data
#. Enumerate all DLP software
#. For each instance of DLP software:
	#. Enumerate the endpoints covered by the DLP software
#. Enumerate all endpoints covered by the set of DLP software
#. Complement the list of covered endpoints with the list of endpoints enumerated in the first operation to get the enumeration of endpoints not covered

Measures
--------
* M1 = List of endpoints capable of storing data
* M2 = List of DLP software instances
* M3 = List of all endpoints covered by the set of DLP software
* M4 = List of all endpoints not covered by the set of DLP software
* M5 = The number of endpoints capable of storing data (count of M1)
* M6 = The number of DLP software instances (count of M2)
* M7 = The number of endpoints covered by the set of DLP software (count of M3)
* M8 = The number of endpoints not covered by the set of DLP software (count of M4)

Metrics
-------

Coverage
^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The ratio of endpoints covered by at least one DLP software instance to the total
	    | number of endpoints capable of storing data
	* - **Calculation**
	  - :code:`M7 / M5`

.. history
.. authors
.. license