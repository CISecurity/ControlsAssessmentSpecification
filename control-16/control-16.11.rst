16.11: Lock Workstation Sessions After Inactivity
=========================================================
Automatically lock workstation sessions after a standard period of inactivity.

.. list-table::
	:header-rows: 1

	* - Asset Type
	  - Security Function
	  - Implementation Groups
	* - Users
	  - Protect
	  - 1, 2, 3

Dependencies
------------
* Sub-control 1.4: Maintain Detailed Asset Inventory
* Sub-control 1.5: Maintain Asset Inventory Information
* Sub-control 5.1: Establish Secure Configurations

Inputs
-----------
#. List of workstations which have enabled automatic workstation locking
#. List of workstations
#. The workstation configuration policy establishing the organization's workstation locking time threshold

Operations
----------
#. For each workstation with locking enabled, collect the locking time threshold
#. Collect the list of workstations whose locking time threshold exceeds the value specified by Input 3

Measures
--------
* M1 = List of workstations
* M2 = Count of M1
* M3 = List of workstations having enabled automatic workstation locking
* M4 = Count of M3
* M5 = List of appropriately configured workstations
* M6 = Count of M5
* M7 = List of inappropriately configured workstations
* M8 = Count of M7

Metrics
-------

Misconfigured Workstations
^^^^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | What percentage of automatic locking enabled workstations are configured within
	    | the locking time threshold?
	* - **Calculation**
	  - :code:`M6 / M2`

Unconfigured Workstations
^^^^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - How many workstations do *not* have automatic locking enabled?
	* - **Calculation**
	  - :code:`M2 - M4`

.. history
.. authors
.. license
