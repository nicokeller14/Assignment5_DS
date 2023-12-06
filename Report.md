Assignment 5 
---------------------

# Team Members

- Nico Keller and Teo Field-Marsham

# GitHub link to your (forked) repository

https://github.com/nicokeller14/Assignment5_DS

# Task 1

Note: Some questions require you to take screenshots. In that case, please join the screenshots and indicate in your answer which image refer to which screenshot.

1. What happens when Raft starts? Why?

> Ans: At the beginning all nodes begin as followers, but if followers don't hear from a leader they become candidates. Then the leader election begins. 
> Each node has a random election timeout, which is the time it waits for communication from a leader before initiating an election.  Candidates send requests 
> votes from other nodes and the other nodes reply with an answer. If a candidate becomes a majority of votes, then that nodes becomes a leader
> and all of the changes to the system go through the leader. If a leader suddenly becomes unavailable, the election process starts again.

Source: https://medium.com/coinmonks/the-raft-algorithm-achieving-distributed-systems-consensus-e8c17542699b#:~:text=At%20its%20core%2C%20the%20Raft,other%20nodes%20in%20the%20system.
https://thesecretlivesofdata.com/raft/


2. Perform one request on the leader, wait until the leader is committed by all servers. Pause the simulation.
Then perform a new request on the leader. Take a screenshot, stop the leader and then resume the simulation.
Once, there is a new leader, perform a new request and then resume the previous leader. Once, this new request is committed by all servers, pause the simulation and take a screenshot. Explain what happened?

