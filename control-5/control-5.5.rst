5.5: Implement Automated Configuration Monitoring Systems
=========================================================

Utilize a Security Content Automation Protocol (SCAP) compliant configuration monitoring system to verify all security configuration elements, catalog approved exceptions, and alert when unauthorized changes occur.

.. list-table::
	:header-rows: 1

	* - Asset Type 
	  - Security Function
	  - Implementation Groups
	* - Applications
	  - Detect
	  - 2, 3

Status
------
Draft

Inputs
------
#. The organization's configuration monitoring system
#. The list (maintained by NIST) of SCAP-validated tools
#. The list of endpoints
#. The inventory and mappings of secure configuration policy(ies) to the list of endpoints
#. The list of approved exceptions, mapped to the endpoints on which they are approved (i.e. some endpoints may be excepting certain configurations, but others under the same configuration policy may not).
#. The organization's approved configuration scanning interval (at least weekly)

Operations
----------
#. (Manual) Ensure the configuration scanning tool (Input 1) is present in the list of SCAP-validated tools (Input 2).
#. For each endpoint, obtain the configuration assessment results using Input 1
#. For each assessment result in Operation 2, obtain the list of recommendations which map to the catalog of approved exceptions for that endpoint.
#. Following the time period specified by Input 6, re-assess to obtain a comparative assessment result

Measures
--------
* M1 = 1 if Operation 1 indicates the organization's scanning tool is present in the list of SCAP-validated tools; 0 otherwise
* M2 = (For each endpoint) The number of non-compliant recommendations resulting from Operation 2
* M3 = (For each endpoint) The number of non-compliant recommendations that do not map to the catalog of approved exceptions for the endpoint
* M4 = (For each endpoint) The number of non-compliant recommendations resulting from Operation 4
* M5 = (For each endpoint) The number of non-compliant recommendations that do not map to the catalog of approved exceptions for the endpoint
* M6 = (For each endpoint) The number of recommendations assessed
* M7 = (For each endpoint) The number of approved configuration policy exceptions
* M8 = The number of the organization's SCAP-validated tools
* M9 = The number of the organization's configuration management tools

Metrics
-------

Tooling Compliance
^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | Are SCAP-validated configuration scanning tool(s) being used?
	* - **Calculation**
	  - :code:`M1 == 1`

Tooling Compliance Coverage
^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The ratio of SCAP-validated tools to the total number of configuration management tools
	* - **Calculation**
	  - :code:`M8 / M9`

Initial Non-Compliance (Per Endpoint)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | Per endpoint, the ratio of non-compliant recommendations to the total recommendations
	    | assessed.
	* - **Calculation**
	  - :code:`M2 / M6`

Initial Exception Coverage (Per Endpoint)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | Per endpoint, the ratio of non-compliant recommendations with approved exceptions, to 
	    | the total recommendations assessed.
	* - **Calculation**
	  - :code:`(M7 - M3) / M7`

Subsequent Non-Compliance (Per Endpoint)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | Per endpoint, the ratio of non-compliant recommendations to the total recommendations
	    | assessed.
	* - **Calculation**
	  - :code:`M4 / M6`

Subsequent Exception Coverage (Per Endpoint)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | Per endpoint, the ratio of non-compliant recommendations with approved exceptions, to
	    | the total recommendations assessed.
	* - **Calculation**
	  - :code:`(M7 - M5) / M7`

.. history
.. authors
.. license