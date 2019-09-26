13.2: Remove Sensitive Data or Systems Not Regularly Accessed by Organization
=============================================================================
Remove sensitive data or systems not regularly accessed by the organization from the network.  These systems shall only be used as stand-alone systems (disconnected from the network) by the business unit needing to occasionally use the system or completely virtualized and powered off until needed.

.. list-table::
	:header-rows: 1

	* - Asset Type
	  - Security Function
	  - Implementation Groups
	* - Data
	  - Protect
	  - 1, 2, 3

Dependencies
------------
* Sub-control 1.4: Maintain Detailed Asset Inventory
* Sub-control 13.1: Maintain an Inventory of Sensitive Information

Inputs
-----------
#. List of sensitive systems (ideally using the endpoint inventory; see sub-control 1.4)
#. The access frequency for any sensitive systems
#. An organizationally-defined access frequency threshold

Assumptions
^^^^^^^^^^^
* Access to sensitive data takes place through some system, therefore the system, when processing, storing, or transmitting sensitive data, is a sensitive system.
* Isolation/exposure score of zero is assumed ideal

Operations
----------
#. Determine subset of sensitive systems that are infrequently used (using all Inputs)
#. For each infrequently used sensitive system, calculate isolation/exposure

Measures
--------
* M1 = List of all systems used to process sensitive information
* M2 = Count of M1
* M3 = Set of infrequently used sensitive systems
* M4 = Count of infrequently used sensitive systems
* M5 = List of infrequently used sensitive systems with isolation/exposure scores greater than 0
* M6 = Count of M4

Metrics
-------

Coverage
^^^^^^^^
.. list-table::

	* - **Metric**
	  - What percentage of infrequently used sensitive systems are not properly isolated?
	* - **Calculation**
	  - :code:`M6 / M4`

.. history
.. authors
.. license