> Ans: We begin with the election process and a leader is chosen. After that we make a request and all other nodes commit the request.
> After making the second request we simulate a leader failure and the request isn't fully replicated nor commmited.
> While having the leader down the nodes notice the abscence of the heartbeats and start a new leader election process.
> Eventually we get a new leader. When having a new leader we make a request, this request gets  processed, replicated, and committed by the new leader and its followers. 
> In the meanwhile the old leader gets back online but this time as a follower because we already have a new leader. In the second screenshot
> we can see that the request made to the new leader is already committed and processed by al other nodes. The old leader is forced to
> update its log to the new state of the rest of the cluster. This is what we call fault`s tolerance. This preserves data consistency and 
> availability even if one leader goes down.


3. Stop the current leader and two other servers. After a few increase in the Raft term, pause the simulation and take a screenshot. 
Then resume all servers and restart the simulation. After the leader election, pause the simulation and take a screenshot. Explain what happened.

> Ans: After stopping the leader and two other nodes, we are left with only two nodes. This leaves the cluster with no majority of nodes working,
> thus not being able to choose a new leader in the cluster. Each failed election attempt results in an increase in the Raft term as nodes continually timeout and start 
> new elections. So we have now a leaderless state, where a term is increased in every failed attempt to choose a new leader.
> When resuming all the other nodes, the election process begins a new leader is chosen. This demonstrates raft's ability to handle multiple node failures, 
> and even including the loss of a leader. 


# Task 2

Indicate the replies that you get from the "/admin/status" endpoint of the HTTP service for each servers. Which server is the leader? Can there be multiple leaders?

> Ans: Here is the reply from 127.0.0.1:6000: {'version': '0.3.12', 'revision': 'deprecated', 'self': TCPNode('127.0.0.1:6000'), 'state': 2, 'leader': TCPNode('127.0.0.1:6000'), 'has_quorum': True, 'partner_nodes_count': 3, 'partner_node_status_server_127.0.0.1:6001': 3, 'partner_node_status_server_127.0.0.1:6002': 0, 'readonly_nodes_count': 0, 'log_len': 2, 'last_applied': 3, 'commit_idx': 3, 'raft_term': 1, 'next_node_idx_count': 2, 'next_node_idx_server_127.0.0.1:6001': 4, 'next_node_idx_server_127.0.0.1:6002': 2, 'match_idx_count': 2, 'match_idx_server_127.0.0.1:6001': 3, 'match_idx_server_127.0.0.1:6002': 0, 'leader_commit_idx': 3, 'uptime': 605, 'self_code_version': 0, 'enabled_code_version': 0}
> The POST operation of Type PUT gives a 204 No Content response code.

> Here is the reply from 127.0.0.1:6001: {'version': '0.3.12', 'revision': 'deprecated', 'self': TCPNode('127.0.0.1:6001'), 'state': 0, 'leader': TCPNode('127.0.0.1:6000'), 'has_quorum': True, 'partner_nodes_count': 3, 'partner_node_status_server_127.0.0.1:6002': 0, 'partner_node_status_server_127.0.0.1:6000': 3, 'readonly_nodes_count': 0, 'log_len': 2, 'last_applied': 3, 'commit_idx': 3, 'raft_term': 1, 'next_node_idx_count': 0, 'match_idx_count': 0, 'leader_commit_idx': 3, 'uptime': 594, 'self_code_version': 0, 'enabled_code_version': 0}
> The GET operation gives a 200 OK response code.

> Here is the reply from 127.0.0.1:6002: {'version': '0.3.12', 'revision': 'deprecated', 'self': TCPNode('127.0.0.1:6002'), 'state': 0, 'leader': TCPNode('127.0.0.1:6000'), 'has_quorum': True, 'partner_nodes_count': 3, 'partner_node_status_server_127.0.0.1:6002': 0, 'partner_node_status_server_127.0.0.1:6000': 3, 'readonly_nodes_count': 0, 'log_len': 2, 'last_applied': 3, 'commit_idx': 3, 'raft_term': 1, 'next_node_idx_count': 0, 'match_idx_count': 0, 'leader_commit_idx': 3, 'uptime': 594, 'self_code_version': 0, 'enabled_code_version': 0}
> The GET operation gives a 200 OK response code.

> As indicated here in all three status calls ('leader': TCPNode('127.0.0.1:6000'), 127.0.0.1:6000 
> which is Server 0 is clearly the leader. And no in a Raft based system there can only be one leader 
> at a time in Raft time.


Perform a Put request for the key ``a" on the leader. What is the new status? What changes occurred and why (if any)?

> Ans: The POST operation of Type PUT gives a 204 No Content response code.
> What changed is that if we now run a get operation, /a now holds ["apple"} instead of ["cat", "dog"]. This shoes that a 
> PUT operation rewrites what is currently stored in /a. 


Perform an Append request for the key ``a" on the leader. What is the new status? What changes occurred and why (if any)?

> Ans: Here is the reply from 127.0.0.1:6000: {'version': '0.3.12', 'revision': 'deprecated', 'self': TCPNode('127.0.0.1:6000'), 'state': 2, 'leader': TCPNode('127.0.0.1:6000'), 'has_quorum': True, 'partner_nodes_count': 2, 'partner_node_status_server_127.0.0.1:6001': 2, 'partner_node_status_server_127.0.0.1:6002': 0, 'readonly_nodes_count': 0, 'log_len': 3, 'last_applied': 4, 'commit_idx': 4, 'raft_term': 1, 'next_node_idx_count': 2, 'next_node_idx_server_127.0.0.1:6001': 5, 'next_node_idx_server_127.0.0.1:6002': 2, 'match_idx_count': 2, 'match_idx_server_127.0.0.1:6001': 4, 'match_idx_server_127.0.0.1:6002': 0, 'leader_commit_idx': 4, 'uptime': 1484, 'self_code_version': 0, 'enabled_code_version': 0}
> The POST operation of Type APPEND gives a 204 No Content response code.

> Changes occur in 'log_len', 'last_applied' and 'commit_idx'. log_len changes because of the new log entry and 
> last_applied and commit_idx are updated as the new entry is applied and committed. Also 'next_node_idx_server'
> and 'match_idx_server' are updated and this is due to how Raft handles log replication and consistency.

> EXTRA EXPLANATION FOR 'next_node_idx_server' AND 'match_idx_server' PROVIDED KINDLY BY CHATGPT
> When an Append request is processed, a new entry is added to the leader's log. This means the leader now has a 
> new entry to replicate to its followers. As a result, the next_node_idx for each follower is incremented by one 
> because there's now one more log entry that the leader needs to send to the follower.
>
> match_idx_server indicates the highest log entry known to be replicated on the follower (127.0.0.1:6001 in this case). 
> It's used by the leader to determine up to which point the logs are consistent between itself and the follower.
> When the follower successfully appends the new log entry sent by the leader, the match_idx is incremented. This 
> indicates that the follower’s log is now matching the leader’s log up to this new index.


Perform a Get request for the key ``a" on the leader. What is the new status? What change (if any) happened and why?

> Ans: Here is the reply from 127.0.0.1:6000: {'version': '0.3.12', 'revision': 'deprecated', 'self': TCPNode('127.0.0.1:6000'), 'state': 2, 'leader': TCPNode('127.0.0.1:6000'), 'has_quorum': True, 'partner_nodes_count': 2, 'partner_node_status_server_127.0.0.1:6001': 2, 'partner_node_status_server_127.0.0.1:6002': 0, 'readonly_nodes_count': 0, 'log_len': 2, 'last_applied': 4, 'commit_idx': 4, 'raft_term': 1, 'next_node_idx_count': 2, 'next_node_idx_server_127.0.0.1:6001': 5, 'next_node_idx_server_127.0.0.1:6002': 2, 'match_idx_count': 2, 'match_idx_server_127.0.0.1:6001': 4, 'match_idx_server_127.0.0.1:6002': 0, 'leader_commit_idx': 4, 'uptime': 1935, 'self_code_version': 0, 'enabled_code_version': 0}
> The GET operation gives a 200 OK response code.

> The request says /a now holds "["cat", "dog", "mouse"]". And due to the fact that a GET request does not modify 
> the state of the server, the status output stays mostly the same. 

NOTE FOR TASK 2: We completed this task before you updated the README and so our answers/outputs might not line up to what is expected.
So for clarification: PUT places values into /a and if there are already some there then they are overwritten. GET simply tells us which
values are in /a. APPEND is similar to PUT however it doesn't overwrite what is in /a, but instead simply adds the value to the end of 
the currently values in /a. 


# Task 3

Shut down the server that acts as a leader. Report the status that you get from the servers that remain active after shutting down the leader.

> Ans: Here are the messages i get after running the /admin/status request. They both give 200 OK and the following complete responses:
> If i shut down Server 0 (the current leader), then Server 1 becomes the leader as can be seen here: 'leader': TCPNode('127.0.0.1:6001')
> {'version': '0.3.12', 'revision': 'deprecated', 'self': TCPNode('127.0.0.1:6001'), 'state': 2, 'leader': TCPNode('127.0.0.1:6001'), 'has_quorum': True, 'partner_nodes_count': 2, 'partner_node_status_server_127.0.0.1:6002': 2, 'partner_node_status_server_127.0.0.1:6000': 0, 'readonly_nodes_count': 0, 'log_len': 3, 'last_applied': 3, 'commit_idx': 3, 'raft_term': 3, 'next_node_idx_count': 2, 'next_node_idx_server_127.0.0.1:6002': 4, 'next_node_idx_server_127.0.0.1:6000': 3, 'match_idx_count': 2, 'match_idx_server_127.0.0.1:6002': 3, 'match_idx_server_127.0.0.1:6000': 0, 'leader_commit_idx': 3, 'uptime': 62, 'self_code_version': 0, 'enabled_code_version': 0}

> And Server 2 says the Server 1 is the leader:
> {'version': '0.3.12', 'revision': 'deprecated', 'self': TCPNode('127.0.0.1:6002'), 'state': 0, 'leader': TCPNode('127.0.0.1:6001'), 'has_quorum': True, 'partner_nodes_count': 2, 'partner_node_status_server_127.0.0.1:6000': 0, 'partner_node_status_server_127.0.0.1:6001': 2, 'readonly_nodes_count': 0, 'log_len': 3, 'last_applied': 3, 'commit_idx': 3, 'raft_term': 3, 'next_node_idx_count': 0, 'match_idx_count': 0, 'leader_commit_idx': 3, 'uptime': 81, 'self_code_version': 0, 'enabled_code_version': 0}


Perform a Put request for the key "a". Then, restart the server from the previous point, and indicate the new status for the three servers. Indicate the result of a Get request for the key ``a" to the previous leader.

> Ans: So after doing a PUT request to the current leader (which is Server1 aka 6001 aka 8081) and then restarting Server0, we get the following 3 statuses:

> The status of 8080 is: {'version': '0.3.12', 'revision': 'deprecated', 'self': TCPNode('127.0.0.1:6000'), 'state': 0, 'leader': TCPNode('127.0.0.1:6001'), 'has_quorum': True, 'partner_nodes_count': 2, 'partner_node_status_server_127.0.0.1:6002': 2, 'partner_node_status_server_127.0.0.1:6001': 2, 'readonly_nodes_count': 0, 'log_len': 4, 'last_applied': 4, 'commit_idx': 4, 'raft_term': 3, 'next_node_idx_count': 0, 'match_idx_count': 0, 'leader_commit_idx': 4, 'uptime': 130, 'self_code_version': 0, 'enabled_code_version': 0}
> The response code is 200 OK.
 
> The status of 8081 is: {'version': '0.3.12', 'revision': 'deprecated', 'self': TCPNode('127.0.0.1:6001'), 'state': 2, 'leader': TCPNode('127.0.0.1:6001'), 'has_quorum': True, 'partner_nodes_count': 2, 'partner_node_status_server_127.0.0.1:6002': 2, 'partner_node_status_server_127.0.0.1:6000': 2, 'readonly_nodes_count': 0, 'log_len': 2, 'last_applied': 4, 'commit_idx': 4, 'raft_term': 3, 'next_node_idx_count': 2, 'next_node_idx_server_127.0.0.1:6002': 5, 'next_node_idx_server_127.0.0.1:6000': 5, 'match_idx_count': 2, 'match_idx_server_127.0.0.1:6002': 4, 'match_idx_server_127.0.0.1:6000': 4, 'leader_commit_idx': 4, 'uptime': 357, 'self_code_version': 0, 'enabled_code_version': 0}
> The response code is 200 OK.
 
> The status of 8082 is: {'version': '0.3.12', 'revision': 'deprecated', 'self': TCPNode('127.0.0.1:6002'), 'state': 0, 'leader': TCPNode('127.0.0.1:6001'), 'has_quorum': True, 'partner_nodes_count': 2, 'partner_node_status_server_127.0.0.1:6000': 2, 'partner_node_status_server_127.0.0.1:6001': 2, 'readonly_nodes_count': 0, 'log_len': 2, 'last_applied': 4, 'commit_idx': 4, 'raft_term': 3, 'next_node_idx_count': 0, 'match_idx_count': 0, 'leader_commit_idx': 4, 'uptime': 395, 'self_code_version': 0, 'enabled_code_version': 0}
> The response code is 200 OK.

> So after turning off Server0, Server1 became the leader and then after restarting Server0 Server1 is still the leader. And if we perform a 
> GET request on the previous leader which is Server0, we get a 200 OK and that the value of /a is correctly also stored in Server0. 
> The status code of this is as follows: {'version': '0.3.12', 'revision': 'deprecated', 'self': TCPNode('127.0.0.1:6000'), 'state': 0, 'leader': TCPNode('127.0.0.1:6001'), 'has_quorum': True, 'partner_nodes_count': 2, 'partner_node_status_server_127.0.0.1:6002': 2, 'partner_node_status_server_127.0.0.1:6001': 2, 'readonly_nodes_count': 0, 'log_len': 2, 'last_applied': 4, 'commit_idx': 4, 'raft_term': 3, 'next_node_idx_count': 0, 'match_idx_count': 0, 'leader_commit_idx': 4, 'uptime': 491, 'self_code_version': 0, 'enabled_code_version': 0}


Has the Put request been replicated? Indicate which steps lead to a new election and which ones do not. Justify your answer using the statuses returned by the servers.

> Ans: Yes as previously mentioned the PUT request was correctly replicated onto the newly restarted server. 
> Here are the steps that lead to the election:
> 1. Shutting down the server that acts as the current leader.
> 2. Observing the status of the remaining servers after the leader is shut down.
> 3. Restarting the server that was shut down (previously the leader).
> 4. Checking the new statuses of all servers and the result of a GET request for a specific key to the previous leader.
> As can be seen by the status codes, Server1 was elected to be leader after Server0 was shut down and even when Server0
> came back online, Server1 remained the leader.
 
> After applying the PUT request to an operational server (Server1) and then restarting the previously shut down Server0, we observed 2 things:
> 1. Whether the PUT request gets replicated across the cluster, including the restarted server, which ensures data consistency and reliability.
> 2. How the cluster handles the reintegration of a server that was previously down, especially in terms of leader election and data synchronization.
> Finally, performing a GET request on the server that was initially shut down allowed us to verify if the state of the data is consistent 
> across the cluster, including on a server that had temporarily been offline.


Shut down two servers, including the leader --- starting with the server that is not the leader. Report the status of the remaining servers and explain what happened.

> Ans: We shut down first Server0 and then Server1 which is the current leader. 
> The status code of Server2 is as follows: {'version': '0.3.12', 'revision': 'deprecated', 'self': TCPNode('127.0.0.1:6002'), 'state': 0, 'leader': TCPNode('127.0.0.1:6001'), 'has_quorum': False, 'partner_nodes_count': 2, 'partner_node_status_server_127.0.0.1:6000': 0, 'partner_node_status_server_127.0.0.1:6001': 0, 'readonly_nodes_count': 0, 'log_len': 2, 'last_applied': 4, 'commit_idx': 4, 'raft_term': 3, 'next_node_idx_count': 0, 'match_idx_count': 0, 'leader_commit_idx': 4, 'uptime': 1539, 'self_code_version': 0, 'enabled_code_version': 0}
> This means that Server1 is still being called the leader by Server2. There are several possible reasons for this:
> 1. Timing and Raft Election Timeouts: If the remaining server has not yet recognized that the leader is down (due to 
> network delays, timing issues, or election timeouts not having expired), it might still consider the shut-down server 
> as the leader. Raft relies on election timeouts to trigger a new election, and if this timeout has not yet elapsed, 
> no new leader election would have been initiated.
> 2. Quorum Requirement: In Raft, a majority of nodes (a quorum) is required to elect a new leader. With two out of 
> three servers down, the system no longer has a quorum. This means the remaining server cannot elect itself or any 
> other node as a new leader. The has_quorum: False status indicates this situation. Without a quorum, the cluster 
> cannot make progress in terms of leader election or log replication.
> 3. Stale Leader Information: The remaining server might still have stale information regarding the leader if it 
> has not yet updated its state based on the latest cluster configuration. This can happen if the server has been 
> isolated from the others due to network partitions or other failures.


Can you perform Get, Put, or Append requests in this system state? Justify your answer.

> Ans:  GET requests are still possible (we tried one), however due to the previously mentioned lack of Quorum, PUT 
> and APPEND requests are no longer possible. PUT or APPEND requests require consensus, which is not possible without 
> a quorum.


Restart the servers and note down the new status. Describe what happened.

> Ans: After restarting both server the statuses are as follows:
> The status code of Server0 is as follows: {'version': '0.3.12', 'revision': 'deprecated', 'self': TCPNode('127.0.0.1:6000'), 'state': 0, 'leader': TCPNode('127.0.0.1:6002'), 'has_quorum': True, 'partner_nodes_count': 2, 'partner_node_status_server_127.0.0.1:6001': 2, 'partner_node_status_server_127.0.0.1:6002': 2, 'readonly_nodes_count': 0, 'log_len': 3, 'last_applied': 5, 'commit_idx': 5, 'raft_term': 4, 'next_node_idx_count': 0, 'match_idx_count': 0, 'leader_commit_idx': 5, 'uptime': 178, 'self_code_version': 0, 'enabled_code_version': 0}
> The status code of Server1 is as follows: {'version': '0.3.12', 'revision': 'deprecated', 'self': TCPNode('127.0.0.1:6001'), 'state': 0, 'leader': TCPNode('127.0.0.1:6002'), 'has_quorum': True, 'partner_nodes_count': 2, 'partner_node_status_server_127.0.0.1:6000': 2, 'partner_node_status_server_127.0.0.1:6002': 2, 'readonly_nodes_count': 0, 'log_len': 3, 'last_applied': 5, 'commit_idx': 5, 'raft_term': 4, 'next_node_idx_count': 0, 'match_idx_count': 0, 'leader_commit_idx': 5, 'uptime': 128, 'self_code_version': 0, 'enabled_code_version': 0}
> The status code of Server2 is as follows: {'version': '0.3.12', 'revision': 'deprecated', 'self': TCPNode('127.0.0.1:6002'), 'state': 2, 'leader': TCPNode('127.0.0.1:6002'), 'has_quorum': True, 'partner_nodes_count': 2, 'partner_node_status_server_127.0.0.1:6000': 2, 'partner_node_status_server_127.0.0.1:6001': 2, 'readonly_nodes_count': 0, 'log_len': 3, 'last_applied': 5, 'commit_idx': 5, 'raft_term': 4, 'next_node_idx_count': 2, 'next_node_idx_server_127.0.0.1:6000': 6, 'next_node_idx_server_127.0.0.1:6001': 6, 'match_idx_count': 2, 'match_idx_server_127.0.0.1:6000': 5, 'match_idx_server_127.0.0.1:6001': 5, 'leader_commit_idx': 5, 'uptime': 2541, 'self_code_version': 0, 'enabled_code_version': 0}

> So now Server2 has become the leader.


# Task 4

1. What is a consensus algorithm? What are they used for in the context of replicated state machines? 

> Ans: A consensus algorithm is design to enable connections of distributed machines ie. different nodes to work together efficiently as a group
> even with the presence of failures and outages. It is used to achieve agreement on a single data value among distributed processes or systems. 
> So it is an algorithm that seeks an organized way of working of different machines that interact with 
>  other, ensuring that they will continue to work in an efficient manner even if errors and failures are present.
> In practice, a consensus algorithm provides a way for multiple servers ro reach agreement on a state. Once there is consensus, the state is final and cannot
> be changed.
> When talking about replicated state machines, we ensure that each replica progresses in the same state. Also, this ensures consistency and 
> reliability because even if some nodes are down, the algorithm will continue working, ie the machines will continue working.
> So even in concurrent updates all replicas hold the same data.

> Sources: https://www.scylladb.com/glossary/consensus-algorithms/#:~:text=Consensus%20algorithms%20are%20designed%20to,scale%2C%20fault%2Dtolerant%20systems.


2. What are the main features of the Raft algorithm? How does Raft enable fault toler- ance?

> Ans: The main features of the raft algorithm are: Leader election, log replication, safety and log matching, term concept and membership changes.
> DO WE NEED TO EXPLAIN?
> Fault tolerance in raft is handled this way:
> - If a leader fails, a new leader is elected, ensuring continued operation of the cluster.
> - we can ensure that the system can operate even if nodes are down by replicating the state across multiple nodes
> - once a log entry is seen as committed, it is guaranteed to be present in any future leader, providing data durability
> - as long as there is a mjority, consensus can be reached
> - log consistency and leader uniqueness are maintained even in the presence of network delays, partitions, and node restarts.

> Source: https://towardsdatascience.com/raft-algorithm-explained-a7c856529f40


3. What are Byzantine failures? Can Raft handle them?

> Ans: We call it a Byzantine failure in the case that a fault is presenting different symptoms to different nodes/observers across
> a distributed system. So a Byzantine failure is the effective loss of a system service due to fault systems that indeed require consensus among the system
> and its nodes For example, a Byzantine node might send different, conflicting messages to different nodes, making it difficult for the system to reach a consensus.
> It is not only difficuly to reach consensus but also to identify the problem.

> And no, raft can't inherently handle these type of failures. The algorightm has to be updated in order to do so.
> It needs additional mechanisms to detect and mitigate deceitful or inconsistent behavior among nodes. 

> Source: https://www.scs.stanford.edu/17au-cs244b/labs/projects/clow_jiang.pdf
> https://en.wikipedia.org/wiki/Byzantine_fault#:~:text=A%20Byzantine%20fault%20is%20any,require%20consensus%20among%20distributed%20nodes.