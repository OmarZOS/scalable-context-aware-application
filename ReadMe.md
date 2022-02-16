# Context for scalable application

## A distributed way to share variables in a scalable environment

### Description

This context server is an RPC server giving access to a shared dictionary that is meant to hold variables and offer strategies in a scalable way.

### Hypothesis

We suppose that the beholding nodes of this shared context have a way of knowing each other.

### Installing
Starting by a preconfigured rabbitMQ server:

    # Start by setting environment variables
    export CONTEXT_RPC_PORT="localhost"
    export CONTEXT_RPC_HOST="6060"
    
    # Giving your rabbit_mq variables
    export RABBIT_MQ_HOST="localhost"
    export RABBIT_MQ_USER=""
    export RABBIT_MQ_PASSWORD=""

    # This one is a specific ID given by another subsystem
    export ZOS_CONTEXT_ID=""

