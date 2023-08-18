# Business Logic Flaws (or) Logic Flaws

[Reference](https://portswigger.net/web-security/logic-flaws/examples)


- Vulnerability in the `design and implementation` of application
- If the logic or rules are directly related to buisness, known as `business logic flaws`. If not, know as `application logic vulnerabilities` or `logic flaws`
- Can found in complicated systems because the development team themselves do not fully understand
- Most security problems are weaknesses in an application that result from a broken or missing security control (authentication, access control, input validation, etc…)
-  if the developers assume that users will pass data exclusively `via a web browser`, the application may rely entirely on `weak client-side controls` to validate input. These are easily `bypassed by an attacker using an intercepting proxy`. 


# Impact of Business Logic Flaws

- It is a broad category and the impact is highly variable
- the impact of any logic flaw depends on what functionality it is related to
- If the flaw is in the authentication mechanism, for example, this could have a serious impact on your overall security. Attackers could potentially exploit this for privilege escalation, or to bypass authentication entirely, gaining access to sensitive data and functionality
- Flawed logic in financial transactions can obviously lead to massive losses for the business through stolen funds, fraud, and so on.


# How to prevent

- Make sure developers and testers understand the domain that the application serves
- Maintain clear design documents and data flows for all transaction and workflows
- wirte code as clearly as possible
- Note any references to other code that uses each component. Think about any side-effects of these dependencies if a malicious party were to manipulate them in an unusual way
