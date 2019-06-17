4.2: Change Default Passwords
=============================
Before deploying any new asset, change all default passwords to have values consistent with administrative level accounts.

.. list-table::
	:header-rows: 1

	* - Asset Type 
	  - Security Function
	  - Implementation Groups
	* - Users
	  - Protect
	  - 1, 2, 3

Status
------
Draft

Inputs
------
#. The organization's inventory of endpoints which utilize credentials, either at the OS level or at the application software level
#. An authoritative source of known default password hashes
#. The organization's defined password policy configuration

Operations
----------
#. For each endpoint, enumerate the available logins, including hashed credentials (M1)
#. For each login, compare the password hash to the authoritative source of known default password hashes
#. For each endpoint, collect the applied password policy configuration
#. For each endpoint, compare the password policy configuration to the organizationally defined password policy recommendations (including password length, complexity requirements, etc.)

Measures
--------
* M1 = The enumerated list of available logins for endpoints which utilized credentialed accounts
* M2 = The number of available logins who's password hash matches a known default password hash
* M3 = The enumerated list of the sampled endpoint password policy configurations
* M4 = The number of sampled password policy configurations that do not match organizationally defined recommendations.


Metrics
-------

Default Password Usage
^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Question**
	  - | What percentage of credentials have been changed from the default value?
	* - **Answer**
	  - | This metric yields the ratio of credentials which have been changed from
	    | the default to the total number of credentials.
	* - **Calculation**
	  - | * If M2 = 0, then no accounts remain configured with the default password.
	    | * Otherwise, the value of this metric is :code:`(M1 - M2) / M1`

Password Policy Compliance
^^^^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Question**
	  - | What percentage of total accounts comply with the organization's password policies?
	* - **Answer**
	  - | This metric yields the ratio of compliant accounts to the total number of accounts.
	* - **Calculation**
	  - | * If M4 = 0, then no accounts deviate from the organization's password policies.
	    | * Otherwise, the value of this metric is :code:`(M3 - M4) / M3`

.. history
.. authors
.. license