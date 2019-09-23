7.2: Disable Unnecessary or Unauthorized Browser or Email Client Plugins
========================================================================
Uninstall or disable any unauthorized browser or email client plugins or add-on applications.

.. list-table::
	:header-rows: 1

	* - Asset Type
	  - Security Function
	  - Implementation Groups
	* - Applications
	  - Protect
	  - 2, 3

Status
------
Draft

Dependencies
------------
* Sub-control 1.5: Maintain Asset Inventory Information
* Sub-control 2.1: Maintain Inventory of Authorized Software

Inputs
------
#. The list of authorized browser plugins
#. The list of authorized email client plugins
#. The list of endpoints

Operations
----------
#. From the list of all endpoints, collect the list of endpoints subject to browser/email plugin restrictions
#. For each endpoint listed by Operation 1, collect the list of installed browser plugins
#. For each endpoint listed by Operation 1, collect the list of installed email client plugins
#. For each endpoint, calculate the complement of the installed browser plugins with the list of approved browser plugins from Input 1. The complement will yield any installed browser plugins not on the approved list.
#. For each endpoint, calculate the complement of the installed email client plugins with the list of approved email client plugins from Input 2. The complement will yield any installed email client plugins not on the approved list.

Measures
--------
* M1 = Count of endpoints subject to browser/email plugin restrictions
* M2(i) = (For each endpoint "i") Count of installed browser plugins not in the approved list (The count resulting from Operation 4)
* M3(i) = 0 if, for each endpoint "i", the value of M2 > 0; 1 if the value of M2 == 0
* M4(i) = (For each endpoint "i") Count of installed email client plugins not in the approved list (The count resulting from Operation 5)
* M5(i) = 0 if, for each endpoint "i", the value of M4 > 0; 1 if the value of M4 == 0

Metrics
-------

Browser Plugin Enforcement Quality
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The ratio of endpoints utilizing browser plugins on the approved list to the total
	    | number of endpoints.
	* - **Calculation**
	  - :code:`(SUM from i=1..M1 (M3(i))) / M1`

Email Client Plugin Enforcement Quality
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The ratio of endpoints utilizing email client plugins on the approved list to the
	    | total number of endpoints.
	* - **Calculation**
	  - :code:`(SUM from i=1..M1 (M5(i))) / M1`

.. history
.. authors
.. license
