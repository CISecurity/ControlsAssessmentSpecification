CIS Control 4: Secure Configuration of Enterprise Assets and Software
==========================================================

Establish and maintain the secure configuration of enterprise assets (end-user devices, including portable and mobile; network devices; non-computing/IoT devices; and servers) and software (operating systems and applications).

**Why is this CIS Control Critical?**

As delivered from manufacturers and resellers, the default configurations for enterprise assets and software are normally geared towards ease-of-deployment and ease-of-use rather than security. Basic controls, open services and ports, default accounts or passwords, pre-configured Domain Name System (DNS) settings, older (vulnerable) protocols, and pre-installation of unnecessary software can all be exploitable if left in their default state. Further, these security configuration updates need to be managed and maintained over the life cycle of enterprise assets and software. Configuration updates need to be tracked and approved through configuration management workflow process to maintain a record that can be reviewed for compliance, leveraged for incident response, and to support audits. This CIS Control is important to on-premises devices, as well as remote devices, network devices, and cloud environments.

Service providers play a key role in modern infrastructures, especially for smaller enterprises. They often are not set up by default in the most secure configuration to provide flexibility for their customers to apply their own security policies. Therefore, the presence of default accounts or passwords, excessive access, or unnecessary services are common in default configurations. These could introduce weaknesses that are under the responsibility of the enterprise that is using the software, rather than the service provider. This extends to ongoing management and updates, as some Platform as a Service (PaaS) only extend to the operating system, so patching and updating hosted applications are under the responsibility of the enterprise.

Even after a strong initial configuration is developed and applied, it must be continually managed to avoid degrading security as software is updated or patched, new security vulnerabilities are reported, and configurations are “tweaked,” to allow the installation of new software or to support new operational requirements.


.. toctree::
   :maxdepth: 1
   :name: toc-control-4

   4.1: Establish and Maintain a Secure Configuration Process <control-4.1>
   4.2: Establish and Maintain a Secure Configuration Process for Network Infrastructure <control-4.2>
   4.3: Configure Automatic Session Locking on Enterprise Assets <control-4.3>
   4.4: Implement and Manage a Firewall on Servers <control-4.4>
   4.5: Implement and Manage a Firewall on End-User Devices <control-4.5>
   4.6: Securely Manage Enterprise Assets and Software <control-4.6>
   4.7: Manage Default Accounts on Enterprise Assets and Software <control-4.7>
   4.8: Uninstall or Disable Unnecessary Services on Enterprise Assets and Software <control-4.8>
   4.9: Configure Trusted DNS Servers on Enterprise Assets <control-4.9>
   4.10: Enforce Automatic Device Lockout on Portable End-User Devices <control-4.10>
   4.11: Enforce Remote Wipe Capability on Portable End-User Devices <control-4.11>
   4.12: Separate Enterprise Workspaces on Mobile End-User Devices <control-4.12>

.. history
.. authors
.. license
