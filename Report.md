Assignment 5 
---------------------

# Team Members

- Nico Keller and Teo Field-Marsham

# GitHub link to your (forked) repository

https://github.com/nicokeller14/Assignment5_DS

# Task 1

Note: Some questions require you to take screenshots. In that case, please join the screenshots and indicate in your answer which image refer to which screenshot.

1. What happens when Raft starts? Why?

Ans: At the beginning all nodes begin as followers, but if followers don't hear from a leader they become candidates. Then the leader election begins. 
Each node has a random election timeout, which is the time it waits for communication from a leader before initiating an election.  Candidates send requests 
votes from other nodes and the other nodes reply with an answer. If a candidate becomes a majority of votes, then that nodes becomes a leader
and all of the changes to the system go through the leader. If a leader suddenly becomes unavailable, the election process starts again.


Source: https://medium.com/coinmonks/the-raft-algorithm-achieving-distributed-systems-consensus-e8c17542699b#:~:text=At%20its%20core%2C%20the%20Raft,other%20nodes%20in%20the%20system.
https://thesecretlivesofdata.com/raft/

2. Perform one request on the leader, wait until the leader is committed by all servers. Pause the simulation.
Then perform a new request on the leader. Take a screenshot, stop the leader and then resume the simulation.
Once, there is a new leader, perform a new request and then resume the previous leader. Once, this new request is committed by all servers, pause the simulation and take a screenshot. Explain what happened?
Ans: We begin with the election process and a leader is chosen. After that we make a request and all other nodes commit the request.
After making the second request we simulate a leader failure and the request isn't fully replicated nor commmited.
While having the leader down the nodes notice the abscence of the heartbeats and start a new leader election process.
Eventually we get a new leader. When having a new leader we make a request, this request gets  processed, replicated, and committed by the new leader and its followers. 
In the meanwhile the old leader gets back online but this time as a follower because we already have a new leader. In the second screenshot
we can see that the request made to the new leader is already committed and processed by al other nodes. The old leader is forced to
update its log to the new state of the rest of the cluster. This is what we call fault`s tolerance. This preserves data consistency and 
availability even if one leader goes down.

3. Stop the current leader and two other servers. After a few increase in the Raft term, pause the simulation and take a screenshot. 
Then resume all servers and restart the simulation. After the leader election, pause the simulation and take a screenshot. Explain what happened.

Ans: After stopping the leader and two other nodes, we are left with only two nodes. This leaves the cluster with no majority of nodes working,
thus not being able to choose a new leader in the cluster. ach failed election attempt results in an increase in the Raft term as nodes continually timeout and start 
new elections. So we have now a leaderless state, where a term is increased in every failed attempt to choose a new leader.
When resuming all the other nodes, the election process begins a new leader is chosen. This demonstrates raft's ability to handle multiple node failures, 
and even including the loss of a leader. 

# Task 2

Indicate the replies that you get from the "/admin/status" endpoint of the HTTP service for each servers. Which server is the leader? Can there be multiple leaders?
Ans:

Perform an Append request for the key ``a" on the leader. What is the new status? What changes occurred and why (if any)?

Ans: 

Perform a Get request for the key ``a" on the leader. What is the new status? What change (if any) happened and why?

Ans:



# Task 3

Shut down the server that acts as a leader. Report the status that you get from the servers that remain active after shutting down the leader.

Ans:

 Perform a Put request for the key "a". Then, restart the server from the previous point, and indicate the new status for the three servers. Indicate the result of a Get request for the key ``a" to the previous leader.

Ans:

Has the Put request been replicated? Indicate which steps lead to a new election and which ones do not. Justify your answer using the statuses returned by the servers.

Ans:

Shut down two servers, including the leader --- starting with the server that is not the leader. Report the status of the remaining servers and explain what happened.

Ans:

Can you perform Get, Put, or Append requests in this system state? Justify your answer.

Ans:

Restart the servers and note down the new status. Describe what happened.

Ans:




# Task 4

1. What is a consensus algorithm? What are they used for in the context of replicated state machines? 

Ans: A consensus algorithm is design to enable connections of distributed machines ie. different nodes to work together efficiently as a group
even with the presence of failures and outages. It is used to achieve agreement on a single data value among distributed processes or systems. 
So it is an algorithm that seeks an organized way of working of different machines that interact with 
each other, ensuring that they will continue to work in a efficiently manner even if errors and failures are present.
In practice, a consensus algorithm provides a way for multiple servers ro reach agreement on a state. Once there is consensus, the state is final and cannot
be changed.
When talking about replicated state machines, we ensure that each replica progresses in the same state. Also, this ensures consistency and 
reliability because even if some nodes are down, the algorithm will continue working, ie the machines will continue working.
So even in concurrent updates all replicas hold the same data.

Sources: https://www.scylladb.com/glossary/consensus-algorithms/#:~:text=Consensus%20algorithms%20are%20designed%20to,scale%2C%20fault%2Dtolerant%20systems.

2. What are the main features of the Raft algorithm? How does Raft enable fault toler- ance?

Ans: The main features of the raft algorithm are: Leader election, log replication, safety and log matching, term concept and membership changes.
DO WE NEED TO EXPLAIN?
Fault tolerance in raft is handled this way:
- If a leader fails, a new leader is elected, ensuring continued operation of the cluster.
- we can ensure that the system can operate even if nodes are down by replicating the state across multiple nodes
- once a log entry is seen as committed, it is guaranteed to be present in any future leader, providing data durability
- as long as there is a mjority, consensus can be reached
- log consistency and leader uniqueness are maintained even in the presence of network delays, partitions, and node restarts.
Source: https://towardsdatascience.com/raft-algorithm-explained-a7c856529f40


3. What are Byzantine failures? Can Raft handle them?

Ans: We call it a Byzantine failure in the case that a fault is presenting different symptoms to different nodes/observers across
a distributed system. So a Byzantine failure is the effective loss of a system service due to fault systems that indeed require consensus among the system
and its nodes For example, a Byzantine node might send different, conflicting messages to different nodes, making it difficult for the system to reach a consensus.
It is not only difficuly to reach consensus but also to identify the problem.

And no, raft can't inherently handle these type of failures. The algorightm has to be updated in order to do so.
It needs additional mechanisms to detect and mitigate deceitful or inconsistent behavior among nodes. 


Source: https://www.scs.stanford.edu/17au-cs244b/labs/projects/clow_jiang.pdf
https://en.wikipedia.org/wiki/Byzantine_fault#:~:text=A%20Byzantine%20fault%20is%20any,require%20consensus%20among%20distributed%20nodes.