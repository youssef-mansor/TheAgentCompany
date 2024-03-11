# JobAgent
A benchmark for agents that could do professional jobs!

## Goal
Goal is to create a realistic, reproducible, executable benchmark that tests agents' ability in performing tasks in professionals' work time from various fields, such as software engineers, designers, analyst, doctors, nurses and lawyers to name a few. 
Existing agent benchmark mostly focused on daily life scenarios, and cannot test the expert domain knowledge and complexities required in many professional tasks.

## Tasks

We have previously created a benchmark called WebArena for evaluating web agents on actual tasks that people perform in every-day life. 
In constructing WebArena, we took a semi-systematic approach of viewing the browsing history of the research team (students and faculty members in the CMU School of Computer Science) and choosing tasks that reflected the types of tasks that we did in our everyday life.

There are several obvious issues with this if we want to evaluate web agents with broader implications:
- Despite some grounding in realistic data, the process of creating tasks from this data was quite heuristic, and no consideration was made for how important or time consuming the tasks are.
- The tasks are biased towards those important for academics in computer science, and not reflective of tasks performed by the entire population

In this work, we plan on significantly expanding WebArena to a broader variety of tasks *motivated by tasks performed during real-world work*. 

We want to have a reproducible, generalized recipe for finding tasks to include in the benchmark is important to enable scalability given a new expert domain (in our case a new job/profession).
That, as a part of the work's contribution, could justify the bias issues in task collection for domains that we are not an expert in.



## Tools
Once we have a list of tasks that are deemed to be important according to the above criteria, we will identify the applications that are typically used to perform those tasks. 
- Open source vs. Non open-source
- Web application vs. desktop GUIs

## Environments
- Fixed environments inside containers for best reproducibility
- Live services for another suite of evaluations

## Observation and Actuation Modalities
For each task, we hope to provide the agents with as many modalities as possible for them to observe and actuate. We also try to compare the performance between using them, and possibly explore dynamically selecting the best for different scenarios.

- Image/video-based observation and pixel coordinate-based actuation: providing screenshot and pixels to the agent.
- XML/DOM/A11y tree-based observation and element-based actuation: providing raw html (webpage) or GUI layout (XML) to the agent.
- API-based interaction: providing API specifications and documentation (OpenAPI) to the agent, where agent could observe and actuate programatically.

## Evaluators

- Execution-based evaluations: write programs to verify the final state, might be difficult for some tasks (e.g. plot a graph)
- Step-based evaluations: check the steps produced by the agents, possibly have partial scores.
- Checkpoint-based evaluations: have verifiable checkpoints along the way of more complex tasks.


## Baselines
- LLMs

## Trajectory Collection
- Looking to incorporate some data collection techniques in plugins for web agents
- Screen recording, key logger, etc.