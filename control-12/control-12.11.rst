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
* Sub-control 1.4: Maintain Detailed Asset Inventory
* Sub-control 1.5: Maintain Asset Inventory Information

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
* M1 = Count of authorized remote hosts (from Input 1)
* M2 = List of authorized remote hosts with encryption required
* M3 = Count of M2
* M4 = List of authorized remote hosts without encryption required
* M5 = Count of M4
* M6 = List of authorized remote hosts with multi-factor authentication required
* M7 = Count of M6
* M8 = List of authorized remote hosts without multi-factor authentication required
* M9 = Count of M8
* M10 = List of authorized remote hosts with both encryption and multi-factor authentication required
* M11 = Count of M10
* M12 = List of authorized remote hosts without either encryption or multi-factor authentication required
* M13 = Count of M12

Metrics
-------

Encryption Coverage
^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | Ratio of authorized remote hosts with encryption required to the total number of authorized remote hosts
	* - **Calculation**
	  - :code:`M3 / M1`

Multi-Factor Authentication Coverage
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | Ratio of authorized remote hosts with multi-factor authentication required to the total number of authorized remote hosts
	* - **Calculation**
	  - :code:`M7 / M1`

Total Coverage
^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | Ratio of authorized remote hosts with both encryption and multi-factor authentication required to the total number of authorized remote hosts
	    | required
	* - **Calculation**
	  - :code:`M11 / M1`

.. history
.. authors
.. license
