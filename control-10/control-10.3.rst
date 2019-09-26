10.3: Test Data on Backup Media
=========================================================
Test data integrity on backup media on a regular basis by performing a data restoration process to ensure that the backup is properly working.

.. list-table::
	:header-rows: 1

	* - Asset Type
	  - Security Function
	  - Implementation Groups
	* - Data
	  - Protect
	  - 2, 3

Dependencies
------------
* Sub-control 1.4: Maintain Detailed Asset Inventory
* Sub-control 1.5: Maintain Asset Inventory Information

Inputs
-----------
#. The current set of backup media for the organization
#. t(i): the timestamp at which a backup restoration i has been performed
#. N: the number of backup restorations (timestamps) performed so far
#. M: the maximum possible irregularity (can be fixed as 30 day)
#. T: (optional) target/desirable review interval threshold
#. D: the number of backup restorations in which at least one anomaly was detected
#. L: The total number of backup restorations

Operations
----------
#. Given a sampling of backup media from Input 1, restore the backup to a temporary location

Assumption
^^^^^^^^^^
* The assumption is made that the organization will know what a "properly working" restored backup entails.

Measures
--------
* M1 = Count of backups under test
* M2 = Count of restored backups deemed "properly working" following restoration
* M3 = The average of backup restorations = :code:`SUM from i=1..N ( t(i+1) - t(i) ) / N`
* M4 (Regularity Measure of Backup Restoration) = :code:`(SUM from i=1..N ((t(i+1) - t(i)) - M3)^2 / N ) / M`
* M5 (Threshold-based Regularity Measure of Backup Restoration) = :code:`(SUM from i=1..N ((t(i+1) - t(i) - T)^2 / N ) / M`
* M6 (The Probability of detecting an anomaly in Backup Restoration) = :code:`D / L`

Metrics
-------

Backup Integrity Quality
^^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - The ratio of "properly working" backups to the total number of backups under test
	* - **Calculation**
	  - :code:`M2 / M1`

Quality of Backup Restoration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | Quality of backup restoration is high if and only if the backup restoration is
	    | highly regular and the potential for detecting anomalies (at least one per review)
	    | is also high.
	* - **Calculation**
	  - :code:`(1-M4) * M6` or (if M5) :code:`(1 - M5) / M6

.. history
.. authors
.. license
