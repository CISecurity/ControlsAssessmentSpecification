15.8: Use Wireless Authentication Protocols That Require Mutual, Multi-Factor Authentication
============================================================================================
Ensure that wireless networks use authentication protocols such as Extensible Authentication Protocol-Transport Layer Security (EAP/TLS), that requires mutual, multi-factor authentication.

.. list-table::
	:header-rows: 1

	* - Asset Type 
	  - Security Function
	  - Implementation Groups
	* - Network
	  - Protect
	  - 3

Status
------
Draft

Dependencies
------------
* Subcontrol 1.4: Maintain Detailed Asset Inventory
* Subcontrol 1.5: Maintain Asset Inventory Information

Inputs
-----------
#. The list of endpoints
#. The list of authorized authentication protocols

Operations
----------
#. Enumerate all wireless access points
#. For each identified wireless access point, examine its configuration for the following noting appropriately and inappropriately configured endpoints along the way:
	#. Configured authentication protocol (compare to list of authorized authentication protocols)
#. Enumerate all appropriately configured endpoints
#. Enumerate all inappropriately configured endpoints

Measures
--------
* M1 = List of all wireless access points
* M2 = List of appropriately configured wireless access points
* M3 = List of inappropriately configured wireless access points
* M4 = The number of wireless access points (count of M1)
* M5 = The number of appropriately configured wireless access points (count of M2)
* M6 = The number of inappropriately configured wireless access points (count of M3)

Metrics
-------

Coverage
^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The ratio of appropriately configured wireless access points to the total number of
	    | wireless access points
	* - **Calculation**
	  - :code:`M5 / M4`

.. history
.. authors
.. license