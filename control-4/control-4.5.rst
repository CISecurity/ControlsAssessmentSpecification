4.5: Implement and Manage a Firewall on End-User Devices
==================================================================
Implement and manage a host-based firewall or port-filtering tool on end-user devices, with a default-deny rule that drops all traffic except those services and ports that are explicitly allowed.

.. list-table::
	:header-rows: 1

	* - Asset Type
	  - Security Function
	  - Implementation Groups
	* - Devices
	  - Protect
	  - 1, 2, 3

Dependencies
------------
* Safeguard 1.1: Establish and Maintain Detailed Enterprise Asset Inventory
* Safeguard 2.1: Establish and Maintain a Software Inventory
* Safeguard 4.1: Establish and Maintain a Secure Configuration Process

Inputs
------
#. :code:`GV1`: Enterprise asset inventory
#. :code:`GV5`: Authorized software inventory
#. :code:`GV3`: Configuration standard

Operations
----------
#. Identify and enumerate end-user devices capable of hosting a firewall or a deny rule using :code:`GV1` (M1)
#. Using configuration standards :code:`GV3` to check if firewalls or deny rules are properly configured on end-user devices
	#. Enumerate assets from Operation 1 with properly configured firewalls or a configured default deny rule (M3)
	#. Enumerate assets from Operation 1 with improperly configured firewalls and lacking a configured default deny rule(M4)

Measures
--------
* M1 = Count of end-user devices capable of hosting a firewall
* M2 = Count of end-user devices with a properly configured firewall or default deny rule
* M3 = Count of end-user devices with an improperly configured firewall and lacking a configured default deny rule

Metrics
-------

Coverage
^^^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The percentage of properly configured firewalls or deny rule on end-user devices
	* - **Calculation**
	  - :code:`M2 / M1`



.. history
.. authors
.. license
