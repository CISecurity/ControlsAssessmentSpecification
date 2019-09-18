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

Status
------
Draft

Dependencies
------------
* Subcontrol 1.4: Maintain Detailed Asset Inventory
* Subcontrol 1.5: Maintain Asset Inventory Information

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
* M1 = Number of workstations which have enabled automatic workstation locking
* M2 = Number of workstations which have enabled automatic locking exceeding the organization's threshold (the count from Operation 2).
* M3 = Number of workstations

Metrics
-------

Misconfigured Workstations
^^^^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | What percentage of automatic locking enabled workstations are configured outside
	    | the locking time threshold?
	* - **Calculation**
	  - :code:`M2 / M1`

Unconfigured Workstations
^^^^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - How many workstations do *not* have automatic locking enabled?
	* - **Calculation**
	  - :code:`M3 - M1`

.. history
.. authors
.. license