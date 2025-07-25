from temporalio import workflow

@workflow.defn
class WeeklySummaryWorkflow:
    @workflow.run
    async def run(self, user_id: str) -> None:
        # Summarize questions asked and checklist progress from MongoDB
        workflow.logger.info(f"Sending weekly onboarding summary to {user_id}")
