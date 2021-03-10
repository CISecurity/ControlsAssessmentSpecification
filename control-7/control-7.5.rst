7.5: Perform Automated Vulnerability Scans of Internal Enterprise Assets
=========================================================
Perform automated vulnerability scans of internal enterprise assets on a quarterly, or more frequent, basis. Conduct both authenticated and unauthenticated scans, using a SCAP-compliant vulnerability scanning tool.

.. list-table::
	:header-rows: 1

	* - Asset Type
	  - Security Function
	  - Implementation Groups
	* - Applications
	  - Identify
	  - 2, 3

Dependencies
------------
* Safeguard 1.1: Establish and Maintain Detailed Enterprise Asset Inventory
* Safeguard 2.1: Establish and Maintain a Software Inventory
* Safeguard 4.1: Establish and Maintain a Secure Configuration Process

Inputs
------
#. :code:`GV1`: Enterprise asset inventory
#. :code:`GV5`: Authorized software inventory
#. :code:`GV3`: Configuration standard

Operations
----------
#. Use the :code:`GV5`authorized software inventory to
	#. Identify and enumerate :code:`GV25` vulnerability scanning software (M1)
	#. Identify and enumerate authenticated vulnerability scanning software (M2)
#. Use the :code:`GV1` enterprise asset inventory to identify and enumerate all internal assets (M3)
#. Use the output of Operation 2 and Operation 1.1 
	#. Identify and enumerate internal assets covered by at least one vulnerability scanning software (M4)
	#. Identify and enumerate internal assets not covered by at least one vulnerability scanning software (M5)
#. Use the output of Operation 2 and Operation 1.2
	#. Identify and enumerate internal assets covered by at least one authenticated vulnerability scanner (M6)
	#. Identify and enumerate internal assets not covered by at least one authenticated vulnerability scanner (M7)
#. Use the output of Operation 1.1 and :code:`GV3` 
	#. Identify and enumerate vulnerability scanners properly configured to scan every 3 months or less (M8)
	#. Identify and enumerate vulnerability scanners not properly configured to scan every 3 months or less (M9)
#. Use the output of Operation 1.2 and :code:`GV3` 
	#. Identify and enumerate authenticated vulnerability scanners properly configured to scan every 3 months or less (M10)
	#. Identify and enumerate authenticated vulnerability scanners not properly configured to scan every 3 months or less (M11)

Measures
--------
* M1 = Count of authorized vulnerability scanning software
* M2 = Count of authorized authenticated vulnerability scanning software
* M3 = Count of internal enterprise assets
* M4 = Count of internal assets covered by a vulnerability scanner
* M5 = Count of internal assets not covered by a vulnerability scanner
* M6 = Count of internal assets covered by an authenticated vulnerability scanner
* M7 = Count of internal assets not covered by an authenticated vulnerability scanner
* M8 = Count of vulnerability scanners properly configured to run every 3 months or less
* M9 = Count of vulnerability scanners not properly configured to run every 3 months or less
* M10 = Count of authenticated vulnerability scanners properly configured to run every 3 months or less
* M11 = Count of authenticated vulnerability scanners not properly configured to run every 3 months or less

Metrics
-------

Coverage of Vulnerability Scans
^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The percentage of internal assets covered by a vulnerability scanner
	* - **Calculation**
	  - :code:`M4 / M3`

Coverage of Authenticated Scans
^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The percentage of internal assets covered by an authenticated 
	  - | vulnerability scanner
	* - **Calculation**
	  - :code:`M6 / M3`

Compliance of Vulnerability Scans
^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The percentage of vulnerability scanners properly configured to
	  - | scan every 3 months or less
	* - **Calculation**
	  - :code:`M8 / M1`

Compliance of Authenticated Scans
^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The percentage of authenticated vulnerability scanners properly 
	  - | configured to scan every 3 months or less
	* - **Calculation**
	  - :code:`M10 / M2`

.. history
.. authors
.. license
