# Cuckoo Sandbox ML GSoC Proposal

Review of Data

There are 199 total malware reports given to us

# What does the typical Report contain?

info - This is the Cuckoo metadata

signatures - Representative of malicious behavior or indicator (Severity levels etc)

target - Metadata of the given file

virustotal - Pretty important and Gets antivirus signatures from VirusTotal.com for various results

static - Static analysis

dropped - Dropped files analysis

behavior - Different classes that analyze behavior dynamically

debug - Debug information

strings - Extract strings from analyzed file

network - Network analysis

Referred to https://github.com/cuckoosandbox/cuckoo/tree/master/modules/processing & http://docs.cuckoosandbox.org/en/latest/customization/processing/ to gain understanding of the reports



