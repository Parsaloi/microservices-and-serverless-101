Cloud lab session on *9/2/23*

```bash
Welcome to IBM Cloud Shell!
Image version: 1.0.135

Note: Your Cloud Shell session is running in Dallas (us-south). Your workspace includes 500 MB of temporary storage. This session will close after an hour of inactivity. If you don't have any active sessions for an hour or you reach the 50-hour weekly usage limit, your workspace data is removed. To track your usage, go to Usage quota in the Cloud Shell menu.

Tip: Enter 'ibmcloud' to use the IBM Cloud CLI. The Dallas (us-south) region is targeted by default. You can switch the region by running 'ibmcloud target -r <region-name>'.
```

```bash
ibmcloud
NAME:
  ibmcloud - A command line tool to interact with IBM Cloud
  Find more information at: https://ibm.biz/cli-docs

USAGE:
  [environment variables] ibmcloud [global options] command [arguments...] [command options]

VERSION:
  2.18.0+53c524b-2023-07-19T19:35:24+00:00

COMMANDS:
  ac                                    Interact with IBM Cloud App Configuration service instance.
  account                               Manage accounts and users
  analytics-engine-v3, ae-v3            Manage IBM Analytics Engine API.
  api                                   Set or view target API endpoint
  atracker, at                          Manage IBM Cloud Activity Tracker Event Routing.
  billing                               Retrieve usage and billing information
  catalog                               Manage catalog
  cbr                                   Manage Context Based Restrictions.
  cis                                   Manage Cloud Internet Service.
  cloud-databases, cdb                  For IBM Cloud Databases commands
  cloud-functions, wsk, functions, fn   Manage Cloud Functions
  cloudant, cl                          Manage Cloudant.
  code-engine, ce                       Manage Code Engine components.
  config                                Modify or read out values in the config
  cos                                   Interact with IBM Cloud Object Storage services
  cr                                    Manage IBM Cloud Container Registry content and configuration.
  cra                                   Discover code vulnerabilities
  dbaas                                 Manage IBM Hyper Protect DBaaS instances for MongoDB or PostgreSQL.
  dev                                   Create, develop, deploy, and monitor applications
  dl                                    Manage Direct Link Service
  dns                                   Manage IBM Cloud DNS Services.
  doi                                   Integrate with DevOps Insights service
  dvaas, watson-query                   Manage Data Virtualization.
  enterprise                            Manage enterprise, account groups and accounts.
  es                                    Manage IBM Event Streams
  event-notifications, en               Manage Event Notifications API.
  hpcs                                  Manage Hyper Protect Crypto Services Instances.
  hpcs-cert-mgr                         hpcs-cert-mgr
  hpnet                                 hpnet
  hpvs                                  Manage Hyper Protect Virtual Server service. 

Note:
  You can now also create Hyper Protect Virtual Servers for VPC that are available in various regions. For more information about creating Virtual servers for VPC by using the IBM Cloud VPC CLI(ibmcloud is instance-create).For more information about Virtual servers for VPC, see the Virtual servers for VPC documentation(https://cloud.ibm.com/docs/vpc?topic=vpc-about-se).
  iam                   Manage identities and access to resources
  is                    Manage Virtual Private Cloud infrastructure service
  kp                    Manage encryption keys on IBM Cloud
  ks, cs, oc            Manage Kubernetes and OpenShift clusters in IBM Cloud. Aliases include 'ibmcloud oc'.
  logging               Manage IBM Cloud logging
  login                 Log user in
  logout                Log user out
  metrics-router, mr    Manage IBM Cloud Metrics Routing.
  monitoring            Manage IBM Cloud monitoring
  ob                    Manage logging and monitoring configurations for IBM Cloud Kubernetes Service clusters.
  pag                   Pag namespace.
  pi                    Manage IBM Cloud Power Virtual Server service
  plugin                Manage plug-ins and plug-in repositories
  project               Manage Projects API.
  qiskit-runtime, qr    [Beta] Manage Qiskit Runtime
  regions               List all the regions
  resource              Manage resource groups and resources
  resources             List all resources
  sat                   Manage IBM Cloud Satellite clusters.
  schematics, sch       Automate the deployment and management of IBM Cloud resources using Infrastructure as Code
  secrets-manager, sm   Manage IBM Cloud Secrets Manager API.
  sl                    Manage Classic infrastructure services
  target                Set or view the targeted region, account, resource group, org or space
  tg                    Manage Transit Gateway service
  tke                   Manage crypto units in the IBM Cloud
  update                Update CLI to the latest version
  version               Print the version
  watson                Manage Watson Assistant v1.
  help, h               Show help

Enter 'ibmcloud help [command]' for more information about a command.

ENVIRONMENT VARIABLES:
  IBMCLOUD_COLOR=false                     Do not colorize output
  IBMCLOUD_VERSION_CHECK=false             Do not check latest version for update
  IBMCLOUD_HTTP_TIMEOUT=5                  A time limit for HTTP requests
  IBMCLOUD_API_KEY=api_key_value           API Key used for login
  IBMCLOUD_CR_VPC_URL=url_value            The custom server URL to use when obtaining an instance identity token and IAM token as a VPC VSI compute resource. This value will replace the default server endpoint of the VPC VSI instance identity token service.
  IBMCLOUD_CR_TOKEN=cr_token_value         Compute resource token used for login. Can either be a token string or a path to a @file.
  IBMCLOUD_CR_PROFILE=profile_value        The name, ID, or CRN of the linked trusted IAM profile to be used when obtaining the IAM access token. If authenticating as a VPC VSI compute resource, only specifying a trusted profile CRN or ID is supported.
  IBMCLOUD_TRACE=true                      Print API request diagnostics to stdout
  IBMCLOUD_TRACE=path/to/trace.log         Append API request diagnostics to a log file
  IBMCLOUD_HOME=path/to/dir                Path to config directory

GLOBAL OPTIONS:
  --version, -v                      Print the version
  --help, -h                         Show help
```

```bash
ibmcloud --version
ibmcloud version 2.18.0+53c524b-2023-07-19T19:35:24+00:00
```
- ***Steps***  
- Create two projects, one for each user in our example...  
```bash
oc create namespace my-first-project
# resource reated

oc create namespace my-second-project
# resource created

oc create user first-user --full-name="arch-parsa"
# user created

oc create user second-user --full-name="second user"
# user created
```

- User Management > Users (view users)
- Home > Projects (view projects)
- Workloads > Pods (view pods)

- User Management > Role Bindings
- Create Binding
- Create Role Binding (fill form) > Create:  
{ Binding-Type(Namespace Role Binding(RoleBindiing)), Name(first-user-rb), Namespace(my-first-project), Role-Name(cluster-admin), SUbject(User), Subject-Name(first-user) }

- Topology > Container-Image > Deploy-Image

Thanks to `role bindings` in OpenShift, we have isolated the workloads across users on the cluster and achieved multitenancy. As a real-world use case, a managed service  
provider could use this feature to provide isolation to its customer while using the same OpenShift Container Platform cluster and the same set of shared hardware  
resources



