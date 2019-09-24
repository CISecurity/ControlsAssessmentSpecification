7.10: Sandbox All Email Attachments
=========================================================
Use sandboxing to analyze and block inbound email attachments with malicious behavior.

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
* Subcontrol 2.1: Maintain Inventory of Authorized Software

Inputs
------
#. The list of authorized software

Operations
----------
#. Enumerate all e-mail servers in the enterprise
#. For each identified e-mail server, examine its configuration to ensure that either native attachment sandboxing is configured or that an external system is configured to be used for that purpose, noting appropriately and inappropriately configured servers

Assumptions
^^^^^^^^^^^
* The majority of e-mail servers have appropriate configuration attributes to examine.

Measures
--------
* M1 = List of all e-mail servers in the enterprise
* M2 = List of appropriately configured e-mail servers
* M3 = List of inappropriately configured e-mail servers
* M4 = The number of all e-mail servers in the enterprise (count of M1)
* M5 = The number of appropriately configured e-mail servers (count of M2)
* M6 = The number of inappropriately configured e-mail servers (count of M3)

Metrics
-------

Coverage
^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The ratio of appropriately configured e-mail servers to the total number of e-mail 
	    | servers
	* - **Calculation**
	  - :code:`M5 / M4`

.. history
.. authors
.. license