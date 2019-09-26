5.4: Deploy System Configuration Management Tools
=========================================================
Deploy system configuration management tools that will automatically enforce and redeploy configuration settings to systems at regularly scheduled intervals.

.. list-table::
	:header-rows: 1

	* - Asset Type
	  - Security Function
	  - Implementation Groups
	* - Applications
	  - Protect
	  - 2, 3

Dependencies
------------
* Sub-control 1.4: Maintain Detailed Asset Inventory
* Sub-control 2.4: Track Software Inventory Information
* Sub-control 5.1: Establish Secure Configurations

Inputs
------
#. The organization's configuration monitoring system
#. The list of endpoints
#. The inventory and mappings of secure configuration policy(ies) to the list of endpoints
#. The organization's approved configuration scanning interval (at least weekly)

Assumptions
^^^^^^^^^^^
#. A timestamp "t" is defined as the time of a given configuration assessment
#. A subsequent assessment, following the approved scanning interval (Input 4), is noted as "t+1"

Operations
----------
#. For each endpoint, obtain the configuration assessment results using Input 1.  Note this as M1(t).
#. Following the time period specified by Input 4, re-assess to obtain a comparative assessment result.  Note this as M1(t+1)

Assumptions
^^^^^^^^^^^
* The assumption is that remediation/redeployment of configuration settings is occurring based on the improvement of scores over time and subsequent assessments.

Measures
--------
* M1(t) = (For each endpoint) Count of non-compliant recommendations resulting from Operation 1
* M1(t+1) = (For each endpoint) Count of non-compliant recommendations resulting from Operation 2
* M2 = (For each endpoint) Count of recommendations assessed
* M3 = The number of endpoints
* M4 = List of non-compliant endpoints resulting from Operation 1
* M5 = List of non-compliant endpoints resulting from Operation 2

Metrics
-------

Initial Non-Compliance
^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The ratio of non-compliant recommendations at time "t", to the total recommendations
	    | assessed.
	* - **Calculation**
	  - :code:`M1(t) / M2`

Subsequent Non-Compliance
^^^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The ratio of non-compliant recommendations at time "t+1" ()
	* - **Calculation**
	  - :code:`M1(t+1) / M2`

Overall Compliance
^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | What is the average overall compliance for all assessed endpoints at time "t"
	* - **Calculation**
	  - :code:`(SUM from 1..M3 (M1(t) / M2)) / M3`

.. history
.. authors
.. license
