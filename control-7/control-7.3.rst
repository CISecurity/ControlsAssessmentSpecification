7.3: Perform Automated Operating System Patch Management
=======================================================================
Perform operating system updates on enterprise assets through automated patch management on a monthly, or more frequent, basis.

.. list-table::
	:header-rows: 1

	* - Asset Type
	  - Security Function
	  - Implementation Groups
	* - Applications
	  - Protect
	  - 1, 2, 3

Dependencies
------------
* Safeguard 1.1: Establish and Maintain Detailed Enterprise Asset Inventory
* Safeguard 2.1: Establish and Maintain a Software Inventory
* Safeguard 4.1: Establish and Maintain a Secure Configuration Process

Inputs
------
#. :code:`GV5`: Authorized software inventory	
#. :code:`GV1`: Enterprise asset inventory
#. Authoritative source of information indicating version details by product
#. :code:`GV3`: Configuration standards

Operations
----------
#. Use :code:`GV5` to identify authorized operating systems within the enterprise
#. Use :code:`GV1` and the output of Operation 1 to identify the operating system currently running on each asset (M1)
#. For each asset, compare the version of the operating system to that listed in Input 4
	#. Identify and enumerate operating systems that are up to date (M2)
	#. Identify and enumerate operating systems that are not up to date (M3)
#. For each operating system idetified in Operation 2.2, determine whether there is a documented exception 
	#. Identify and enumerate operating systems with a documented exception (M4)
	#. Identify and enumerate operating systems without a documented exception (M5)
#. Use :code:`GV5` to identify authorized automated patch management software (M6)
#. Compare output of Operation 5 and Operation 1
	#. Identify and enumerate operating systems covered by at least one automated patch management software (M7)
	#. Identify and enumerate operating systems not covered by at least one automated patch management software (M8)
#. Check configurations of automated patch mangement software identified in Operation 5 using :code:`GV3`
	#. Identify and enumerate those configured to run every 30 days or less (M9)
	#. Identify and enumerate those not configured to run every 30 days or less (M10)


Measures
--------
* M1 = Count of authorized operating sytem installed on an asset
* M2 = Count of up to date operating system installed on an asset
* M3 = Count of operating system installed on an asset that is not up to date
* M4 = Count of not up to date operating system with a documented exception
* M5 = Count of not up to date operating system without a documented exception
* M6 = Count of authorized automated patch management software
* M7 = Count of operating systems covered by at least one automated patch management software
* M8 = Count of operating systems not covered by at least one automated patch management software
* M9 = Count of automated patch management software properly configured to run every 30 days or less
* M10 = Count of automated patch management software not properly configured to run every 30 days

Metrics
-------

Update Effectiveness (Per Asset)
^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The percent of operating system on an asset that are up to date
	* - **Calculation**
	  - :code:`(M2 + M4) / M1`

Update Effectiveness (Organizational)
^^^^^^^^
Calculate the organizational metric by averaging the asset scores 

Coverage of Automation
^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The percent of operating systems covered by at least one automated patch
	  - | management software.
	* - **Calculation**
	  - :code:`M7 / M1`

Scan Compliance
^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The percent of automated patch management software configured to run 
	  - | every 30 days or less.
	* - **Calculation**
	  - :code:`M9 / M6`

.. history
.. authors
.. license
