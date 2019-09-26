16.4: Encrypt or Hash All Authentication Credentials
=========================================================
Encrypt or hash with a salt all authentication credentials when stored.

.. list-table::
	:header-rows: 1

	* - Asset Type
	  - Security Function
	  - Implementation Groups
	* - Users
	  - Protect
	  - 2, 3

Dependencies
------------
* Sub-control 16.1: Inventory of Authentication Systems

Inputs
-----------
#. Inventory of Authentication Systems (for each, include any related components used for credential storage for that authentication system such as any databases that require configuration independent of the authentication system)
#. Approved configuration(s) to ensure that all credentials are encrypted and/or hashed with a salt when stored.  There may be multiple configurations to handle the different types of authentication systems used in the organization, and configurations may also be required for related components involved in storing this data (i.e. database configurations).

Operations
----------
#. For each authentication system provided in Input 1 (along with any listed related components), check to see if it is configured properly according to the appropriate configuration(s) provided in Input 2.
#. Create a list of the authentication systems that are properly configured (M1)
#. Create a list of the authentication systems that are not properly configured (M2) including the deviations from proper configuration (if any related component identified in Input 1 is not configured according to the appropriate configuration, then its associated authentication system should be considered improperly configured, and the specific component should be noted as part of the deviation from proper configuration).

Measures
--------
* M1 = List of properly configured authentication systems (compliant list)
* M2 = List of improperly configured authentication systems (non-compliant list)
* M3 = Count of properly configured authentication systems (count of M1)
* M4 = Total count of authentication systems (count of Input 1)

Metrics
-------

Coverage
^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The ratio of properly configured authentication systems to the total number of
	    | authentication systems.
	* - **Calculation**
	  - :code:`M3 / M4`

.. history
.. authors
.. license
