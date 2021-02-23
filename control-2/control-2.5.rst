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
* Safeguard 4.2: Establish and Maintain a Secure Configuration Process for Network Infrastructure

Inputs
------
#. Detailed enterprise asset inventory
#. Authorized software inventory with detailed information
#. Approved configuration (s) for allowlisting software 

Operations
----------
#. Using Input 1 identify and note assets capable of supporting allowlisting software (some assets may not enable third-party software installation or otherwise have constrained environments precluding the use of allowlisting software) (M1).
#. Using the output from Operation 1 and authorizes software inventory from Input 2
	#. Identify and note allowlisting capable assets with allowlisting software installed (M2)
	#. Identify and note allowlisting capable assets without allowlisting software installed (M3)
#. For each asset with allowlisting software installed (M2) from Operation 2 use Input 3 to check and
	#. Note properly configured software (M4)
	#. Note improperly configured software (M5)

Measures
--------
* M1 = Count of enterprise assets capable of supporting allowlisting software
* M2 = Count of enterprise assets capable of supporting allowlisting software and have the software installed
* M3 = Count of enterprise assets capable of supporting allowlisting software and do not have the software installed
* M4 = Count of enterprise assets with allowlisting software that is properly configured 
* M5 = Count of enterprise assets with allowlisting software that is properly configured

Metrics
-------

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
