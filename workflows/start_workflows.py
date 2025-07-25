from temporalio.client import Client
import asyncio

async def main():
    client = await Client.connect("localhost:7233")
    
    await client.start_workflow(
        "DailyCheckinWorkflow",
        "user123",
        id="daily-checkin-user123",
        task_queue="onboarding-assistant",
    )

if __name__ == "__main__":
    asyncio.run(main())
