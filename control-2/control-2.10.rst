2.10: Physically or Logically Segregate High Risk Applications
==============================================================
Physically or logically segregated systems should be used to isolate and run software that is required for business operations but incurs higher risk for the organization.

.. list-table::
	:header-rows: 1

	* - Asset Type 
	  - Security Function
	  - Implementation Groups
	* - Applications
	  - Protect
	  - 3

Status
------
Draft

Dependencies
------------
* Subcontrol 2.1: Maintain Inventory of Authorized Software

Inputs
------
#. List of approved high-risk applications (subset of Approved Software List). For each, include the mechanisms used to provide separation.
#. Approved configuration(s) for each separation mechanism listed in Input 1

Operations
----------
#. For each application in Input 1, compare the configurations of the associated separation mechanisms to the appropriate approved configuration(s) from Input 2.
	#. Create a list of applications that are adequately separated noting which configuration(s) were checked (M1)
	#. Create a list of applications that are not adequately separated noting which configurations were checked and any deviations

Measures
--------
* M1 = List of high-risk applications that are properly segregated (compliant list)
* M2 = List of high-risk applications that are not properly segregated (non-compliant list)
* M3 = The number of high-risk applications that are properly segregated (count of M1)
* M4 = The total number of approved high-risk applications (count of Input 1)

Metrics
-------

.. list-table::

	* - **Metric**
	  - | The ratio of properly separated high-risk applications to the total number of high-risk
	    | applications
	* - **Calculation**
	  - :code:`M3 / M4`

.. history
.. authors
.. license