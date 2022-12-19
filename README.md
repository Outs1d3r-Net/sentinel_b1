# Sentinel B1  
> For find threat IPs with AbuseipDB API.   
#  
[![Banner](img/banner.png)](https://matrix.fandom.com/wiki/Sentinel)  
#   
## Dependencies   
Most of the libraries used are already native to ```Python3```, but make sure you have adequate support for each of them.  
### **requests:**   
```python3
agentsmith@matrix:~$ python3 -m pip install requests
```
### **json:**   
```python3
agentsmith@matrix:~$ python3 -m pip install json
```
### **sys:**   
```python3
agentsmith@matrix:~$ python3 -m pip install sys
```   
## Variables   
There are only 3 variables that need attention before the script is executed.  
#   
[![Variables](img/vars.png)](https://www.abuseipdb.com/check/142.250.218.74)  
#   
1. * **URL:**  
     - This variable is found in ```line 11``` of the script and it sets the API endpoint of abuseIPDB.   
2. * **API_KEY:**  
     - This variable is in ```line 12``` of the script and it should contain the API key for your account at https://www.abuseipdb.com/ (registration is free.)   
3. * **MXAGEDAYS:**
     - This variable is on ```line 13``` of the script and it sets the search time on the abuseipdb base in days.  

* More information:  
  - [Documentation API abuseIPDB](https://docs.abuseipdb.com/?python#introduction "Click here")  
## Single Scan  
For single scan execute the follow command:  
```python3
agentsmith@matrix:~$ python3 sentinelb1.py --single <TARGET_IP>
``` 
#   
[![SingleScan](img/00.png)](https://www.abuseipdb.com/check/142.250.218.74)   
#  
## Multiple Scan  
For scan with list IP's execute the fallow command:  
```python3
agentsmith@matrix:~$ python3 sentinelb1.py -l <LIST_IPs.txt>
``` 
#   
[![MultipleScan](img/01.png)](https://www.abuseipdb.com/)   
#  
## Hashes
### Sha512     
```
a622c298dd42d47f4e8b4838e2529b0f159eafab4d198198d441ca9360830ec12ed7d942abb1e04f82efa9e3ae67edefd54463a2ba9477cea2a4e214f425db99  sentinelb1.py
````
### Sha256     
```
ec4ad2c564de2e64c4fc06dedc76a0500c820bac5b5c655ff20322ddcd776518  sentinelb1.py
```
### MD5     
```
5f9ae7c7013f33b13cc85b7c811a918b  sentinelb1.py
```
:frog: