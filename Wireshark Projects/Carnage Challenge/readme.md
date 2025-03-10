# Wireshark Network Analysis Notes

![image.png](./images/image.png)

### Author
Emilio Shakhawat

### Carnage Challenge
This is my network analysis of the Carnage challenge on TryHackMe.com:

The scenario is as follows: an employee opened an email from a known contact, which contained a Word document that injected malicious code into the victim’s device. The security team managed to capture the packets during the time frame of the attack. My job is to assess and uncover the malicious activities.

### Finding the Origin Point of the Breach

I started by finding information on the origin point of the breach, specifically the first HTTP connection to the malicious IP.

Filtering the log with “http”, the first result shows a GET request to download a zip file.

![image1.png](./images/image1.png)

From this information:
- **Timestamp**: 2021-09-24 16:44:38
- **File Downloaded**: Document.zip

Following the HTTP stream reveals more details about the malicious connection.

![image2.png](./images/image2.png)

- **Timestamp**: 2021-09-24 16:44:38
- **File Downloaded**: Document.zip
- **Domain Host**: attirenepal.com
- **File in the Zip**: chart-1530076591.xls
- **Webserver Used**: LiteSpeed PHP/7.2.34

### Investigating Further Malicious Files

THM hints that more malicious files were downloaded within a specific time frame under HTTPS traffic. Since HTTPS uses the TLS protocol, I used the following filter to narrow down the search.

![image3.png](./images/image3.png)

After investigating packets, I found three suspicious domains:

![image4.png](./images/4db5a7c9-6149-4157-80ec-3b9cf238b1f1.png)
![image5.png](./images/a61c180f-25cd-44a0-a194-29671b142e74.png)
![image6.png](./images/20f61e46-3124-4a77-b4c9-376c28ab69af.png)

Following the TCP stream, I also found the provider for the SSL certificates on these servers.

![image7.png](./images/image4.png)

**Information gathered so far:**
- **Timestamp**: 2021-09-24 16:44:38
- **File Downloaded**: Document.zip
- **Domain Host**: attirenepal.com
- **File in the Zip**: chart-1530076591.xls
- **Webserver Used**: LiteSpeed PHP/7.2.34
- **Additional Malicious Connections**: finejewels.com.au, thietbiagt.com, new.americold.com
- **SSL Authority**: GoDaddy

### Cobalt Strike Servers

I was introduced to the term "Cobalt Strike Servers". These servers attack by sending a large amount of traffic, mostly GET and POST requests. I filtered for GET requests and analyzed the frequently accessed IPs.

![image8.png](./images/image5.png)

I sorted by IPs and found two IPs flagged in the VirusTotal community page as Cobalt Strike C2 Servers.

![image9.png](./images/image6.png)
![image10.png](./images/image7.png)
![image11.png](./images/image8.png)
![image12.png](./images/image9.png)
![image13.png](./images/image10.png)

**Recap of information gathered so far:**
- **Timestamp**: 2021-09-24 16:44:38
- **File Downloaded**: Document.zip
- **Domain Host**: attirenepal.com
- **File in the Zip**: chart-1530076591.xls
- **Webserver Used**: LiteSpeed PHP/7.2.34
- **Additional Malicious Connections**: finejewels.com.au, thietbiagt.com, new.americold.com
- **SSL Authority**: GoDaddy
- **Cobalt Strike C2 Server IPs**: 185.106.96.158, 185.125.204.174
- **Server Domains**: survmeter.live, securitybusinpuff.com

### Investigating POST Requests

I filtered for POST requests and followed the TCP stream to see if the victim sent any data.

![image14.png](./images/image11.png)

The victim host sent out a lot of packets, as evident from the filter.

We can see the receiver’s domain name and the server header.

![image15.png](./images/image12.png)
![image16.png](./images/image13.png)

**Another recap of information gathered so far:**
- **Timestamp**: 2021-09-24 16:44:38
- **File Downloaded**: Document.zip
- **Domain Host**: attirenepal.com
- **File in the Zip**: chart-1530076591.xls
- **Webserver Used**: LiteSpeed PHP/7.2.34
- **Additional Malicious Connections**: finejewels.com.au, thietbiagt.com, new.americold.com
- **SSL Authority**: GoDaddy
- **Cobalt Strike C2 Server IPs**: 185.106.96.158, 185.125.204.174
- **Server Domains**: survmeter.live, securitybusinpuff.com
- **POST Infection Domain**: maldivehost.net
- **Server Header**: Apache/2.4.49 (cPanel) OpenSSL/1.1.1l mod_bwlimited/1.4

### API Used by Malware

THM states that an API is used by the malware, so I filtered the log to show frames and DNS that contain “api”.

The results show two API requests. One from MSN (discarded) and one from api.ipify.org (suspicious).

![image17.png](./images/image14.png)

### MalSpam

Finally, THM indicates that malicious spam was sent to the email server from multiple addresses.

I filtered the log with the words “MAIL FROM” to find the suspected emails.

![image18.png](./images/image15.png)

**Final information recap:**
- **Timestamp**: 2021-09-24 16:44:38
- **File Downloaded**: Document.zip
- **Domain Host**: attirenepal.com
- **File in the Zip**: chart-1530076591.xls
- **Webserver Used**: LiteSpeed PHP/7.2.34
- **Additional Malicious Connections**: finejewels.com.au, thietbiagt.com, new.americold.com
- **SSL Authority**: GoDaddy
- **Cobalt Strike C2 Server IPs**: 185.106.96.158, 185.125.204.174
- **Server Domains**: survmeter.live, securitybusinpuff.com
- **POST Infection Domain**: maldivehost.net
- **Server Header**: Apache/2.4.49 (cPanel) OpenSSL/1.1.1l mod_bwlimited/1.4
- **Suspicious API**: api.ipify.org