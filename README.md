# **Assignment: ReAct Agent with Tools**

## **Description**

In this assignment, you will create a **ReAct agent** that uses tools to answer questions about **Utah Tech University**.
Your agent will be called the **Campus Companion**.

You will begin with the *travel agent* demo from class and adapt it to serve as the Campus Companion.
This will involve redesigning the tools, modifying the prompts, and ensuring the agent can meaningfully respond to university-related questions.

## **Learning Outcomes**

By completing this assignment, you will be able to:

- Implement a ReAct agent
- Design and integrate agent tools
- Direct an agent to use tools effectively
- Customize an agent’s system prompt

## **Resources**

- **Starter Code:**
  Download and unpack `travel-demo.zip`, which contains the sample code from class.
  Use this as your starting point, renaming files and folders appropriately for your Campus Companion.

- **Event Data:**
  The file `events.csv` provides a list of Utah Tech events for the coming month.
  At least one of your tools must allow the agent to access and use the information in this file meaningfully.

## **Requirements**

- Running
  ```bash
  python3 run.py "My question about the university."
  ```  
  must trigger your ReAct agent to generate a response.

- Your agent should be able to handle a wide range of questions, such as:
  - "What biology courses are offered at the university?"
  - "When was the last win by the football team?"

- Design and implement tools that support question answering.
  You may use text processing, data retrieval, or other appropriate strategies.