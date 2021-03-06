# Context for scalable application

## A distributed way to share variables in a scalable environment

### Description

This context server is an RPC server giving access to a shared dictionary that is meant to hold variables and offer strategies in a scalable way.


### Installing

#### Native installation
Starting by a preconfigured rabbitMQ server:

    # Giving your rabbit_mq variables
    export RABBIT_MQ_HOST="localhost"
    export RABBIT_MQ_USER=""
    export RABBIT_MQ_PASSWORD=""

Configure your application's context rpc server: 

    export CONTEXT_RPC_PORT="localhost"
    export CONTEXT_RPC_HOST="6060"

Now, this variable is meant to be handled by another system, use the value 1 as a start:

    # This one is a specific ID given by another subsystem
    export ZOS_CONTEXT_ID="1"

#### Docker

Use this command to build and deploy the containers:

    sudo docker-compose up -d

### Hypothesis

We suppose that the beholding nodes of this shared context have a way of knowing each other. The subsystem responsible for making knowledge between the nodes is meant keep groups of nodes knowing eachother, another feature that I plan to add is the election process using the sidecar pattern to elect one coordinator from within each group in order to communicate with other groups. But for now, I just suppose that these subsystems are already made.

### Progress

- [x] Current code consistency. ![](https://us-central1-progress-markdown.cloudfunctions.net/progress/70)
- [x] Consensus handling. ![](https://us-central1-progress-markdown.cloudfunctions.net/progress/70)
  - [x] In between node communication.
  - [x] Stateless strategy instances.
    - [x] Key value store. (REDIS)
- [x] Accessibility. ![](https://us-central1-progress-markdown.cloudfunctions.net/progress/90)
  - [x] Context as an RPC service.
  - [X] Strategies:
    -  Scheduling:
       - Round robin
  - [x] Text storage.
- [x] Containerisation. (Dockerfile) ![](https://us-central1-progress-markdown.cloudfunctions.net/progress/90)
  - [x] Automation of deployment. 
  - [x] Smaller footprint. 
