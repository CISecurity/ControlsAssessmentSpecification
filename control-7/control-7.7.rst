7.7: Use of DNS Filtering Services
===================================
Use Domain Name System (DNS) filtering services to help block access to known malicious domains.

.. list-table::
	:header-rows: 1

	* - Asset Type 
	  - Security Function
	  - Implementation Groups
	* - Network
	  - Protect
	  - 1, 2, 3

Status
------
Draft

Assumptions
-----------
* An authoritative source of blacklisted URLs is available, i.e. phishtank
* M2 (below) is available via formal analytics or AT

Measures
--------
* M1 = # of blacklisted URLs from authoritative source
* M2 = # of blocked URLs
* M3 = time new URL "U1" available in authoritative source
* M4 = time that URL "U1" is added to DNS filter

Metrics
-------

Coverage
^^^^^^^^
.. list-table::

	* - **Question**
	  - Determine the percentage of blocked URLs which are currently blacklisted by an authoritative source.
	* - **Answer**
	  - The calculation will yield a percentage, from 0 to 100, indicating the ratio of blocked URLs to those currently blacklisted.
	* - **Calculation**
	  - :code:`(M2/M1) * 100`

Freshness
^^^^^^^^^
.. list-table::

	* - **Question**
	  - How much time is required to include a newly blacklisted URL in an organization's DNS filters?
	* - **Answer**
	  - The calculation will provide a numeric value, with "larger" values indicating a longer timespan between URL blacklisting and inclusion in DNS filters.
	* - **Calculation**
	  - :code:`(M3/M4)`

.. history
.. authors
.. license