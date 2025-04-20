There are a couple of different vectors when approaching the question of "how do I make my already correct program run faster?" 
* algorithmic efficiency
* parallelism & concurrency
* hardware accelerators
* distributed systems

## Algorithmic Efficiency
You have a function which takes x and returns y. You've determined that the runtime of the algorithm is O(n). Algorithmic efficiency asks the question
> can I take the same function, and give it a runtime less than O(n)
And sometimes we ask the question, can I get very close to y via a faster approximation.

## Parallelism and Concurrency

Parallelism: Tasks executed on truly separate processes
```
Time →
Task A: [===========]
Task B: [===========]
Task C: [===========]
```

Concurrency: Tasks interleaved on a single process
```
Time →
Task A: [===]  [=====]    [==]
Task B:    [======]  [====]
Task C:        [==]      [========]
```

## Hardware Accelerators
Different pieces of hardware can support different kinds of parallelism, through different programming models.

CPU
* Traditional threading which is good for networking/ IO bound tasks 

GPU
* SIMT parallelism, good at doing many simple calculations in parallel

Eg. CPUs are the only choice for running most applications (web servers, databases, distributed systems). But for select tasks with high degrees of parallelism (training a neural net, cryptography, complex weather models), GPUs can offer orders of magnitude improvement.

## Distributed Systems
Compute tasks can be scaled vertically by enriching the set of available processors on a single machine, but after a certain point this introduce crucial problems
* single points of failure
* heating issues
* power density

It can be cheaper and much more effecient to instead add on additional cheaper compute units and introduce communication protocols to synchronize across the machines. Sometimes this involves have a primary node and worker nodes, wherin the primary node is coordinating the computation and the worker nodes are each picking up small tasks as they come in.

The greater complexity with these distributed systems is handling failure cases
* what happens when the primary node fails?
* what happens when a worker node fails?

Especially considering the probability of failure goes up considerably as we add more and more machines to the system.