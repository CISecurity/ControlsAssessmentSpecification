2.6: Allowlist Authorized Libraries
================================
Use technical controls to ensure that only authorized software libraries, such as specific .dll, .ocx, .so, etc. files, are allowed to load into a system process. Block unauthorized libraries from loading into a system process. Reassess bi-annually, or more frequently.

.. list-table::
	:header-rows: 1

	* - Asset Type
	  - Security Function
	  - Implementation Groups
	* - Applications
	  - Protect
	  - 2, 3

Dependencies
------------
* Safeguard 2.1: Establish and Maintain a Software Inventory
* Safeguard 2.5: Allowlist Authorized Software
* Safegaurd 4.2: Establish and Maintain a Secure Configuration Process for Network Infrastructure

Inputs
------
#. Authorized software inventory with detailed information
#. The list of authorized software libraries
#. Approved configuration (s) for allowlisting software
#. Date of last assessement of this safeguard

Operations
----------
#. Using Input 1, identify and note all allowlisting software authorized within the enterprise (M1).
#. For each item identified in the output of Operation 1 (M1), use the approved configurations from Input 3 and authorized library list from Input 2
	#. Identify and note allowlisting software properly configured to allow process loading of authorized libraries (M2)
	#. Identify and note allowlisting software improperly configured to allow process loading of authorized libraries (M3)
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
