12.12: Manage All Devices Remotely Logging Into Internal Network
================================================================
Scan all enterprise devices remotely logging into the organization’s network prior to accessing the network to ensure that each of the organization’s security policies has been enforced in the same manner as local network devices.

.. list-table::
	:header-rows: 1

	* - Asset Type
	  - Security Function
	  - Implementation Groups
	* - Devices
	  - Protect
	  - 3

Dependencies
------------
* Sub-control 16.1: Maintain an Inventory of Authentication Systems

Inputs
-----------
#. List of the organization's authentication systems that allow remote logins (subset of Inventory of Authentication Systems). For each, provide the configuration location(s) for the mechanisms used to ensure remote device security policy enforcement.
#. Approved configuration(s) for each type of remote device security policy enforcement mechanism provided in Input 1

Operations
----------
#. For each authentication system in Input 1, check each of the enforcement mechanisms provided for that authentication system against the appropriate approved configuration(s) provided in Input 2.
	#. Create a list of those authentication systems for which all of the associated enforcement mechanisms comply with the approved configuration(s) noting which configurations were checked (M1).
	#. Create a list of those authentication systems for which at least one of the associated enforcement mechanisms does not comply with the appropriate configurations, noting the configurations checked and any deviations (M2).

Measures
--------
* M1 = List of authentication systems that have properly configured mechanisms in place to ensure that organizational security policies are enforced in remote devices (compliant list)
* M2 = List of authentication systems that do not have properly configured mechanisms in place to ensure that organizational security policies are enforced in remote devices (non-compliant list)
* M3 = Count of authentication systems with properly configured mechanisms in place (count of M1)
* M4 = The total number of authentication systems that allow remote connections (count of Input 1)

Metrics
-------

Coverage
^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The ratio of authentication systems with properly configured mechanisms to ensure that
	    | organizational security policies are enforced in remote devices to the total number of
	    | authentication systems
	* - **Calculation**
	  - :code:`M3 / M4`

.. history
.. authors
.. license
