17.2: Establish and Maintain Contact Information for Reporting Security Incidents
=========================================================
Establish and maintain contact information for parties that need to be informed of security incidents. Contacts may include internal staff, third-party vendors, law enforcement, cyber insurance providers, relevant government agencies, Information Sharing and Analysis Center (ISAC) partners, or other stakeholders. Verify contacts annually to ensure that information is up-to-date.

.. list-table::
	:header-rows: 1

	* - Asset Type
	  - Security Function
	  - Implementation Groups
	* - N/A
	  - Respond
	  - 1, 2, 3

Dependencies
------------
* None

Inputs
-----------
#. :code:`GV51`: Enterprise Incident Response Documentation
#. Date of last update or review of the documentation

Operations
----------
#. Determine whether the enterprise documents establish and maintain contact information for reporting security incidents by reviewing Input 1 :code:`GV51`. Input 1 can be an incident response plan or other documentation.
	#. If documentation outlining contact information exists, M1 = 1
	#. If documentation outlining contact information does not exist, M1 = 0
#. Compare Input 2 to current date and capture timeframe in months (M2)

Measures
--------
* M1 = Output of Operation 1
* M2 = Timeframe since last update or review of documentation in months

Metrics
-------
* If M1 is 0, this safeguard receives a failing score. The other metrics don't apply.
* If M2 is greater than twelve months, then this safeguard is measured at a 0 and receives a failing score. The other metrics don't apply.


.. history
.. authors
.. license
