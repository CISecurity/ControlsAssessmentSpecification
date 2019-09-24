9.5: Implement Application Firewalls
=========================================================
Place application firewalls in front of any critical servers to verify and validate the traffic going to the server. Any unauthorized traffic should be blocked and logged.

.. list-table::
	:header-rows: 1

	* - Asset Type 
	  - Security Function
	  - Implementation Groups
	* - Devices
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
#. Enumerate endpoints identified as critical in the endpoint inventory
#. Enumerate all application firewalls from the software inventory
#. For each identified application firewall, enumerate the endpoints it covers
	#. Enumerate the set of identified endpoints - covered endpoints
#. Complement the set of covered endpoints with the set of critical endpoints

Measures
--------
* M1 = List of critical endpoints
* M2 = List of application firewalls
* M3 = List of endpoints covered by at least one application firewall
* M4 = List of endpoints not covered by at least one application firewall
* M5 = The number of critical endpoints (count of M1)
* M6 = The number of application firewalls (count of M2)
* M7 = The number of endpoints covered by at least one application firewall (count of M3)
* M8 = The number of endpoints not covered by at least one application firewall (count of M4)

Metrics
-------

Coverage
^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The ratio of endpoints covered by at least one application firewall to the total number
	    | of critical endpoints
	* - **Calculation**
	  - :code:`M7 / M5`

.. history
.. authors
.. license