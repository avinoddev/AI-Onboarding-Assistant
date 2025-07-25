from temporalio import workflow

@workflow.defn
class QuestionLoggingWorkflow:
    @workflow.run
    async def run(self, user_id: str, question: str) -> None:
        # Log question in MongoDB or perform LLM feedback logic
        workflow.logger.info(f"Logging question from {user_id}: {question}")