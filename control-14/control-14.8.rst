14.8: Encrypt Sensitive Information at Rest
=========================================================
Encrypt all sensitive information at rest using a tool that requires a secondary authentication mechanism not integrated into the operating system, in order to access the information.

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
#. Enumerate all encryption tools requiring secondary authentication systems from the software inventory
#. Enumerate all endpoints storing sensitive information using the sensitive information inventory
#. For each identified encryption tool
	#. Enumerate endpoints covered by the encryption tool
#. Enumerate all endpoints covered by at least one encryption tool
#. Complement all covered endpoints with the enumeration of all endpoints storing sensitive information to find those endpoints not covered by at least one encryption tool


Measures
--------
* M1 = List of all encryption tools that require secondary authentication
* M2 = List of all endpoints storing sensitive information
* M3 = List of all endpoints covered by at least one encryption tool
* M4 = List of all endpoints not covered by at least one encryption tool
* M5 = Count of encryption tools that require secondary authentication (count of M1)
* M6 = Count of endpoints storing sensitive information (count of M2)
* M7 = Count of endpoints covered by at least one encryption tool (count of M3)
* M8 = Count of endpoints not covered by at least one encryption tool (count of M4)


Metrics
-------

Coverage
^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The ratio of endpoints covered by an encryption tool to the total number of endpoints
	    | storing sensitive information
	* - **Calculation**
	  - :code:`M7 / M6`

.. history
.. authors
.. license
