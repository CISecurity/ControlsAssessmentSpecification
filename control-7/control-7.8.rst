7.8: Implement DMARC and Enable Receiver-Side Verification
==========================================================
To lower the chance of spoofed or modified emails from valid domains, implement Domain-based Message Authentication, Reporting and Conformance (DMARC) policy and verification, starting by implementing the Sender Policy Framework (SPF) and the DomainKeys Identified Mail (DKIM) standards.

.. list-table::
	:header-rows: 1

	* - Asset Type
	  - Security Function
	  - Implementation Groups
	* - Network
	  - Protect
	  - 2, 3

Dependencies
------------
* Sub-control 2.4: Track Software Inventory Information

Inputs
------
#. DMARC policy
#. TXT record published in DNS
#. The Mail Transfer Agent used by the organization (this could indicate DKIM is used to sign outgoing messages)
#. The Mail User Agent used by the organization (this could indicate DKIM is used to verify incoming messages)

Assumptions
^^^^^^^^^^^
* The DMARC configuration policy includes instructions to produce either Aggregate (rua) or Forensic (ruf) reports.
* The organization has access to these reports either daily (for Aggregate) or in real-time (for Forensic).

Operations
----------
#. Examine the TXT records in DNS for a :code:`v` value indicating DMARC
#. Examine the TXT records in DNS for a :code:`v` value indicating SPF
#. Examine the TXT records in DNS for a :code:`v` value indicating DKIM

Measures
--------
* M1 = 1 if Input 1 exists and Operation 1 indicates the use of DMARC
* M2 = 1 if Operation 2 indicates the use of SPF
* M3 = 1 if Operation 3 indicates the use of DKIM

Metrics
-------

DMARC Usage
^^^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | Ensure usage and proper configuration of DMARC/SPF/DKIM
	* - **Calculation**
	  - :code:`M1 AND M2 AND M3`

.. history
.. authors
.. license
