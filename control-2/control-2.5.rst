2.5: Allowlist Authorized Software
=========================================================
Use technical controls, such as application allowlisting, to ensure that only authorized software can execute or be accessed. Reassess bi-annually, or more frequently.

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
* Safeguard 1.1: Establish and Maintain Detailed Enterprise Asset Inventory
* Safeguard 2.1: Establish and Maintain a Software Inventory
* Safeguard 2.3: Address Unauthorized Software
* Safeguard 4.1: Establish and Maintain a Secure Configuration Process

Inputs
------
#. :code:`GV7`: Software capable assets
#. :code:`GV5`: Authorized software inventory
#. :code:`GV3`: Approved configuration Standards
#. Date of last assessment of this safeguard

Operations
----------
#. Using :code:`GV7` identify and enumerate assets capable of supporting allowlisting software (some assets may not enable third-party software installation or otherwise have constrained environments precluding the use of allowlisting software) (M1).
#. Using :code:`GV5` identify all authorized allowlisting software within the enterprise (:code:`GV8`)
#. Using the output from Operation 1 and authorized allowlisting software :code:`GV8`
	#. Identify and enumerate allowlisting capable assets with allowlisting software installed (M2)
	#. Identify and enumerate allowlisting capable assets without allowlisting software installed (M3)
#. Use :code:`GV3` to identify allowlisting software configurations (:code:`GV9`)
#. For each asset with allowlisting software installed (M2) from Operation 2 use the output from Operation 3 to 
	#. Identify and enumerate properly configured software (M4)
	#. Identify and enumerate improperly configured software (M5)
#. Compare Input 4 to current date and note timeframe in months (M6)

Measures
--------
* M1 = Count of enterprise assets capable of supporting allowlisting software
* M2 = Count of enterprise assets capable of supporting allowlisting software and have the software installed
* M3 = Count of enterprise assets capable of supporting allowlisting software and do not have the software installed
* M4 = Count of enterprise assets with allowlisting software that is properly configured 
* M5 = Count of enterprise assets with allowlisting software that is properly configured
* M6 = Timeframe since last assessment of this safeguard

Metrics
-------
* If M6 is greater than six months, then this safeguard is measured at a 0 and receives a failing score. The other metrics don’t apply.

Allowlisting Installation Coverage
^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The percentage of enterprise assets capable of supporting allowlisting with allowlisting installed
	* - **Calculation**
	  - :code:`M2 / M1`

Allowlisting Configuration Coverage
^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The percentage of enterprise assets with properly configured allowlisting installed
	* - **Calculation**
	  - :code:`M4 / M2`

.. history
.. authors
.. license
