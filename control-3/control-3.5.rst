3.5: Deploy Automated Software Patch Management Tools
=====================================================
Deploy automated software update tools in order to ensure that third-party software on all systems is running the most recent security updates provided by the software vendor.

.. list-table::
	:header-rows: 1

	* - Asset Type
	  - Security Function
	  - Implementation Groups
	* - Applications
	  - Protect
	  - 1, 2, 3

Dependencies
------------
* Sub-control 2.1: Maintain Inventory of Authorized Software

Inputs
------
#. From the authorized software list (ASL; sub-control 2.1), information on the current authorized version.
#. Access to an authoritative source of information indicating version details by product.
#. A list of approved exceptions, noting any reasons that an authorized software package does not match the latest version.

Operations
----------
#. For each software in Input 1, list the software products which do not match the latest version as described by Input 2.
#. For each endpoint, obtain the current software load (the list of installed software).
#. For each endpoint, list the installed software that does not match the current authorized version from Input 1.
#. For each software product listed in Operation 3, list any that exist in the approved exceptions list (Input 3).

Measures
--------
* M1 = List of authorized software products installed on the endpoint which are not at the latest version.
* M2 = Count of M1
* M3 = List of authorized software products installed on the endpoint.
* M4 = Count of M3
* M5 = List of authorized software products installed on the endpoint which are not at the latest version, but have approved exceptions.
* M6 = Count of M5

Metrics
-------

Update Effectiveness (Per Endpoint)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | For a given endpoint, calculate the ratio of installed software updates to the
	    | total number of required software updates.
	* - **Calculation**
	  - | If :code:`M2 == 0`, this indicates the endpoint requires no software updates.
	    | If :code:`(M2 - M5) == 0`, this indicates the endpoint requires software updates,
	    | but the out-of-date software has an approved exception.
	    | Otherwise, this metric is calculated as :code:`(M2 - M5) / M4`

Update Effectiveness (Organizational)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The organizational metric is calculated by averaging the results of the "per endpoint" metric above.

.. history
.. authors
.. license
