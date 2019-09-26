6.7: Regularly Review Logs
=========================================================
On a regular basis, review logs to identify anomalies or abnormal events.

.. list-table::
	:header-rows: 1

	* - Asset Type
	  - Security Function
	  - Implementation Groups
	* - Network
	  - Detect
	  - 2, 3

Dependencies
------------
* None

Inputs
------
#. The timestamp at which a log review i has been made, represented as t(i)
#. The number of reviews (timestamps) taken so far, represented as N
#. The maximum possible irregularity (can be fixed as 30 day), represented as R
#. (Optional) Target/desirable review interval threshold, represented as T
#. The number of log reviews in which at least one anomaly was detected, represented as D
#. The total number of Log Reviews, represented as L

Operations
----------
#. Calculate the average of log review, M1 = :code:`(SUM from i=1..N (t(i+1) - t(i))) / N`
#. Calculate the threshold-based regularity measure of log review, M2 = :code:`(SUM from i=1..N ( (t(i+1) - t(i)) - T)^2 / N ) / R`
#. Calculate the probability of detecting an anomaly in log review, M3 = :code:`D / L`

Measures
--------
* M1 = The average of log review from Operation 1
* M2 = The threshold-based regularity measure of log review from Operation 2
* M3 = The probability of detecting an anomaly in log review from Operation 3

Metrics
-------

Regularity Measure of Log Review
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | Measure the irregularity or variance of log review.  The higher the value the more
	    | irregularity.
	* - **Calculation**
	  - :code:`(SUM from i=1..N ( (t(i+1) - t(i)) - M1)^2 / N ) / R`

Quality of Log Review
^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The quality of review is high if-and-only-if the review is highly regular and the
	    | potential for detecting anomalies (at least one per review) is also high.
	* - **Calculation**
	  - :code:`(1-M2) * M3`


.. history
.. authors
.. license
