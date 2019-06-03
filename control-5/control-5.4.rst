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

Status
------
Draft

Assumptions
-----------
* The configuration management system has access to and authority to apply configuration settings to the systems under test.

Measures
--------
* M1 = number of configurations that are enforced
* M2 = number of total configurations in the system
* M3 = last deployment time
* M4 = current time
* M5 = deployment interval threshhold

Metrics
-------

Enforcement Quality
^^^^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Question**
	  - Determine the percentage of total system configurations which are currently being enforced.
	* - **Answer**
	  - The calculation will yield a percentage, from 0 to 100, indicating the ratio of total system configurations to those currently being enforced.
	* - **Calculation**
	  - :code:`((M1 - M2) / M1) * 100`

Enforcement Freshness
^^^^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Question**
	  - Ensure configuration enforcement is occurring at a regular interval.
	* - **Answer**
	  - The calculation will yield a true or false answer for each system under test.  If configurations are enforced on the system within the (re)deployment threshold, enforcement is considered "fresh".
	* - **Calculation**
	  - :code:`if ((M4 - M3) <= M5) then TRUE; otherwise FALSE`

.. history
.. authors
.. license