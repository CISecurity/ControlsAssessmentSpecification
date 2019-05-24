3.5: Deploy Automated Software Patch Management Tools
=========================================================
Deploy automated software update tools in order to ensure that third-party software on all systems is running the most recent security updates provided by the software vendor.

.. list-table::
	:header-rows: 1

	* - Asset Type 
	  - Security Function
	  - Implementation Groups
	* - Applications
	  - Protect
	  - 1, 2, 3

Status
------
Draft

Assumptions
-----------
Does this sub-control cover software components comprising that piece of software (such as 3d party libraries used by the software, like OpenSSL)
We're gonna say "NO" to this one.


Measures
--------
M1 = # of updated software (software with 0 CVE)
M2 = # of total software in a machine
M2 = time of installed CVE that is most recent
M3 = release time of most recent CVE of a software

Metrics
-------

Update Ratio
^^^^^^^^^^^^
.. list-table::

	* - **Question**
	  - TBD
	* - **Answer**
	  - TBD
	* - **Calculation**
	  - :code:`(M1/M2) * 100`

Freshness
^^^^^^^^^
.. list-table:

* - **Question**
	- TBD
* - **Answer**
	- TBD
* - **Calculation**
	- :code:`TRUE if M2 == M3; FALSE otherwise`

.. history
.. authors
.. license
