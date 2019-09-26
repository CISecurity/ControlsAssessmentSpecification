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

Dependencies
------------
* Sub-control 2.4: Track Software Inventory Information

Inputs
------
#. The organization's inventory of endpoints which utilize credentials, either at the OS level or at the application software level (ideally software inventory from sub-control 2.4)
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
* M1 = The list of available logins for endpoints which utilized credentialed accounts
* M2 = The count of M1
* M3 = The list of enumerated logins who's password has matches a known default password hash
* M4 = The count of M3
* M5 = The list of the sampled endpoint password policy configurations
* M6 = The count of M5
* M7 = The list of sampled password policy configurations that do not match organizationally defined recommendations
* M8 = The count of M7
* M9 = The list of sampled password policy configurations that do match organizationally defined recommendations
* M10 = The count of M9

Metrics
-------

Default Password Usage
^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | What percentage of credentials have been changed from the default value?
	* - **Calculation**
	  - | * If M4 = 0, then no accounts remain configured with the default password.
	    | * Otherwise, the value of this metric is :code:`(M2 - M4) / M2`

Password Policy Compliance
^^^^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | What percentage of total accounts comply with the organization's password policies?
	* - **Calculation**
	  - | * If M4 = 0, then no accounts deviate from the organization's password policies.
	    | * Otherwise, the value of this metric is :code:`(M3 - M4) / M3`

.. history
.. authors
.. license
