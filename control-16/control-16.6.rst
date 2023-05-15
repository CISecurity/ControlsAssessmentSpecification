16.6: Establish and Maintain a Severity Rating System and Process for Application Vulnerabilities
=========================================================
Establish and maintain a severity rating system and process for application vulnerabilities that facilitates prioritizing the order in which discovered vulnerabilities are fixed. This process includes setting a minimum level of security acceptability for releasing code or applications. Severity ratings bring a systematic way of triaging vulnerabilities that improves risk management and helps ensure the most severe bugs are fixed first. Review and update the system and process annually.

.. list-table::
	:header-rows: 1

	* - Asset Type
	  - Security Function
	  - Implementation Groups
	* - Applications 
	  - Protect
	  - 2, 3

Dependencies
------------
* Safeguard 16.2: Establish and Maintain a Process to Accept and Address Software Vulnerabilities

Inputs
-----------
#. :code:`GV48`: Process to Accept and Address Software Vulnerabilities 
#. Date of last update or review of the severity rating system and process

Operations
----------
#. Using Input 1 :code:`GV48`` determine whether the enterprise has a severity rating system and process for application vulnerabilities
	#. If the system and process exist, M1 = 1
	#. If the system and process do not exist, M1 = 0
#. Review Input 1 :code:`GV48` and dermine whether it includes, at a minimum, the following components: guidance for prioritizing the order vulnerabilities are fixed, level of security acceptability for releasing code or applications
	#. For each component included in the process, assign a value of 1.  Sum all values. (M2)
#. Compare Input 2 to current date and capture timeframe in months (M3)

Measures
--------
* M1 = Output of Operation 1
* M2 = Count of components included in the process
* M3 = Timeframe in months since last review or update

Metrics
-------
* If M1 is 0, this safeguard receives a failing score. The other metrics don't apply.
* If M3 is greater than twelve months, then this safeguard is measured at a 0 and receives a failing score. The other metrics don't apply.

Completeness
^^^^^^^^^
.. list-table::

	* - **Metric**
	  - | The percent of components included in the secure application 
	    | development process
	* - **Calculation**
	  - :code:`M2 / 2`

.. history
.. authors
.. license
