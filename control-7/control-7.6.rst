7.6: Log All URL Requests
=========================================================
Log all URL requests from each of the organization’s systems, whether on-site or a mobile device, in order to identify potentially malicious activity and assist incident handlers with identifying potentially compromised systems.

.. list-table::
	:header-rows: 1

	* - Asset Type 
	  - Security Function
	  - Implementation Groups
	* - Network
	  - Detect
	  - 2, 3

Status
------
Draft

Dependencies
------------
* Subcontrol 1.5: Maintain Asset Inventory Information

Inputs
------
#. The list of endpoints
#. The organization's logging configuration policy, detailing URL logging configuration

Operations
----------
#. For each endpoint, collect the system logging configuration

Measures
--------
* M1(i) = (For each endpoint "i") 1 if the endpoint's logging configuration complies with the organizations logging policy; 0 otherwise.
* M2 = The number of endpoints from Input 1

Metrics
-------

Configuration Coverage
^^^^^^^^^^^^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The ratio of devices which enable URL request logging to the total number of devices.
	* - **Calculation**
	  - :code:`(SUM from i=1..M2 (M1(i))) / M2`

.. history
.. authors
.. license