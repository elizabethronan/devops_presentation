# DevOps Topic Overview: Secrets Management 

## By Elizabeth Ronan and Grace Kluender 

### Executive Summary 

Secrets management is the practice of securely handling sensitive credentials like database passwords, API keys, encryption certificates, and cloud access tokens that are used by applications, services, and infrastructure. Modern DevOps and DevSecOps environments require automated, identity-driven, and auditable secret management to protect against data breaches, compromised systems, and compliance violations. Tools like HashiCorp Vault and AWS Secrets Manager enable centralized control, dynamic credentials, and lifecycle management of secrets while integrating with CI/CD pipelines, cloud platforms, and infrastructure. 

### How Do Secrets Managers Work? 

Secrets managers work by acting as a centralized control plane for securely storing, generating, and distributing sensitive credentials. The workflow begins when a client (an application, CI/CD pipeline, or user) authenticates through an external identity provider such as IAM, OIDC, Kubernetes service accounts, establishing a verified identity without relying on static credentials. The secrets manager then evaluates identity-based authorization policies to determine what secrets the client can access and what actions are permitted. If authorization is granted, the system either retrieves a stored secret, or it dynamically generates a short-lived credential (such as a database login or certificate). It then decrypts the secret in memory and returns it to the client via a secure connection. Secrets managers log every interaction for auditing and compliance purposes. They also have lifecycle management features that scan repos and pipelines for secrets and automatically rotate, expire, and revoke credentials to reduce risk and prevent secret sprawl.  

### Industry Tools & Use Cases 

There are many secrets management tools on the market today, but two of the leading solutions are HashiCorp Vault and AWS Secrets Manager. HashiCorp Vault supports self-managed deployments, making it highly customizable and useful in multi-cloud or hybrid environments. AWS Secrets Manager is a fully managed AWS service that requires less setup and maintenance but is less customizable and uses simpler infrastructures. HashiCorp Vault is widely adopted by large enterprises working in complex infrastructure environments within sectors like banking, healthcare, and technology. AWS Secrets Manager is popular with organizations already heavily invested in the AWS ecosystem. The use cases for these tools are expansive, but in general, these tools are used by organizations and DevOps engineers to centralize secrets and integrate security directly into CI/CD pipelines and workflows. 

### Helpful Links 

[Helpful Overview of AWS Secrets Manager](https://www.geeksforgeeks.org/devops/aws-secrets-manager/) , [AWS Secrets Manager Demo Video](https://www.youtube.com/watch?v=ItzzgWe7elE) , [HashiCorp Vault Demo Video](https://www.youtube.com/watch?v=klyAhaklGNU) , [Overview of The Vault Plugin Ecosystem](https://developer.hashicorp.com/vault/docs/plugins) , [Which Tool Should I Use?](https://infisical.com/blog/aws-secrets-manager-vs-hashicorp-vault)

 
