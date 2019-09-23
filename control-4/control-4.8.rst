4.8: Log and Alert on Changes to Administrative Group Membership
================================================================
Configure systems to issue a log entry and alert when an account is added to or removed from any group assigned administrative privileges.

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
* Sub-control 5.1: Establish Secure Configurations

Inputs
------
#. Endpoint inventory
#. Approved configuration(s) for logging of accounts being added to groups with administrative privileges
#. Approved configuration(s) for logging of accounts being removed from groups with administrative privileges
#. Approved configuration(s) for alerting when accounts are added to groups with administrative privileges
#. Approved configuration(s) for alerting when accounts are removed from groups with administrative privileges

**Note**: there may be multiple configurations for Inputs 2 - 5 to account for various groups/types of endpoints.

Operations
----------
#. For each endpoint in Input 1, select the appropriate approved configuration from Inputs 2 - 5 in turn for that endpoint and check to see if that endpoint's actual configuration complies with the approved configuration for each Input. Record this information as M1 - a list of endpoints annotated with whether that endpoint is compliant or non-compliant with the appropriate approved configuration from each of the four inputs (Input 2 - Input 5).
#. For each of the Inputs 2 - 5, generate a count of compliant endpoints from M1 and record these as M2, M3, M4, and M5 respectively
#. Count the number of endpoints that are compliant with all 4 inputs and record this as M6

Measures
--------
* M1 = List of endpoints with each endpoint entry labeled with compliance or non-compliance for each of the 4 logging/alerting configurations from Inputs 2 - 5
* M2 = Count of compliant endpoints based on Input 2 configurations
* M3 = Count of compliant endpoints based on Input 3 configurations
* M4 = Count of compliant endpoints based on Input 4 configurations
* M5 = Count of compliant endpoints based on Input 5 configurations
* M6 = Count of endpoints that are compliant with configurations from all 4 inputs
* M7 = Count of endpoints from Input 1
* M8 = List of compliant endpoints based on Input 2 configurations
* M9 = List of non-compliant endpoints based on Input 2 configurations
* M10 = List of compliant endpoints based on Input 3 configurations
* M11 = List of non-compliant endpoints based on Input 3 configurations
* M12 = List of compliant endpoints based on Input 4 configurations
* M13 = List of non-compliant endpoints based on Input 4 configurations
* M14 = List of compliant endpoints based on Input 5 configurations
* M15 = List of non-compliant endpoints based on Input 5 configurations
* M16 = Count of non-compliant endpoints based on Input 2 configurations
* M16 = Count of non-compliant endpoints based on Input 3 configurations
* M16 = Count of non-compliant endpoints based on Input 4 configurations
* M16 = Count of non-compliant endpoints based on Input 5 configurations


Metrics
-------

Logging of Accounts Added to Groups
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The ratio of endpoints logging when accounts are added to groups to the total number
	    | of endpoints
	* - **Calculation**
	  - :code:`M2 / M7`

Logging of Accounts Removed from Groups
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The ratio of endpoints logging when accounts are removed from groups to the total number
	    | of endpoints
	* - **Calculation**
	  - :code:`M3 / M7`

Alerting of Accounts Added to Groups
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The ratio of endpoints alerting when accounts are added to groups to the total number
	    | of endpoints
	* - **Calculation**
	  - :code:`M4 / M7`

Alerting of Accounts Removed from Groups
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The ratio of endpoints alerting when accounts are removed from groups to the total
	    | number of endpoints
	* - **Calculation**
	  - :code:`M5 / M7`

Combined Compliance
^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The ratio of endpoints both alerting and logging when accounts are both added and
	    | removed to the total number of endpoints
	* - **Calculation**
	  - :code:`M6 / M7`

.. history
.. authors
.. license
