11.5: Test Data Recovery
=========================================================
Test backup recovery quarterly, or more frequently, for a sampling of in-scope enterprise assets.

.. list-table::
	:header-rows: 1

	* - Asset Type
	  - Security Function
	  - Implementation Groups
	* - Data
	  - Recover
	  - 2, 3

Dependencies
------------
* Safeguard 1.1: Establish and Maintain Detailed Enterprise Asset Inventory

Inputs
------
#. Current set of backups for the enterprise
#. Date of last backup recovery test

Assumption
^^^^^^^^^^
#. Enterprise will know what a properly working restored backup looks like. 

Operations
----------
#. Use Input 1 to restore a sampling of the backups to a temporary location
	#. Enumerate the total numer of backups restored (M1)
	#. Identify and enumerate backups that are properly working after being restored (M2)
	#. Identify and enumerate backups that did not properly work after being restored (M3)
#. Compare Input 2 to current date and capture time frame in months (M4)

Measures
--------
* M1 = Count of backups being tested
* M2 = Count of properly working backups after restoration 
* M3 = Count of backups not properly working after restoration
* M4 = Timeframe between tests of backup recovery

Metrics
-------

If M4 is greater than three months, then this safeguard is measured at a 0 and receives a failing score. The other metrics don't apply.
 
Backup Integrity Quality
^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The percentage of restored backups sampling deemed to be properly working
	* - **Calculation**
	  - :code:`M2 / M1`


.. history
.. authors
.. license
