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
#. An authoritative source of known default passwords
#. The organization's defined password policy configuration

Operations
----------
#. For each endpoint in Input 1, enumerate the available logins, including hashed credentials (becomes M1)
#. For each endpoint in Input 1, generate password hashes for all relevant default passwords provided in Input 2 in accordance with the corresponding hashing procedures for the appropriate OS, application, etc. including any applicable salting
#. For each login, compare the password hash for that login to the default password hashes generated in the previous operation.  Create a list containing any logins that have hashes that match default password hashes, including the endpoint to which the login corresponds and the default password and hash that was matched (becomes M3)
#. For each endpoint, collect the applied password policy configuration (becomes M5)
#. For each endpoint, compare the password policy configuration to the organizationally defined password policy recommendations (including password length, complexity requirements, etc.), creating a list of endpoint password policies that adhere to organizational policy (becomes M7) and a list of endpoint password policies that deviate from the organizational policy (becomes M9) noting where the deviations occur.

Measures
--------
* M1 = The list of available logins for endpoints which utilized credentialed accounts
* M2 = The count of logins from all endpoints that use credentiale accouts (count of M1)
* M3 = The list of enumerated logins with a password hash that matches a known default password hash
* M4 = The count of logins with a password hash that matches a known default password hash (count of M3)
* M5 = The list of the collected endpoint password policy configurations
* M6 = The count of collected password policy configurations (count of M5)
* M7 = The list of collected password policy configurations that do match organizationally defined recommendations
* M8 = The count of compliant collected password policies (count of M7)
* M9 = The list of collected password policy configurations that do not match organizationally defined recommendations

Metrics
-------

Default Password Usage
^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | What percentage of credentials have been changed from the default value?
	* - **Calculation**
	  - | :code:`(M2 - M4) / M2`

Password Policy Compliance
^^^^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | What percentage of collected password policies comply with the organization's password policies?
	* - **Calculation**
	  - | If M6 = 0, then no endpoint password policy configurations were collected. Otherwise, the value of this metric is :code:`M8 / M6`

.. history
.. authors
.. license
