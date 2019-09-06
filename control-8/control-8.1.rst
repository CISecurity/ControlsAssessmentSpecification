8.1: Utilize Centrally Managed Anti-Malware Software
=========================================================
Utilize centrally managed anti-malware software to continuously monitor and defend each of the organization’s workstations and servers.

.. list-table::
	:header-rows: 1

	* - Asset Type 
	  - Security Function
	  - Implementation Groups
	* - Devices
	  - Protect
	  - 2, 3

Status
------
Draft

Dependencies
------------
* Subcontrol 1.4: Maintain Detailed Asset Inventory
* Subcontrol 1.5: Maintain Asset Inventory Information
* Subcontrol 2.1: Maintain Inventory of Authorized Software

Assumption(s)
^^^^^^^^^^^^^
* It is assumed that this sub-control is specific to host-based anti-malware solutions.

Inputs
------
#. List of deployed anti-malware software
#. The list of endpoints

Operations
----------
#. For each deployed anti-malware solution, verify that it is centrally managed
#. For each deployed anti-malware solution, enumerate the set of endpoints covered
#. Union the set of covered endpoints
#. Identify set of endpoints eligible for anti-malware coverage (i.e. network devices likely do not run anti-malware agents)

Measures
--------
* M1 = Base count of anti-malware solutions in use
* M2 = Count of anti-malware solutions that are centrally managed
* M3 = Total number of endpoints covered by anti-malware solutions
* M4 = Total number of endpoints eligible for anti-malware coverage

Metrics
-------

Anti-Malware Management Coverage
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | Percentage of anti-malware solutions that are centrally managed
	* - **Calculation**
	  - :code:`M2 / M1`


Endpoint Anti-Malware Coverage
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | Percentage of endpoints covered by anti-malware solutions
	* - **Calculation**
	  - :code:`M3 / M4`


.. history
.. authors
.. license