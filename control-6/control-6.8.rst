6.8: Regularly Tune SIEM
=========================================================
On a regular basis, tune your SIEM system to better identify actionable events and decrease event noise.

.. list-table::
	:header-rows: 1

	* - Asset Type 
	  - Security Function
	  - Implementation Groups
	* - Network
	  - Detect
	  - 3

Status
------
Draft

Dependencies
------------
* None

Inputs
------
#. Enterprise-defined SIEM operation procedures
#. Current time

Operations
----------
#. Examine enterprise SIEM operation procedures to identify maximum allowed delay in tuning frequency (default: 1 week)
#. Ask SIEM operators when they last tuned the SIEM

Measures
--------
* M1 = Boolean value, 1, if a set of enterprise-defined SIEM operational procedures exists, 0 otherwise
* M2 = Maximum allowed delay in tuning
* M3 = Current time
* M4 = Last SIEM tuning time

Metrics
-------

Procedure Existence
^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | Does an enterprise-defined set of SIEM operational procedures exist?
	* - **Calculation**
	  - :code:`M1 = 1?`

SIEM Tuning Freshness
^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | How recently was the SIEM last tuned?
	* - **Calculation**
	  - :code:`(M3 - M4) / M2`

.. history
.. authors
.. license