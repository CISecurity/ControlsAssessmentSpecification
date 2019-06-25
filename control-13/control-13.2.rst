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

Status
------
Draft

Inputs
-----------
#. List of sensitive systems
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
* M1 = Set of infrequently used sensitive systems
* M2 = Number of infrequently used sensitive systems with isolation/exposure scores greater than 0


Metrics
-------

Coverage
^^^^^^^^
.. list-table::

	* - **Question**
	  - What percentage of infrequently used sensitive systems are not properly isolated?
	* - **Answer**
	  - 
	* - **Calculation**
	  - :code:`M2 / M1`

.. history
.. authors
.. license