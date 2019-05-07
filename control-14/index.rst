CIS Control 14: Controlled Access Based on the Need to Know
=======================================================

The processes and tools used to track/control/prevent/correct secure access to critical assets
(e.g., information, resources, systems) according to the formal determination of which persons,
computers, and applications have a need and right to access these critical assets based on an
approved classification.

**Why is this CIS Control Critical?**

Encrypting data provides a level of assurance that even if data is compromised, it is impractical to
access the plaintext without significant resources; however, controls should also be put in place
to mitigate the threat of data exfiltration in the first place. Many attacks occurred across the
network, while others involved physical theft of laptops and other equipment holding sensitive
information. Yet, in many cases, the victims were not aware that the sensitive data were leaving
their systems because they were not monitoring data outflows. The movement of data across
network boundaries both electronically and physically must be carefully scrutinized to minimize
its exposure to attackers.

The loss of control over protected or sensitive data by organizations is a serious threat to business
operations and a potential threat to national security. While some data are leaked or lost as a
result of theft or espionage, the vast majority of these problems result from poorly understood
data practices, a lack of effective policy architectures, and user error. Data loss can even occur as
a result of legitimate activities such as e-Discovery during litigation, particularly when records
retention practices are ineffective or nonexistent.

The adoption of data encryption, both in transit and at rest, provides mitigation against data
compromise. This is true if proper care has been taken in the processes and technologies
associated with the encryption operations. An example of this is the management of
cryptographic keys used by the various algorithms that protect data. The process for generation,
use, and destruction of keys should be based on proven processes as defined in standards such as
NIST SP 800-57.

Care should also be taken to ensure that products used within an enterprise implement well
known and vetted cryptographic algorithms, as identified by NIST. Re-evaluation of the algorithms
and key sizes used within the enterprise on an annual basis is also recommended to ensure that
organizations are not falling behind in the strength of protection applied to their data.

For organizations that are moving data to the cloud, it is important to understand the security
controls applied to data in the cloud multi-tenant environment, and determine the best course of
action for application of encryption controls and security of keys. When possible, keys should be
stored within secure containers such as Hardware Security Modules (HSMs).

Data loss prevention (DLP) refers to a comprehensive approach covering people, processes, and
systems that identify, monitor, and protect data in use (e.g., endpoint actions), data in motion
(e.g., network actions), and data at rest (e.g., data storage) through deep content inspection
and with a centralized management framework. Over the last several years, there has been a
noticeable shift in attention and investment from securing the network to securing systems
within the network, and to securing the data itself. DLP controls are based on policy, and include
classifying sensitive data, discovering that data across an enterprise, enforcing controls, and
reporting and auditing to ensure policy compliance.

.. toctree::
   :maxdepth: 1
   :name: toc-control-14

   14.1: Segment the Network Based on Sensitivity <control-14.1>
   14.2: Enable Firewall Filtering Between VLANs <control-14.2>
   14.3: Disable Workstation-to-Workstation Communication <control-14.3>
   14.4: Encrypt All Sensitive Information in Transit <control-14.4>
   14.5: Utilize an Active Discovery Tool to Identify Sensitive Data <control-14.5>
   14.6: Protect Information Through Access Control Lists <control-14.6>
   14.7: Enforce Access Control to Data Through Automated Tools <control-14.7>
   14.8: Encrypt Sensitive Information at Rest <control-14.8>
   14.9: Enforce Detail Logging for Access or Changes to Sensitive Data <control-14.9>
   
.. history
.. authors
.. license