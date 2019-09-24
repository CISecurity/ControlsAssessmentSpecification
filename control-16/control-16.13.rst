16.13: Alert on Account Login Behavior Deviation
=========================================================
Alert when users deviate from normal login behavior, such as time-of-day, workstation location, and duration.

.. list-table::
	:header-rows: 1

	* - Asset Type
	  - Security Function
	  - Implementation Groups
	* - Users
	  - Detect
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

Operations
----------
#. Enumerate user behavioral monitoring software systems
#. Enumerate endpoints
#. For each identified behavioral monitoring system
	#. Enumerate endpoints covered by this behavioral monitoring system
	#. Examine the system's configuration, noting appropriate and inappropriate configurations along the way, to ensure that it is configured to alert for at least the following deviation points:
		#. Time of day
		#. Workstation location
		#. Duration
#. Enumerate all endpoints covered by at least one behavioral monitoring system
#. Complement covered endpoints with the list of all endpoints to enumerate the list of endpoints not covered by at least one behavioral monitoring system
#. Enumerate all appropriately configured behavioral monitoring systems
#. Enumerate all inappropriately configured behavioral monitoring systems

Measures
--------
* M1 = List of user behavioral monitoring software systems
* M2 = List of endpoints
* M3 = List of endpoints covered by at least one behavioral monitoring system
* M4 = List of endpoints not covered by at least one behavioral monitoring system
* M5 = List of appropriately configured behavioral monitoring systems
* M6 = List of inappropriately configured behavioral monitoring systems
* M7 = Count of user behavioral monitoring software systems (count of M1)
* M8 = Count of endpoints (count of M2)
* M9 = Count of endpoints covered by at least one behavioral monitoring system (count of M3)
* M10 = Count of endpoints not covered by at least one behavioral monitoring system (count of M4)
* M11 = Count of appropriately configured behavioral monitoring systems (count of M5)
* M12 = Count of inappropriately configured behavioral monitoring systems (count of M6)

Metrics
-------

Endpoint Coverage
^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The ratio of endpoints covered by at least one behavioral monitoring system to the
	    | total number of endpoints
	* - **Calculation**
	  - :code:`M9 / M8`

Behavioral Monitoring System Coverage
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The ratio of appropriately configured behavioral monitoring systems to the total
	    | number of behavioral monitoring systems
	* - **Calculation**
	  - :code:`M11 / M7`

.. history
.. authors
.. license
