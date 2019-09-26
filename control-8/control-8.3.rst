8.3: Enable Operating System Anti-Exploitation Features/ Deploy Anti-Exploit Technologies
=========================================================================================
Enable anti-exploitation features such as Data Execution Prevention (DEP) and Address Space Layout Randomization (ASLR) that are available in an operating system or deploy appropriate toolkits that can be configured to apply protection to a broader set of applications and executables.

.. list-table::
	:header-rows: 1

	* - Asset Type
	  - Security Function
	  - Implementation Groups
	* - Devices
	  - Detect
	  - 2, 3

Dependencies
------------
* Sub-control 1.4: Maintain Detailed Asset Inventory
* Sub-control 1.5: Maintain Asset Inventory Information
* Sub-control 5.1: Establish Secure Configurations

Inputs
-----------
#. List of endpoints
#. Approved configuration(s) to enable anti-exploitation features (Operating System feature, toolkit, etc.) for each type of endpoint in Input 1

Operations
----------
#. For each endpoint in Input 1, examine the endpoint to see if it is configured according to the approved configuration(s).
#. Create a list of the endpoints that meet the the approved configurations (M1)
#. Create a list of the endpoints that do not meet the approved configurations (M2), noting each deviation.

Measures
--------
* M1 = Count of endpoints that meet the approved anti-exploitation configurations, such as DEP, ASLR or similar technologies (compliant list)
* M2 = Count of endpoints
* M3 (Optional) = List of endpoints that meet the approved anti-exploitation configurations, such as DEP, ASLR or similar technologies (compliant list)
* M4 (Optional) = List of endpoints that do not meet the approved anti-exploitation configurations, such as DEP, ASLR or similar technologies (non-compliant list)
* M5 (Optional) = Count of non-compliant endpoints (M2 - M1)
* M6 = List of non-compliant endpoints

Metrics
-------
.. list-table::

	* - **Metric**
	  - | Ratio of endpoints compliant with anti-exploitation configurations to the total
	    | number of endpoints
	* - **Calculation**
	  - :code:`M1 / M2`

.. history
.. authors
.. license
