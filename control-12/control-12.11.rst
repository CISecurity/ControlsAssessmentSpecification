12.11: Require All Remote Logins to Use Multi-Factor Authentication
===================================================================
Require all remote login access to the organization’s network to encrypt data in transit and use multi-factor authentication.

.. list-table::
	:header-rows: 1

	* - Asset Type 
	  - Security Function
	  - Implementation Groups
	* - Users
	  - Protect
	  - 2, 3

Status
------
Draft

Dependencies
------------
* Subcontrol 1.4: Maintain Detailed Asset Inventory
* Subcontrol 1.5: Maintain Asset Inventory Information

Inputs
-----------
#. List of authorized remote hosts

Operations
----------
#. For each host in the list of authorized remote hosts, check the remote access software configuration:
	#. Encrypted connections are required
	#. Multi-factor authentication is required

Measures
--------
* M1 = Count of authorized remote hosts
* M2 = Count of authorized remote hosts with encryption required
* M3 = Count of authorized remote hosts with multi-factor authentication required
* M4 = Count of authorized remote hosts with both encryption and multi-factor authentication required

Metrics
-------

Encryption Coverage
^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | Percentage of authorized remote hosts without encryption required
	* - **Calculation**
	  - :code:`(M1 - M2) / M1`

Multi-Factor Authentication Coverage
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | Percentage of authorized remote hosts without multi-factor authentication required
	* - **Calculation**
	  - :code:`(M1 - M3) / M1`

Total Coverage
^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | Percentage of authroized remote hosts without encryption or multi-factor authentication
	    | required
	* - **Calculation**
	  - :code:`(M1 - M4) / M1`

.. history
.. authors
.. license