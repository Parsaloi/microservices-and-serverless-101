
## Multitenancy on Openshift
> <https://developer.ibm.com/learningpaths/multitenancy-red-hat-openshift/>

### Overview:
>  <https://en.wikipedia.org/wiki/Multitenancy>  
**Software multitenancy** is a software arhitecture in which a single *instance* of software runs on a server and serves multiple tenants. Systems designed in such  
manner are "shared" (rather than "dedicated" or "isolated"). A tenant is a group of users who share a common access with speific priviledges to the software instance.  
With a multitenant architecture, a `software application` is designed to provide every tenant a dedicated share of the instance - including its data, configuration,  
user management, tenant individual funtionality and *non-funtion properties*:
  
> > (NFR in systems engineering and requirements engineering is a requirement that specifies  
criteria that can be used to judge the operation of a system, rather than specific behaviours. They are contrasted with *funtional requirements* that define specific  
behavior or funtions. The plan for implementing *funtional requirements* is detailed in `system design`. The plan for *non-funtional requirements* is detailed in the  
`system architecture`, because they are usually architecturally significant requirements)

> **Multitenancy** contrasts with `multi-instance` architectures, where separate software instances operate on behalf of different tenants (isolation is good...right?)

### Cloud Lab : Setting up a multitenant environment on Red Hat OpenShift

- Tutorial: Role-based access control

Operations:  
1. Create users
2. Create role bindings
3. Impersonate user and deploy application
4. Create and deploy the pod
5. Switch to another user


## Definition

**Multitenancy** is an architecture in which a *single instance* of a software application serves multiple (customers) tenants, where each tenant's data is logically  
separated from the other tenants. Role-based access control (RBAC) is a method of restricting access based in the roles of the users in the cluster, where users have  
the rights to access the resources they need. In RBAC, role bindings defines which users are entitles to view and manage authorized resources, and they grant the  
permissions defined in a role to a user or a group. While a `role binding` grants permissions at a project scope, `cluster role binding` grants permissions at a cluster  
level.




