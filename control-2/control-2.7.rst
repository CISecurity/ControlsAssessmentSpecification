2.7: Allowlist Authorized Scripts
=========================================================
Use technical controls, such as digital signatures and version control, to ensure that only authorized scripts, such as specific .ps1, .py, etc. files, are allowed to execute. Block unauthorized scripts from executing. Reassess bi-annually, or more frequently.

.. list-table::
	:header-rows: 1

	* - Asset Type
	  - Security Function
	  - Implementation Groups
	* - Applications
	  - Protect
	  - 3

Dependencies
------------
* Safeguard 2.1: Establish and Maintain a Software Inventory
* Safeguard 4.2: Establish and Maintain a Secure Configuration Process for Network Infrastructure

Inputs
------
#. Authorized software inventory with detailed information
#. The list of authorized scripts
#. Approved configuration (s) for allowlisting software
#. Date of last assessement of this safeguard

Operations
----------
#. Using Input 1, identify and note all allowlisting software authorized within the enterprise (M1)
#. For each item identified in the output of Operation 1 (M1), use the approved configurations from Input 3 and authorized scripts list from Input 2
	#. Identify and note allowlisting software properly configured to allow execution of authorized and signed scripts (M2)
	#. Identify and note allowlisting software improperly configured to allow execution of authorized and signed scripts (M3)
#. Compare the date from Input 4 to current date and note timeframe in months (M4).

Measures
--------
* M1 = Count of authorized allowlisting software 
* M2 = Count of properly configured allowlisting software
* M3 = Count of improperly configured allowlisting software
* M4 = Timeframe since last assessment of this safeguard


Metrics
-------

* If M4 is greater than six months, then this safeguard is measured at a 0 and receives a failing score. The other metrics don’t apply.

Coverage
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The percentage of appropriately configured allowlisting software instances within the enterprise. 
	* - **Calculation**
	  - :code:`M2 / M1`


.. history
.. authors
.. license
