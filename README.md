# Discrete-Event-Simulation
 DES models the operation of a system as a (discrete) sequence of events in time.
 
 # Components
 <h3>State</h3>
 <p>A system state is a set of variables that captures the salient properties of the system to be studied. The state trajectory over time S(t) can be mathematically represented by a step function whose value can change whenever an event occurs.</p>
 <h3>Clock</h3>
 <p>The simulation must keep track of the current simulation time, in whatever measurement units are suitable for the system being modeled. In discrete-event simulations, as opposed to continuous simulations, time 'hops' because events are instantaneous – the clock skips to the next event start time as the simulation proceeds.</p>
 <h3>Events List</h3>
 <p>The simulation maintains at least one list of simulation events. This is sometimes called the pending event set because it lists events that are pending as a result of previously simulated event but have yet to be simulated themselves. An event is described by the time at which it occurs and a type, indicating the code that will be used to simulate that event. It is common for the event code to be parametrized, in which case, the event description also contains parameters to the event code. Typically, events are scheduled dynamically as the simulation proceeds.</p>
<h3>Random-number generators</h3>
<p>The simulation needs to generate random variables of various kinds, depending on the system model. This is accomplished by one or more Pseudorandom number generators. The use of pseudo-random numbers as opposed to true random numbers is a benefit should a simulation need a rerun with exactly the same behavior.</p>
<h4>Linear Congruential Generator</h4>
<p>A linear congruential generator (LCG) is an algorithm that yields a sequence of pseudo-randomized numbers calculated with a discontinuous piecewise linear equation. The method represents one of the oldest and best-known pseudorandom number generator algorithms. The theory behind them is relatively easy to understand, and they are easily implemented and fast, especially on computer hardware which can provide modulo arithmetic by storage-bit truncation.</p>
<h3>Statistics</h3>
<p>The simulation typically keeps track of the system's statistics, which quantify the aspects of interest. In the bank example, it is of interest to track the mean waiting times. In a simulation model, performance metrics are not analytically derived from probability distributions, but rather as averages over replications, that is different runs of the model. Confidence intervals are usually constructed to help assess the quality of the output.</p>
<h3>Ending condition</h3>
<p>Because events are bootstrapped, theoretically a discrete-event simulation could run forever. So the simulation designer must decide when the simulation will end. Typical choices are "at time t" or "after processing n number of events" or, more generally, "when statistical measure X reaches the value x".</p>

 # Theory of Constraints
<p>The theory of constraints (TOC) is a management paradigm that views any manageable system as being limited in achieving more of its goals by a very small number of constraints. There is always at least one constraint, and TOC uses a focusing process to identify the constraint and restructure the rest of the organization around it. TOC adopts the common idiom "a chain is no stronger than its weakest link". This means that processes, organizations, etc., are <strong>vulnerable because the weakest person or part can always damage or break them or at least adversely affect the outcome</strong>.</p>

# Common Uses

<h3>Diagnosing process issues</h3>
<p>Simulation approaches are particularly well equipped to help users diagnose issues in complex environments. The Theory of Constraints illustrates the importance of understanding bottlenecks in a system. Identifying and removing bottlenecks allows improving processes and the overall system. For instance, in manufacturing enterprises bottlenecks may be created by excess inventory, overproduction, variability in processes and variability in routing or sequencing. By accurately documenting the system with the help of a simulation model it is possible to gain a bird’s eye view of the entire system.</p>

<p>A working model of a system allows management to understand performance drivers. A simulation can be built to include any number of performance indicators such as worker utilization, on-time delivery rate, scrap rate, cash cycles, and so on.</p>

<h3>Hospital applications</h3>
<p>An operating theater is generally shared between several surgical disciplines. Through better understanding the nature of these procedures it may be possible to increase the patient throughput. Example: If a heart surgery takes on average four hours, changing an operating room schedule from eight available hours to nine will not increase patient throughput. On the other hand, if a hernia procedure takes on average twenty minutes providing an extra hour may also not yield any increased throughput if the capacity and average time spent in the recovery room is not considered.</p>

# Run (on terminal)
pip install -r requirements.txt
<br>
python main.py
