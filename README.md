---

<br />
<div align="center">

  <h3 align="center">AWS ECS Service Connect</h3>

  <p align="center">
    Microservices on AWS with ECS Service Connect
  </p>
</div>

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#series-outline">Series Outline</a>
      <ul>
        <li><a href="#aws-components">AWS Components</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <ul>
            <li><a href="#software">Software</a></li>
            <li><a href="#aws">AWS</a></li>
            <li><a href="#cmd-line">CMD Line</a></li>
          </ul>
      </ul>
    </li>
    <li><a href="#commands">AWS (CDK) Commands</a></li>
    <li><a href="#references">References</a></li>
  </ol>
</details>

## Series Outline

1. Get microservices example running locally using `docker-compose`

1. Create working example of microservices on AWS using [ECS Service Connect](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs.html)

   - will not be production ready
   - will rely on a lot of default values provided by AWS, with no networking setup by us

1. Create production-ready example of microservices on AWS using [ECS Service Connect](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs.html)

   - configure networking setup and apply that to ECS components

1. Use GitHub Actions to automate deployments to AWS ECS components, referred to as Continuous Deployment (CD)

1. Create networking setup and ECS components automatically with a single script using [AWS CDK](https://docs.aws.amazon.com/cdk/v2/guide/home.html)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### AWS Components

- Virtual Private Cloud (VPC)
- NAT Gateway & Internet Gateway (IGW)
- Elastic Container Registry (ECR)
- Elastic Container Service (ECS)
- ECS Clusters
- ECS Services
- ECS Task Definitions
- Cloud Map
- Application Load Balancer (ALB)
- AWS Cloud Development Kit (CDK)
  - written in Python

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Getting Started

### Prerequisites

#### Software

- Python: version requirement determined by [AWS CLI requirement](https://github.com/aws/aws-cli) and optionally [AWS CDK requirement](https://github.com/aws/aws-cdk)
- [Docker Desktop](https://www.docker.com/products/docker-desktop/): account not required, just installation

#### AWS

- create [AWS IAM user account](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html) than can be configured with the AWS CLI

