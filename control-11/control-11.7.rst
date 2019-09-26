11.7: Manage Network Infrastructure Through a Dedicated Network
===============================================================
Manage the network infrastructure across network connections that are separated from the business use of that network, relying on separate VLANs or, preferably, on entirely different physical connectivity for management sessions for network devices.

.. list-table::
	:header-rows: 1

	* - Asset Type
	  - Security Function
	  - Implementation Groups
	* - Network
	  - Protect
	  - 2, 3

Dependencies
------------
* None

Inputs
------
#. List of management/administration paths for network infrastructure

Operations
----------
#. For each management path in Input 1, use a tool or process (which might be manual review) to determine if that management network connection is separate from all business (non-network management) network connections.
#. Create a list (M1) of the management paths that are separate from all non-network management network connections (noting the type of network separation - VLAN, physical, etc.)
#. Create a list of the management paths that do not have adequate separation from non-network management connections (M2) noting the deviations.

Measures
--------
* M1 = List of network management paths that are adequately separated (compliant list)
* M2 = List of network management paths that are not adequately separated (non-compliant list)
* M3 = Count of adequately separated network management paths (count of M1)
* M4 = Total count of network management paths (count of Input 1)

Metrics
-------

Coverage
^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The ratio of adequately separated management paths to the total number of management
	    | paths.
	* - **Calculation**
	  - :code:`M3 / M4`

.. history
.. authors
.. license
