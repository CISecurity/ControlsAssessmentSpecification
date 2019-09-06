7.4: Maintain and Enforce Network-Based URL Filters
=========================================================
Enforce network-based URL filters that limit a system’s ability to connect to websites not approved by the organization. This filtering shall be enforced for each of the organization’s systems, whether they are physically at an organization’s facilities or not.

.. list-table::
	:header-rows: 1

	* - Asset Type 
	  - Security Function
	  - Implementation Groups
	* - Network
	  - Protect
	  - 2, 3

Status
------
Draft

Dependencies
------------
* Subcontrol 2.5: Integration Software and Hardware Asset Inventories

Inputs
------
#. List of web clients/browsers installed in the organization by endpoint
#. Approved configuration(s) covering each web browser/client in Input 1 indicating whether or not the browser must utilize URL filtering

Operations
----------
#. For each application instance (web browser/client) in Input 1, check the application's configuration against the appropriate approved configuration(s) from Input 2.
#. Create a list of the application instances that meet the approved configuration (M1)
#. Create a list of the application instances that that do not meet the approved configuration (M2) noting each deviation.

Measures
--------
* M1 = List of application instances (web browser/client) that meet the approved configuration (compliant list)
* M2 = List of application instances (web browser or email client) that do not meet the approved configuration (non-compliant list)
* M3 = Count of compliant application instances (count of M1)
* M4 = Count of non-compliant application instances (count of M2)
* M5 = Total count of installed web browser and email client instances (count of Input 1)

Metrics
-------

Coverage
^^^^^^^^
.. list-table::

	* - **Metric**
	  - | Calculate the quality of URL-filter enforcement.
	* - **Calculation**
	  - :code:`M3 / M5`

.. history
.. authors
.. license