## Challenge:
Utilizing Python and SQL, your challenge is to process the malicious urls csv file, keeping the original input and producing certain outputs:
--Python
1. Parse the domain into a new column
2. Parse the top-level domain into a new column
3. Retrieve and write who owns the domain
4. How many times does the letter E appear in the domain name  
5. How many records that contain the letter A and the letter T in the domain name are considered to be malware & phishing
---SQL 
6. Output how many domains are in each type
7. What percentage of each is the total table population? For example, phishing accounts for 20 % of types in the file.
8. Rank and order each record based on the following scale
	a. Malware  = High 
	b. Defacement = Medium High	
	c. Phishing = Medium
	d. Benign = Low

We don't expect this to be a sophisticated system as this exercise is just a prototype, but it must be working and satisfy the requirements. We are 
interested in how you tackle the challenge and design and test your solution. The requirements are flexible and vague, so use your best
judgment on how to create your solution. 

* No specific requirements on what libraries you should use
* No specific requirements on how to import the sample data set and transform it
* No specific requirements for the input or output of file formats
* No specific requirements for how to test 
* No specific requirements around performance, runtime, etc.
* No specific requirement for streaming, batch, incremental, etc.

## Dataset

Column     | Description
-----------|--------------------------------------------
url	   | malicious url 
type	   | type of URL such as malware, defacement, phishing, and benign

## Example Data

Type	   | Description
-----------|--------------------------------------------
phishing   | br-icloud.com.br
benign	   | mp3raid.com/music/krizz_kaliko.html
defacement | http://www.garage-pirenne.be/index.php?option=com_content&view=article&id=70&vsig70_0=15
malware	   | http://9779.info/%E5%B9%BC%E5%84%BF%E7%B2%BD%E5%8F%B6%E8%B4%B4%E7%94%BB/



