16.12: Monitor Attempts to Access Deactivated Accounts
=========================================================
Monitor attempts to access deactivated accounts through audit logging.

.. list-table::
	:header-rows: 1

	* - Asset Type 
	  - Security Function
	  - Implementation Groups
	* - Users
	  - Detect
	  - 2, 3

Status
------
Draft

Dependencies
------------
* Subcontrol 2.1: Maintain Inventory of Authorized Software
* Subcontrol 16.1: Inventory of Authentication Systems

Inputs
-----------
#. Authentication System Inventory
#. Approved configuration(s) for logging attempts to access deactivated accounts
#. Approved configuration(s) for alerting on attempts to access deactivated accounts

**Note**: There may be multiple configurations for Inputs 2 and 3 to account for various groups/types of authentication systems.

Operations
----------
#. For each authentication system in Input 1, select the appropriate approved configuration from Inputs 2 and 3 in turn for that endpoint and check to see if that authentication system's actual configuration complies with the approved configuration for each Input.  Record this information as M1 - a list of authentication systems annotated with whether that authentication system is compliant or non-compliant with the appropriate approved configuration from each of the two inputs (Input 2 and Input 3).
#. For Input 2, and for Input 3, generate a count of compliant authentication systems from M1 and record these as M2 and M3 respectively.
#. Count the number of authentication systems that are compliant with both inputs and record this as M4

Measures
--------
* M1 = List of authentication systems with each endpoint entry labeled with compliance or non-compliance for both Input 2 and Input 3
* M2 = Number of compliant authentication systems based on Input 2 configurations
* M3 = Number of compliant authentication systems based on Input 3 configurations
* M4 = Number of authentication systems that are compliant with configurations from both inputs
* M5 = Total number of authentication systems from Input 1

Metrics
-------

Logging Coverage
^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The ratio of authentication systems configured to log attempts to access deactivated
	    | accounts to the total number of authentication systems.
	* - **Calculation**
	  - :code:`M2 / M5`

Alerting Coverage
^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The ratio of authentication systems configured to log attempts to access deactivated
	    | accounts to the total number of authentication systems.
	* - **Calculation**
	  - :code:`M3 / M5`

Full Coverage
^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The ratio of authentication systems configured to both log and alert on attempts to
	    | access deactivated accounts to the total number of authentication systems.
	* - **Calculation**
	  - :code:`M4 / M5`

.. history
.. authors
.. license