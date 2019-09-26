20.7: Ensure Results From Penetration Test Are Documented Using Open, Machine-Readable Standards
================================================================================================
Wherever possible, ensure that Red Team results are documented using open, machine-readable standards (e.g., SCAP). Devise a scoring method for determining the results of Red Team exercises so that results can be compared over time.

.. list-table::
	:header-rows: 1

	* - Asset Type
	  - Security Function
	  - Implementation Groups
	* - N/A
	* - N/A
	  - 3

Dependencies
------------
* Sub-control 20.1: Establish a Penetration Testing Program

Inputs
-----------
#. Enterprise red team policy
#. Latest red team result documentation

Operations
----------
#. Examine the enterprise red team policy for the following properties:
	#. Red team documentation is machine-readable
	#. Red team documentation is based on open specification
	#. Red team results must be scored to support ongoing comparison
#. Examine the latest red team results documentation to verify
	#. Documentation is machine-readable
	#. Documentation is based on open specification
	#. Current score was compared to previous score

Measures
--------
* M1 = (Boolean) 1 if the Policy demands machine-readable red team results documentation; 0 otherwise
* M2 = (Boolean) 1 if the Policy demands open specification for machine-readable results; 0 otherwise
* M3 = (Boolean) 1 if the Policy demands results to be scored to support ongoing comparison; 0 otherwise
* M4 = (Boolean) 1 if the Last red team results are machine-readable; 0 otherwise
* M5 = (Boolean) 1 if the Last red team results are based on an open specification; 0 otherwise
* M6 = (Boolean) 1 if the Last red team results includes current and previous score for comparison.  In the event the current score is the result of the enterprise's first red team exercise, this can be set to 1; 0 otherwise

Metrics
-------

Policy Conformance
^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | Is the enterprise's Red Team policy specified to produce results using open, machine
	    | readable standards, and is scoring designed to facilitate ongoing comparison?
	* - **Calculation**
	  - :code:`M1 AND M2 AND M3`

Operational Conformance
^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | Is the enterprise's Red Team policy being practiced operationally?
	* - **Calculation**
	  - :code:`M4 AND M5 AND M6`

.. history
.. authors
.. license
