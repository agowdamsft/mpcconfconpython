# Multi-Party Secure Rich Data Collaboration on Confidential Containers
This solution demonstrates a basic Python based container applications that bring a math based model for a secured collaboration with protection of IP and Data in use.
3 parties coming together with rich trade sensitive data for accurate predictions. Parties involved have Intellectual Property that needs to be protected for any tampering or misuse.
 
* Party 1 :The consortium hosting provider. The subscription owner and simulation run owner with customer data
* Party 2: Software Inferencing Provider/ML Model + Sensitive Data Provider 
* Party 3: Trade sensitive mathematical simulation model provider

## Architecture
![Architecture Image](/arch.jpg)

## Sample Modules
This solution has 4 Python based modules that form various data enrichment and analysis to derive the output that is intended.

### Module 1
Does the basic math to add +100 to the input
> curl POST -http://0.0.0.0:4996/api/simvalue {
"runid":"123-test",
"invalue":123
}

> Returns
> 223
