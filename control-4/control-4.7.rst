4.7: Limit Access to Scripting Tools
=========================================================
Limit access to scripting tools (such as Microsoft® PowerShell and Python) to only administrative or development users with the need to access those capabilities.

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
* Sub-control 2.1: Maintain Inventory of Authorized Software
* Sub-control 5.1: Establish Secure Configurations
* Sub-control 16.6: Maintain an Inventory of Accounts

Inputs
------
#. Inventory of Accounts including how/where access to scripting tools is restricted
#. List of accounts (administrative or developer accounts) with the need to access scripting tools, including which scripting tools are required for each account
#. Approved configuration(s) to restrict scripting tool access to only approved accounts
#. List of scripting tools to be checked
#. (Optional) List of scripting tools allowed in organization (subset of the Authorized Software List)

Operations
----------
#. For each account in Input 1, determine if the account has access to any of the scripting tools provided in Input 4 by comparing the appropriate approved configuration(s) from Input 3 to the configuration location(s) specified for that account in Input 1. Create a list of accounts that conform to the appropriate configuration(s) and policy for scripting tool access (M1) noting which configuration(s) they were checked against, and a list of accounts that do not conform to the appropriate configuration(s) and policy for scripting tool access (M2) noting the configuration(s) they were checked against and the deviations from those configurations. For each account on both lists, note which, if any, scripting tools that account has access to.
#. (Optional) Compare the scripting tools authorized for particular accounts identified in Input 2 to the authorized scripting tools provided in Input 5. Create a list of scripting tools that are authorized for particular accounts but are not authorized for use in the organization (M5).
#. (Optional) For each account authorized to access scripting tools in M2, verify that the account is an administrative or developer account. Create a list of accounts that are authorized for scripting tools but that are not administrative or developer accounts (M6).

Measures
--------
* M1 = List of accounts that conform to the appropriate configuration(s) and policy for scripting tool access (compliant list)
* M2 = List of accounts that do not conform to the appropriate configuration(s) and policy for scripting tool access (non-compliant list)
* M3 = Count of accounts that are compliant with the scripting tool access policy (count of M1)
* M4 = Total count of accounts (count of Input 1)
* M5 (Optional) = List of scripting tools authorized for particular accounts but not authorized for use in the organization
* M6 (Optional) = List of accounts that are authorized for scripting tools but that are not administrative or developer accounts

Metrics
-------

Coverage
^^^^^^^^
.. list-table::

	* - **Metric**
	  - | Ratio of accounts that comply with the scripting tool access policy
	* - **Calculation**
	  - :code:`M3 / M4`

.. history
.. authors
.. license
