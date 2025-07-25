from temporalio.worker import Worker
from temporalio.client import Client
import asyncio

from workflows import DailyCheckinWorkflow
from question_logging_workflow import QuestionLoggingWorkflow
from summary_workflow import WeeklySummaryWorkflow

async def main():
    client = await Client.connect("localhost:7233")
    worker = Worker(
        client,
        task_queue="onboarding-assistant",
        workflows=[
            DailyCheckinWorkflow,
            QuestionLoggingWorkflow,
            WeeklySummaryWorkflow
        ],
    )
    await worker.run()

if __name__ == "__main__":
    asyncio.run(main())