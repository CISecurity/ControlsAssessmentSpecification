7.6: Perform Automated Vulnerability Scans of Externally-Exposed Enterprise Assets
=========================================================
Perform automated vulnerability scans of externally-exposed enterprise assets using a SCAP-compliant vulnerability scanning tool. Perform scans on a monthly, or more frequent, basis. 

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
#. :code:`GV25`: Vulnerability scanning software
#. :code:`GV3`: Configuration standard

Operations
----------
#. Use the :code:`GV1` enterprise asset inventory to identify and enumerate all external assets (M2)
#. Use the output of Operation 1 and :code:`GV25` to
	#. Identify and enumerate external assets covered by at least one vulnerability scanning software (M3)
	#. Identify and enumerate external assets not covered by at least one vulnerability scanning software (M4)
#. Use the :code:`GV25` and :code:`GV3` 
	#. Identify and enumerate vulnerability scanners properly configured to scan every 30 days or less (M5)
	#. Identify and enumerate vulnerability scanners not properly configured to scan every 30 days or less (M6)

Measures
--------
* M1 = Count of authorized :code:`GV25` vulnerability scanning software
* M2 = Count of external enterprise assets
* M3 = Count of external assets covered by a vulnerability scanner
* M4 = Count of external assets not covered by a vulnerability scanner
* M5 = Count of vulnerability scanners properly configured to run every 30 days or less
* M6 = Count of vulnerability scanners not properly configured to run every 30 days or less

Metrics
-------

Coverage of Vulnerability Scans
^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The percentage of external assets covered by a vulnerability scanner
	* - **Calculation**
	  - :code:`M3 / M2`

Compliance of Vulnerability Scans
^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The percentage of vulnerability scanners properly configured to
	  - | scan every 30 days or less
	* - **Calculation**
	  - :code: `M5 / M1`


.. history
.. authors
.. license
