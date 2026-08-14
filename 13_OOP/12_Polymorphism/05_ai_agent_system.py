# Program: AI Agent System using Polymorphism

# Description: Demonstrates polymorphism by using the same run()
# method in different agent classes with different behaviors.

class ResearchAgent:

    def run(self):
        print("Research Agent is collecting information")

class CodingAgent:

    def run(self):
        print("Coding Agent is writing code")

class WritingAgent:

    def run(self):
        print("Writing Agent is generating content")

def execute_agent(agent):
    agent.run()

execute_agent(ResearchAgent())
execute_agent(CodingAgent())
execute_agent(WritingAgent())