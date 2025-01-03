from crewai import Agent, Crew, Process, Task,LLM
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import FileWriterTool

# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators
file_writer_tool_summary=FileWriterTool(file_name="meeting_minutes_summary.txt",directory='meeting_minutes',overwrite=True)
file_writer_tool_actions=FileWriterTool(file_name="meeting_minutes_actions.txt",directory='meeting_minutes',overwrite=True)
file_writer_tool_mood=FileWriterTool(file_name="meeting_minutes_mood.txt",directory='meeting_minutes',overwrite=True)
@CrewBase
class MeetingMinutesCrew:
    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"
    OUTPUTS = ["summary", "actions", "mood"]
    llm = LLM(
    model="gemini/gemini-1.5-pro",
    temperature=0.7
)


    @agent
    def summarizer(self) -> Agent:
        return Agent(
            config=self.agents_config["summarizer"],
            tools=[file_writer_tool_summary,file_writer_tool_actions,file_writer_tool_mood],
            llm=self.llm
        )
    
    @agent
    def writer(self) -> Agent:
        return Agent(
            config=self.agents_config["writer"],
            llm=self.llm
        )
  
    @task
    def summarize_meeting(self) -> Task:
        return Task(
            config=self.tasks_config["summarize_meeting"],
        )
    def writer_task(self) -> Task:
        return Task(
            config=self.tasks_config["writer_task"],
        )
    @crew
    def crew(self) -> Crew:
        """Creates the Summary Crew"""

        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
        )
