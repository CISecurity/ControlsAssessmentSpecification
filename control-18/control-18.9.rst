18.9: Separate Production and Non-Production Systems
=========================================================
Maintain separate environments for production and non-production systems. Developers should not have unmonitored access to production environments.

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
* Sub-control 1.4: Maintain Detailed Asset Inventory
* Sub-control 1.5: Maintain Asset Inventory Information
* Sub-control 2.1: Maintain Inventory of Authorized Software
* Sub-control 2.5: Integrate Software and Hardware Asset Inventories

Inputs
-----------
#. The inventory of systems used for production and non-production deployments
#. The inventory of user accounts
#. The mechanism for monitoring user account access to systems

Operations
----------
#. From Input 1, categorize the deployments of systems into those with production deployments and those with non-production deployments.  Note that systems *should* have both production and 1..n non-production deployments (including development, staging, integration testing, etc).
#. From Input 2, determine the list of user accounts with access to production environments

Measures
--------
* M1(i) = (For each system with a production deployment "i") 1 if at least one non-production deployment environment exists for that system, 0 otherwise.
* M2 = Count of systems with a production deployment
* M3 = Count of user accounts whose access to production environments is monitored by the mechanism defined by Input 3.
* M4 = Count of user accounts with access to production environments (the count from Operation 2).

Metrics
-------

Environment Coverage
^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The ratio of production systems where at least one non-production deployment exists
	    | to the total number of production systems
	* - **Calculation**
	  - :code:`(SUM from i=1..M2 (M1(i))) / M2`

Monitored Account Coverage
^^^^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The ratio of accounts with production system access that are monitored to the total
	    | accounts with production system access
	* - **Calculation**
	  - :code:`M3 / M4`

.. history
.. authors
.. license
