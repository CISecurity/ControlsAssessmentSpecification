4.9: Log and Alert on Unsuccessful Administrative Account Login
===============================================================
Configure systems to issue a log entry and alert on unsuccessful logins to an administrative account.

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
* Sub-control 1.4: Maintain Detailed Asset Inventory

Inputs
------
#. Endpoint inventory
#. Approved configuration(s) for logging on unsuccessful login attempts to administrative accounts
#. Approved configuration(s) for alerting on unsuccessful login attempts to administrative accounts

**Note**: there may be multiple configurations for Inputs 2 and 3 to account for various groups/types of endpoints.

Operations
----------
#. For each endpoint in Input 1, select the appropriate approved configuration from Inputs 2 and 3 in turn for that endpoint and check to see if that endpoint's actual configuration complies with the approved configuration for each Input. Record this information as M1 - a list of endpoints annotated with whether that endpoint is compliant or non-compliant with the appropriate approved configuration from each of the two inputs (Input 2 and Input 3).
#. For Input 2, and for Input 3, generate a count of compliant endpoints from M1 and record these as M2 and M3 respectively.
#. Count the number of endpoints that are compliant with both inputs and record this as M4

Measures
--------
* M1 = List of endpoints with each endpoint entry labeled with compliance or non-compliance for both Input 2 and Input 3
* M2 = Count of compliant endpoints based on Input 2 configurations
* M3 = Count of compliant endpoints based on Input 3 configurations
* M4 = Count of endpoints that are compliant with configurations from both inputs
* M5 = Total number of endpoints from Input 1
* M6 = List of compliant endpoints based on Input 2 configurations
* M7 = List of non-compliant endpoints based on Input 2 configurations
* M8 = List of compliant endpoints based on Input 3 configurations
* M9 = List of non-compliant endpoints based on Input 3 configurations
* M10 = Count of non-compliant endpoints based on Input 2 configurations
* M11 = Count of non-compliant endpoints based on Input 3 configurations


Metrics
-------

Logging Unsuccessful Login Attempts
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The ratio of endpoints logging when unsuccessful login attempts are made, to the total
	    | number of endpoints
	* - **Calculation**
	  - :code:`M2 / M5`

Alerting Unsuccessful Login Attempts
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The ratio of endpoints alerting when unsuccessful login attempts are made, to the total
	    | number of endpoints
	* - **Calculation**
	  - :code:`M3 / M5`


Combined Compliance
^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The ratio of endpoints both alerting and logging unsuccessful login attempts are made,
	    | to the total number of endpoints
	* - **Calculation**
	  - :code:`M4 / M5`

.. history
.. authors
.. license
