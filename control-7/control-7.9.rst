7.9: Block Unnecessary File Types
=========================================================
Block all email attachments entering the organization’s email gateway if the file types are unnecessary for the organization’s business.

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
#. The list of endpoints
#. The organization's approved email gateway configuration, including file types to be blocked.

Operations
----------
#. From Input 1, collect endpoints configured as email gateway(s) (M2)
#. For each endpoint collected in Operation 1, collect the system's attachment blocking configuration

Measures
--------
* M1(i) = (For each email gateway "i") 1 if the email gateway's configuration complies with the organizations attachment blocking policy; 0 otherwise.
* M2 = The number of email gateways

Metrics
-------

Coverage
^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The ratio of endpoints configured as email gateways that are properly configured to 
	    | the total number of email gateway endpoints
	* - **Calculation**
	  - :code:`(SUM from i=1..M2 (M1(i))) / M2`

.. history
.. authors
.. license