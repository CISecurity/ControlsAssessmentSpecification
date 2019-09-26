18.3: Verify That Acquired Software Is Still Supported
=========================================================
Verify that the version of all software acquired from outside your organization is still supported by the developer or appropriately hardened based on developer security recommendations.

.. list-table::
	:header-rows: 1

	* - Asset Type
	  - Security Function
	  - Implementation Groups
	* - N/A
	  - N/A
	  - 2, 3

Dependencies
------------
* Sub-control 2.1: Maintain Inventory of Authorized Software
* Sub-control 2.2: Ensure Software is Supported by Vendor
* Sub-control 5.1: Establish Secure Configurations

Inputs
-----------
#. List of software acquired from outside the organization, including version information for each (subset of Authorized Software List from Sub-Control 2.1). As described in Sub-Control 2.2, this list should also include the supported or unsupported status for each.
#. The list of organizational security configuration standards from Sub-Control 5.1

Operations
----------
#. For each software version listed in Input 1, check the list of organizational security configuration standards provided in Input 2.
	#. Create a list of software versions that have at least one associated organizational security configuration standard (M1) including identifiers for the associated standard(s)
	#. Create a list of software versions that do not have any associated organizational security configuration standards (M2)
#. For each software version listed in M2, check the supported/unsupported status field for that software version in Input 1 to see if that product version is still supported by the developer.
	#. Create a list of software versions that appear in M2 and are not supported (M3).

Measures
--------
* M1 = List of externally acquired software that has an associated organizational security configuration standard
* M2 = List of externally acquired software that does not have an associated organizational security configuration standard
* M3 = List of externally acquired software that does not have an associated organizational security configuration standard and is also not supported by the developer (non-compliant list)
* M4 = Count of externally acquired software that does not have an associated organizational security configuration standard and is also not supported by the developer (count of M3)
* M5 = Total count of externally acquired software (count of Input 1)

Metrics
-------

Coverage
^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The ratio of externally acquired software that is either supported or has an associated
	    | organizational security configuration standard
	* - **Calculation**
	  - :code:`(M5 - M4) / M5`

.. history
.. authors
.. license
