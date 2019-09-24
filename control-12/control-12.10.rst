12.10: Decrypt Network Traffic at Proxy
=========================================================
Decrypt all encrypted network traffic at the boundary proxy prior to analyzing the content.  However, the organization may use whitelists of allowed sites that can be accessed through the proxy without decrypting the traffic.

.. list-table::
	:header-rows: 1

	* - Asset Type 
	  - Security Function
	  - Implementation Groups
	* - Network
	  - Detect
	  - 3

Status
------
Draft

Dependencies
------------
* Subcontrol 2.1: Maintain Inventory of Authorized Software

Inputs
-----------
#. The list of authorized software
#. The list of authorized sites not requiring decryption before analysis

Operations
----------
#. Enumerate each boundary proxy system
#. For each identified proxy system, examine its configuration as follows, noting appropriately and inappropriately configured systems:
	#. Encrypted network traffic is decrypted prior to analysis, when traffic is not related to an authorized site
#. Enumerate the set of appropriately configured proxy systems
#. Enumerate the set of inappropriately configured proxy systems

Measures
--------
* M1 = List of boundary proxy systems
* M2 = List of appropriately configured boundary proxy systems
* M3 = List of inappropriately configured boundary proxy systems
* M4 = The number of boundary proxy systems (count of M1)
* M5 = The number of appropriately configured boundary proxy systems (count of M2)
* M6 = The number of inappropriately configured boundary proxy systems (count of M3)

Metrics
-------

Coverage
^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The ratio of appropriately configured boundary proxy systems to the total number
	    | of boundary proxy systems
	* - **Calculation**
	  - :code:`M5 / M4`

.. history
.. authors
.. license