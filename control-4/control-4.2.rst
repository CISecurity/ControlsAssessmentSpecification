4.2: Establish and Maintain a Secure Configuration Process for Network Infrastructure
=============================
Establish and maintain a secure configuration process for network devices. Review and update documentation annually, or when significant enterprise changes occur that could impact this Safeguard.

.. list-table::
	:header-rows: 1

	* - Asset Type
	  - Security Function
	  - Implementation Groups
	* - Network
	  - Protect
	  - 1, 2, 3

Dependencies
------------
* Safeguard 2.1: Establish and Maintain a Software Inventory

Inputs
------
#. :code:`GV2`: Authorized software inventory
#. :code:`GV1`: Enterprise asset inventory
#. :code:`GV3`: Configuration Standard: this should include any enterprise approved deviations from industry standard baselines  such as CIS benchmarks, DISA Security Technical Implementation Guides (STIGs), or U.S. government configuration baselines (USGCB).
#. Date of last review and updat of configuration standard

Operations
----------
#. Identify whether Input 2 exists
	#. If it exists M1 = 1
	#. If it does not exist M1 = 0
#. Identify and enumerate network infrastructure assets in :code:`GV1` (M2)
#. Using the output of Operation 2 (M2), identify and enumerate the software installed on the assets using :code:`GV2` (M3)
#. For each software identified in Operation 3 (M3)
	#. Enumerate software that is listed in the configuration standard :code:`GV3`(M4)
	#. Enumerate software that is not listed in the configuration standard :code:`GV3`(M5)
#. Compare current date to date provided in Input 4.  Note the timeframe in months (M6)

Measures
--------
* M1 = Output of Operation 1
* M2 = Count of applicable enterprise assets 
* M3 = Count of software insalled on applicable enterprise assets
* M4 = Count of software that is listed in the configuration standard
* M5 = Count of software that is not listed in the configuration standard
* M6 = Timeframe since last review and update in months

Metrics
-------
* If M1 is 0, this safeguard receives a failing score. The other metrics don't apply.
* If M6 is greater than twelve, this safeguard is measured at a 0 and receives a failing score. The other metrics don't apply.

Standard Configuration Coverage
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The perecentage of authorized software  with secure configuration standards documented
	  - | and maintained.
	* - **Calculation**
	  - :code:`M4 / M3`

.. authors
.. license
